def minion_game(string):
    # your code goes here
    vowels = 'AEIOU'

    kevin = 0
    stuart = 0
    for i in xrange(len(string)):
        if string[i] in vowels:
            kevin += (len(string)-i)
        else:
            stuart += (len(string)-i)

    if kevin > stuart:
        print "Kevin", kevin
    elif kevin < stuart:
        print "Stuart", stuart
    else:
        print "Draw"
        
if __name__ == '__main__':
    s = raw_input()
    minion_game(s)
