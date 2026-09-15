import os

# Project root path
ROOT_DIR = r"E:\assign_ll\AI_Agent\et_agent_v1\Slack-ClawdBot-main"


# Keywords to search for OpenAI-related usage
KEYWORDS = [
    "openai",
    "OpenAI",
    "gpt-4",
    "gpt-4o",
    "text-embedding",
    "embedding",
    "OPENAI_API_KEY",
    "openaiApiKey",
    "api.openai.com"
]

# Ignore these folders
IGNORE_DIRS = {
    "node_modules",
    ".git",
    "dist",
    "build",
    "__pycache__"
}

def search_keywords():
    print("=" * 80)
    print("Searching for OpenAI-related code/files...")
    print("=" * 80)

    found_any = False

    for root, dirs, files in os.walk(ROOT_DIR):
        # Skip ignored folders
        dirs[:] = [d for d in dirs if d not in IGNORE_DIRS]

        for file in files:
            file_path = os.path.join(root, file)

            # Only check code/text files
            if not file.endswith((
                ".ts", ".js", ".json", ".md", ".env",
                ".yml", ".yaml", ".py", ".txt"
            )):
                continue

            try:
                with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                    lines = f.readlines()

                matches = []

                for line_no, line in enumerate(lines, start=1):
                    for keyword in KEYWORDS:
                        if keyword in line:
                            matches.append(
                                f"Line {line_no}: {line.strip()}"
                            )
                            break

                if matches:
                    found_any = True
                    print(f"\nFILE: {file_path}")
                    print("-" * 80)

                    for match in matches[:10]:  # show first 10 matches only
                        print(match)

                    if len(matches) > 10:
                        print(f"... and {len(matches) - 10} more matches")

            except Exception as e:
                print(f"Could not read: {file_path}")
                print(f"Reason: {e}")

    print("\n" + "=" * 80)

    if not found_any:
        print("No OpenAI-related code found.")
    else:
        print("Search completed.")

    print("=" * 80)


if __name__ == "__main__":
    search_keywords()