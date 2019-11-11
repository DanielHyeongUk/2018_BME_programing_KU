#숫자를 맞추는 야구게임으로서 자리와 숫자가 일치하면 strike 자리는 다르나 숫자가 정답에 포함되어 있으면 Ball이다.
#정답을 맞추면 눈사람이 나와서 축하해준다.
#숫자를 직접 입력하고 약간의 시간이 지나면 결과를 알려준다
#플레이어는 결과를 보고 숫자를 추측하면 된다.
#총 15번의 기회가 주어진다
#게임 처음의 let's go 버튼을 누르면 게임이 진행되고
#게임 종료 후 y / n 키를 눌러 y를 누르면 새로운 창이 뜨면서 새로운 게임을 할 수 있고
#n을 누르면 빈화면이 나왔다가 good bye 라는 인사와 함께 종료된다

from BMP_Packages.BMEgraphics import*
import random
import time
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

class getting_number():
    def __init__(self):
        self.numbers = []
        random.shuffle(numbers)
        self.number1 = numbers[0]
        self.number2 = numbers[1]
        self.number3 = numbers[2]
        self.numbers.append(self.number1)
        self.numbers.append(self.number2)
        self.numbers.append(self.number3)

class Game_board():
    def __init__(self):
        self.canvas = Canvas(800, 800)
        self.canvas.setBackgroundColor((70, 152, 64))
        self.canvas.setTitle("The Base Ball Game")
        self.welcome = Text("Welcome to Base Ball Game", 30)
        self.welcome.moveTo(400, 200)
        self.canvas.add(self.welcome)

        self.play_button = Layer()

        self.button = Rectangle(200, 100, Point(400, 400))
        self.button.setFillColor((255, 228, 0))
        self.button.setDepth(30)

        self.button_text = Text("Let's Go!\n  (Click!)", 20)
        self.button_text.moveTo(400,400)
        self.button_text.setDepth(10)
        self.play_button.add(self.button)
        self.play_button.add(self.button_text)

        self.canvas.add(self.play_button)

    def Game_board_play(self):
        self.player_number = Text("0~9 까지 중복된 숫자가 없는 3자리 숫자를 입력해주세요", 20)
        self.player_number.setFontColor((90, 255, 255))
        self.player_number.moveTo(400, 50)
        self.canvas.add(self.player_number)


def ask(Game):
    e = Game.canvas.wait()
    d = e.getDescription()

    if d == "mouse click":
        position = e.getMouseLocation()
        mx, my = position.get()
        if ((mx <= 500) and (mx >= 300) and (my <= 450) and (my >= 350)):
            Game.canvas.clear()
            Game.Game_board_play()

def input_number (Game):

    i = 10
    input_numbers = []
    rec = Rectangle(200, 100)
    rec.setFillColor((70, 152, 64))
    rec.setBorderColor((70, 152, 64))
    rec.moveTo(360, 200)

    while (i <= 50):
        e = Game.canvas.wait()
        d = e.getDescription()
        if d == "keyboard":
            player_input = e.getKey()
            display_input = Text(player_input, 30)
            display_input.setFontColor((255, 187, 0))
            input_numbers.append(player_input)
            display_input.moveTo(360 + i, 200)
            Game.canvas.add(display_input)
            i = i + 20
    time.sleep(1)
    Game.canvas.add(rec)

    return input_numbers

def strike_check (answer, player_number):
    strike = 0
    indexing = 0
    for i in answer.numbers:
        if i == int(player_number[indexing]):
            strike = strike + 1
        indexing = indexing + 1
    return strike

def ball_check (answer, player_number):
    ball = 0
    if answer.numbers[0] == int(player_number[1]):
        ball = ball + 1
    if answer.numbers[0] == int(player_number[2]):
        ball = ball + 1
    if answer.numbers[1] == int(player_number[0]):
        ball = ball + 1
    if answer.numbers[1] == int(player_number[2]):
        ball = ball + 1
    if answer.numbers[2] == int(player_number[0]):
        ball = ball + 1
    if answer.numbers[2] == int(player_number[1]):
        ball = ball + 1
    return ball



def displaying_result(Game,player_number,strike,high, ball,life):
    final_answer = int(player_number[0])*100 + int(player_number[1])*10 +int(player_number[2])
    if len(str(final_answer)) == 2:
        final_answer = '0' + str(final_answer)
    result = Text("%s is Strike = %d  and  Ball = %d  남은 시도 횟수 : %d" % (final_answer, strike, ball, life-1), 20)
    result.moveTo(300, 300 + high)


    Game.canvas.add(result)



