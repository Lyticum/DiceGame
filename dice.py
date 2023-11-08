import sys
import random

win_score=0
lose_score=0
game_count=0

while True:
    def dice():
        
        dice_list=[]
        for i in range(1,7):
            dice_list.append(i)
        player = random.choice(dice_list)
        computer = random.choice(dice_list)
        print(f"Sizin zarınız; {player}\nBilgisayarın zarı; {computer}")
        
        def winner(player, computer):
            global win_score 
            global lose_score
            global game_count
            if player > computer:
                print("Kazandınız")
                win_score += 1
                print(f"Galibiyet; {win_score}")
            elif player < computer:
                print("Kaybettiniz")
                lose_score +=1
                print(f"Yenilgi; {lose_score}")
            else:
                print("Berabere")
            game_count += 1
            print(f"Oyun sayısı; {game_count}")
            def exit():
                devam = input("Devam etmek için 'Y' çıkış yapmak için 'N' basınız").lower()
                if devam == "y":
                    pass
                elif devam =="n":
                    sys.exit(f"Oynadığınız için teşekkürler skorunuz; {win_score}!")
            exit()
        winner(player, computer)
    dice()


        

