from typing import List, Optional

import typer
from rich.console import Console
from rich.table import Table
from typing_extensions import Annotated

from py_do_you_even_diff_bro.commandments import SUMMARY_BRO_PROMPT, get_diff_prompt
from py_do_you_even_diff_bro.constants import (
    DETAILED_BROGRAMMER_DESCRIPTION,
    PROGRAMMING_FILE_EXTENSIONS,
)
from py_do_you_even_diff_bro.git import get_git_diff
from py_do_you_even_diff_bro.llm import prompt
from py_do_you_even_diff_bro.models import BroMode

app = typer.Typer(help=DETAILED_BROGRAMMER_DESCRIPTION)
console = Console()


def display_summary_table(model: str, bro_mode: BroMode, git_diff: str):
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Model", style="dim", width=12)
    table.add_column("Bro Mode", style="dim", width=12)
    table.add_column("Git Diff", style="dim", width=50)
    table.add_row(
        model, str(bro_mode), git_diff[:50] + "..." if len(git_diff) > 50 else git_diff
    )
    console.print(table)


def determine_bro_mode(chill: bool, mid: bool, chad: bool, model: str) -> BroMode:
    bro_mode: BroMode = BroMode.CHILL
    if mid:
        bro_mode = BroMode.MID
    elif chad:
        bro_mode = BroMode.CHAD
        if model != "gpt-4":
            user_input = input(
                "Chad mode is engaged. It is suggested to use 'gpt-4' model for optimal results. Do you want to switch to 'gpt-4'? (y/n): "
            )
            if user_input.lower() not in ["yes", "y"]:
                model = input(
                    "Enter the model you want to use (e.g., 'gpt-3.5-turbo'): "
                )
    return bro_mode, model


def fetch_git_diff(
    only: List[str], ignore: List[str], peer_review: Optional[str]
) -> str:
    git_diff = get_git_diff(only, ignore, peer_review)
    if not git_diff:
        print(f"No git diff for BROGRAMMER to review. Exiting.")
        return ""
    return git_diff


def run_diff(
    bro_mode: BroMode,
    model: str,
    git_diff: str,
    custom_prompt: Optional[str],
    summarize: bool,
):
    print(
        f"Building prompt for diffbro in bromode: '{bro_mode.name.lower()}' mode on GPT model '{model}'"
        f"{f' with custom prompt: {custom_prompt}' if custom_prompt else ''}"
        f"{f' Will generate diff summary.' if summarize else ''}"
    )

    if not custom_prompt:
        prompt_text = get_diff_prompt(bro_mode, git_diff)
    else:
        prompt_text = f"{custom_prompt}\n\n{git_diff}"

    print(f"Running BROGRAMMER")

    diff_resp = prompt(prompt_text, model)

    print("\n\nBROGRAMMER\n\n", diff_resp)

    if summarize:
        print(f"\n\nSummarizing git diff for diffbro on GPT model '{model}'")

        summary_prompt_text = f"{SUMMARY_BRO_PROMPT}\n\n{git_diff}"

        summary_diff_resp = prompt(summary_prompt_text, model)

        print("\n\nBROGRAMMER SUMMARY\n\n", summary_diff_resp)


@app.command()
def main(
    chill: bool = typer.Option(
        True, help="Get a chill, jr-level engineer, relaxed diffbro PR review"
    ),
    mid: bool = typer.Option(False, help="Get a mid-level engineer, diffbro PR review"),
    chad: bool = typer.Option(
        False, help="Get a chad, sr-level engineer, intense diffbro PR review"
    ),
    model: Annotated[Optional[str], typer.Argument()] = "gpt-4",
    only: List[str] = typer.Option(
        PROGRAMMING_FILE_EXTENSIONS, help="Only include files with these extensions"
    ),
    ignore: List[str] = typer.Option([], help="Ignore files with these extensions"),
    custom_prompt: Optional[str] = typer.Option(None, help="Specify a custom prompt"),
    summarize: bool = typer.Option(False, help="Summarize the git diff"),
    peer_review: Optional[str] = typer.Option(
        None, help="Specify the branch to compare the git diff against"
    ),
):
    try:
        bro_mode, model = determine_bro_mode(chill, mid, chad, model)
        git_diff = fetch_git_diff(only, ignore, peer_review)
        if git_diff:
            run_diff(bro_mode, model, git_diff, custom_prompt, summarize)
    except Exception as e:
        console.print(f"[red]An error occurred: {e}[/red]")


if __name__ == "__main__":
    app()
