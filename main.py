import random

# Quotes grouped by difficulty
easy_history = ["I came, I saw, I conquered",
                 "Those who cannot remember the past are condemned to repeat it",
                 "If I had eith hours to chop down a tree, I'd spend the first six sharpening my axe",
                 "When the rich wage war, it's the poor who die"]
easy_history_answer = ["Julius Caesar", 
                        "George Santayana",
                        "Abraham Lincoln",
                        "Jean-Paul Sartre"]

medium_history = ["History is a set of lies agreed upon",
                 "I have become Death, the destroyer of worlds",
                 "In war, truth is the first casualty",
                 "I die the king's faithful servant, but God's first",
                 "The lamps are going out all over Europe. We shall not see them lit again in our lifetime"]
medium_history_answer = ["Napoleon Bonaparte",
                         "J. Robert Oppenheimer",
                         "Aeschylus",
                         "Sir Thomas More",
                         "Sir Edward Grey"]

hard_history = ["Our greatest glory is not in never falling, but in rising every time we fall",
                "Following the light of the sun, we left the Old World",
                "I am the State",
                "I would rather die standing than live on my knees",
                "The only thing we have to fear, is fear itself"]
hard_history_answer = ["Confucius", 
                        "Christopher Columbus", 
                        "Louis XIV",
                        "Emiliano Zapata",
                        "Franklin D. Roosevelt"]

easy_fiction = ["I am your father", 
                "Winter is coming",
                "Hope is the only thing stronger than fear",
                "You either die a hero, or live long enough to see yourself become the villain",
                "The past can hurt. But the way I see it, you can either run from it, or learn from it"]
easy_fiction_answer = ["Darth Vader (Star Wars)", 
                    "Every Stark ever (Game of Thrones)",
                    "President Snow (The Hunger Games)",
                    "Harvey Dent (The Dark Knight)",
                    "Rafiki (The Lion King)"]

medium_fiction = ["Fear cuts deeper than swords", 
                "Men go to war over women like you",
                "To deny our own impulses is to deny the very thing that makes us human",
                "Peace is a lie. There is only passion",
                "A man who won't fight for what he wants deserves what he gets",
                "Do or do not. There is no try"]
medium_fiction_answer = ["Arya Stark (Game of Thrones)",
                        "Achilles (Troy)",
                        "Mouse (The Matrix)",
                        "The Sith Code (Star Wars)",
                        "Tommy Shelby (Peaky Blinders)",
                        "Yoda (Star Wars)"]

hard_fiction = ["All that we see or seem is but a dream within a dream",
                "All we have to decide is what to do with the time that is given us",
                "Fear is the mind-killer",
                "A man who won't die for something is not fit to live",
                "War is not about glory. War is about victory"]
hard_fiction_answer = ["Edgar Allan Poe (A Dream Within a Dream)", 
                        "Gandalf (The Lord of the Rings)", 
                        "Bene Gesserit (Dune)", 
                        "Ezio Auditore (Assassins Creed 2)",
                        "Commander Shepard (Mass Effect)"]

def number_generator(a, b):
    return random.randint(a, b)

def ask_question(difficulty, history_quotes, history_answers, fiction_quotes, fiction_answers):
    quote_list = history_quotes + fiction_quotes
    quote = random.choice(quote_list)

    answer = input(f"Quote: '{quote}'\nIs this history or fiction? ").strip().lower()

    if quote in history_quotes and answer == "history":
        print(f"Correct! This was said by {history_answers[history_quotes.index(quote)]}.")
    elif quote in fiction_quotes and answer == "fiction":
        print(f"Correct! This was said by {fiction_answers[fiction_quotes.index(quote)]}.")
    else:
        print("Wrong answer!")

def game():
    print("You will be guessing whether the quote is from history or fiction! Are you ready?")
    
    while True:
        difficulty = input("Choose difficulty: easy, medium, hard, or type 'exit' to quit: ").strip().lower()

        if difficulty == "easy":
            ask_question(difficulty, easy_history, easy_history_answer, easy_fiction, easy_fiction_answer)
        elif difficulty == "medium":
            ask_question(difficulty, medium_history, medium_history_answer, medium_fiction, medium_fiction_answer)
        elif difficulty == "hard":
            ask_question(difficulty, hard_history, hard_history_answer, hard_fiction, hard_fiction_answer)
        elif difficulty == "exit":
            print("Thanks for playing!")
            break
        else:
            print("Invalid input. Please enter easy, medium, hard, or exit.")

game()
