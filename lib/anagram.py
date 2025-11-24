class Anagram:
    def __init__(self, word):
        self.word = word.lower()
        self.sorted_word = ''.join(sorted(self.word))

    def match(self, word_list):
        matches = []
        for w in word_list:
            if w.lower() == self.word:
                continue  # Skip if exact match, anagram shouldn't include itself?
            if ''.join(sorted(w.lower())) == self.sorted_word:
                matches.append(w)
        return matches
