from app.text_processor import count_words, extract_title


def test_count_words():
    assert count_words("hello world") == 2


def test_empty_text():
    assert count_words("") == 0


def test_multiple_spaces():
    assert count_words("hello    world") == 2


def test_extract_title():
    text = "PaperPal Document\nThis is the document body."
    assert extract_title(text) == "PaperPal Document"


def test_extract_title_with_whitespace():
    text = "\n   PaperPal Document   \nBody"
    assert extract_title(text) == "PaperPal Document"


def test_extract_title_skips_empty_lines():
    text = "\n\nPaperPal Document\nBody"
    assert extract_title(text) == "PaperPal Document"


def test_extract_title_empty():
    assert extract_title("") == ""
