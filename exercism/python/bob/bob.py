def response(hey_bob: str) -> str: 
    def is_question(hey_bob: str) -> bool:
        return True if hey_bob != "" and hey_bob[-1] == "?" else False
    return ("Calm down, I know what I'm doing!" if is_question(hey_bob) and hey_bob.isupper()\
            else "Fine. Be that way!" if hey_bob.isspace() or hey_bob == ""\
            else "Sure." if is_question(hey_bob.strip())\
            else "Whoa, chill out!" if hey_bob.isupper()\
            else "Whatever."\
            )
