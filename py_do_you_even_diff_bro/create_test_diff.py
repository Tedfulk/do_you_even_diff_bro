import io
import os
import re
import subprocess
from datetime import datetime

from unidiff import PatchSet

# Regex patterns to identify variable name changes and comment/docstring changes
VARIABLE_NAME_CHANGE = re.compile(r"^\s*[\w\.]+\s*=\s*")
COMMENT_OR_DOCSTRING_CHANGE = re.compile(r'^\s*(#|"""|\'\'\')')


def get_git_repo_root() -> str:
    """
    Returns the absolute path of the top-level directory for the Git repository.
    """
    try:
        git_root_cmd = ["git", "rev-parse", "--show-toplevel"]
        completed_process = subprocess.run(
            git_root_cmd, capture_output=True, check=True, text=True
        )
        return completed_process.stdout.strip()
    except subprocess.CalledProcessError as e:
        raise FileNotFoundError(
            "Could not find Git repository root. Are you inside a Git repository?"
        ) from e


def is_significant_change(line: str) -> bool:
    return not (
        VARIABLE_NAME_CHANGE.match(line) or COMMENT_OR_DOCSTRING_CHANGE.match(line)
    )


def get_file_content(repo_path: str, file_path: str) -> list:
    with open(os.path.join(repo_path, file_path), "r") as file:
        return file.readlines()


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
        significant_changes = any(
            is_significant_change(line.value.strip())
            for hunk in patched_file
            for line in hunk
            if line.is_added or line.is_removed
        )

        if significant_changes:
            file_content = get_file_content(repo_path, patched_file.path)
            with open(diff_file_path, "a") as diff_file:
                diff_file.writelines(file_content)

    return diff_file_path


# Example usage:
try:
    repository_path = get_git_repo_root()
    full_diff_file_path = create_significant_diff(repository_path)
    print(f"Full diff file created at: {full_diff_file_path}")
except Exception as e:
    print(f"An error occurred: {str(e)}")
