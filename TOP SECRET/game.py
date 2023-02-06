from graphics import Canvas
import time

canvas = Canvas()

CanvasHeight = 720
CanvasWidth = 1280
delay = 0.02
mainCharacterSpeed = 10

def openingScene():
    mainScreen = canvas.create_image_with_size(0,0,CanvasWidth,CanvasHeight,'bg.png')

    openingText = canvas.create_text(CanvasWidth //2, CanvasHeight // 2,"Ezgi, Emir'i Kurtarıyor")
    canvas.set_font(openingText, 'Gabriola', 70)

    helpText = canvas.create_text(CanvasWidth //2, CanvasHeight // 2+60,"Başlamak için 'e' tuşuna basın.")
    canvas.set_font(helpText, 'Gabriola',20)

    opening = 1
    while opening == 1:
        presses = canvas.get_new_key_presses()
        for press in presses:
            if press.keysym == 'e':
                canvas.delete(mainScreen)
                canvas.delete(openingText)
                canvas.delete(helpText)
                opening -= 1
        time.sleep(delay)
        canvas.update()

def inGameFirst(background):
    mainCharacter = canvas.create_image_with_size(0, 500, 110, 110, 'babe.png')

    first_text = canvas.create_text(CanvasWidth//4*3,CanvasHeight//3, "Ezgi: Bugün birinci yılımız. Emir'i çok özledim.🥺\nAcaba nerede? Onu bulsam iyi olacak.")
    canvas.set_font(first_text, "Gabriola",30)

    helpText = canvas.create_text(120,17,"İlerlemek için 'Sağ Ok' tuşuna basın.")
    canvas.set_font(helpText, 'Gabriola', 15)

    hareket = 1
    while hareket == 1:
        presses = canvas.get_new_key_presses()
        for press in presses:
            if press.keysym == 'Right':
                canvas.move(mainCharacter,mainCharacterSpeed,0)
                if canvas.get_left_x(mainCharacter) >= CanvasWidth:
                    canvas.delete(background)
                    canvas.delete(mainCharacter)
                    canvas.delete(first_text)
                    canvas.delete(helpText)
                    hareket -= 1
        canvas.update()

def inGameSecond(background):
    secondScreenBG = canvas.create_image_with_size(0,0,CanvasWidth,CanvasHeight,background)

    second_text = canvas.create_text(CanvasWidth //2+200, 75, "Ezgi: Bir saniyeee, havaya ne olduu?🤨😮\nBir gariplik seziyorum. Umarım Emir iyidir.")
    canvas.set_font(second_text, 'Gabriola', 30)

    helpText = canvas.create_text(120, 17, "İlerlemek için 'Sağ Ok' tuşuna basın.")
    canvas.set_font(helpText, 'Gabriola', 15)

    mainCharacter = canvas.create_image_with_size(0, 530, 110, 110, 'babe.png')

    hareket = 1
    while hareket == 1:
        presses = canvas.get_new_key_presses()
        for press in presses:
            if press.keysym == 'Right':
                canvas.move(mainCharacter,mainCharacterSpeed,0)
                if canvas.get_left_x(mainCharacter) >= CanvasWidth:
                    canvas.delete(secondScreenBG)
                    canvas.delete(mainCharacter)
                    canvas.delete(second_text)
                    canvas.delete(helpText)
                    hareket -= 1
        canvas.update()

def inGameThird(background):
    thirdScreenBG = canvas.create_image_with_size(0, 0, CanvasWidth, CanvasHeight, background)

    wtf = canvas.create_text(CanvasWidth //2, 100,"Ezgi: Nasıl geldim buraya? 🤔")
    canvas.set_font(wtf, 'Gabriola', 25)
    canvas.set_color(wtf, 'Purple')

    helpText = canvas.create_text(120, 17, "İlerlemek için 'Sağ Ok' tuşuna basın.")
    canvas.set_font(helpText, 'Gabriola', 15)
    canvas.set_color(helpText, 'White')

    mainCharacter = canvas.create_image_with_size(0, 570, 110, 110, 'babe.png')

    hareket = 1
    while hareket == 1:
        presses = canvas.get_new_key_presses()
        for press in presses:
            if press.keysym == 'Right':
                canvas.move(mainCharacter, mainCharacterSpeed, 0)
                if canvas.get_left_x(mainCharacter) >= CanvasWidth//4:
                    canvas.delete(wtf)
                    canvas.delete(helpText)
                    hareket -= 1
        canvas.update()

def witchCame(witch):
    witch = canvas.create_image_with_size(CanvasWidth//4*3, 450, 110, 110, witch)
    witch_textOne = canvas.create_text(CanvasWidth // 2, 50, "Cadı: DUR!")
    canvas.set_font(witch_textOne, "Gabriola", 25)
    canvas.set_color(witch_textOne, 'White')

    dialogOne = canvas.create_text(CanvasWidth // 2, 85, "Ezgi: Sen de kimsinnn?")
    canvas.set_font(dialogOne, "Gabriola", 25)
    canvas.set_color(dialogOne, 'Purple')

    witch_textTwo = canvas.create_text(CanvasWidth // 2, 120, "Cadı: Emir, elimde. Eğer saldırıma karşı durabilirsen onu geri alabilirsin.😈")
    canvas.set_font(witch_textTwo, "Gabriola", 25)
    canvas.set_color(witch_textTwo, 'White')

    dialogTwo = canvas.create_text(CanvasWidth // 2, 155, "Ezgi: Emir'i bana geri verrrrr.😡")
    canvas.set_font(dialogTwo, "Gabriola", 25)
    canvas.set_color(dialogTwo, 'Purple')

    helpText = canvas.create_text(135, 17, "Savaşa girmek için 'Yukarı Ok' tuşuna basın.")
    canvas.set_font(helpText, 'Gabriola', 15)
    canvas.set_color(helpText, 'White')

    canvas.update()

    dialog = 1
    while dialog == 1:
        presses = canvas.get_new_key_presses()
        for press in presses:
            if press.keysym == 'Up':
                canvas.delete(witch_textOne)
                canvas.delete(dialogOne)
                canvas.delete(witch_textTwo)
                canvas.delete(dialogTwo)
                canvas.delete(witch)
                canvas.delete(helpText)
                dialog -= 1
        canvas.update()

def witchFight(heart,witch,boom):
    witch = canvas.create_image_with_size(CanvasWidth // 4 * 3, 450, 110, 110, witch)
    heartAnimation = canvas.create_image_with_size(CanvasWidth//2-55, CanvasHeight//3-55, 110, 110, heart)

    helpText = canvas.create_text(CanvasWidth//4, CanvasHeight//4, "Arka arkaya 'Sağ Ok' tuşuna bassss.")
    canvas.set_font(helpText, 'Gabriola', 30)
    canvas.set_color(helpText, 'White')

    counter = 0
    versus = 1
    while versus == 1:
        presses = canvas.get_new_key_presses()
        for press in presses:
            if press.keysym == 'Right':
                counter += 1
                canvas.delete(heartAnimation)
                heartAnimation= canvas.create_image_with_size(CanvasWidth // 2 - 55+(counter*10), CanvasHeight // 3 - 55+(counter*10), 120+(counter*10), 120+(counter*10), heart)
                if counter == 16:
                    canvas.delete(heartAnimation)
                    boom = canvas.create_image_with_size(CanvasWidth // 2 - 55+(counter*10), CanvasHeight // 3 - 55+(counter*10), 120+(counter*10), 120+(counter*10), boom)
                    canvas.delete(witch)
                    canvas.delete(helpText)
                    versus -= 1
        canvas.update()
    canvas.update()
    time.sleep(1)

def wonFight(background):
    wonFightBG = canvas.create_image_with_size(0, 0, CanvasWidth, CanvasHeight, background)
    mainCharacter = canvas.create_image_with_size(CanvasWidth//4+2, 570, 110, 110, 'babe.png')

    wonText = canvas.create_text(CanvasWidth // 2, 85, "Ezgi: Onu kurtarmama çok az kaldı.😍")
    canvas.set_font(wonText, "Gabriola", 25)
    canvas.set_color(wonText, 'Purple')

    helpText = canvas.create_text(120, 17, "İlerlemek için 'Sağ Ok' tuşuna basın.")
    canvas.set_font(helpText, 'Gabriola', 15)
    canvas.set_color(helpText, 'White')

    canvas.update()

    hareket = 1
    while hareket == 1:
        presses = canvas.get_new_key_presses()
        for press in presses:
            if press.keysym == 'Right':
                canvas.move(mainCharacter, mainCharacterSpeed, 0)
                canvas.update()
                if canvas.get_left_x(mainCharacter) >= CanvasWidth:
                    canvas.delete(wonFightBG)
                    canvas.delete(mainCharacter)
                    canvas.delete(wonText)
                    canvas.delete(helpText)
                    hareket -= 1
        canvas.update()
    canvas.update()

def inGameFourth(background):
    inGameFourthBG = canvas.create_image_with_size(0, 0, CanvasWidth, CanvasHeight, background)
    mainCharacter = canvas.create_image_with_size(0, 600, 110, 110, 'babe.png')
    fakeEmir = canvas.create_image_with_size(CanvasWidth//4*3, 600, 110, 110, 'fakeEmir.png')
    cage = canvas.create_image_with_size(CanvasWidth//4*3-30, 528, 180, 180, 'cage.png')

    wonText = canvas.create_text(CanvasWidth // 4*3, 85, "Ezgi: LETSGOOOOO!\nHemen kafesten çıkarmam lazım onu.🥳")
    canvas.set_font(wonText, "Gabriola", 25)
    canvas.set_color(wonText, 'White')

    helpText = canvas.create_text(120, 17, "İlerlemek için 'Sağ Ok' tuşuna basın.")
    canvas.set_font(helpText, 'Gabriola', 15)
    canvas.set_color(helpText, 'White')

    canvas.update()

    hareket = 1
    while hareket == 1:
        presses = canvas.get_new_key_presses()
        for press in presses:
            if press.keysym == 'Right':
                canvas.move(mainCharacter, mainCharacterSpeed, 0)
                canvas.update()
                if canvas.get_left_x(mainCharacter) >= CanvasWidth//4*3-115:
                    canvas.delete(cage)
                    time.sleep(1)
                    canvas.update()
                    hareket -= 1
        canvas.update()
    canvas.update()
    canvas.delete(fakeEmir)
    canvas.delete(mainCharacter)

def beforeEndingScene(background):
    aFewTime = 1
    beforeEnd = canvas.create_image_with_size(0, 0, CanvasWidth, CanvasHeight, background)

    helpText = canvas.create_text(120, 17, "İlerlemek için 'Yukarı Ok' tuşuna basın.")
    canvas.set_font(helpText, 'Gabriola', 15)
    canvas.set_color(helpText, 'White')

    while aFewTime == 1:
        presses = canvas.get_new_key_presses()
        for press in presses:
            if press.keysym == 'Up':
                canvas.delete(helpText)
                aFewTime -= 1
        time.sleep(1)
        canvas.update()

def endingScene(background):
    finalbg = canvas.create_image_with_size(0,0,CanvasWidth,CanvasHeight,background)
    couple = canvas.create_image_with_size(0, 600, 110, 110, 'couple.png')

    helpText = canvas.create_text(120, 17, "İlerlemek için 'Sağ Ok' tuşuna basın.")
    canvas.set_font(helpText, 'Gabriola', 15)
    canvas.set_color(helpText, 'White')

    runCouple = 1
    while runCouple == 1:
        presses = canvas.get_new_key_presses()
        for press in presses:
            if press.keysym == 'Right':
                canvas.move(couple, mainCharacterSpeed, 0)
                canvas.update()
                if canvas.get_left_x(couple) >= CanvasWidth //2-60:
                    canvas.delete(helpText)
                    finalText = canvas.create_text(CanvasWidth // 2, 50, "💕SENİ ÇOK SEVİYORUM, BEBEĞİM💕")
                    finalText2 = canvas.create_text(CanvasWidth // 2, 120, "💖Birinci Yılımız Kutlu Olsunnn💖")
                    canvas.set_font(finalText, "Gabriola", 40)
                    canvas.set_color(finalText, 'White')
                    canvas.set_font(finalText2, "Gabriola", 25)
                    canvas.set_color(finalText2, 'White')
                    time.sleep(1.5)
                    canvas.update()
                    runCouple -= 1
        canvas.update()
    canvas.update()

def theEnd(background):
    endbg = canvas.create_image_with_size(0, 0, CanvasWidth, CanvasHeight, background)

    endText = canvas.create_text(CanvasWidth//2,CanvasHeight//2+60,'Created by Emir Yorgun')
    canvas.set_font(endText,"Gabriola",25)
    canvas.set_color(endText, 'White')

    resText = canvas.create_text(CanvasWidth // 2, CanvasHeight // 2 + 250, "tekrar oynamak için 'r' tuşuna basın.")
    canvas.set_font(resText, "Gabriola", 15)
    canvas.set_color(resText, 'White')

def restartGame():
    restartGame = 1
    while restartGame == 1:
        restart = canvas.get_new_key_presses()
        for press in restart:
            if press.keysym == "r":
                canvas.delete_all()
                restartGame = 0
                main()
            time.sleep(delay)
        time.sleep(delay)
        canvas.update()

def main():
    canvas.set_canvas_size(CanvasWidth, CanvasHeight)
    canvas.set_canvas_title("Ezgi, Emir'i Kurtarıyor")
    background = canvas.create_image_with_size(0,0,CanvasWidth,CanvasHeight,'bg.png')

    openingScene()
    inGameFirst(background)
    inGameSecond('snow.jpg')
    inGameThird('forest.png')
    witchCame('witch.png')
    witchFight('heart.png','witch.png','boom.png')
    wonFight('forest.png')
    inGameFourth('night.jpg')
    beforeEndingScene('afewmin.jpg')
    endingScene('finalbg.jpg')
    time.sleep(8)
    theEnd('end.png')
    restartGame()

    canvas.update()
    canvas.mainloop()

if __name__ == '__main__':
    main()