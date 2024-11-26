import random


def display_random_joke():
    jokes = [
        "Why do Python programmers prefer dark mode? Because light attracts bugs! 🐛",
        "Why was the function feeling lazy? It didn’t want to return to work! 😴",
        "How do you tell if a Python developer is introverted? They look at your shoes instead of their own when talking to you. 👟",
        "Why did the Python programmer get stuck in the shower? The instructions said 'wash', 'rinse', 'repeat'. 🌀",
        "What’s a programmer's favorite place to hang out? The foo bar. 🍹",
        "Why do Java programmers have to wear glasses? Because they don’t C#. 👓",
        "How do you comfort a JavaScript bug? You console it. 📋",
        "Why did the Python programmer break up with JavaScript? Too many arguments. 💔",
        "Why are Python jokes so funny? Because they’re interpreted, not compiled! 😄",
        "Why was the Python developer always calm? They had plenty of try-except blocks to catch all their problems! 🧘‍♂️"
    ]

    # Select a random joke
    joke = random.choice(jokes)

    # Display the joke
    print("\nHere's a joke for you:\n")
    print(f"🐍 {joke}")


if __name__ == "__main__":
    display_random_joke()
