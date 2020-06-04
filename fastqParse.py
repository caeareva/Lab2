# !/usr/bin/env python3
# Name: Carlos Arevalo (caeareva)
# Group Members: “None”

'''
Program sparces sequence name information from a single line of a FASTQ formatted file.

Example sequence input:
        FASTQ sequence name: @EAS139:136:FC706VJ:2:2104:15343:197393
Output:
        Instrument = EAS139
        Run ID = 136
        Flow Cell ID = FC706VJ
        Flow Cell Lane = 2
        Tile Number = 2104
        X-coord = 15343
        Y-coord = 197393
'''

class FastqString(str):
    '''
    This class takes an string object and returns a sliced string object of a FASTQ formatted file.
    '''

    def parseSeq():
        '''
        Function parses the input string and matches them with their respective value
        '''
        # concatenate fields to a object
        parseField = (instrument, runID, flowCell, cellLane, tileNumber, x_Coord, y_Coord)
        splitField = parseField.split(",", 6)  # split fields into 6 groups
        pass


def main():
    '''
    Function takes the FASTQ String and explit then into six elements, and print their values
    '''
    myString = input("Enter string of FASTAQ formatted file: ")
    splitString = myString.split(":", 6)  # split FASTQ string into 6 elements
    instrument = print("Instrument = {}".format(splitString[0][1:]))  # print Instrument without @
    runID = print("Run ID = {}".format(splitString[1]))  # print Run ID with value
    flowCell = print("Flow Cell ID = {}".format(splitString[2]))  # print Flow Cell ID with value
    cellLane = print("Flow Cell Lane = {}".format(splitString[3]))  # print Flow Cell Lane with value
    tileNumber = print("Tile Number = {}".format(splitString[4]))  # print Tile Number with value
    x_Coord = print("X-coord = {}".format(splitString[5]))  # print X-coordinate
    y_Coord = print("Y-coord = {}".format(splitString[6]))  # print Y-coordinate
    pass

main()

