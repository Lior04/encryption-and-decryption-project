class Zigzag:
    def Encrypt(self, text):
        Text = text.replace(" ", "")
        Text = Text.lower()
        count = 0
        tempText = ""
        for i in Text:
            if i != ' ':
                tempText += i
        text = tempText
        textHalf1 = text[::2]
        textHalf2 = text[1::2]
        text = ""
        for i in (textHalf1 + textHalf2):
            count += 1
            text += i
            if count % 4 == 0:
                text += " "
        return text

    def Decrypt(self, text):
        Text = text.replace(" ", "")
        Text = Text.lower()
        tempText = ""
        for i in Text:
            if i != ' ':
                tempText += i
        if len(tempText) % 2 != 0:
            text2Half1 = tempText[:1 + len(tempText) // 2]
            text2Half2 = tempText[1 + len(tempText) // 2:]
        else:
            text2Half1 = tempText[:len(tempText) // 2]
            text2Half2 = tempText[len(tempText) // 2:]

        text = ""
        for i in range(len(text2Half1)):
            if i >= len(text2Half2):
                text += text2Half1[i]
            else:
                text += text2Half1[i] + text2Half2[i]
        return text


