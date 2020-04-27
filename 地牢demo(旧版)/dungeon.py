# coding : utf-8 # Author : Parallel
# Create On 2020 2020/4/24 12:13
import linecache
import random
import time
import sys
from winsound import Beep

FLOOR = 1
SEARCH_TURNS = 0
MAX_SEARCH = 5
FATE_LIST = [
    "怪物来袭",
    "怪物来袭",
    "获得治疗",
    "怪物来袭",
    "踩中陷阱",
    "怪物来袭",
    "获得强化",
    "怪物来袭",
    "怪物强化",
    "怪物来袭",
    "获得经验",
]



class Hero:
    def __init__(self):
        self.NAME = None
        if not self.NAME: self.NAME = str(input("欢迎你,冒险者.给自己取个名字:>"))
        self.MAX_HEALTHY = 1500
        self.HEALTHY = 1500
        if self.HEALTHY > self.MAX_HEALTHY: self.HEALTHY = self.MAX_HEALTHY
        self.MIN_ATTACK = 8  # 8
        self.MAX_ATTACK = 18  # 16
        self.MAX_MAGIC = 500
        self.MAGIC = 500
        if self.MAGIC > self.MAX_MAGIC: self.MAGIC = self.MAX_MAGIC
        self.HIDE = 1
        self.EXP = 0
        self.UP_EXP = 5
        self.LEVEL = 1

    def show(self):
        print(
            f"""
{self.NAME}:
生命:{self.HEALTHY}/{self.MAX_HEALTHY}
攻击:{self.MIN_ATTACK}~{self.MAX_ATTACK}
魔法:{self.MAX_MAGIC}/{self.MAGIC}
防御:{self.HIDE}
等级:{self.LEVEL},经验:{self.EXP}/{self.UP_EXP}
        """)

    def Attack(self, who):
        attack = random.randint(self.MIN_ATTACK, self.MAX_ATTACK) - who.HIDE
        who.HEALTHY -= attack
        print(f"你击中了{who.NAME},造成了{attack}点伤害")

    def AttackPlus(self, who):
        attack = random.randint(self.MIN_ATTACK * 2,
                                self.MAX_ATTACK * 2) * 2 - who.HIDE
        who.HEALTHY -= attack
        self.MAGIC -= 40
        print(f"你使用了普通攻击Plus,造成了{attack}点伤害")

    def BloodAttack(self, who):
        attack = random.randint(self.MIN_ATTACK,
                                self.MAX_ATTACK) * 2 - who.HIDE
        who.HEALTHY -= attack
        self.MAGIC -= 50
        self.HEALTHY += attack // 4 * 3
        print(f"你使用了虹吸斩,造成了{attack}点伤害并且恢复了{attack // 2}点生命值")

    def MagicAttack(self, who):
        attack = random.randint(self.MIN_ATTACK, self.MAX_ATTACK) + \
                 random.randint(1, self.HIDE) * 2 - who.HIDE
        who.HEALTHY -= attack
        self.MAGIC -= 50
        print(f"你使用了远古的魔法秘术,对{who.NAME}造成了{attack}点伤害")

    def WeakenAttack(self, who):
        attack = random.randint(self.MIN_ATTACK,
                                self.MAX_ATTACK) // 1 - who.HIDE
        weaken = random.randint(self.LEVEL, self.MAX_HEALTHY) // 10
        who.HEALTHY -= attack
        if who.MIN_ATTACK > 10 and who.MAX_ATTACK > 10:
            who.MIN_ATTACK -= weaken
            who.MAX_ATTACK -= weaken
        self.MAGIC -= 120
        print(f"你使用了腐蚀攻击,造成了{attack}点伤害,并且削弱了{who.NAME}{weaken}点攻击")

    def AddMagicAttack(self, who):
        attack = random.randint(self.MIN_ATTACK + 10,
                                self.MAX_ATTACK + 10)
        magic = attack // 2 + self.MAX_HEALTHY // 20
        who.HEALTHY -= attack
        self.HEALTHY -= self.MAX_HEALTHY // 20
        self.MAGIC += magic
        print(f"你消耗了{self.MAX_HEALTHY // 20}生命值,对{who.NAME}造成了"
              f"{attack}点伤害并回复了{magic}点魔法")

    def StrongerAttack(self, who):
        attack = random.randint(self.MIN_ATTACK,
                                self.MAX_ATTACK) * 2
        self.MAX_ATTACK += self.LEVEL // 5 + 3
        self.MIN_ATTACK += self.LEVEL // 10 + 2
        who.HEALTHY -= attack
        self.MAGIC -= 150
        print(f"你对{who.NAME}造成了{attack}点伤害并让自己的力量更强了")

    def LuckAttack(self, who):
        FATE = [1, 2, 3, 4, 5, 6, -1, -2, -3]
        print("你使用了全靠运气的命运齿轮...\n开始掷骰子!")
        for _ in range(10):
            random.shuffle(FATE)
        first = random.choice(FATE)
        print(f"你的点数:{first}")
        self.MAGIC -= first * 10
        if first > 0:
            attack = random.randint(self.MIN_ATTACK * first,
                                    self.MAX_ATTACK * first) - who.HIDE
            who.HEALTHY -= attack
            print(f"你对{who.NAME}造成了{attack}点伤害!")
        if first < 0:
            attack = random.randint(self.MAX_ATTACK * first,
                                    self.MIN_ATTACK * first) - who.HIDE
            who.HEALTHY -= attack
            print(f"你对{who.NAME}造成了{attack}点伤害!")

    def LevelUp(self):
        if self.EXP >= self.UP_EXP:
            self.LEVEL += 1
            self.EXP = 0
            self.UP_EXP += self.LEVEL * 2 - 1
            self.MAX_HEALTHY += self.LEVEL * 20 + 100
            self.MAX_ATTACK += self.LEVEL // 5 + 6
            self.MIN_ATTACK += self.LEVEL // 5 + 4
            self.MAX_MAGIC += self.LEVEL // 10 + 5
            self.HIDE += self.LEVEL // 40
            print("升级!")

    def ChoiceAttack(self, monster):
        self.show()
        print(
            f"""
你可以选择:
1.普通攻击/2.攻击Plus
3.虹吸斩击/4.能量斩击
5.腐蚀斩击/6.献祭攻击
7.强化攻击/8.命运齿轮
             """)
        try:
            you = int(input("选择攻击方式:"))
            if you == 1:
                self.Attack(who=monster)
            elif you == 2:
                if self.MAGIC > 0:
                    self.AttackPlus(who=monster)
                else:
                    print("魔法不足")
            elif you == 3:
                if self.MAGIC > 0:
                    self.BloodAttack(who=monster)
                else:
                    print("魔法不足")
            elif you == 4:
                if self.MAGIC > 0:
                    self.MagicAttack(who=monster)
                else:
                    print("魔法不足")
            elif you == 5:
                if self.MAGIC > 0:
                    self.WeakenAttack(who=monster)
                else:
                    print("魔法不足")
            elif you == 6:
                self.AddMagicAttack(who=monster)
            elif you == 7:
                if self.MAGIC > 0:
                    self.StrongerAttack(who=monster)
                else:
                    print("魔法不足")
            elif you == 8:
                if self.MAGIC > 0:
                    self.LuckAttack(who=monster)
                else:
                    print("魔法不足")

        except ValueError:
            print("选择错误")
            self.ChoiceAttack(monster=monster)


