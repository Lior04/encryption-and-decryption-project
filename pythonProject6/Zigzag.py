class Zigzag:
    def __init__(self, Text):
        self.text = Text

    def Encrypt(self):
        count = 0
        textHalf1 = self.text[::2]
        textHalf2 = self.text[1::2]
        self.text = ""
        for i in (textHalf1 + textHalf2):
            count += 1
            self.text += i
            if count % 4 == 0:
                self.text += " "
        return self.text

    def Decrypt(self):
        tempText = ""
        for i in self.text:
            if i != ' ':
                tempText += i
        if len(tempText) % 2 != 0:
            text2Half1 = tempText[:1 + len(tempText) // 2]
            text2Half2 = tempText[1 + len(tempText) // 2:]
        else:
            text2Half1 = tempText[:len(tempText) // 2]
            text2Half2 = tempText[len(tempText) // 2:]
        print(text2Half1)
        print(text2Half2)

        self.text = ""
        for i in range(len(text2Half1)):
            if i >= len(text2Half2):
                self.text += text2Half1[i]
            else:
                self.text += text2Half1[i] + text2Half2[i]
        return self.text


