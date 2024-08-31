from Atbash import ABC

class Caesar:
    def Encrypt(self, text, key):
        Text = text.replace(" ", "")
        Text = Text.lower()
        tempText = ""
        tempkey = 0
        if key > 26:
            tempkey = key % 26
        else:
            tempkey = key
        for i in Text:
            if i != ' ':
                indexLetter = ABC.find(i) + tempkey
                if indexLetter > 25:
                    indexLetter -= 26
                tempText += ABC[indexLetter]
            else:
                tempText += " "
        text = tempText
        return text

    def Decrypt(self, text, key):
        Text = text.replace(" ", "")
        Text = Text.lower()
        tempText = ""
        tempkey = 0
        if key > 26:
            tempkey = key % 26
        else:
            tempkey = key
        for i in Text:
            if i != ' ':
                indexLetter = ABC.find(i) - tempkey
                if indexLetter < 0:
                    indexLetter += 26
                tempText += ABC[indexLetter]
            else:
                tempText += " "
        text = tempText
        return text