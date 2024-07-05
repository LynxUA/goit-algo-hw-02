from collections import deque

def is_palindrome(input_string):
    normalized_string = ''.join(input_string.lower().split())
    
    char_deque = deque(normalized_string)
    
    while len(char_deque) > 1:
        if char_deque.popleft() != char_deque.pop():
            return False
    return True

print(is_palindrome("Я несу гусеня"))
print(is_palindrome("Де помити мопед"))
print(is_palindrome("hello"))
