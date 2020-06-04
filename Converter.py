# !/usr/bin/env python3
# Name: Carlos Arevalo (caeareva)
# Group Members: “None”

'''
Program uses mapping to convert from RNA to DNA to Amino Acids, and viceversa. For Amino Acids and codons,
the program uses both; one-letter and three-letters representations.Enter any amino acid acronym,
codon, or one-letter representation, and program will translate it using multiple dictionaries.
However, if the program does not get a valid input, it will output "Unknown"
'''

class Converter(str):
    '''
    This class converts RNA to DNA, amino acids to codons, and viceversa using dictionaries.
    '''
    # write single dictionaries
    short_AA = {
        'CYS': 'C', 'ASP': 'D', 'SER': 'S', 'GLN': 'Q', 'LYS': 'K',
        'ILE': 'I', 'PRO': 'P', 'THR': 'T', 'PHE': 'F', 'ASN': 'N',
        'GLY': 'G', 'HIS': 'H', 'LEU': 'L', 'ARG': 'R', 'TRP': 'W',
        'ALA': 'A', 'VAL': 'V', 'GLU': 'E', 'TYR': 'Y', 'MET': 'M'
    }

    long_AA = {value: key for key, value in short_AA.items()}

    RNA_codon_table = {
        # Second Base
        # U             C             A             G
        # U
        'UUU': 'Phe', 'UCU': 'Ser', 'UAU': 'Tyr', 'UGU': 'Cys',
        'UUC': 'Phe', 'UCC': 'Ser', 'UAC': 'Tyr', 'UGC': 'Cys',
        'UUA': 'Leu', 'UCA': 'Ser', 'UAA': '---', 'UGA': '---',
        'UUG': 'Leu', 'UCG': 'Ser', 'UAG': '---', 'UGG': 'Trp',
        # C
        'CUU': 'Leu', 'CCU': 'Pro', 'CAU': 'His', 'CGU': 'Arg',
        'CUC': 'Leu', 'CCC': 'Pro', 'CAC': 'His', 'CGC': 'Arg',
        'CUA': 'Leu', 'CCA': 'Pro', 'CAA': 'Gln', 'CGA': 'Arg',
        'CUG': 'Leu', 'CCG': 'Pro', 'CAG': 'Gln', 'CGG': 'Arg',
        # A
        'AUU': 'Ile', 'ACU': 'Thr', 'AAU': 'Asn', 'AGU': 'Ser',
        'AUC': 'Ile', 'ACC': 'Thr', 'AAC': 'Asn', 'AGC': 'Ser',
        'AUA': 'Ile', 'ACA': 'Thr', 'AAA': 'Lys', 'AGA': 'Arg',
        'AUG': 'Met', 'ACG': 'Thr', 'AAG': 'Lys', 'AGG': 'Arg',
        # G
        'GUU': 'Val', 'GCU': 'Ala', 'GAU': 'Asp', 'GGU': 'Gly',
        'GUC': 'Val', 'GCC': 'Ala', 'GAC': 'Asp', 'GGC': 'Gly',
        'GUA': 'Val', 'GCA': 'Ala', 'GAA': 'Glu', 'GGA': 'Gly',
        'GUG': 'Val', 'GCG': 'Ala', 'GAG': 'Glu', 'GGG': 'Gly'
    }

    # converts RNA codon table to DNA codon table
    dnaCodonTable = {key.replace('U', 'T'): value for key, value in RNA_codon_table.items()}

    # stores dictionaries in object to be call
    context = dict(short_AA.items() | long_AA.items() | RNA_codon_table.items() | dnaCodonTable.items())

def main():  # write an input function and then execute the string
    '''
    The function asks for a short amino acid or long amino acid or DNA codon or RNA codon input, and
    then outputs the correct convertion using the dictionaries. If input is entered in lower case, method converts it to upper case.
    '''
    myConverter = Converter()
    inContext = myConverter.context
    # asks for short or long amino acid or DNA or RNA codon to translate
    character = (input("Enter amino acid, RNA or DNA codon: ")).upper()
    if character in inContext:
        newCharacter = print("{} = {}".format(character, inContext[character], ))
    else:  # if the input is not in the dictionary, program will output "Unknown"
        print("{} = Unknown".format(character))
    pass

main()
