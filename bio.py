class DNA:
    ##Class representing DNA as a string sequence.

    basecomplement = {'A': 'T', 'C': 'G', 'T': 'A', 'G': 'C'}

    def __init__(self, s):
        #Create DNA instance initialized to string s.
        self.seq = s

    def transcribe(self):
        #Return as rna string.
        return self.seq.replace('T', 'U')

    def reverse(self):
        #Return dna string in reverse order.
        letters = list(self.seq)
        letters.reverse()
        return ''.join(letters)

    def complement(self):
        #Return the complementary dna string
        letters = list(self.seq)
        letters = [self.basecomplement[base] for base in letters]
        return ''.join(letters)

    def reversecomplement(self):
        # Return the reverse complement of the dna string.
        letters = list(self.seq)
        letters.reverse()
        letters = [self.basecomplement[base] for base in letters]
        return ''.join(letters)

    def gc(self):
        # Return the percentage of dna composed of G+C.
        s = self.seq
        gc = s.count('G') + s.count('C')
        return gc * 100.0 / len(s)

    def codons(self):
        # Return list of codons for the dna string.
        s = self.seq
        end = len(s) - (len(s) % 3) - 1
        codons = [s[i:i+3] for i in range(0, end, 3)]
        return codons
