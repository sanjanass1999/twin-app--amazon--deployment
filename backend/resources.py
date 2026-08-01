import json
from pathlib import Path

DATA_DIR = Path("./data")


def load_text_file(filename: str, fallback: str = "") -> str:
    path = DATA_DIR / filename
    if path.exists():
        return path.read_text(encoding="utf-8")
    return fallback


# Load text / markdown resources
summary = load_text_file("summary.md")
style = load_text_file("style.md")
linkedin = load_text_file("linkedin.md", fallback="LinkedIn profile not available")

# Load structured JSON data
facts_path = DATA_DIR / "facts.json"
if facts_path.exists():
    with open(facts_path, "r", encoding="utf-8") as f:
        facts = json.load(f)
else:
    facts = {}