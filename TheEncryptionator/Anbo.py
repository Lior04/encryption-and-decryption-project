from Atbash import ABC
abcHalf1 = ABC[:len(ABC) // 2]
abcHalf2 = ABC[len(ABC) // 2:]



class Anbo:

    def Encrypt(self, text):
        Text = text.replace(" ", "")
        Text = Text.lower()
        encText = ""
        for i in Text:
            if i != ' ':
                indexLetter = abcHalf1.find(i)
                if indexLetter == -1:
                    indexLetter = abcHalf2.find(i)
                    encText += abcHalf1[indexLetter]
                else:
                    encText += abcHalf2[indexLetter]
            else:
                encText += ' '
        return encText

    def Decrypt(self, text):
        Text = text.replace(" ", "")
        Text = Text.lower()
        decText = ""
        for i in Text:
            if i != ' ':
                indexLetter = abcHalf1.find(i)
                if indexLetter == -1:
                    indexLetter = abcHalf2.find(i)
                    decText += abcHalf1[indexLetter]
                else:
                    decText += abcHalf2[indexLetter]
            else:
                decText += ' '
        return decText
