"""
Rosalind Problem: RNA — Transcribing DNA into RNA
URL: https://rosalind.info/problems/rna/
Topic: String Algorithms
Difficulty: Easy

Problem:
    Given a DNA string, return the RNA transcription by replacing T with U.

Sample Input:  GATGGAACTTGACTACGTAAATT
Sample Output: GAUGGAACUUGACUACGUAAAUU

Approach:
use Python's built-in str.replace() for each T nucleotide and change it to "U".
"""

def transcribe(dna: str) -> str:
    return dna.replace("T", "U")

if __name__ == "__main__":
    with open("rosalind_rna.txt") as f:
        dna = f.read().strip()
    print(transcribe(dna))