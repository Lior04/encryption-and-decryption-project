ABC = "abcdefghijklmnopqrstuvwxyz"
ZYX = "zyxwvutsrqponmlkjihgfedcba"


class Atbash:
    def Encrypt(self, text):
        Text = text.replace(" ", "")
        Text = Text.lower()
        tempText = ""
        for i in Text:
            letterIndex = ABC.find(i)
            tempText += ZYX[letterIndex]
        text = tempText
        return text

    def Decrypt(self, text):
        Text = text.replace(" ", "")
        Text = Text.lower()
        tempText = ""
        for i in Text:
            letterIndex = ZYX.find(i)
            tempText += ABC[letterIndex]
        text = tempText
        return text
