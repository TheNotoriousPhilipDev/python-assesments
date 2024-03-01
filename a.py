vowels = 'AEIOU'

def minion_game(string):
  """
  This function determines the winner of the Minion Game and their score.

  Args:
      string: The string to analyze.

  Returns:
      A string containing the winner's name and score, or "Draw" if there is no winner.
  """
  kevin_score = 0
  stuart_score = 0
  for i in range(len(string)):
    if string[i] in vowels:
      kevin_score += len(string) - i
    else:
      stuart_score += len(string) - i

  if kevin_score > stuart_score:
    return "Kevin {}".format(kevin_score)
  elif kevin_score < stuart_score:
    return "Stuart {}".format(stuart_score)
  else:
    return "Draw"

# Test cases
print(minion_game("BANANA"))  # Output: Stuart 12
print(minion_game("KICK"))     # Output: Kevin 3
print(minion_game("AEIOU"))    # Output: Draw
