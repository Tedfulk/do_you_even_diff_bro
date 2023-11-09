PROGRAMMING_FILE_EXTENSIONS = [
    ".py",
    ".c",
    ".cpp",
    ".java",
    ".cs",
    ".php",
    ".vb",
    ".html",
    ".css",
    ".js",
    ".ts",
    ".asp",
    ".aspx",
    ".cfm",
    ".cgi",
    ".pl",
    ".cer",
    ".htm",
    ".xhtml",
    ".shtml",
    ".jsp",
    ".jsx",
    ".tsx",
    ".vue",
    ".solid",
    ".toml",
    ".md",
    ".go",
    ".rs",
    ".swift",
    ".rb",
    ".erb",
    ".rake",
    ".gemspec",
    ".ru",
    ".yml",
    ".scss",
    ".sass",
    ".coffee",
    ".haml",
    ".sh",
    ".bash",
    ".zsh",
    ".fish",
    ".json",
    ".xml",
    ".sql",
    ".kt",
    ".kts",
    ".dart",
    ".groovy",
    ".svelte",
    ".lua",
    ".jl",
]

DETAILED_BROGRAMMER_DESCRIPTION = """
First export your api key, then run an example below.

You can get an API key here: https://platform.openai.com/account/api-keys

Export command in terminal:
      `export OPENAI_API_KEY=<your openai apikey>`

Examples:
  * I want a chill review on my .py and .js files:
      brogrammer --chill --only .py .js

  * I'm about to ship production, mission critical UI code, I need a hardcore review on my frontend code:
      brogrammer --chad --model gpt-4 --only .js .jsx .tsx .svelte

  * I'm about to a fullstack app and need a comprehensive mid level review on all my code excluding .tsx files:
      brogrammer --mid --model gpt-4 --ignore .tsx

  * I want legit reviews of all the diff:
      brogrammer --chad 
"""
