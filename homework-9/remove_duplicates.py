# remove_duplicates.py
import re

def remove_consecutive_duplicates(s):
    # Регулярное выражение для удаления повторяющихся слов
    return re.sub(r'\b(\w+)\s+\1\b', r'\1', s)
