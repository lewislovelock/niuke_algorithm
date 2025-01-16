def reverse_words(s: str) -> str:
    """
    Reverse the order of letters in each word while preserving non-letter characters.
    
    Test Cases:
    >>> reverse_words("Hello, world.")
    "olleH, dlrow."
    >>> reverse_words("Python, is awesome?")
    "nohtyP, si emosewa?"
    >>> reverse_words("Test, this out.")
    "tseT, siht tuo."
    
    Args:
        s (str): Input string containing letters and non-letter characters
    
    Returns:
        str: String with letters in each word reversed
    """
    words = []
    result = []
    for c in s:
        if c.isalpha():
            words.append(c)
        else:
            if words:
                result.append("".join(reversed(words)))  # Use reversed() instead of .reverse()
                words = []
            result.append(c)

    if words:
        result.append("".join(reversed(words)))  # Use reversed() here as well

    return "".join(result)

if __name__ == "__main__":
    # Test command: python reverse_words.py
    import doctest
    doctest.testmod()
    # s = input().strip()
    # print(reverse_words(s))