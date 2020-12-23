import coder
from collections import Counter


class alphabetHelper:

    def __init__(self):
        self.list = list('abcdefghijklmnopqrstuvwxyz')
        self.size = len(self.list)
        self.dict = {self.list[indx]: indx for indx in range(self.size)}


class CeasarCoder(coder.Coder):

    alphabet = alphabetHelper()

    @staticmethod
    def __code(text, key):
        text = super(CeasarCoder, CeasarCoder)._normalizeText(text)
        codedText = ''
        for char in text:
            codedText += CeasarCoder.alphabet.list[(CeasarCoder.alphabet.dict[char] + key) %
                                                   CeasarCoder.alphabet.size]

        return codedText

    @staticmethod
    def encode(text, key):
        return CeasarCoder.__code(text, key)

    @staticmethod
    def decode(text, key):
        return CeasarCoder.__code(text, key*(-1))

    @staticmethod
    def train(text):
        text = super(CeasarCoder, CeasarCoder)._normalizeText(text)
        size = len(text)
        model = Counter(text)
        for char in model:
            model[char] /= size
        return model

    @staticmethod
    def hack(text, model):
        similarity = [0] * CeasarCoder.alphabet.size
        for i in range(CeasarCoder.alphabet.size):
            text = CeasarCoder.__code(text, 1)
            newModel = CeasarCoder.train(text)
            similarity[i] = sum(
                [(model[c] - newModel[c])**2 for c in CeasarCoder.alphabet.list])
        shift = similarity.index(min(similarity))
        text = CeasarCoder.__code(text, shift + 1)
        return text
