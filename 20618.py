

import random

import time

import os

def clear_screen():

    os.system('cls' if os.name == 'nt' else 'clear')

class Player:

    def init(self, name):

        self.name = name

        self.health = 100

        self.energy = 100

        self.hacking_skills = ["방어막 해제", "시스템 무력화", "역추적 방어"]

        self.current_objective = "원자로 제어실 침투"

class Enemy:

    def init(self, name, attack_type):

        self.name = name

        self.health = 100

        self.attack_type = attack_type

class Game:

    def init(self):

        self.player = None

        self.is_running = True

        self.current_enemy = None

    def start_game(self):

        clear_screen()

        print("=== 네오시티 2077: 마지막 해커 ===")

        print("\n메가코퍼레이션 '테크노다인'의 비밀 프로젝트 책임자였던 당신...")

        print("그들의 계획이 도시 전체를 핵으로 날려버리는 것임을 알게 되었습니다.")

        print("이제 당신은 그들을 막기 위해 마지막 임무를 수행해야 합니다.\n")



        player_name = input("당신의 해커 코드네임을 입력하세요: ")

        self.player = Player(player_name)

        print(f"\n접속을 시작합니다, {self.player.name}. 행운을 빕니다.\n")

        time.sleep(2)

        self.chapter_one()

    def show_battle_status(self):

        print(f"\n=== 상태 ===")

        print(f"해커: {self.player.name}")

        print(f"체력: {self.player.health}")

        print(f"에너지: {self.player.energy}")

        print(f"현재 목표: {self.player.current_objective}")

        if self.current_enemy:

            print(f"\n적 유닛: {self.current_enemy.name}")

            print(f"적 체력: {self.current_enemy.health}")

    def battle(self, enemy_name, enemy_attack):

        self.current_enemy = Enemy(enemy_name, enemy_attack)

        while self.current_enemy.health > 0 and self.player.health > 0:

            clear_screen()

            self.show_battle_status()

            print(f"\n{self.current_enemy.name}이(가) {self.current_enemy.attack_type}으로 공격합니다!")

            print("\n=== 가능한 해킹 스킬 ===")

            for i, skill in enumerate(self.player.hacking_skills, 1):

                print(f"{i}. {skill}")

            try:

                choice = int(input("\n해킹 스킬을 선택하세요: "))

                if 1 <= choice <= len(self.player.hacking_skills):

                    skill = self.player.hacking_skills[choice-1]

                    self.use_skill(skill)

                else:

                    print("잘못된 선택입니다.")

            except ValueError:

                print("유효한 숫자를 입력하세요.")



            time.sleep(1.5)

        return self.player.health > 0

    def use_skill(self, skill):

        if skill == "방어막 해제":

            damage = random.randint(20, 30)

            self.current_enemy.health -= damage

            self.player.energy -= 10

            print(f"\n>>> 방어막 해제 성공! {damage}의 데미지를 입혔습니다.")

        elif skill == "시스템 무력화":

            damage = random.randint(30, 40)

            self.current_enemy.health -= damage

            self.player.energy -= 20

            print(f"\n>>> 시스템 무력화 성공! {damage}의 데미지를 입혔습니다.")

        elif skill == "역추적 방어":

            heal = random.randint(15, 25)

            self.player.health = min(100, self.player.health + heal)

            self.player.energy -= 15

            print(f"\n>>> 역추적 방어 성공! {heal}의 체력을 회복했습니다.")

        if self.current_enemy.health > 0:

            damage = random.randint(10, 20)

            self.player.health -= damage

            print(f"적의 반격으로 {damage}의 데미지를 받았습니다!")

    def chapter_one(self):

        print("\n=== Chapter 1: 원자로로 가는 길 ===")

        print("\n보안 시스템이 당신의 침입을 감지했습니다!")

        time.sleep(2)

        enemies = [

            ("보안 드론", "전기 충격파"),

            ("방어 터렛", "레이저 공격"),

            ("보안 AI", "신경망 공격")

        ]

        for enemy_name, attack_type in enemies:

            if not self.battle(enemy_name, attack_type):

                print("\n=== 게임 오버 ===")

                print("테크노다인의 보안 시스템에 당신의 해킹이 막혔습니다...")

                return

            print(f"\n{enemy_name}을(를) 무력화했습니다!")

            time.sleep(1.5)

        print("\n=== Chapter 1 클리어! ===")

        print("원자로 제어실 접근에 성공했습니다.")

        print("하지만 이것은 시작에 불과합니다...")

        self.end_game()

    def end_game(self):

        print("\n게임을 종료합니다.")

        self.is_running = False

if name == "__main__":

    game = Game()

    game.start_game()

