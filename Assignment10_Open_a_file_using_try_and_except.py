try:
    f = open("test.txt", "r")
except IOError:    
    print ("Oops, no file by that name")
