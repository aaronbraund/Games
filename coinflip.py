from random import randint as rand

class CoinFlip:
    def flip(self):
        if rand(0,1) == 0:
            print("Heads")
        else:
            print("Tails")

coin = CoinFlip()

coin.flip()