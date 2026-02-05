for i in range (1,101):
        if i % 15 == 0:  print ("FizzBuzz", end ="\n")
        elif i % 5 == 0: print ("Buzz", end = "\n")
        elif i % 3 == 0: print ("Fizz", end = "\n")
        else:            print (i)
