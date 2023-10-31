import logging
from typing import List

from py_do_you_even_diff_bro.utils import run_shell_command

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


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
        logger.info(f"Diffing against branch {branch}")
        command.append(branch)

    if only or ignore:
        command.append("--")

    if ignore:
        logger.info(f"Diffing ALL files except those with extensions {ignore}")
        files = [f":(exclude)**/*{ext}" for ext in ignore]
        command.extend(files)
    elif only:
        logger.info(f"Diffing exclusively files with extensions {only}")
        files = [f"**/*{ext}" for ext in only]
        command.extend(files)
    else:
        logger.info(f"Diffing all files (no extensions specified))")

    return run_shell_command(" ".join(command))
