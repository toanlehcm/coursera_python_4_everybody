score = input("enter score: ")

try:
    fscore = float(score)
except:
    print("Error, please enter numeric input")
    quit()

if fscore >= 0.9:
    print("A")
elif fscore >= 0.8:
    print("B")
elif fscore >= 0.7:
    print("C")
elif fscore >= 0.6:
    print("D")
elif fscore < 0.6:
    print("F")
