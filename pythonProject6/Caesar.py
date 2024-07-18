from Atbash import ABC

class Caesar:
    def Encrypt(self, text, key):
        tempText = ""
        for i in text:
            if i != ' ':
                indexLetter = ABC.find(i) + key
                if indexLetter > 25:
                    indexLetter -= 26
                tempText += ABC[indexLetter]
            else:
                tempText += " "
        text = tempText
        return text

    def Decrypt(self, text, key):
        tempText = ""
        for i in text:
            if i != ' ':
                indexLetter = ABC.find(i) - key
                if indexLetter < 0:
                    indexLetter += 26
                tempText += ABC[indexLetter]
            else:
                tempText += " "
        text = tempText
        return text