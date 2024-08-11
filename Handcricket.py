import random
i = list(range(1, 11)) 

def bat():
    batscore = 0
    while True:
        g = int(input("Enter your number: "))
        if random.choice(i) == g:
            print(f"You are out and your score is: {batscore}")
            return batscore
        batscore += g
        print(f"Your score is: {batscore}")

def ball():
    ballscore = 0
    while True:
        g = int(input("Enter your number: "))
        if random.choice(i) == g:
            print(f"Hurry! You bowled out the computer with {ballscore}")
            return ballscore
        ballscore += g
        print(f"Computer's score is: {ballscore}")

def game_result(pscore, cscore):
    if pscore > cscore:
        return "Congrats, you won!"
    elif pscore < cscore:
        return "You lost."
    return "It's a Draw."

print("Welcome to hand cricket!")
d = input("What do you choose (ODD/EVEN): ").lower()
b, c = int(input("Choose a number between (1-10): ")), random.choice(i)
print(f"You chose {b} and the computer chose {c}")

if (b + c) % 2 == (0 if d == "even" else 1):
    print("Congratulations, you have won the toss.")
    if input("What do you choose (bat/ ball)? : ").lower() == "bat":
        pscore, cscore = bat(), ball()
    else:
        cscore, pscore = ball(), bat()
else:
    print("Oops, you have lost the toss.\nComputer has chosen to bowl. Get ready to bat first.")
    pscore, cscore = bat(), ball()

print(game_result(pscore, cscore))