class Monster:
    def restart(self):
        if self.HEALTHY <= 0:
            print(f"{self.NAME}去世.")
            self.NAME = random.choice(self.NAME_LIST)
            hero.MAGIC += hero.MAX_MAGIC // 10
            self.HEALTHY += 100 + self.DEAD * 10 + hero.LEVEL \
                            * 10
            self.HIDE += self.DEAD // 10
            self.MAX_ATTACK = self.CMAX_ATTACK
            self.MIN_ATTACK = self.CMIN_ATTACK
            self.MAX_ATTACK += self.DEAD // 10 + hero.LEVEL // 10
            self.MIN_ATTACK += self.DEAD // 15 + hero.LEVEL // 10
            self.ALIVE = False
            hero.EXP += self.EXP
            if self.DEAD > 5:
                self.DEAD = 0
                self.EXP += 2

    def __init__(self):
        self.NAME_LIST = ["地牢巡守", "豺狼人哨兵", "哥布林", "DM-便携型", "下水道螃蟹"]
        self.NAME = random.choice(self.NAME_LIST)
        self.DEAD = 0
        self.HEALTHY = 30 * hero.LEVEL + 20 * FLOOR + self.DEAD * 6
        self.MIN_ATTACK = 2 * FLOOR // 2 + 8
        self.MAX_ATTACK = 3 * FLOOR // 2 + 12
        self.CMIN_ATTACK = self.MIN_ATTACK
        self.CMAX_ATTACK = self.MAX_ATTACK
        self.HIDE = 3 + FLOOR // 10
        self.ALIVE = False
        self.EXP = 3

    def show(self):
        print(
            f"""
{self.NAME}:
生命:{self.HEALTHY},攻击力:{self.MIN_ATTACK}~{self.MAX_ATTACK}
防御:{self.HIDE}
            """)

    def Attack(self, who):
        if self.ALIVE:
            attack = random.randint(self.MIN_ATTACK,
                                    self.MAX_ATTACK) - who.HIDE
            who.HEALTHY -= attack
            print(f"{self.NAME}攻击了{who.NAME}并造成了{attack}点伤害")


