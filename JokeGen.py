# The program generates a random joke from a list of jokes and displays it to the user.

import random

def main():
    print("\n🐍 Python Joke Generator 🐍")
    print("=" * 50)
    print(get_random_joke())
    print("=" * 50)

def get_random_joke():
    jokes = [
        "Why do programmers prefer dark mode? Because light attracts bugs!",
        "How many programmers does it take to change a light bulb? None, that's a hardware problem!",
        "Why do Python programmers prefer snakes over dogs? Because Pythons don’t bark, they just hiss!",
        "What is a programmer’s favorite place to hang out? The Foo Bar!",
        "Why was the JavaScript developer sad? Because he didn't 'null' his feelings!"
        "Why do C programmers have trouble making friends? Because they have too many pointers!",
        "Why did the developer go broke? Because he used up all his cache!",
        "Why do Java developers wear glasses? Because they don’t C#!",
        "Why was the function feeling so lost? Because it didn’t return anything!",
        "Why was the Git repository so tense? Because it had too many conflicts!"
        ]
    return random.choice(jokes)

main()