import io
import os
import re
import subprocess
from datetime import datetime

from unidiff import PatchSet

# Regex patterns to identify variable name changes and comment/docstring changes
VARIABLE_NAME_CHANGE = re.compile(r"^\s*[\w\.]+\s*=\s*")
COMMENT_OR_DOCSTRING_CHANGE = re.compile(r'^\s*(#|"""|\'\'\')')


def is_significant_change(line):
    """
    Check if a given line represents a significant change that is not just
    a variable name change or a comment/docstring change.
    """
    return not (
        VARIABLE_NAME_CHANGE.match(line) or COMMENT_OR_DOCSTRING_CHANGE.match(line)
    )


def get_file_content(repo_path: str, file_path: str) -> str:
    """
    Get the content of the file at the given path.
    :param repo_path: The path to the git repository.
    :param file_path: The relative path to the file from the repo root.
    :return: The content of the file.
    """
    full_path = os.path.join(repo_path, file_path)
    if not os.path.exists(full_path):
        # File doesn't exist, handle the case appropriately
        return None  # or return an appropriate message/error
    with open(full_path, "r") as file:
        return file.read()


def create_significant_diff(repo_path: str, base_branch: str = "main") -> str:
    diffs_dir = os.path.join(repo_path, "diffs")
    os.makedirs(diffs_dir, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    diff_file_name = f"full_diff_{timestamp}.diff"
    diff_file_path = os.path.join(diffs_dir, diff_file_name)

    git_diff_cmd = ["git", "-C", repo_path, "diff", base_branch]
    diff_output = subprocess.run(git_diff_cmd, capture_output=True, text=True).stdout
    patch_set = PatchSet(io.StringIO(diff_output))

    for patched_file in patch_set:
        file_content = get_file_content(repo_path, patched_file.path)
        if file_content is None:
            # Skip this file since it doesn't exist
            continue

        significant_changes = any(
            is_significant_change(line.value.strip())
            for hunk in patched_file
            for line in hunk
            if line.is_added or line.is_removed
        )

        if significant_changes:
            with open(diff_file_path, "a") as diff_file:
                diff_file.write(
                    f"--- a/{patched_file.path}\n+++ b/{patched_file.path}\n"
                )

                for hunk in patched_file:
                    # Write out the full file content with markings for changes
                    for line_number, original_line in enumerate(file_content, start=1):
                        line_to_write = original_line
                        for line in hunk:
                            if line.target_line_no == line_number:
                                if line.is_added:
                                    line_to_write = f"+{line.value}"
                                elif line.is_removed:
                                    line_to_write = f"-{line.value}"
                                elif line.is_context:
                                    line_to_write = f" {line.value}"
                                break
                        diff_file.write(line_to_write)

    return diff_file_path


# Example usage:
try:
    repository_path = get_git_repo_root()
    full_diff_file_path = create_significant_diff(repository_path)
    print(f"Full diff file created at: {full_diff_file_path}")
except Exception as e:
    print(f"An error occurred: {str(e)}")
