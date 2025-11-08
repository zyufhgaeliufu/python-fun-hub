# --- Python Fun Hub Ultimate (Upgraded + True Universal Math Solver) ---
import time
import random
from math import *
from sympy import symbols, Eq, solve, diff, integrate, limit, sin, cos, tan, sqrt, sympify

# --- Smooth print function for animation ---
def smooth_print(text, delay=0.01):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

# --- Mini-games ---
def guess_number():
    number = random.randint(1, 100)
    smooth_print("Guess the number between 1 and 100")
    while True:
        guess = input("Your guess: ")
        try:
            guess = int(guess)
            if guess < number:
                smooth_print("Too low!")
            elif guess > number:
                smooth_print("Too high!")
            else:
                smooth_print("Correct!")
                break
        except:
            smooth_print("Invalid input!")

def rock_paper_scissors():
    smooth_print("Rock, Paper, Scissors!")
    choices = ["rock", "paper", "scissors"]
    comp = random.choice(choices)
    player = input("Enter rock, paper, or scissors: ").lower()
    if player not in choices:
        smooth_print("Invalid choice!")
    else:
        smooth_print(f"Computer chose {comp}")
        if player == comp:
            smooth_print("Tie!")
        elif (player=="rock" and comp=="scissors") or \
             (player=="paper" and comp=="rock") or \
             (player=="scissors" and comp=="paper"):
            smooth_print("You win!")
        else:
            smooth_print("You lose!")

def dice_roll():
    smooth_print(f"You rolled a {random.randint(1,6)}")

def coin_flip():
    smooth_print(f"Coin flip: {random.choice(['Heads','Tails'])}")

def trivia():
    smooth_print("Trivia: What's the fastest land animal? Cheetah!")

def hangman():
    word = random.choice(["python","fun","hub","ultimate","game"])
    guessed = []
    tries = 6
    while tries > 0:
        display = ''.join([c if c in guessed else '_' for c in word])
        smooth_print(display)
        if '_' not in display:
            smooth_print("You guessed it!")
            break
        guess = input("Guess a letter: ").lower()
        if guess in guessed:
            smooth_print("Already guessed!")
        elif guess in word:
            smooth_print("Correct!")
            guessed.append(guess)
        else:
            smooth_print("Wrong!")
            guessed.append(guess)
            tries -= 1

def math_challenge():
    problem = f"{random.randint(1,50)} + {random.randint(1,50)} * {random.randint(1,10)}"
    smooth_print(f"Solve: {problem}")
    answer = eval(problem)
    guess = input("Answer: ")
    if guess == str(answer):
        smooth_print("Correct!")
    else:
        smooth_print(f"Wrong! Correct answer was {answer}")

def word_scramble():
    words = ["python","ultimate","fun","solver","game"]
    word = random.choice(words)
    scrambled = ''.join(random.sample(word,len(word)))
    smooth_print(f"Unscramble: {scrambled}")
    guess = input("Your guess: ")
    if guess == word:
        smooth_print("Correct!")
    else:
        smooth_print(f"Wrong! Correct was {word}")

def guess_even_odd():
    number = random.randint(1,100)
    guess = input("Even or Odd? ").lower()
    if (number%2==0 and guess=="even") or (number%2!=0 and guess=="odd"):
        smooth_print(f"Correct! It was {number}")
    else:
        smooth_print(f"Wrong! It was {number}")

def reverse_string():
    s = input("Enter a string: ")
    smooth_print(s[::-1])

def guess_square():
    number = random.randint(1,20)
    smooth_print(f"Guess the square of {number}")
    guess = int(input())
    if guess == number**2:
        smooth_print("Correct!")
    else:
        smooth_print(f"Wrong! It was {number**2}")

def guess_cube():
    number = random.randint(1,10)
    smooth_print(f"Guess the cube of {number}")
    guess = int(input())
    if guess == number**3:
        smooth_print("Correct!")
    else:
        smooth_print(f"Wrong! It was {number**3}")

