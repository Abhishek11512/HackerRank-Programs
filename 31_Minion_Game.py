#Minion Game

def minion_game(string):
    ScoreSt = 0
    ScoreKe = 0
    l = len(string)
    v = "AEIOU"
    for i in range(l):
        if string[i] in v:
            ScoreKe += l-i
        else:
            ScoreSt += l-i    
    if (ScoreSt == ScoreKe):
      print("Draw")
    elif (ScoreSt > ScoreKe):
      print(f"Stuart {ScoreSt}")
    else:
      print(f"Kevin {ScoreKe}")

if __name__ == '__main__':
    s = input()
    minion_game(s)