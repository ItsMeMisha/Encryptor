import coder


class alphabetHelper:

    def __init__(self):
        self.list = list('abcdefghijklmnopqrstuvwxyz')
        self.size = len(self.list)
        self.matrix = {self.list[i]: {self.list[j]: self.list[(
            j+i) % self.size] for j in range(self.size)} for i in range(self.size)}

        self.reverseMatrix = {key: {
            self.matrix[key][char]: char for char in self.matrix[key].keys()} for key in self.matrix.keys()}


class VigenereCoder(coder.Coder):

    alphabet = alphabetHelper()

    @staticmethod
    def encode(text, key):
        return VigenereCoder.__code(text, key, VigenereCoder.alphabet.matrix)

    @staticmethod
    def decode(text, key):
        return VigenereCoder.__code(text, key, VigenereCoder.alphabet.reverseMatrix)

    @staticmethod
    def __code(text, key, matrixToUse):
        text = super(VigenereCoder, VigenereCoder)._normalizeText(text)
        codedText = ''

        for indx in range(len(text)):
            codedText += matrixToUse[key[indx % len(key)]][text[indx]]

        return codedText
