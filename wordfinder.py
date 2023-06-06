"""Word Finder: finds random words from a dictionary."""
import random

class WordFinder:

    def __init__(self, file):
        self.file = file
        self.read_words = []
        file = open(self.file)
        for line in file:
            line = line.split()
            self.read_words.append(line)
        print(f"{len(self.read_words)} words read")
    
    def random(self):
        word = random.choice(self.read_words)
        return word[0]


class SpecialWordFinder(WordFinder):
    def __init__(self,file):
        super().__init__(file)

        self.read_words = [word for word in self.read_words if not word.startswith('#') and word.split()]





