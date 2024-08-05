import os


def main():

    path = input("path here:")

    dicti = {}
    lastName = ""
    oldFiles = []
    counter = 0

    for filename in os.listdir(path):
        if filename[4] == "-":
            oldFiles.append(filename)
            continue

    for i, filename in enumerate(os.listdir(path)):

        if not filename in oldFiles:

            tempName = filename.split('_')[0]
            finalName = ""

            for x, letter in enumerate(tempName):

                if x == 4:
                    finalName += "-" + letter
                elif x == 6:
                    finalName += "-" + letter
                else:
                    finalName += letter

        else:
            finalName = filename.split('.')[0]
            if finalName[-2] == "#":
                counter = int(finalName[-1])
                finalName = finalName.split("#")[0]

        if lastName == finalName or lastName == finalName + "#" + str(counter):
            counter += 1
            finalName += "#" + str(counter)

        temp1 = finalName + ".jpg"
        temp2 = finalName + "#" + str(counter) + ".jpg"

        if (temp1 in oldFiles and counter == 0) or temp2 in oldFiles:

            counter += 1
            temp3 = finalName + "#" + str(counter) + ".jpg"
            if temp3 in oldFiles:
                while finalName + "#" + str(counter) + ".jpg" in oldFiles:
                    counter += 1

            finalName += "#" + str(counter)

        else:
            counter = 0

        dicti.update({finalName: filename})
        lastName = finalName

    for newName in dicti.keys():

        src = path + "/" + dicti[newName]
        dest = path + "/" + newName + ".jpg"
        os.rename(src, dest)

    return


if __name__ == '__main__':
    main()
