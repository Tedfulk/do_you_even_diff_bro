import typer
from rich.prompt import Prompt
from typing import List, Optional

PROGRAMMING_FILE_EXTENSIONS = ["py", "js", "java", "c", "cpp", "go", "rb", "php", "ts", "cs", "swift", "kt", "rs"]

app = typer.Typer(help="Awesome CLI user manager.")

@app.command()
def main(
    chill: bool = typer.Option(False, help="Get a chill, jr-level engineer, relaxed diffbro PR review"),
    mid: bool = typer.Option(False, help="Get a mid-level engineer, diffbro PR review"),
    chad: bool = typer.Option(False, help="Get a chad, sr-level engineer, intense diffbro PR review"),
    model: str = typer.Option("gpt-4", help="GPT model use 'gpt-3.5-turbo' or 'gpt-4'"),
    only: List[str] = typer.Option(PROGRAMMING_FILE_EXTENSIONS, help="Only include files with these extensions"),
    ignore: List[str] = typer.Option([], help="Ignore files with these extensions"),
    prompt: Optional[str] = typer.Option(None, help="Specify a custom prompt"),
    summarize: bool = typer.Option(False, help="Summarize the git diff"),
    peer_review: Optional[str] = typer.Option(None, help="Specify the branch to compare the git diff against"),
):
    try:
        # typer logic goes here
        pass
    except Exception as e:
        # Log the error to a durable storage medium
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    app()
