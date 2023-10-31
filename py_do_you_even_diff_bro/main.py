from typing import List, Optional
import typer
from rich.console import Console
from rich.table import Table
from constants import PROGRAMMING_FILE_EXTENSIONS, DETAILED_BROGRAMMER_DESCRIPTION
from models import GPTRequest, BroMode
from git import get_git_diff

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


@app.command()
def main(
    chill: bool = typer.Option(
        False, help="Get a chill, jr-level engineer, relaxed brogrammer PR review"
    ),
    mid: bool = typer.Option(
        False, help="Get a mid-level engineer, brogrammer PR review"
    ),
    chad: bool = typer.Option(
        False, help="Get a chad, sr-level engineer, intense brogrammer PR review"
    ),
    model: str = typer.Option("gpt-4", help="GPT model use 'gpt-3.5-turbo' or 'gpt-4'"),
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
        bro_mode = (
            BroMode.CHILL
            if chill
            else BroMode.MID
            if mid
            else BroMode.CHAD
            if chad
            else BroMode.CHILL
        )
        git_diff = get_git_diff(only, ignore, peer_review)

        if not git_diff:
            console.print("[red]No git diff for brogrammer[/red]")
            return

        display_summary_table(model, bro_mode, git_diff)
        console.print(
            f"[green]Building prompt for brogrammer in {bro_mode} mode on GPT model {model}[/green]"
        )
    except Exception as e:
        console.print(f"[red]An error occurred: {e}[/red]")


if __name__ == "__main__":
    app()
