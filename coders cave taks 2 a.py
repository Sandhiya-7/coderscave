import time
import random

def generate_random_text(words_count):
    word_list = ["apple", "banana", "cherry", "dog", "elephant"]
    random_text = ' '.join(random.choice(word_list) for _ in range(words_count))
    return random_text

def calculate_typing_speed(start_time, end_time, typed_words):
    total_time_seconds = end_time - start_time
    words_per_minute = (typed_words / total_time_seconds) * 60
    return words_per_minute

def typing_speed_test():
    print("Welcome to the Typing Speed Tester!")
    input("Press Enter when you are ready to start...")

    # Generate random text
    words_count = 12
    random_text = generate_random_text(words_count)
    print("\nType the following text:")
    print(random_text)

    # Record start time
    start_time = time.time()

    # User types the text
    typed_text = input("\nType here: ")

    # Record end time
    end_time = time.time()

    # Calculate typing speed
    typed_words = len(typed_text.split())
    speed = calculate_typing_speed(start_time, end_time, typed_words)

    # Compare typed and original text for accuracy
    accuracy = sum(a == b for a, b in zip(typed_text, random_text)) / max(len(typed_text), 1) * 100

    print("\nTyping Speed: {:.2f} WPM".format(speed))
    print("Accuracy: {:.2f}%".format(accuracy))

if __name__ == "__main__":
    typing_speed_test()
