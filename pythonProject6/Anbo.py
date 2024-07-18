from Atbash import ABC
abcHalf1 = ABC[:len(ABC) // 2]
abcHalf2 = ABC[len(ABC) // 2]

class Anbo:

    def Encrypt(self, text):
        decText = ""
        for i in text:
            if i != ' ':
                indexLetter = abcHalf1.find(i)
                if indexLetter == -1:
                    indexLetter = abcHalf2.find(i)
                    decText += abcHalf1[indexLetter]
                else:
                    decText += abcHalf2[indexLetter]
        return decText
