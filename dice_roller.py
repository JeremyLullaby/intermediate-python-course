import random
def main():
  dice_rolls = int(input('How many dice would you like to roll? '))
  dice_sides = int(input('How many sides are the dice? '))
  dice_sum = 0
  for i in range(0, dice_rolls):
    roll = random.randint(1, dice_sides)
    dice_sum += roll
    if roll == 1:
      print(f'You rolled : {roll} Critical Fail!')
    elif roll == dice_sides:
      print(f'You rolled : {roll} Successful Crit!')
    else:
      print(f'You rolled : {roll}')

  print(f'Total : {dice_sum}')

if __name__== "__main__":
  main()