class BOSS:
    def restart(self):
        if self.HEALTHY <= 0:
            hero.MAGIC += hero.MAX_MAGIC // 5
            print(f"{self.NAME}去世.")
            self.NAME = random.choice(self.NAME_LIST)
            self.HEALTHY = self.HEALTHY_COPY + self.DEAD * 10 + hero.LEVEL \
                           * 5
            self.HIDE += self.DEAD // 10
            self.HEALTHY_COPY = self.HEALTHY
            self.MIN_ATTACK = self.CMIN_ATTACK
            self.MAX_ATTACK = self.CMAX_ATTACK
            self.MAX_ATTACK += self.DEAD // 10 + FLOOR * 2
            self.MIN_ATTACK += self.DEAD // 15 + FLOOR * 2
            self.ALIVE = False
            if self.DEAD > 1:
                self.EXP += 10
                self.DEAD = 0

    def __init__(self):
        self.NAME_LIST = ["地牢典狱司", "DM-2500", "要你命-3000", "地牢猎手", "陨落战甲"]
        self.NAME = random.choice(self.NAME_LIST)
        self.HEALTHY = 6500
        self.MIN_ATTACK = 26 + hero.MIN_ATTACK // 8 + FLOOR
        self.MAX_ATTACK = 42 + hero.MIN_ATTACK // 8 + FLOOR
        self.CMIN_ATTACK = self.MIN_ATTACK
        self.CMAX_ATTACK = self.MAX_ATTACK
        self.DEAD = 1
        self.ALIVE = False
        self.HIDE = 6
        self.EXP = 20
        self.HEALTHY_COPY = 7800 + 200

    def show(self):
        print(
            f"""
{self.NAME}:
生命:{self.HEALTHY},攻击力:{self.MAX_ATTACK}~{self.MIN_ATTACK}
防御:{self.HIDE}
            """)

    def Attack(self, who):
        if self.ALIVE:
            attack = random.randint(self.MIN_ATTACK,
                                    self.MAX_ATTACK) - who.HIDE
            who.HEALTHY -= attack
            print(f"{self.NAME}攻击了{who.NAME}并造成了{attack}点伤害")


hero = Hero()
monster = Monster()
boss = BOSS()
print("欢迎来到<简陋的文字地牢1.0>")
print("加载中...")
print("加载成功!")
print("走你.")


