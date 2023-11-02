from typing import List

from py_do_you_even_diff_bro.utils import run_shell_command


def get_git_diff(
    only: List[str] = None, ignore: List[str] = None, branch: str = None
) -> str:
    """
    Returns the git diff as a string
    If ignore is specified, diffs all files except those with those extensions
    If only is specified, only diffs files with those extensions
    If neither are specified, diffs all files
    """

    command = ["git", "diff"]

    if branch:
        command.append(branch)

    if only or ignore:
        command.append("--")

    if ignore:
        files = [f":(exclude)**/*{ext}" for ext in ignore]
        command.extend(files)
    elif only:
        files = [f"**/*{ext}" for ext in only]
        command.extend(files)
    else:
        pass

    return run_shell_command(" ".join(command))
