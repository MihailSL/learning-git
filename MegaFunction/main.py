from __future__ import annotations  # for Python 2.X
import random


def unusual_printing(word: str) -> str:
    """Returns word+exlamation"""

    exclamations = ["!", "?", ".", ",", "?!", "!?", "!!!", ";", "???", ":", "...", "|"]
    return f"{word}{random.choice(exclamations)}"


if __name__ == "__main__":
    print(unusual_printing("Hello world"))
