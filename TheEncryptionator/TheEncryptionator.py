import pygame
from Zigzag import Zigzag
from Atbash import Atbash
from Caesar import Caesar
from Anbo import Anbo
from Words import words
from ButtonClass import Button
import PyInstaller


pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 700
ABC = "abcdefghijklmnopqrstuvwxyz"

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


pygame.display.set_caption("The Encryptionator")
clock = pygame.time.Clock()
baseFont = pygame.font.Font(None, 32)
pygame.scrap.init()
pygame.scrap.set_mode(pygame.SCRAP_CLIPBOARD)

#frame selection
StartMenu = True
CodeMenu = False
Translator = False



#text box
userText = 'write text here'
inputRect = pygame.Rect(295, 200, 250, 36)
TextDraw = True
TextActive = False
userKey = 'write key here'
inputRectKey = pygame.Rect(295, 250, 250, 36)

showDecryption = False
showEncryption = False
decryptedText = ''
encryptedText = ''

processedText = ''


current_code = "Zigzag"
anbo = Anbo()
caesar = Caesar()
zigzag = Zigzag()
atbash = Atbash()

#image
decrypt_img = pygame.image.load('decrypt_button.png').convert_alpha()
encrypt_img = pygame.image.load('encrypt_button.png').convert_alpha()
Anbo_img = pygame.image.load('ANBO.png').convert_alpha()
Atbash_img = pygame.image.load('ATBASH.png').convert_alpha()
Back_img = pygame.image.load('BACK.png').convert_alpha()
Copy_img = pygame.image.load('COPY.png').convert_alpha()
Quit_img = pygame.image.load('QUIT.png').convert_alpha()
Start_img = pygame.image.load('START.png').convert_alpha()
Zigzag_img = pygame.image.load('ZIGZAG.png').convert_alpha()
Caesar_img = pygame.image.load('CAESAR.png').convert_alpha()
Title_img = pygame.image.load('Title.png').convert_alpha()




#buttons
DecryptButton = Button(420, 300, pygame.transform.scale(decrypt_img, (200, 100)))
EncryptButton = Button(180, 300, pygame.transform.scale(encrypt_img, (200, 100)))
ZigzagButton = Button(275, 100, pygame.transform.scale(Zigzag_img, (250, 125)))
CaesarButton = Button(275, 225, pygame.transform.scale(Caesar_img, (250, 125)))
AtbashButton = Button(275, 350, pygame.transform.scale(Atbash_img, (250, 125)))
AnboButton = Button(275, 475, pygame.transform.scale(Anbo_img, (250, 125)))
CopyButton = Button(700, 400, pygame.transform.scale(Copy_img, (100, 50)))
BackButton = Button(50, 50, pygame.transform.scale(Back_img, (150, 75)))
StartButton = Button(225, 310, pygame.transform.scale(Start_img, (350, 175)))
QuitButton = Button(225, 485, pygame.transform.scale(Quit_img, (350, 175)))



def encrypt():
    if current_code == "Zigzag":
        return zigzag.Encrypt(userText)
    if current_code == "Atbash":
        return atbash.Encrypt(userText)
    if current_code == "Caesar":
        return caesar.Encrypt(userText, int(userKey))
    if current_code == "Anbo":
        return anbo.Encrypt(userText)

def decrypt():
    if current_code == "Zigzag":
        return zigzag.Decrypt(userText)
    if current_code == "Atbash":
        return atbash.Decrypt(userText)
    if current_code == "Caesar":
        return caesar.Decrypt(userText, int(userKey))
    if current_code == "Anbo":
        return anbo.Decrypt(userText)

def buttonClickedReset():
    DecryptButton.clickTrue()
    EncryptButton.clickTrue()
    ZigzagButton.clickTrue()
    CaesarButton.clickTrue()
    AtbashButton.clickTrue()
    AnboButton.clickTrue()
    CopyButton.clickTrue()
    BackButton.clickTrue()
    StartButton.clickTrue()
    QuitButton.clickTrue()

run = True
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN: #checks if user is typing
            if event.key == pygame.K_BACKSPACE and TextActive:
                userText = userText[:-1]
            elif TextActive:
                userText += event.unicode
            elif event.key == pygame.K_BACKSPACE and KeyTextActive:
                userKey = userKey[:-1]
            elif KeyTextActive:
                userKey += event.unicode


        if event.type == pygame.MOUSEBUTTONDOWN: #checks if user is clicking on text box
            if inputRect.collidepoint(event.pos):
                TextActive = True
                KeyTextActive = False
                userText = ''
            if inputRectKey.collidepoint(event.pos):
                KeyTextActive = True
                TextActive = False
                userKey = ''




    screen.fill((0, 100, 209))

    if StartMenu:
        if StartButton.draw(screen):
            CodeMenu = True
            StartMenu = False
        if QuitButton.draw(screen):
            run = False
        screen.blit(pygame.transform.scale(Title_img, (800, 350)), (0,0))


    if CodeMenu:
        if ZigzagButton.draw(screen):
            current_code = "Zigzag"
            Translator = True
            CodeMenu = False
            userText = 'Write Text Here'
        if CaesarButton.draw(screen):
            current_code = "Caesar"
            Translator = True
            CodeMenu = False
            userText = 'Write Text Here'
            userKey = 'Write Key Here'
        if AtbashButton.draw(screen):
            current_code = "Atbash"
            Translator = True
            CodeMenu = False
            userText = 'Write Text Here'
        if AnboButton.draw(screen):
            current_code = "Anbo"
            Translator = True
            CodeMenu = False
            userText = 'Write Text Here'

        if BackButton.draw(screen):
            StartMenu = True
            CodeMenu = False
            buttonClickedReset()


    if Translator:
        pygame.draw.rect(screen, (0, 0, 0), inputRect, 2)
        textSurface = baseFont.render(userText, True, (0, 0, 0))
        screen.blit(textSurface, (inputRect.x + 5, inputRect.y + 5))
        inputRect.w = max(200, textSurface.get_width() + 10)
        inputRect.x = (SCREEN_WIDTH - inputRect.w) / 2
        if current_code == "Caesar":
            pygame.draw.rect(screen, (0, 0, 0), inputRectKey, 2)
            textSurfaceKey = baseFont.render(userKey, True, (0, 0, 0))
            screen.blit(textSurfaceKey, (inputRectKey.x + 5, inputRectKey.y + 5))
            inputRectKey.w = max(200, textSurfaceKey.get_width() + 10)
            inputRectKey.x = (SCREEN_WIDTH - inputRectKey.w) / 2
        if CopyButton.draw(screen):
            if showDecryption:
                pygame.scrap.put(pygame.SCRAP_TEXT, decrypt())
            else:
                pygame.scrap.put(pygame.SCRAP_TEXT, encrypt())
        if BackButton.draw(screen):
            Translator = False
            CodeMenu = True
            TextActive = False
            KeyTextActive = False
            userText = ''
            showEncryption = False
            showDecryption = False
            buttonClickedReset()



        if DecryptButton.draw(screen):
            showEncryption = False
            showDecryption = True
            decryptedText = baseFont.render(decrypt(), True, (0, 0, 0))

        if EncryptButton.draw(screen):
            showDecryption = False 
            showEncryption = True
            encryptedText = baseFont.render(encrypt(), True, (0, 0, 0))

        if showDecryption:
            screen.blit(decryptedText, (((800 - decryptedText.get_width()) / 2, 500)))
        if showEncryption:
            screen.blit(encryptedText, (((800 - encryptedText.get_width()) / 2, 500)))






    pygame.display.flip()
    clock.tick(60)


pygame.quit()