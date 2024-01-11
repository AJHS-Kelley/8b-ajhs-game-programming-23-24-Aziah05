# DNA Replication Game, Aziah Hill, v0.0

# Import Entire Modules -- Get the whole tool box.
import time, datetime

# Import Specific Methods -- Get the s[ecific tool.
from random import choice

# Store the DNA Bases
dnaBases = ["A", "T", "G", "C"]

# GAME FUNCTIONS
def gameIntro() -> None:
    pass

def genDNA() -> str:
    basesGenerated = 0
    basesRequested = int(input("Please enter a positive integer"))
    dnaSequence = ""
    while basesGenerated < basesRequested:
        dnaSequence += choice(dnaBases)
        basesGenerated += 1
    return dnaSequence
    
dna = genDNA()
print(dna)
