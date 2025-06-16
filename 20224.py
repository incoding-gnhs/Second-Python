import random

import time

class Card:

    def init(self, suit, rank):

        self.suit = suit

        self.rank = rank

    def str(self):

        return f"{self.rank}{self.suit}"

class Deck:

    def init(self):

        suits = ['♠', '♥', '♦', '♣']

        ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

        self.cards = [Card(suit, rank) for suit in suits for rank in ranks]

        random.shuffle(self.cards)

    def draw(self):

        if self.cards:

            return self.cards.pop()

        return None

class Hand:

    def init(self):

        self.cards = []

    def add_card(self, card):

        self.cards.append(card)

    def get_value(self):

        value = 0

        aces = 0

        for card in self.cards:

            if card.rank in ['J', 'Q', 'K']:

                value += 10

            elif card.rank == 'A':

                aces += 1

            else:

                value += int(card.rank)

        for _ in range(aces):

            if value + 11 <= 21:

                value += 11

            else:

                value += 1

        return value

    def str(self):

        return ' '.join(str(card) for card in self.cards)

def slow_print(text):

    for char in text:

        print(char, end='', flush=True)

        time.sleep(0.03)

    print()

def play_blackjack():

    chips = 1000

    while chips > 0:

        slow_print(f"\n현재 칩: {chips}")

        bet = 0

        while bet <= 0 or bet > chips:

            try:

                bet = int(input("베팅 금액을 입력하세요: "))

                if bet <= 0 or bet > chips:

                    print("올바른 베팅 금액을 입력하세요!")

            except ValueError:

                print("숫자를 입력하세요!")

        deck = Deck()

        player_hand = Hand()

        dealer_hand = Hand()

        # 초기 카드 배분

        player_hand.add_card(deck.draw())

        dealer_hand.add_card(deck.draw())

        player_hand.add_card(deck.draw())

        dealer_hand.add_card(deck.draw())

        slow_print(f"\n할아버지의 카드: {dealer_hand.cards[0]} [?]")

        slow_print(f"당신의 카드: {player_hand}")

        # 플레이어 턴

        while True:

            choice = input("\n1: Hit  2: Stand > ")

            if choice == "1":

                player_hand.add_card(deck.draw())

                slow_print(f"당신의 카드: {player_hand}")

                if player_hand.get_value() > 21:

                    slow_print("버스트! 게임 오버...")

                    chips -= bet

                    break

            elif choice == "2":

                break

        # 딜러 턴

        if player_hand.get_value() <= 21:

            slow_print(f"\n딜러의 카드: {dealer_hand}")

            while dealer_hand.get_value() < 17:

                dealer_hand.add_card(deck.draw())

                slow_print(f"딜러가 카드를 뽑습니다: {dealer_hand}")

            player_value = player_hand.get_value()

            dealer_value = dealer_hand.get_value()

            slow_print(f"\n당신의 점수: {player_value}")

            slow_print(f"딜러의 점수: {dealer_value}")

            if dealer_value > 21:

                slow_print("딜러 버스트! 당신의 승리!")

                chips += bet

            elif player_value > dealer_value:

                slow_print("당신의 승리!")

                chips += bet

            elif player_value < dealer_value:

                slow_print("딜러의 승리...")

                chips -= bet

            else:

                slow_print("무승부!")

        if chips <= 0:

            slow_print("\n모든 칩을 잃었습니다. 게임 오버!")

            break

        play_again = input("\n계속하시겠습니까? (Y/N) > ").upper()

        if play_again != 'Y':

            break

    return chips

if name == "__main__":

    slow_print("\n=== 신비한 카드의 방 ===\n")

    slow_print("어느 날, 당신은 할아버지의 유품을 정리하다가 신비한 편지를 발견했습니다.")

    time.sleep(1)

    slow_print("\n'우리 가문에는 대대로 전해 내려오는 비밀이 있단다...")

    slow_print("바로 이 신비한 카드의 방이지.'")

    time.sleep(1)

    slow_print("\n편지와 함께 발견된 열쇠로 문을 열자")

    slow_print("먼지 쌓인 방 안에서 할아버지의 모습이 보입니다.")

    time.sleep(1)

    slow_print("\n'자네가 올 줄 알았다네. 내 카드 실력을 이어받을 준비가 되었나?'")

    slow_print("'1000개의 행운의 칩으로 시작해보지.'")

    time.sleep(2)



    final_chips = play_blackjack()



    if final_chips > 1000:

        slow_print("\n'훌륭하군! 자네는 이제 진정한 카드의 달인이야.'")

    else:

        slow_print("\n'괜찮아. 언제든 다시 도전할 수 있다네.'")

    slow_print(f"\n최종 칩: {final_chips}")