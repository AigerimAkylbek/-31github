def fib(length):
    myList=[0,1]
 
    for i in range(length-1):
        myList.append(myList[-2]+myList[-1])
    return myList
       

def main():
    print(fib(25))

main()