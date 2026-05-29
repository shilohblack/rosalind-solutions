"""
Rosalind Problem: DNA — Counting DNA Nucleotides
URL: https://rosalind.info/problems/dna/
Topic: String Algorithms
Difficulty: Easy

Problem:
    Given a DNA string, count occurrences of A, C, G, and T.

Sample Input:  AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC
Sample Output: 20 12 17 21

Approach:
    Use Python's built-in str.count() for each nucleotide.
"""

def count_nucleotides(dna: str) -> str:
    return f"{dna.count('A')} {dna.count('C')} {dna.count('G')} {dna.count('T')}"

if __name__ == "__main__":
    with open("rosalind_dna.txt") as f:
        dna = f.read().strip()
    print(count_nucleotides(dna))