def NormalDungeon():
    global FLOOR, SEARCH_TURNS, MAX_SEARCH, FATE_LIST
    print(
        f"""
当前层数:{FLOOR},本层你已经探索了{SEARCH_TURNS}次
你可以采取的行动:
1.下楼(你可以这么做,但是你的属性不会得到任何的变化.最好多探索几次)
2.探索(你最多可以探索{MAX_SEARCH}次...)
3.查看状态
        """)
    try:
        you = int(input("你的命运掌握在你的手中:"))
        if you == 1:
            print("你来到了更险恶的地方")
            FLOOR += 1
            SEARCH_TURNS = 0
            monster.HEALTHY += hero.HEALTHY // 100 + 10
            monster.HEALTHY_COPY = monster.HEALTHY
        if you == 2:
            if SEARCH_TURNS < MAX_SEARCH:
                random.shuffle(FATE_LIST)
                print("你开始探索")
                fate = random.choice(FATE_LIST)
                if fate == "怪物来袭":
                    print(f"你遇上了{monster.NAME}")
                    monster.ALIVE = True
                    SEARCH_TURNS += 1
                    while hero.HEALTHY > 0 and monster.ALIVE:
                        monster.show()
                        hero.ChoiceAttack(monster=monster)
                        monster.restart()
                        monster.Attack(hero)
                        hero.LevelUp()

                        if hero.HEALTHY <= 0:
                            SEARCH_TURNS += 1
                            print("你长眠在了这片地牢里......")
                            input("Press enter key to exit...")
                            sys.exit("死亡")

                if fate == "获得治疗":
                    print("你获得了治疗")
                    hero.HEALTHY += hero.MAX_HEALTHY // 20
                    SEARCH_TURNS += 1

                if fate == "踩中陷阱":
                    print("你触碰到了陷阱")
                    hero.HEALTHY -= hero.MAX_HEALTHY // 20
                    SEARCH_TURNS += 1
                    if hero.HEALTHY <= 0:
                        print("你挂了")
                        input("Press enter key to exit...")
                        sys.exit("死亡")

                if fate == "获得经验":
                    print("你感觉获得了什么...")
                    hero.EXP += hero.UP_EXP // 20 + 1
                    hero.LevelUp()
                    SEARCH_TURNS += 1

                if fate == "怪物强化":
                    print("地牢里仿佛更加阴森了")
                    monster.HEALTHY += FLOOR // 10
                    monster.HEALTHY_COPY = monster.HEALTHY
                    monster.MIN_ATTACK += FLOOR // 20
                    monster.MAX_ATTACK += FLOOR // 20
                    SEARCH_TURNS += 1
                if fate == "获得强化":
                    print("你感觉更加强壮了")
                    hero.MAX_HEALTHY += FLOOR // 10 + hero.LEVEL * 10
                    hero.MAX_ATTACK += FLOOR // 20 + 1
                    hero.MIN_ATTACK += FLOOR // 20 + 1
                    hero.HIDE += 2
                    SEARCH_TURNS += 1
        if you == 3:
            hero.show()

        

    except ValueError:
        print("重新选择")
        NormalDungeon()


def BossFloor():
    global FLOOR
    print("这个地牢的房间格外的恐怖...")
    print("你看到一个庞大的身影......")
    print(f"Boss层:{boss.NAME}")
    boss.ALIVE = True
    while boss.ALIVE and hero.HEALTHY > 0:
        boss.show()
        hero.ChoiceAttack(boss)

        boss.restart()
        boss.Attack(hero)
        if hero.HEALTHY <= 0:
            print("你死了")
            sys.exit("死亡")
        if not boss.ALIVE:
            print(f"你打败了{monster.NAME}!")
            FLOOR += 1
            break


def main():
    while True:
        if (FLOOR % 20) != 0:
            NormalDungeon()
        elif (FLOOR % 20) == 0:
            BossFloor()


if __name__ == '__main__':
    # NormalSound()
    main()
