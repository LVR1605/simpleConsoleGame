import pickle

def load_high_scores():
    try:
        with open("high_scores.pkl", "rb") as file:
            return pickle.load(file)
    except FileNotFoundError:
        return {}

def save_high_scores(high_scores):
    with open("high_scores.pkl", "wb") as file:
        pickle.dump(high_scores, file)

def display_high_scores(high_scores):
    print("High Scores:")
    for name, score in high_scores.items():
        print(f"{name}: {score}")

def ask_question(question, options, answer):
    print(question)
    for idx, option in enumerate(options):
        print(f"{chr(97 + idx)}) {option}")
    response = input("Your answer: ").strip().lower()
    return response == answer.lower()

def play_quiz(questions):
    score = 0
    for question, options_and_answer in questions.items():
        question_text, options, answer = options_and_answer
        if ask_question(question_text, options, answer):
            print("Correct!")
            score += 1
        else:
            print("Incorrect!")
    return score

def display_high_scores(high_scores):
    print("High Scores:")
    sorted_scores = sorted(high_scores.items(), key=lambda x: x[1], reverse=True)
    for name, score in sorted_scores:
        print(f"{name}: {score}")


def main():
    high_scores = load_high_scores()

    while True:
        name = input("Enter your name: ").strip()
        questions = {
            "What is the capital of France?": ("What is the capital of France?", ["Paris", "Berlin", "Rome", "Madrid"], "a"),
            "Which planet is known as the Red Planet?": ("Which planet is known as the Red Planet?", ["Mars", "Venus", "Jupiter", "Saturn"], "a"),
            "What is the largest mammal?": ("What is the largest mammal?", ["Elephant", "Giraffe", "Blue Whale", "Hippopotamus"], "c"),
            "What is the chemical symbol for water?": ("What is the chemical symbol for water?", [ "CO2", "H2O", "NaCl", "O2"], "b"),
            "Who wrote 'Romeo and Juliet'?": ("Who wrote 'Romeo and Juliet'?", ["Shakespeare", "Charles Dickens", "Mark Twain", "Jane Austen"], "a"),
            "What is the tallest mountain in the world?": ("What is the tallest mountain in the world?", ["K2", "Kangchenjunga", "Lhotse", "Mount Everest"], "d"),
            "Which gas do plants primarily absorb during photosynthesis?": ("Which gas do plants primarily absorb during photosynthesis?", ["Oxygen", "Carbon Dioxide", "Nitrogen", "Hydrogen"], "b"),
            "Who is known as the father of modern physics?": ("Who is known as the father of modern physics?", ["Isaac Newton", "Albert Einstein", "Galileo Galilei", "Niels Bohr"], "b"),
            "Which country is the largest by land area?": ("Which country is the largest by land area?", ["Canada", "China", "Russia", "United States"], "c"),
            "What is the chemical symbol for gold?": ("What is the chemical symbol for gold?", ["Ag", "Au", "Pt", "Pb"], "b"),
            "What is the currency of Japan?": ("What is the currency of Japan?", ["Dollar", "Euro", "Pound", "Yen"], "d"),
            "Who painted the Mona Lisa?": ("Who painted the Mona Lisa?", ["Pablo Picasso", "Vincent van Gogh", "Leonardo da Vinci", "Michelangelo"], "c"),
            "What is the chemical symbol for iron?": ("What is the chemical symbol for iron?", ["Fe", "Ir", "In", "Io"], "a"),
            "Which element is the most abundant in the Earth's atmosphere?": ("Which element is the most abundant in the Earth's atmosphere?", ["Oxygen", "Carbon", "Hydrogen", "Nitrogen"], "d"),
            "What is the largest ocean on Earth?": ("What is the largest ocean on Earth?", ["Pacific Ocean", "Atlantic Ocean", "Indian Ocean", "Arctic Ocean"], "a"),
            "Who was the first person to step on the moon?": ("Who was the first person to step on the moon?", ["Buzz Aldrin", "Neil Armstrong", "Yuri Gagarin", "Alan Shepard"], "b"),
            "Which animal is known as the 'ship of the desert'?": ("Which animal is known as the 'ship of the desert'?", ["Camel", "Horse", "Elephant", "Lion"], "a"),
            "What is the chemical symbol for silver?": ("What is the chemical symbol for silver?", ["Si", "Ag", "Au", "Al"], "b"),
            "Who discovered penicillin?": ("Who discovered penicillin?", ["Alexander Fleming", "Marie Curie", "Louis Pasteur", "Robert Koch"], "a"),
            "What is the powerhouse of the cell?": ("What is the powerhouse of the cell?", ["Mitochondria", "Nucleus", "Ribosome", "Endoplasmic reticulum"], "a")
        }


        score = play_quiz(questions)
        print(f"Your score: {score}")

        if name in high_scores:
            if score > high_scores[name]:
                print("Congratulations! You've beaten your previous high score.")
                high_scores[name] = score
        else:
            print("Congratulations! You've set a new high score.")
            high_scores[name] = score

        save_high_scores(high_scores)
        display_high_scores(high_scores)

        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != "yes":
            break

if __name__ == "__main__":
    main()
