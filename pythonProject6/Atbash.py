ABC = "abcdefghijklmnopqrstuvwxyz"
ZYX = ABC[::-1]


class Atbash:
    def Encrypt(self, text):
        tempText = ""
        for i in text:
            letterIndex = ABC.find(i)
            tempText += ZYX[letterIndex]
        text = tempText
        return text

    def Decrypt(self, text):
        tempText = ""
        for i in text:
            letterIndex = ZYX.find(i)
            tempText += ABC[letterIndex]
        text = tempText
        return text
