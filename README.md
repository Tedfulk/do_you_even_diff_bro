# Introduction

This project is a command-line tool named BROGRAMMER, an AI Peer Review Bro. It uses the GPT model to review your code and provide feedback. The tool is designed to be flexible, allowing you to specify the level of feedback you want, the files you want to include or exclude, and even the branch to compare the git diff against.

<<<<<<< HEAD
## Detailed Description
=======
# Detailed Description
>>>>>>> bb087a9 (aider: Updated the README.md to include an introduction, a detailed description, and instructions on how to use the tool.)

The main functionality of the tool is contained within the `main.py` file. This script uses the `typer` library to parse command-line arguments and options. It also uses the `rich` library to display the results in a formatted table in the console.

The `git.py` file contains a function to get the git diff of the current project. It allows you to specify the file extensions to include or exclude, and the branch to compare against.

The `llm.py` file contains functions to interact with the GPT model. It sends a prompt to the model and parses the response.

The `models.py` file defines the `BroMode` enum, which represents the level of feedback you want from the tool.

The `utils.py` file contains utility functions used by the other scripts.

The `constants.py` and `commandments.py` files contain constant values and functions to generate prompts for the GPT model, respectively.

<<<<<<< HEAD
## How to Use


To use the tool, run the `python -m py_do_you_even_diff_bro.main` script with the desired options. For example, to get a chill, jr-level engineer review, use the `--chill` option:

```bash
python -m py_do_you_even_diff_bro.main --chill
```

To specify the GPT model to use, use the `--model` option:

```bash
python -m py_do_you_even_diff_bro.main --model gpt-4
```

To only include files with certain extensions, use the `--only` option:

```bash
python -m py_do_you_even_diff_bro.main --only .py .js
```

To ignore files with certain extensions, use the `--ignore` option:

```bash
python -m py_do_you_even_diff_bro.main --ignore .txt .md
```

To specify a custom prompt for the GPT model, use the `--prompt` option:

```bash
python -m py_do_you_even_diff_bro.main --prompt "Review this code"
```

To summarize the git diff, use the `--summarize` option:

```bash
python -m py_do_you_even_diff_bro.main --summarize
```

To specify the branch to compare the git diff against, use the `--peer-review` option:

```bash
python -m py_do_you_even_diff_bro.main --peer-review main
=======
# How to Use

To use the tool, run the `main.py` script with the desired options. For example, to get a chill, jr-level engineer review, use the `--chill` option:

```bash
python main.py --chill
```

To specify the GPT model to use, use the `--model` option:

```bash
python main.py --model gpt-4
```

To only include files with certain extensions, use the `--only` option:

```bash
python main.py --only .py .js
```

To ignore files with certain extensions, use the `--ignore` option:

```bash
python main.py --ignore .txt .md
```

To specify a custom prompt for the GPT model, use the `--prompt` option:

```bash
python main.py --prompt "Review this code"
```

To summarize the git diff, use the `--summarize` option:

```bash
python main.py --summarize
```

To specify the branch to compare the git diff against, use the `--peer-review` option:

```bash
python main.py --peer-review main
>>>>>>> bb087a9 (aider: Updated the README.md to include an introduction, a detailed description, and instructions on how to use the tool.)
```
# Introduction

This project is a command-line tool named BROGRAMMER, an AI Peer Review Bro. It uses the GPT model to review your code and provide feedback. The tool is designed to be flexible, allowing you to specify the level of feedback you want, the files you want to include or exclude, and even the branch to compare the git diff against.

# Detailed Description

The main functionality of the tool is contained within the `main.py` file. This script uses the `typer` library to parse command-line arguments and options. It also uses the `rich` library to display the results in a formatted table in the console.

The `git.py` file contains a function to get the git diff of the current project. It allows you to specify the file extensions to include or exclude, and the branch to compare against.

The `llm.py` file contains functions to interact with the GPT model. It sends a prompt to the model and parses the response.

The `models.py` file defines the `BroMode` enum, which represents the level of feedback you want from the tool.

The `utils.py` file contains utility functions used by the other scripts.

The `constants.py` and `commandments.py` files contain constant values and functions to generate prompts for the GPT model, respectively.

# How to Use

To use the tool, run the `main.py` script with the desired options. For example, to get a chill, jr-level engineer review, use the `--chill` option:

```bash
python main.py --chill
```

To specify the GPT model to use, use the `--model` option:

```bash
python main.py --model gpt-4
```

To only include files with certain extensions, use the `--only` option:

```bash
python main.py --only .py .js
```

To ignore files with certain extensions, use the `--ignore` option:

```bash
python main.py --ignore .txt .md
```

To specify a custom prompt for the GPT model, use the `--prompt` option:

```bash
python main.py --prompt "Review this code"
```

To summarize the git diff, use the `--summarize` option:

```bash
python main.py --summarize
```

To specify the branch to compare the git diff against, use the `--peer-review` option:

```bash
python main.py --peer-review main
```
