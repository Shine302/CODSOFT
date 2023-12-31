#Display welcome message and rules
print("Welcome! to Random Quiz game")
print("````````````````````````````")
print("The rules of this game is simple\njust enter the option you think is correct for each question")

count = 0

#Display the Quiz questions
print("\nQ1)Which planet is known as the 'Red Planet'?\n[A]Venus\n[B]Mars\n[C]Jupiter\n[D]Saturn")
ans1 = input("Enter an option: ").upper()
#Checking users answers
if ans1 == 'B':
    print("\nCORRECT!")
    count+=1
else:
    print("\nWRONG!")
    print("Right answer is [B]Mars")

print("\nQ2)Who painted the Mona Lisa?\n[A]Vincent van Gogh\n[B]Pablo Picasso\n[C]Leonardo da Vinci\n[D]Michelangelo")
ans2 = input("Enter an option: ").upper()
if ans2 == 'C':
    print("\nCORRECT!")
    count+=1
else:
    print("\nWRONG!")
    print("Right answer is [C]Leonardo da Vinci")

print("\nQ3)What is the chemical symbol for gold?\n[A]Au\n[B]Ag\n[C]Fe\n[D]Cu")
ans3 = input("Enter an option: ").upper()
if ans3 == 'A':
    print("\nCORRECT!")
    count+=1
else:
    print("\nWRONG!")
    print("Right answer is [A]Au")

print("\nQ4)What is the capital of Japan?\n[A]Beijing\n[B]Tokyo\n[C]Seoul\n[D]Bangkok")
ans4 = input("Enter an option: ").upper()
if ans4 == 'B':
    print("\nCORRECT!")
    count+=1
else:
    print("\nWRONG!")
    print("Right answer is [B]Tokyo")

print("\nQ5)Who is the author of the Harry Potter book series?\n[A]J.R.R. Tolkien\n[B]Suzanne Collins\n[C]George R.R. Martin\n[D]J.K. Rowling")
ans5 = input("Enter an option: ").upper()
if ans5 == 'D':
    print("\nCORRECT!")
    count+=1
else:
    print("\nWRONG!")
    print("Right answer is [D]J.K. Rowling")

#Compare users answers with correct answers
print("\n-----Result-----")
print("Your answers are:-\nQ1)[{}]    Q2)[{}]    Q3)[{}]    Q4)[{}]    Q5)[{}]  ".format(ans1,ans2,ans3,ans4,ans5))    
print("Right answers are:-\nQ1)[B]    Q2)[C]    Q3)[A]    Q4)[B]    Q5)[D]")

#Print users score
print("\nYour score is {}/5".format(count))
print("-----------------")

diss = input("\nDO you want to play again?\n'Y' for Yes    'N' for No\n ").upper()

if diss == 'Y':
    flag = 0
    print("\nQ1)Which river is the longest in the world?\n[A]Amazon\n[B]Yangtze\n[C]Nile\n[D]Mississippi")
    ans6 = input("Enter an option: ").upper()
    if ans6 == 'C':
        print("\nCORRECT!")
        count+=1
        flag+=1
    else:
        print("\nWRONG!")
        print("Right answer is [C]Nile")

    print("\nQ2)Who is often referred to as 'The Greatest' in the history of boxing?\n[A]Muhammad Ali\n[B]Mike Tyson\n[C]Floyd Mayweather Jr.\n[D]Sugar Ray Robinson")
    ans7 = input("Enter an option: ").upper()
    if ans7 == 'A':
        print("\nCORRECT!")
        count+=1
        flag+=1
    else:
        print("\nWRONG!")
        print("Right answer is [A]Muhammad")

    print("\nQ3)In which year did Christopher Columbus reach the Americas?\n[A]1607\n[B]1776\n[C]1453\n[D]1492")
    ans8 = input("Enter an option: ").upper()
    if ans8 == 'D':
        print("\nCORRECT!")
        count+=1
        flag+=1
    else:
        print("\nWRONG!")
        print("Right answer is [D]1492")

    print("\nQ4)Which actor played the character of Tony Stark in the Marvel Cinematic Universe?\n[A]Chris Evans\n[B]Chris Hemsworth\n[C]Robert Downey Jr.\n[D]Mark Ruffalo")
    ans9 = input("Enter an option: ").upper()
    if ans9 == 'C':
        print("\nCORRECT!")
        count+=1
        flag+=1
    else:
        print("\nWRONG!")
        print("Right answer is [C]Robert Downey Jr.")        
    
    print("\nQ5)What is the largest type if big cat in the world?\n[A]Lion\n[B]Tiger\n[C]Leopard\n[D]Jaguar")
    ans10 = input("Enter an option: ").upper()
    if ans10 == 'B':
        print("\nCORRECT!")
        count+=1
        flag+=1
    else:
        print("\nWRONG!")
        print("Right answer is [B]Tiger")

    print("\n-----Result-----")
    print("Your answers are:-\nQ1)[{}]    Q2)[{}]    Q3)[{}]    Q4)[{}]    Q5)[{}]  ".format(ans6,ans7,ans8,ans9,ans10))    
    print("Right answers are:-\nQ1)[C]    Q2)[A]    Q3)[D]    Q4)[C]    Q5)[B]")

    print("\nYour score is in this round {}/5".format(flag))
    print("-------------------------------")
    print("Your total score is {}/10".format(count))
    print("-------------------------")
    print("\nThank you for playing")

else:
    print("Thank you for playing")    

