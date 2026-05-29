"""
Rosalind Problem: REVC — Complementing a Strand of DNA
URL: https://rosalind.info/problems/revc/
Topic: String Algorithms
Difficulty: Easy

Problem:
    Given a DNA string, return its reverse complement.

Sample Input:  AAAACCCGGT
Sample Output: ACCGGGTTTT

Approach:
    Reverse the string, then substitute each base with its
    complement using a dictionary (A↔T, C↔G).
"""

def complements(dna: str) -> str:
    complement = {"A":"T", "T":"A", "C":"G", "G":"C"}
    reverse_complement = ""
    for base in dna[::-1]:
        reverse_complement += complement[base]
    return reverse_complement


if __name__ == "__main__":
    with open("rosalind_revc.txt") as f:
        dna = f.read().strip()
    print(complements(dna))