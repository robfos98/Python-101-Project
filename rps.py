import random
rps = 'prs'
p, r, s = 'Paper', 'Rock', 'Scissors'
win = loss = 0
intro = 'Please throw Rock, Paper, or Scissors (R, P, S), or throw Q to quit.'
def throw():
    print('\nThrow:')
    x = input().lower()
    if x == 'p' or x == p.lower(): return 'p'
    elif x == 'q' or x == 'quit': return 'q' 
    elif x == 'r' or x == r.lower(): return 'r'
    elif x == 's' or x == s.lower(): return 's'
    else: return f'I\'m sorry, I didn\'t catch that. {intro}'
def output(letter):
    match letter:
        case 'p': return p
        case 'r': return r
        case 's': return s

print('\nHello!')
print('This program can play Rock, Paper, Scissors.')
print(intro)
while True:
    x = throw()
    if len(x) > 1:
        print(x)
        continue
    x = rps.find(x)
    if x < 0: break
    beat = random.choice(rps)
    match (x - rps.find(beat)) % 3:
        case 0: print('A tie.')
        case 1:
            print(f'Sorry, but I threw {output(beat)}.')
            loss += 1;
        case 2:
            print(f'Nice, you beat {output(beat)}.')
            win += 1;
    print(f'You\'ve won {win} games, and lost {loss}.')