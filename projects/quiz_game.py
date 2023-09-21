print("Welcome to my Quiz Game!")

playing = input("Do you want to play ? ")

if playing.lower() != "yes":
    quit()

print("Okay lets play :) ")
score = 0

answer = input("What does CPU stand for ? ")
if answer.lower() == "central processing unit":
    print("Correct ! ")
    score += 1
else:
    print("Incorecct ! ")

answer = input("What does GPU stand for ? ")
if answer.lower() == "graphic processing unit":
    print("Correct ! ")
    score += 1
else:
    print("Incorecct ! ")

answer = input("What does RAM stand for ? ")
if answer.lower() == "random acces memory":
    print("Correct ! ")
    score += 1
else:
    print("Incorecct ! ")

answer = input("What does PSU stand for ? ")
if answer.lower() == "power supply":
    print("Correct ! ")
    score += 1
else:
    print("Incorecct ! ")

print("You got " + str(score) + " questions correct ! ")
