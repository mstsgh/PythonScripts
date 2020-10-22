from random import shuffle
import pygame

superlatives = "amazing gorgeous blazing stunning tremendous greatest best fantastic \
               phenomenal delightful ambitious outstanding incredible spectacular \
               super cool magical revolutionary beautiful jaw-dropping lovely".upper().split()
shuffle(superlatives)

for strophe in range(5):
    for n in range(2):
        for i in range(4):
            print("Spam", end=' ')
        print()
    print(superlatives.pop() + " Spam, " + superlatives.pop() + " Spam")
    print()
    