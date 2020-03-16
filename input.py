from os.path import abspath, exists

def readInput(inputFile):
    f_path = abspath(inputFile)
    places = []

    if exists(f_path):
        with open(f_path, 'r') as filehandle:
            filecontents = filehandle.readlines()
            for line in filecontents:
                current_place = line[:-1]
                places.append(current_place.upper())
    return places