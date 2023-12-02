def powerball1():
    line = input ("Enter powerball data-->")
    plist = line.split(",")
    numbers = plist[:6]
    print(numbers)

powerball1()