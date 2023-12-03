# Stacks
def is_balanced(expression):
    """
    Checks if the given expression containing parentheses, curly braces, and square brackets is balanced.

    Args:
    expression (str): The input expression to be checked for balance.

    Returns:
    bool: True if the expression is balanced, False otherwise.
    """
    stack = []
    mapping = {")": "(", "}": "{", "]": "["}
    for char in expression:
        if char in mapping:
            top_element = stack.pop() if stack else '#'
            if mapping[char] != top_element:
                return False
        else:
            stack.append(char)
    return not stack

expression1 = "([]{})"
expression2 = "([)]"
print(is_balanced(expression1))  # Output: True
print(is_balanced(expression2))  # Output: False


# Sequences (Lists/Tuples)
def remove_duplicates(sequence):
    """
    Removes duplicates from the given sequence (list or tuple) while maintaining the original order of elements.

    Args:
    sequence (list or tuple): The input sequence from which duplicates are to be removed.

    Returns:
    list: A new sequence with duplicates removed.
    """
    seen = set()
    return [x for x in sequence if not (x in seen or seen.add(x))]

input_sequence = [2, 3, 2, 4, 5, 3, 6, 7, 5]
result = remove_duplicates(input_sequence)
print(result)  # Output: [2, 3, 4, 5, 6, 7]


# Dictionaries
import re
from collections import Counter

def word_frequency(sentence):
    """
    Returns a dictionary containing the frequency of each word in the given sentence.

    Args:
    sentence (str): The input sentence for word frequency analysis.

    Returns:
    dict: A dictionary containing the frequency of each word in the sentence.
    """
    words = re.findall(r'\w+', sentence.lower())
    return dict(Counter(words))

sentence = "This is a test sentence. This sentence is a test."
result = word_frequency(sentence)
print(result)

