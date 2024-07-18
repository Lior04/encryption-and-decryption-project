from Zigzag import Zigzag
from Atbash import Atbash
from Caesar import Caesar
from Anbo import Anbo


ABC = "abcdefghijklmnopqrstuvwxyz"


zigzag = Zigzag()
print(zigzag.Encrypt("hello word"))
print(zigzag.Decrypt("hloe l"))

atbash = Atbash()
print(atbash.Encrypt("hello"))
print(atbash.Decrypt("svool"))

caesar = Caesar()
print(caesar.Encrypt("hello wrfk", 2))
print(caesar.Decrypt("wtaad lguz", 2))

anbo = Anbo()
print(anbo.Encrypt("bob"))