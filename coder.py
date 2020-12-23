class Coder:
    @staticmethod
    def encode(text, key):
        pass

    @staticmethod
    def decode(text, key):
        pass

    @staticmethod
    def train(text):
        pass

    @staticmethod
    def hack(text, model):
        pass

    @staticmethod
    def _normalizeText(text):
        alphabet = set('abcdefghijklmnopqrstuvwxyz')
        text = text.lower()
        for char in set(text):
            if not (char in alphabet):
                text = text.replace(char, '')
        return text