def number_guess_range():
    low = random.randint(1,50)
    high = random.randint(51,100)
    number = random.randint(low,high)
    smooth_print(f"Guess a number between {low} and {high}")
    guess = int(input())
    if guess == number:
        smooth_print("Correct!")
    else:
        smooth_print(f"Wrong! It was {number}")

def random_math():
    problem = f"{random.randint(1,50)} + {random.randint(1,50)} - {random.randint(1,20)}"
    smooth_print(f"Solve: {problem}")
    answer = eval(problem)
    guess = input("Answer: ")
    if guess == str(answer):
        smooth_print("Correct!")
    else:
        smooth_print(f"Wrong! Correct was {answer}")

def flip_coin_times():
    n = int(input("How many flips? "))
    results = [random.choice(["Heads","Tails"]) for _ in range(n)]
    smooth_print(f"Results: {results}")

def rock_paper_scissors_best_of():
    rounds = int(input("Best of how many rounds? "))
    player_score = 0
    comp_score = 0
    for _ in range(rounds):
        choices = ["rock", "paper", "scissors"]
        comp = random.choice(choices)
        player = input("Enter rock, paper, scissors: ").lower()
        if player not in choices:
            smooth_print("Invalid choice!")
            continue
        if player==comp:
            smooth_print(f"Tie! Computer chose {comp}")
        elif (player=="rock" and comp=="scissors") or (player=="paper" and comp=="rock") or (player=="scissors" and comp=="paper"):
            smooth_print(f"You win this round! Computer chose {comp}")
            player_score +=1
        else:
            smooth_print(f"You lose this round! Computer chose {comp}")
            comp_score +=1
    smooth_print(f"Final Score: You {player_score} - Computer {comp_score}")

# --- All mini-games list ---
mini_games = [guess_number, rock_paper_scissors, dice_roll, coin_flip, trivia, hangman,
              math_challenge, word_scramble, guess_even_odd, reverse_string, guess_square,
              guess_cube, number_guess_range, random_math, flip_coin_times, rock_paper_scissors_best_of]

# --- Random facts ---
facts = ["Honey never spoils.", "Octopuses have three hearts.", "Bananas are berries.",
         "Sharks existed before trees.", "There are more stars than grains of sand on Earth."]

# --- Universal Math Solver (True Universal Version) ---
def universal_math_solver():
    smooth_print("Universal Math Solver (type 'quit' to exit)")
    # Define common symbols for algebra, calculus, etc.
    x, y, z, a, b, c = symbols('x y z a b c')
    while True:
        problem = input("Enter problem: ")
        if problem.lower() == "quit":
            break
        try:
            # --- Detect equations ---
            if '=' in problem:
                left_str, right_str = problem.split('=')
                left_expr = sympify(left_str)
                right_expr = sympify(right_str)
                eq = Eq(left_expr, right_expr)
                result = solve(eq)
            else:
                # Try to evaluate as expression
                expr = sympify(problem)
                result = expr.evalf()
            smooth_print(f"Answer: {result}")
        except Exception as e:
            smooth_print(f"Cannot solve this problem: {e}")

# --- Main menu ---
def main_menu():
    while True:
        smooth_print("\n--- Python Fun Hub Ultimate ---")
        smooth_print("1. Pick a mini-game")
        smooth_print("2. Random fact")
        smooth_print("3. Universal Math Solver")
        smooth_print("4. Random mini-game")
        smooth_print("5. Quit")
        choice = input("Choose: ")
        if choice == "1":
            for idx, game in enumerate(mini_games,1):
                smooth_print(f"{idx}. {game.__name__.replace('_',' ').title()}")
            g = int(input("Pick game number: "))
            if 1 <= g <= len(mini_games):
                mini_games[g-1]()
            else:
                smooth_print("Invalid choice!")
        elif choice == "2":
            smooth_print(random.choice(facts))
        elif choice == "3":
            universal_math_solver()
        elif choice == "4":
            random.choice(mini_games)()
        elif choice == "5":
            smooth_print("Goodbye!")
            break
        else:
            smooth_print("FUCK YOU PRICK")  # Troll message

# --- Start ---
if __name__=="__main__":
    main_menu()