def result(answer, strike, life, Game):
    final_answer = int(answer.numbers[0]) * 100 + int(answer.numbers[1]) * 10 + int(answer.numbers[2])
    if len(str(final_answer)) == 2:
        final_answer = '0' + str(final_answer)

    if ((life >= 1) and (strike == 3)):
        congra = Text("Congraturation!! 홈런!\nThe Answer was %s " % (final_answer), 30)
        congra.setFontColor("red")
        congra.moveTo(400, 200)
        congra.setDepth(0)
        Game.canvas.add(congra)
        symbol = Layer()
        symbol2 = Layer()
        snow_man(symbol)
        snow_man(symbol2)
        symbol.move(40, 20)
        symbol2.move(550, 20)
        Game.canvas.add(symbol)
        Game.canvas.add(symbol2)
        a = play_more(Game)
        return a

    elif ((strike != 3) and (life - 1) == 0):
        loose = Text("You loose!!\nThe Answer was %s " % (final_answer), 30)
        loose.setFontColor("yellow")
        loose.moveTo(400, 200)
        loose.setDepth(0)
        Game.canvas.add(loose)
        a = play_more(Game)
        return a

def snow_man(symbol):
    circle1 = Circle(50, Point(100, 100))
    circle2 = Circle(50, Point(100, 185))
    eye_brow = Rectangle(50, 5, Point(99, 79))
    eye1 = Circle(5, Point(83, 97))
    eye2 = Circle(5, Point(117, 97))
    hand1 = Rectangle(80, 10, Point(150, 140))
    hand2 = Rectangle(80, 10, Point(50, 140))
    mouth = Polygon(Point(82, 115), Point(101, 128), Point(119, 115), Point(122, 119), Point(103, 134), Point(78, 120))
    belly1 = Polygon(Point(102, 172), Point(94, 188), Point(107, 189))
    belly2 = Polygon(Point(101, 206), Point(92, 219), Point(106, 219))
    circle1.setFillColor('white')
    circle1.setBorderColor('white')
    circle2.setFillColor('white')
    circle2.setBorderColor('white')
    eye_brow.setFillColor('black')
    mouth.setFillColor((224, 132, 79))
    eye1.setFillColor((93, 93, 93))
    eye2.setFillColor((93, 93, 93))
    hand1.setFillColor((99, 58, 0))
    hand2.setFillColor((99, 58, 0))
    belly1.setFillColor((128, 65, 217))
    belly2.setFillColor((243, 97, 220))
    hand1.rotate(120)
    hand1.setDepth(100)
    hand2.rotate(-120)
    hand2.setDepth(100)
    symbol.add(circle1)
    symbol.add(circle2)
    symbol.add(eye_brow)
    symbol.add(eye1)
    symbol.add(eye2)
    symbol.add(hand1)
    symbol.add(hand2)
    symbol.add(mouth)
    symbol.add(belly1)
    symbol.add(belly2)

def play_more(Game):
    question = Text("Do you want more game?\nYes : Y / No : N", 20)
    question.setFontColor('yellow')
    question.moveTo(400, 750)
    Game.canvas.add(question)

    e = Game.canvas.wait()
    d = e.getDescription()
    if d == "keyboard":
        one_more_try = e.getKey()

        if one_more_try == 'y':
            Game.canvas.close()
            return False
        if one_more_try == 'n':
            Game.canvas.clear()
            time.sleep(1)
            good_bye = Text("GOOD BYE", 40)
            good_bye.setFontColor('red')
            good_bye.moveTo(400, 400)
            Game.canvas.add(good_bye)
            time.sleep(2)
            Game.canvas.close()
            return True




while (True):
    answer = getting_number()
    Game = Game_board()
    ask(Game)
    high = 0
    life = 15
    #print(answer.numbers) #정답 표시용

    while (life >= 1):
        player_number = input_number(Game)
        strike = strike_check(answer, player_number)
        ball = ball_check(answer, player_number)
        displaying_result(Game, player_number, strike, high, ball, life)
        b = result(answer, strike, life, Game)
        if b == 0:
            break
        if b == 1:
            break
        life = life - 1
        high = high + 28
    if b == 1:
        Game.canvas.close()
        break

