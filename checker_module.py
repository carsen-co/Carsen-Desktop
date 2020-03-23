
from bs4_module import getCarPriceChecker

import csv


# existing searches checker
def checker():
    print("\nChecker initiated")
    changes = []
    # check for files to be checked
    with open("csvFilesIndex.txt", mode="r") as cFi:
        files = cFi.readlines()
        cFi.close()

    for file in files:
        file = file.strip("\n")

        with open(file, mode="r", newline='') as csvFile:
            csvReader = csv.reader(csvFile)
            data = list(csvReader)
            csvFile.close()

        with open(file, mode="w", newline='') as csvFile:
            csvWriter = csv.writer(csvFile)
            links = []
            for i in range(len(data) - 1):
                links.append(data[i + 1][0])

            i = -1
            for link in links:
                i += 1
                if i == 0:
                    print(i + 1, "ad checked")
                else:
                    print(i + 1, "ads checked")

                newPrice = getCarPriceChecker(link)
                if(data[i + 1][3]) == newPrice:
                    continue
                else:
                    changedPrice = int(data[i + 1][3]) - newPrice
                    changedPrice = -changedPrice
                    '''
                    try:
                        data[i + 1].pop(6)
                    except:
                        None
                    '''
                    if changedPrice == 0:
                        continue
                    else:
                        data[i + 1].append(changedPrice)
                        changes.append(file)
                        changes.append(i + 1)
                        changes.append(changedPrice)
        
            csvWriter.writerows(data)
            csvFile.close()
        print(file, " checked\n")

    print("Changes found:")
    for i in range(int(len(changes) / 3)):
        print("In file -", changes[i+(i*2)], "- at line ", changes[i+1+(i*2)], " by ", changes[i+2+(i*2)])

    print("Checker executed successfully")