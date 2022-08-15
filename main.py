from art import logo
from art import vs
import random
from game_data import data
from replit import clear


def compare(guess, followerA, followerB):
  if followerA > followerB:
    return "A" == guess
  elif followerA < followerB:
    return "B" == guess
def get_random_account():
  return random.randint(0,49)
def game():
  game_shoiuld_continie = True
  compare_a = get_random_account()
  compare_b = get_random_account()
  follower_countA = data[compare_a]['follower_count']
  follower_countB = data[compare_b]['follower_count']
  
  score = 0
  while game_shoiuld_continie:
    compare_a = compare_b
    compare_b = get_random_account()
    # Aclear()
    print(logo)
    print(f"Compare A: {data[compare_a]['name']}, a {data[compare_a]['description']}, from {data[compare_a]['country']}.")
    print(vs)
    print(f"Against B: {data[compare_b]['name']}, a {data[compare_b]['description']}, from {data[compare_b]['country']}.")
    guess = input("Who has more followers? Type 'A' or 'B': ")
    is_correct = compare(guess, follower_countA, follower_countB)
    clear()
   # print(logo)
    if is_correct:
        score +=1
        print(f"You are right! Current score {score}")
        
    else:
        print(f"Sorry, that's wrong. Final score {score}")
        game_shoiuld_continie = False
game()