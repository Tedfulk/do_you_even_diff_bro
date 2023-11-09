from typing import List

import typer
from rich.console import Console
from rich.table import Table
from typer import Argument, Option, confirm, prompt

from py_do_you_even_diff_bro.commandments import SUMMARY_BRO_PROMPT, get_diff_prompt
from py_do_you_even_diff_bro.constants import (
    DETAILED_BROGRAMMER_DESCRIPTION,
    PROGRAMMING_FILE_EXTENSIONS,
)
from py_do_you_even_diff_bro.git import get_git_diff
from py_do_you_even_diff_bro.llm import gpt_prompt
from py_do_you_even_diff_bro.models import BroMode

app = typer.Typer(
    name="BROGRAMMER",
    help="BROGRAMMER: Your AI Peer Review Bro",
    epilog=DETAILED_BROGRAMMER_DESCRIPTION,
)
console = Console()


def get_bro_mode(chill: bool, mid: bool, chad: bool) -> BroMode:
    mode_map = {chill: BroMode.CHILL, mid: BroMode.MID, chad: BroMode.CHAD}
    return next((mode for cond, mode in mode_map.items() if cond), BroMode.CHILL)


def display_diff_summary(summary_diff_response: str):
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Summary", justify="left")
    table.add_row(summary_diff_response)
    console.print(table)


def validate_extensions(
    ctx: typer.Context, param: typer.CallbackParam, value: List[str]
) -> List[str]:
    invalid_exts = [ext for ext in value if ext not in PROGRAMMING_FILE_EXTENSIONS]
    if invalid_exts:
        for ext in invalid_exts:
            console.log(f"Invalid file extension: {ext}", style="bold red")
        raise typer.BadParameter(f"Invalid extensions: {', '.join(invalid_exts)}")
    return value


@app.command()
def main(
    chill: bool = typer.Option(
        False,
        "--chill",
        "-c",
        help="Get a chill, jr-level engineer, relaxed BROGRAMMER PR review",
    ),
    mid: bool = typer.Option(
        False, "--mid", "-m", help="Get a mid-level engineer, BROGRAMMER PR review"
    ),
    chad: bool = typer.Option(
        False,
        "--chad",
        "-d",
        help="Get a chad, sr-level engineer, intense BROGRAMMER PR review",
    ),
    model: str = typer.Option(
        "gpt-4", "--model", "-o", help="GPT model use 'gpt-3.5-turbo' or 'gpt-4'"
    ),
    only: list[str] = typer.Option(
        PROGRAMMING_FILE_EXTENSIONS,
        "--only",
        callback=validate_extensions,
        help="Only include files with these extensions",
    ),
    ignore: list[str] = typer.Option(
        [],
        "--ignore",
        callback=validate_extensions,
        help="Ignore files with these extensions",
    ),
    prompt: str = typer.Option("", "--prompt", "-p", help="Specify a custom prompt"),
    summarize: bool = typer.Option(
        False, "--summarize", "-s", help="Summarize the git diff"
    ),
    peer_review: str = typer.Option(
        "",
        "--peer-review",
        "-r",
        help="Specify the branch to compare the git diff against",
    ),
):
    try:
        valid_models = ["gpt-3.5-turbo", "gpt-4"]
        if model not in valid_models:
            console.log(
                "Invalid model. Choose from 'gpt-3.5-turbo' or 'gpt-4'",
                style="bold red",
            )
            return

        invalid_only_exts = [
            ext for ext in only if ext not in PROGRAMMING_FILE_EXTENSIONS
        ]
        invalid_ignore_exts = [
            ext for ext in ignore if ext not in PROGRAMMING_FILE_EXTENSIONS
        ]

        if invalid_only_exts or invalid_ignore_exts:
            if invalid_only_exts:
                console.log(
                    f"Invalid file extensions in --only: {', '.join(invalid_only_exts)}",
                    style="bold red",
                )
            if invalid_ignore_exts:
                console.log(
                    f"Invalid file extensions in --ignore: {', '.join(invalid_ignore_exts)}",
                    style="bold red",
                )
            return

        if sum([chill, mid, chad]) > 1:
            console.log(
                "Only one of --chill, --mid, or --chad can be True.", style="bold red"
            )
            return

        bro_mode = get_bro_mode(chill, mid, chad)

        git_diff = get_git_diff(only, ignore, peer_review)

        if not git_diff:
            print(f"No git diff for BROGRAMMER")
            return

        print(
            f"Building prompt for BROGRAMMER in bromode: '{str(bro_mode)}' mode on GPT model '{model}'"
            f"{f' with custom prompt: {prompt}' if prompt else ''}"
            f"{f' Will generate diff summary.' if summarize else ''}"
        )

        if summarize:
            print(f"\n\nSummarizing git diff for BROGRAMMER on GPT model '{model}'")

            summary_prompt_text = f"{SUMMARY_BRO_PROMPT}\n\n{git_diff}"

            summary_diff_response = gpt_prompt(summary_prompt_text, model)
            display_diff_summary(summary_diff_response)
        else:
            if not prompt:
                prompt_text = get_diff_prompt(bro_mode, git_diff)
            else:
                prompt_text = f"{prompt}\n\n{git_diff}"

            print(f"Running BROGRAMMER")

            diff_response = gpt_prompt(prompt_text, model)

            print("\nBROGRAMMER\n\n", diff_response)
    except Exception as e:
        console.log(f"An error occurred: {e}", style="bold red")


if __name__ == "__main__":
    app()
