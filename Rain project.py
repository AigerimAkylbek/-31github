import matplotlib.pyplot as plt
from datetime import datetime

def main():
    filePath = input("Please enter the file name for rain data: ")
    rawData = None

    while True:
        try:
            rawData = open(filePath)
            break
        except:
            print(f"The file {filePath} was not found, please enter the file again.")
            filePath = input("Re-enter file: ")

    rainData = []
    for line in rawData:
        rainList = [item.strip() for item in line.split(',')]
        rainData.append([rainList[0], float(rainList[1])])
    
    monthlyData = {}
    for line in rainData:
        if (line[0] not in monthlyData):
            monthlyData[line[0]] = [line[1]]
        else:
            monthlyData[line[0]].append(line[1])
    
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    rainAvg = []
    for month in months:
        avg = 0;
        for data in monthlyData[month]:
            avg += data
        avg /= len(monthlyData[month])
        rainAvg.append(avg)

    plt.bar(months, rainAvg)
    plt.title("Average Rainfall by Month")
    plt.show()

            

main()