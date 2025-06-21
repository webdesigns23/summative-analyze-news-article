import re

def validate_task_word(word):
    if not re.match(r'^[A-Za-z]+$', word):
        raise ValueError("word can only contain letters.")
    if len(word) > 10:
        raise ValueError("Word cannot be more than 10 characters.")