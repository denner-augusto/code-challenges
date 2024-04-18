def response(hey_bob: str) -> str: 
    hey_bob_strip = hey_bob.rstrip()
    is_question = hey_bob_strip.endswith("?")
    is_yelling = hey_bob_strip.isupper()
    if not hey_bob_strip or hey_bob_strip.isspace():
        return "Fine. Be that way!"
    elif is_question and is_yelling:
        return "Calm down, I know what I'm doing!"
    elif is_question:
        return "Sure."
    return "Whoa, chill out!" if is_yelling else "Whatever." 