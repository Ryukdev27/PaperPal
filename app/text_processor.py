def count_words(text: str) -> int:
    """Return the number of words in a text."""

    if not text:
        return 0

    return len(text.split())


def extract_title(text: str) -> str:
    """Extract the first non-empty line as a document title."""

    if not text:
        return ""

    for line in text.splitlines():
        title = line.strip()

        if title:
            return title

    return ""
