import random
qu = input("Do you wanna play?").lower()
if qu == "yes":
    print("Welcome")
else:
    quit()

top = input("Enter top of range: ")
if top.isdigit():
    top = int(top)
    if top <= 0:
        print("Choose a number above 0")
else:
    print("Use numbers ONLY")

ra = random.randint(0, top)
counter = 0
while True:
    que = int(input("Guess a number"))
    counter += 1
    if que == ra:
        print("Correct !!")
        break
    elif que > ra:
        print("Too High")
    else:
        print("Too Low")
print("You seceeded in", counter, "no. of attempts. Cheers !!")