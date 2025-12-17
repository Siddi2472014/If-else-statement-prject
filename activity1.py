#Accepting the user's expectations and score
score=(int)(input("Please enter your score:"))
expectations=(int)(input("Please enter your expectations:"))
if expectations>score:
    print("Unfortunately, you have not reached your expectations, try harder next time!")
else:
    print("You have reched your expectaions, well done!")