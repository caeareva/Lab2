# !/usr/bin/env python3
# Name: Carlos Arevalo (caeareva)
# Group Members: “None”

'''
Read a DNA string from user input and return a collapsed substring of embedded Ns to: {count}.

Example:
 input: AaNNNNNNGTC
output: AA{6}GTC

Any lower case letters are converted to uppercase
'''

class DNAstring(str):
    '''
    This class returns a string object in upper case letters and remove Ns
    and indicates their total number as an integer.
    '''

    def length(self):
        '''
        Function returns the length of input sequence
        '''
        return (length(self))

    def purify(self):
        '''
        Function returns an uppercased version of the string, collapsing a run of Ns
        '''
        countN = self.count("N")  # count number of Ns in DNA sequence
        numN = "{" + str(countN) + "}"  # make a character for the total number of Ns
        cleanSeq = self.replace("N", numN, 1)
        outSeq = cleanSeq.replace("N", "")  # clean sequence and stores it in object
        return (outSeq)

def main():
    '''
    Function gets DNA sequence and clean it up
    '''
    data = input("DNA sequence: ")  # receives input dna sequence
    upperDNA = data.upper()  # convert any lowercase character to upper
    thisDNA = DNAstring(upperDNA)
    pureSeq = thisDNA.purify()
    print(pureSeq)  # print the clean sequence

main()
