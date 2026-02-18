# Choose the one most appropriate of the following ADT for your implementation.
import stack
import queue
import deque
from sll import SLList

def match_brackets(s: str) -> bool:
    """
    Returns True if the sting has matching brackets, otherwise False.
    The program checks if for each bracket ( '(', '[' '}' ) there is a matching
    closing bracket. Note, the order and type of the brackets is important.
    For example, if you open a '(' and then a '[', then you need to "close" first
    the ']' before the ')'.
    An example of a matching bracket sting is for example
        "(a [b (c {dd} ) ] [2] )"
    where the following strings are not:
        "(a [b ) ]"  <--- closes [ with a )
        "]b ["   <--- close with ] before opening
        "{{ a }"   <-- missing }
    """
    open_brackets = ("(", "[", "{")
    closed_brackets =(")", "]", "}")
    bracket_stack = stack.Stack(SLList())
    brackets_match = False
    for ch in s:
        if ch in open_brackets:
            bracket_stack.push(ch)
            brackets_match = False
            continue
        if bracket_stack.is_empty() and ch in closed_brackets:
            return False

        if ch == ")" and bracket_stack.top() == "(":
            bracket_stack.pop()
            if bracket_stack.is_empty():
                brackets_match = True
            continue
        elif ch == "]" and bracket_stack.top() == "[":
            bracket_stack.pop()
            if bracket_stack.is_empty():
                brackets_match = True
            continue
        elif ch == "}" and bracket_stack.top() == "{":
            bracket_stack.pop()
            if bracket_stack.is_empty():
                brackets_match = True

    return brackets_match

def main():
    name = 'brackets.txt'
    try:
        with open(name, 'r') as file:
            lines = file.readlines()
            for line in lines:
                line = line.strip()
                print(f'{line:40} {match_brackets(line)}')
    except FileNotFoundError:
        print("File not found!")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()

