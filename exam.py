def AsteriskBox(row,columns):
  for i in range(row):
     for j in range(columns):
        print('*', end='')
     print()

def main():
    row=int(input("Enter the number of row:--> "))
    columns=int(input("Enter the number of columns-->"))
    AsteriskBox(row,columns)
main()


