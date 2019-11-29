"""This is a program that asks for user's name, age and after that, pops up a beautiful message."""

print("Hey, my name is Gage Sebastian! What is your name?")
user_name = input()

print(f'Nice to meet you, {user_name}!')
print("You have such a cool name!")

print("Now, tell me, how old are you?")
age = input()

if int(age) > 18:
    print("Nice, but I'm younger, I'm 18.")
if int(age) < 18:
    print("Oh, I feel old now.")
else:
    print("We are the same age.")

print("It was nice to meet you, have a wonderful day!")
