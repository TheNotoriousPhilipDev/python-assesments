def minion_game(string):
    vowel = 'AEIOU'
    StuartPoints = 0
    KevinPoints = 0
    l = 0
    l = len(string)
    for i in range(l):
        if string[i] not in vowel:
            
            StuartPoints += l - i
        else:
            
            KevinPoints += l - i
    if StuartPoints > KevinPoints:
        print("Stuart", StuartPoints)
    elif StuartPoints < KevinPoints:
        print("Kevin", KevinPoints)
    else:
        print("Draw") 
    return
    

if __name__ == '__main__':
    s = input()
    minion_game(s)
