def sumOfFirstNnumbers(n):
    #add up 1+2+3+...+n
    sum = 0
    for i in range (1,n+1):
        sum+=i
    return sum

def main():
    n = int(input("How many numbers should we sum up"))
    print(f"the sum is {sumOfFirstNnumbers(n)}")

main()