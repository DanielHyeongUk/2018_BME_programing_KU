import random
# 도둑잡기 게임
# 카드를 분배받고 먼저 딜러와 플레이어 각각 겹치는 숫자의 카드를 버리고 본격적으로 게임을 시작합니다.
# 서로 카드를 뽑아가면서 (사용자는 자신이 뽑고 싶은 카드를 생각하고 뽑고 Dealer는 랜덤하게 뽑음) 같은 숫자의 카드를 버린다.
# 마지막에 조커카드 1장만 갖고있게 되면 패배하고 모든 카드를 다 버리면 승리한다. 순서는 항상 플레이어가 선플레이한다.

FACES = list(range(2, 11)) + ['Jack', 'Queen', 'King', 'Ace']
SUITS = ['Clubs', 'Diamonds', 'Hearts', 'Spades']

class Card:
    def __init__(self, face, suit):
        assert (face in FACES and suit in SUITS)
        self.face = face
        self.suit = suit

    def __str__(self):
        return str(str(self.face) + " of " + self.suit)

class Deck:
    def __init__(self):
        self.cards = []
        for suit in SUITS:
            for face in FACES:
                self.cards.append(Card(face, suit))
        self.cards.append("Color Joker") #덱을 만들때 조커카드를 추가함

        random.shuffle(self.cards) # 입력받은 리스트의 원소의 순서를 바꿈

    def draw(self):
        return self.cards.pop()

def log_in(): #사용자가 게임에서 사용할 닉네임을 입력 받는 함수
    print("Welcome to A hunt for thieves")
    user_name = input("Please your nick_name : ")
    return user_name

def card_distribute(): #카드를 분배하는 함수, 총 카드 갯수가 홀수 이므로 사용자는 랜덤하게 26장 혹은 27장을 분배받음
    deck = Deck()
    player_card = []
    dealer_card = []
    All_cards = []

    a = random.randint(0,1)

    if a == 0:
        for i in range(27):
            player_card.append(deck.draw())
        for j in range(26):
            dealer_card.append(deck.draw())
    elif a == 1:
        for i in range(26):
            player_card.append(deck.draw())
        for j in range(27):
            dealer_card.append(deck.draw())

    All_cards.append(dealer_card) #리스트의 0번째 서브 리스트가 딜러의 카드
    All_cards.append(player_card) #리스트의 1번째 서브 리스트가 플레이어의 카드
    return All_cards

def show_card(card_list): # 현재 내가 가지고 있는 카드들의 상태를 보여주는 함수
    print("------당신의 카드들 입니다------.")
    if len(card_list) == 0:
        print("------------N o n e------------\n")
    else:
        for i in card_list:
            print(i)
        print("")


def hunting_thief(All_cards, player_name):
    # 본격적인 도둑잡기 게임 함수, 숫자가 같은 2개의 카드를 버릴 수 있으며 마지막에 조커카드를 갖고 있으면 패배
    print("먼저 같은 숫자의 카드를 버리고 시작하겠습니다.")
    new_dealer = []
    new_player = []

    while True: # 딜러가 갖고 있는 같은 숫자의 카드들을 버림
        for i in All_cards[0]:
            for p in All_cards[0][1:]:
                if str(i)[:2] == str(p)[:2]:
                    print("Dealer throws out (%s) & (%s)" % (i, p))
                    All_cards[0].remove(i)
                    All_cards[0].remove(p)
                    break
            break

        m = 0

        for i in All_cards[0][1:]: # 카드에 겹치는 것이 없을 때 실행
            if str(All_cards[0][0])[:2] != str(i)[:2]:
                m = m + 1

        if m == (len(All_cards[0]) - 1):
            new_dealer.append(All_cards[0][0])
            All_cards[0].remove(All_cards[0][0])

        if len(All_cards[0]) == 0: # 모든 카드를 탐색하면 종료
            break

    print("")


    while True:
        for w in All_cards[1]: #숫자가 겹치는 카드가 있으면 자신의 덱에서 버림
            for e in All_cards[1][1:]:
                if str(w)[:2] == str(e)[:2]:
                    print("Player throws out (%s) & (%s)" % (w, e))
                    All_cards[1].remove(w)
                    All_cards[1].remove(e)
                    break
            break

        d = 0

        for v in All_cards[1][1:]: # 카드에 겹치는 것이 없을 때 실행
            if str(All_cards[1][0])[:2] != str(v)[:2]:
                d = d + 1

        if d == (len(All_cards[1]) - 1):
            new_player.append(All_cards[1][0])
            All_cards[1].remove(All_cards[1][0])

        if len(All_cards[1]) == 0: # 모든 카드를 탐색하면 종료
            break

    print("")
    print("게임을 본격적으로 시작합니다")
    print("상대방의 카드를 1장씩 뽑으며 숫자가 같은 2장의 카드를 버릴 수 있습니다.")

    while True:
        show_card(new_player)
        num = input("%s님 Dealer 의 카드 중 어느것을 가져오겠습니까? (1번 ~ %d번 중 숫자만 입력) : " % (player_name, len(new_dealer)))
        # 사용자는 Dealer의 카드중에서 어떤 카드를 뽑아올지 고민하고 선택
        print("%s 카드를 가져왔습니다." % (new_dealer[int(num) - 1]))
        new_player.append(new_dealer[int(num) - 1])

        for x in new_player[:len(new_player)-1]: # 새로 뽑은 카드와 겹치는 숫자가 있으면 겹치는 카드들을 버림
            if str(new_player[len(new_player)-1])[:2] == str(x)[:2]:
                print("%s throws out (%s) & (%s)\n" % (player_name, x, new_player[len(new_player)-1]))
                new_player.remove(new_player[len(new_player)-1])
                new_player.remove(x)
                break

        random.shuffle(new_player) # 카드섞기

        del (new_dealer[int(num) - 1]) #딜러의 카드에서 뽑았으므로 딜러의 덱에서 삭제


        if len(new_player) == 0: #모든 카드를 버리면 승리
            print("승리자는 %s 입니다. 축하합니다!!!" % player_name)
            show_card(new_player)
            break

        if len(new_dealer) == 0:
            print("아쉽지만 패배하였습니다.")
            show_card(new_player)
            break

        dealer_pick = random.randint(1, len(new_player)) #Dealer 는 랜덤하게 플레이어의 패에서 카드를 뽑음
        print("Dealer 가 당신의 %s 카드를 가져갔습니다." % (new_player[dealer_pick - 1]))
        new_dealer.append(new_player[dealer_pick - 1])

        for n in new_dealer[:len(new_dealer)-1]: # 새로 뽑은 카드와 겹치는 숫자가 있으면 겹치는 카드들을 버림
            if str(n)[:2] == str(new_dealer[len(new_dealer)-1])[:2]:
                print("Dealer throws out (%s) & (%s)" % (n, new_dealer[len(new_dealer)-1]))
                new_dealer.remove(n)
                new_dealer.remove(new_dealer[len(new_dealer)-1])
                break

        random.shuffle(new_dealer) # 카드 섞기

        del (new_player[dealer_pick - 1])

        if len(new_player) == 0:
            print("승리자는 %s 입니다. 축하합니다!!!\n" % player_name)
            show_card(new_player)
            break

        if len(new_dealer) == 0:
            print("아쉽지만 패배하였습니다.\n")
            show_card(new_player)
            break


player_name = log_in() #사용자 닉네임 생성
print("Hi~ %s!!, Let's start A hunt for thieves\n" % player_name)
All_cards = card_distribute()
hunting_thief(All_cards, player_name)

