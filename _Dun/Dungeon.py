# coding : utf-8 # Author : Administrator
# Create On 2020 2020/4/25 14:35
import random
import sys
import os
import time

FLOOR = 1
MAX_SEARCH_TURNS = 15
SEARCH_TURNS = 0
FATE_LIST = [
    "怪物来袭",
    "怪物来袭",
    "获得治疗",
    "获得治疗",
    "怪物来袭",
    "踩中陷阱",
    "获得治疗",
    "怪物来袭",
    "怪物来袭",
    "怪物来袭",
    "怪物来袭",
    "怪物来袭",
    "怪物来袭"
]
os.system("title 陈旧的地牢")


class MonsterOrigin:
    """
    怪物基类.
    """

    def restart(self, who):
        self.__init__()
        who.EXP += self.EXP
        who.MAGIC += who.MAX_MAGIC // 20

    def __init__(self):
        self.NAME = ""
        self.HEALTHY = 20 * FLOOR
        self.MIN_ATTACK = 5 + FLOOR - 1
        self.MAX_ATTACK = 12 + FLOOR - 1
        self.HIDE = FLOOR // 20
        self.SHIELD = 0
        self.EXP = 2

    def Attack(self, who):
        attack = random.randint(self.MIN_ATTACK, self.MAX_ATTACK) - who.HIDE
        try:
            if who.SHIELD > 0:
                who.SHIELD -= attack
            else:
                who.HEALTHY -= attack
        except AttributeError:
            who.HEALTHY -= attack

        print(f"{self.NAME}攻击了{who.NAME}造成了{attack}点伤害")

    def show(self):
        print(
            f"""
{self.NAME}:
血量:{self.HEALTHY},防御:{self.HIDE}
护甲:{self.SHIELD},攻击力:{self.MIN_ATTACK}~{self.MAX_ATTACK}
            """
        )


class UndeadSkeleton(MonsterOrigin):
    """
    亡灵骷髅,算是普通小兵.
    """

    def __init__(self):
        super().__init__()
        self.NAME = "亡灵骷髅"


class JackalSoldier(MonsterOrigin):
    """
    豺狼人巡守,普通的豺狼人士兵,血厚了一点.
    """

    def __init__(self):
        super().__init__()
        self.NAME = "豺狼人巡守"
        self.HEALTHY = FLOOR * 30
        self.MIN_ATTACK += 1
        self.MAX_ATTACK += 1


class CaveBat(MonsterOrigin):
    """
    洞穴蝙蝠,会吸血.攻击比较疼.血量薄.
    """

    def __init__(self):
        super().__init__()
        self.NAME = "洞穴蝙蝠"
        self.HEALTHY = FLOOR * 15
        self.MIN_ATTACK += FLOOR
        self.MAX_ATTACK += FLOOR
        self.EXP = 4

    def Attack(self, who):
        attack = random.randint(self.MIN_ATTACK, self.MAX_ATTACK) - who.HIDE
        try:
            if who.SHIELD:
                if who.SHIELD > 0:
                    who.SHIELD -= attack
                else:
                    who.HEALTHY -= attack
            else:
                who.HEALTHY -= attack
        except AttributeError:
            who.HEALTHY -= attack
        self.HEALTHY += attack
        print(f"{self.NAME}攻击了{who.NAME}造成了{attack}点伤害")


class DarkElement(MonsterOrigin):
    """
    暗元素,攻击很疼.
    """

    def __init__(self):
        super().__init__()
        self.NAME = "暗元素"
        self.MIN_ATTACK += FLOOR * 5
        self.MAX_ATTACK += FLOOR * 5
        self.EXP = 2


class DM200(MonsterOrigin):
    """
    比较恶心,血厚盾厚穿甲攻击还高.
    """

    def __init__(self):
        super().__init__()
        self.NAME = "DM-200"
        self.SHIELD = FLOOR * 10
        self.HEALTHY = FLOOR * 50 + self.SHIELD * 2
        self.MIN_ATTACK += FLOOR * 2
        self.MAX_ATTACK += FLOOR * 4
        self.EXP = 6

    def Attack(self, who):
        attack = random.randint(self.MIN_ATTACK, self.MAX_ATTACK)
        try:
            if who.SHIELD:
                if who.SHIELD > 0:
                    who.SHIELD -= attack
                else:
                    who.HEALTHY -= attack
            else:
                who.HEALTHY -= attack
        except AttributeError:
            who.HEALTHY -= attack
        print(f"{self.NAME}攻击了{who.NAME}造成了{attack}点伤害")


class DarkBeliever(MonsterOrigin):
    """
    黑暗信徒,真的,一个纯粹的输出怪物.
    """

    def __init__(self):
        super().__init__()
        self.NAME = "黑暗信徒"
        self.HEALTHY = FLOOR * 5
        self.MIN_ATTACK = FLOOR * 10
        self.MAX_ATTACK = FLOOR * 15
        self.EXP = 5


class ForestSoul(MonsterOrigin):
    """
    森林之魂,每次攻击同时回血.
    """

    def __init__(self):
        super().__init__()
        self.NAME = "森林之魂"
        self.HEALTHY = FLOOR * 25
        self.MIN_ATTACK = FLOOR * 2
        self.MAX_ATTACK = FLOOR * 2
        self.EXP = 4

    def Attack(self, who):
        attack = random.randint(self.MIN_ATTACK, self.MAX_ATTACK) - who.HIDE
        try:
            if who.SHIELD:
                if who.SHIELD > 0:
                    who.SHIELD -= attack
                else:
                    who.HEALTHY -= attack
            else:
                who.HEALTHY -= attack
        except AttributeError:
            who.HEALTHY -= attack
        self.HEALTHY += attack // 10
        print(f"{self.NAME}攻击了{who.NAME}造成了{attack}点伤害")


class Shaman(MonsterOrigin):
    """
    萨满祭司,攻击力非~常~不~稳~定!
    """

    def __init__(self):
        super().__init__()
        self.NAME = "萨满祭司"
        self.MIN_ATTACK = 1
        self.MAX_ATTACK = FLOOR * 15 - 5
        self.HEALTHY = FLOOR * 15
        self.EXP = random.randint(1, 8)


class BugMachine(MonsterOrigin):
    """
    出故障的机器人,无视护甲并造成两倍伤害.
    """

    def __init__(self):
        super().__init__()
        self.NAME = "出故障的机器人"

    def Attack(self, who):
        attack = random.randint(self.MIN_ATTACK, self.MAX_ATTACK) * 2
        try:
            if who.SHIELD:
                if who.SHIELD > 0:
                    who.SHIELD -= attack
                else:
                    who.HEALTHY -= attack
            else:
                who.HEALTHY -= attack
        except AttributeError:
            who.HEALTHY -= attack

        print(f"{self.NAME}攻击了{who.NAME}造成了{attack}点伤害")


class IronSoul(MonsterOrigin):
    """
    钢铁之魂,血量很~很~很~很~很~厚...
    """

    def __init__(self):
        super().__init__()
        self.NAME = "钢铁之魂"
        self.HEALTHY = FLOOR * 50 + FLOOR // 0.5 + 50
        self.MIN_ATTACK -= 1
        self.MAX_ATTACK -= 1
        self.SHIELD += FLOOR * 30


class IronScavenger(MonsterOrigin):
    """
    钢铁清道夫,防御很高,游侠：”你打我一个试试?“
    """

    def __init__(self):
        super().__init__()
        self.NAME = "地牢·钢铁清道夫"
        self.MIN_ATTACK += FLOOR - 1
        self.MAX_ATTACK += FLOOR - 1
        self.HIDE += 1
        self.SHIELD += FLOOR * 25


UndeadSkeleton = UndeadSkeleton()
JackalSoldier = JackalSoldier()
CaveBat = CaveBat()
DarkElement = DarkElement()
DM200 = DM200()
DarkBeliever = DarkBeliever()
ForestSoul = ForestSoul()
Shaman = Shaman()
BugMachine = BugMachine()
IronSoul = IronSoul()
IronScavenger = IronScavenger()

__all__ = [UndeadSkeleton,
           JackalSoldier,
           CaveBat,
           DarkElement,
           DM200,
           DarkBeliever,
           ForestSoul,
           Shaman,
           BugMachine,
           IronSoul,
           IronScavenger
           ]


def Choice():
    global __all__
    random.shuffle(__all__)
    return random.choice(__all__)


class BossOrigin:
    """
    Boss基类
    """

    def restart(self, who):
        self.__init__()
        who.EXP += self.EXP
        who.MAGIC += who.MAX_MAGIC // 5

    def __init__(self):
        self.NAME = "The Origin Of Bosses"
        self.HEALTHY = FLOOR * 300
        self.MIN_ATTACK = FLOOR
        self.MAX_ATTACK = FLOOR * 1.5 // 1
        self.SHIELD = 0
        self.EXP = FLOOR * 1.5 // 1
        self.HIDE = FLOOR // 100
        self.ATTACK_TURNS = 0
        self.BOSS_ATTACK_TURNS = 10

    def BossAttack(self, who):
        pass

    def NormalAttack(self, who):
        attack = random.randint(self.MIN_ATTACK, self.MAX_ATTACK) - who.HIDE
        try:
            if who.SHIELD > 0:
                who.SHIELD -= attack
            else:
                who.HEALTHY -= attack
        except AttributeError:
            who.HEALTHY -= attack
        self.ATTACK_TURNS += 1
        print(f"{self.NAME}对{who.NAME}造成了{attack}点伤害.")

    def Attack(self, who):
        if self.ATTACK_TURNS >= self.BOSS_ATTACK_TURNS:
            self.ATTACK_TURNS = 0
            self.BossAttack(who)
        else:
            self.NormalAttack(who)

    def show(self):
        print(
            f"""
{self.NAME}:
血量:{self.HEALTHY},攻击力:{self.MIN_ATTACK}~{self.MAX_ATTACK}
防御力:{self.HIDE},护甲:{self.SHIELD}
下次Boss攻击回合:{self.ATTACK_TURNS}/{self.BOSS_ATTACK_TURNS}
"""
        )

    def __str__(self):
        return "你不可能调出这个Boss来."


class StoneGiant(BossOrigin):
    """
    石头巨人,血量较高.
    """

    def __init__(self):
        super().__init__()
        self.NAME = "石头魔像"
        self.HEALTHY = FLOOR * 400 - 500
        self.BOSS_ATTACK_TURNS = 10

    def BossAttack(self, who):
        print(f"{self.NAME}开始蓄力...")
        plus = random.randint(2, 3)
        attack = random.randint(self.MIN_ATTACK * plus, self.MAX_ATTACK * plus) - who.HIDE
        who.HEALTHY -= attack
        print("BOOM!")
        print(f"{self.NAME}")

    def __str__(self):
        return f"{self.NAME}:好久没有人来过这里了......"


class DungeonWarden(BossOrigin):
    """
    地牢守望者,血量少但是攻击高.
    """

    def __init__(self):
        super().__init__()
        self.NAME = "地牢守望者"
        self.HEALTHY = FLOOR * 250
        self.MAX_ATTACK = FLOOR * 2.5 + random.randint(1, 10) // 1
        self.MIN_ATTACK = FLOOR * 2.5 + random.randint(1, 10) // 1
        self.BOSS_ATTACK_TURNS = 6

    def BossAttack(self, who):
        print(f"{self.NAME}:你完蛋了!")
        attack = random.randint(self.MIN_ATTACK, self.MAX_ATTACK) * 6
        who.HEALTHY -= attack
        print(f"{self.NAME}致命地打击了{who.NAME}")

    def __str__(self):
        return f"{self.NAME}:开始狂欢吧!"


class Kraken(BossOrigin):
    """
    克拉肯,Boss攻击造成惊天伤害,血量低于50%狂暴.
    """

    def __init__(self):
        super().__init__()
        self.NAME = "克拉肯"
        self.HEALTHY = FLOOR * 350
        self.HEALTHY_SIZE = self.HEALTHY
        self.MIN_ATTACK = FLOOR * 2.5 + random.randint(1, 3) // 1
        self.MAX_ATTACK = FLOOR * 2.5 + random.randint(1, 3) // 1
        self.BOSS_ATTACK_TURNS = 3
        self.MAD_ACTIVE = False

    def BossAttack(self, who):
        pd = self.HEALTHY / self.HEALTHY_SIZE
        if pd > 0.5:
            self.NormalAttack(who)
        if pd <= 0.5:
            if not self.MAD_ACTIVE:
                print(f"{self.NAME}狂暴了!")
                self.MIN_ATTACK *= 2
                self.MAX_ATTACK *= 2
                self.NAME = "狂暴克拉肯"
                self.NormalAttack(who)
                self.MAD_ACTIVE = True
            if self.MAD_ACTIVE:
                self.NormalAttack(who)

    def __str__(self):
        return f"{self.NAME}:'&%%%^*(**((*&&^%%*((()()(#(*@)('?!"


class DM3000(BossOrigin):
    """
    纯粹一个超级血厚的能扛的机器人,血量变少攻击变高.
    """

    def __init__(self):
        super().__init__()
        self.NAME = "DM-3000"
        self.HEALTHY = FLOOR * 400
        self.MIN_ATTACK = FLOOR
        self.MAX_ATTACK = FLOOR + random.randint(1, 13)
        self.HEALTHY_SIZE = self.HEALTHY
        self.SHIELD = self.HEALTHY // 5
        self.BOSS_ATTACK_TURNS = 5

    def BossAttack(self, who):
        print(f"{self.NAME}开始蓄力...")
        pd = self.HEALTHY / self.HEALTHY_SIZE
        min_attack = self.MIN_ATTACK + self.MIN_ATTACK * (1 - pd) // 1
        max_attack = self.MAX_ATTACK + self.MAX_ATTACK * (1 - pd) // 1
        attack = random.randint(min_attack, max_attack)
        who.HEALTHY -= attack
        if pd <= 0.5:
            print(f"{self.NAME}自身完整度:{pd}%,开启疯狂模式.")
        print(f"{self.NAME}对{who.NAME}造成了{attack}点伤害!")

    def __str__(self):
        return f"{self.NAME}:检测到非法生命体入侵,启动“驱除”任务."


class Tengu(BossOrigin):
    """
    天狗,攻击力飘忽不定,会回血.
    """

    def __init__(self):
        super().__init__()
        self.NAME = "天狗"
        self.MIN_ATTACK = 1
        self.MAX_ATTACK = FLOOR * 20
        self.SHIELD = FLOOR * 5
        self.BOSS_ATTACK_TURNS = 5

    def BossAttack(self, who):
        print(f"{self.NAME}:秘术·虹吸斩!")
        attack = random.randint(self.MIN_ATTACK + FLOOR, self.MAX_ATTACK + FLOOR)
        who.HEALTHY -= attack
        self.HEALTHY += attack // 5
        print(f"{self.NAME}:勇士,继续战斗!")

    def __str__(self):
        return f"{self.NAME}:勇士,直面我!"


class DemiGod(BossOrigin):
    """
    两条命(第二条半价),如果一定时间打不死他会回血.
    """

    def __init__(self):
        super().__init__()
        self.NAME = "陨落的半神"
        self.MIN_ATTACK = FLOOR
        self.MAX_ATTACK = FLOOR + random.randint(1, FLOOR)
        self.HEALTHY_COPY = self.HEALTHY
        self.TWICE = False
        self.SHIELD = FLOOR
        self.BOSS_ATTACK_TURNS = 8

    def BossAttack(self, who):
        if self.HEALTHY > 0:
            print(f"{who.NAME}清楚地听到了{self.NAME}在吟唱!")
            attack = random.randint(self.MIN_ATTACK, self.MAX_ATTACK)
            who.HEALTHY -= attack
            self.HEALTHY += attack // 5
            self.SHIELD += attack // 2
        if self.HEALTHY <= 0:
            if not self.TWICE:
                print(f"{self.NAME}:重见天日吧,陨落灵魂!")
                self.HEALTHY = self.HEALTHY_COPY // 2
                self.SHIELD = self.HEALTHY_COPY // 5
                self.MIN_ATTACK += FLOOR
                self.MAX_ATTACK += FLOOR
                self.TWICE = True
            if self.TWICE:
                print(f"DEAD")

    def __str__(self):
        return f"{self.NAME}:啊,终于有活人来到我的面前了,半神与人类之间的战斗决不罢休!"


StoneGiant = StoneGiant()
DungeonWarden = DungeonWarden()
Kraken = Kraken()
DM3000 = DM3000()
Tengu = Tengu()
DemiGod = DemiGod()

__BossAll__ = [
    StoneGiant,
    DungeonWarden,
    Kraken,
    DM3000,
    Tengu,
    DemiGod
]


def Choose():
    while True:
        random.shuffle(__BossAll__)
        return random.choice(__BossAll__)


class OriginMan:
    """
    人物基类,所有人物的东西都是在这里继承的.
    """

    def __init__(self):
        # 其他类，如姓名和等级，经验
        self.NAME = ""
        self.EXP = 0
        self.UP_EXP = 6
        self.LEVEL = 1
        # 生命值
        self.HEALTHY = 1000
        self.MAX_HEALTHY = 1000
        # 攻击力
        self.MIN_ATTACK = 8
        self.MAX_ATTACK = 12
        self.MAGIC_ATTACK = 12
        # 魔法值
        self.MAX_MAGIC = 100
        self.MAGIC = 100
        # 其他值
        self.HIDE = 1
        self.SPEED = 1
        self.SHIELD = 0
        self.STRONG = 0
        self.CRIT = 0

    def Attack(self, who):
        """
        :rtype: object
        """
        attack = random.randint(self.MIN_ATTACK, self.MAX_ATTACK) - who.HIDE
        try:
            if who.SHIELD > 0:
                who.SHIELD -= attack
            else:
                who.HEALTHY -= attack
        except AttributeError:
            who.HEALTHY -= attack

        print(f"{self.NAME}攻击了{who.NAME}造成了{attack}点伤害")

    def LevelUp(self):
        pass


class Warrior(OriginMan):
    """
    狂暴，卖血，巨量的物理攻击
    """

    def __init__(self):
        super().__init__()
        self.NAME = "战士"
        self.HEALTHY += 500
        self.MAX_HEALTHY += 500
        self.MIN_ATTACK += 17
        self.MAX_ATTACK += 17
        self.STRONG += 2
        self.MAX_MAGIC += 250
        self.MAGIC += 250
        self.HEAVY_BLOW_TURNS = 0
        self.HEAVY_BLOW_SPEND = 10 + self.HEAVY_BLOW_TURNS * 5
        self.HEAVY_BLOW_ATTACK = 10 + self.HEAVY_BLOW_TURNS * self.LEVEL

    def Siphon(self, who):
        """
        造成伤害的2倍(最大最小伤害*2)并回复伤害50%的血量
        """
        attack = random.randint(self.MIN_ATTACK * 2, self.MAX_ATTACK * 2) - who.HIDE
        blood = attack // 2
        self.MAGIC -= 80
        self.HEALTHY += blood
        who.HEALTHY -= attack
        print("魔法-50")
        print(f"{self.NAME}攻击了{who.NAME}造成了{attack}点伤害,并恢复了{blood}滴血.")

    def PlusPlus(self, who):
        """
        强力攻击，将攻击*3
        """
        attack = random.randint(self.MIN_ATTACK, self.MAX_ATTACK) - who.HIDE
        attack *= 3
        self.MAGIC -= 50
        who.HEALTHY -= attack
        print("魔法-50")
        print(f"{self.NAME}重重地攻击了{who.NAME}造成了{attack}点伤害.")

    def LifeBlow(self, who):
        """
        舍身一击，牺牲最大生命值10%并造成4倍伤害+力量*10
        """
        attack = random.randint(self.MIN_ATTACK, self.MAX_ATTACK) - who.HIDE
        sub_healthy = self.MAX_HEALTHY // 10
        attack *= 4
        attack += self.STRONG * 10
        self.HEALTHY -= sub_healthy
        who.HEALTHY -= attack
        print(f"生命-{sub_healthy}")
        print(f"{self.NAME}以生命为代价对{who.NAME}造成了{attack}点伤害.")

    def BerserkerRoar(self, who):
        """
        @神技
        狂战士的怒吼,血量越少攻击越高(理论上上不封顶),和舍身一击一起用有奇效.
        """
        angry = self.MAX_HEALTHY // self.HEALTHY + 1
        if angry > 3:
            angry += 2
        attack = random.randint(self.MIN_ATTACK, self.MAX_ATTACK)
        attack *= angry

        self.MAGIC -= 10
        who.HEALTHY -= attack
        self.HEALTHY -= self.MAX_HEALTHY // 100
        print(f"生命-{self.MAX_HEALTHY // 100}")
        print(f"{self.NAME}怒吼着斩向了{who.NAME}造成了{attack}点伤害!")

    def HeavyBlow(self, who):
        """
        要害重击,无视防御力并造成攻击.三连击哦.还会清空最后赢家的次数哟.
        """
        print("魔法-120")
        for _ in range(3):
            attack = random.randint(self.MIN_ATTACK,
                                    self.MAX_ATTACK)
            self.HEAVY_BLOW_TURNS = 0
            self.MAGIC -= 40
            who.HEALTHY -= attack
            print(f"{self.NAME}对{who.NAME}造成了{attack}点伤害!")

        else:
            self.HEAVY_BLOW_TURNS = 0

    def EndWinner(self, who):
        """
        最后赢家.连击,随着使用次数的增多造成更多伤害和魔法.
        """
        print(f"魔法-{self.HEAVY_BLOW_SPEND}")
        attack = self.HEAVY_BLOW_ATTACK
        self.MAGIC -= self.HEAVY_BLOW_SPEND
        self.HEAVY_BLOW_TURNS += 1
        self.HEAVY_BLOW_SPEND = 5 + self.HEAVY_BLOW_TURNS * 2
        self.HEAVY_BLOW_ATTACK = 10 + self.HEAVY_BLOW_TURNS * self.LEVEL + 2
        who.HEALTHY -= self.HEAVY_BLOW_ATTACK
        print(f"{self.NAME}对{who.NAME}造成了{attack}点伤害,谁知道呢?")

    def show(self):
        print(
            f"""
{self.NAME}:
生命值:{self.HEALTHY}/{self.MAX_HEALTHY},攻击力:{self.MIN_ATTACK}~{self.MAX_ATTACK}
魔法值:{self.MAGIC}/{self.MAX_MAGIC},力量:{self.STRONG}
防御:{self.HIDE},等级:{self.LEVEL},经验{self.EXP}/{self.UP_EXP}
最终赢家使用情况:次数:{self.HEAVY_BLOW_TURNS},下次花费:{self.HEAVY_BLOW_SPEND},攻击力{self.HEAVY_BLOW_ATTACK}
""")

    def LevelUp(self):
        if self.EXP >= self.UP_EXP:
            print("你升级了!你的力量,生命值,灵敏度,魔法等级都提高了!")
            self.MAX_HEALTHY += self.LEVEL * 10 + self.STRONG * 5
            self.HEALTHY += self.MAX_HEALTHY // 10
            self.MIN_ATTACK += self.LEVEL + 1
            self.MAX_ATTACK += self.LEVEL + 1
            self.STRONG += self.LEVEL // 10
            self.MAX_MAGIC += 10
            self.MAGIC += self.MAX_MAGIC // 10
            self.MAGIC_ATTACK += self.LEVEL * 2
            self.EXP = 0
            self.LEVEL += 1
            self.UP_EXP += self.LEVEL * 1.5 // 2

    def Choice(self, who):
        """
        选择如何攻击,这个判断有点骚.
        """
        print(
            """
你的选择:
0.普通攻击
1.虹吸斩/2.强力攻击
3.舍身一击/4.狂战士的怒吼
5.要害重击/6.最后赢家
            """
        )
        choice = str(input("你的选择:"))
        if choice == "0":
            self.Attack(who)
        elif choice == "1":
            if self.MAGIC > 0:
                self.Siphon(who)
        elif choice == "2":
            if self.MAGIC > 0:
                self.PlusPlus(who)
        elif choice == "3":
            self.LifeBlow(who)
        elif choice == "4":
            if self.MAGIC > 0:
                self.BerserkerRoar(who)
        elif choice == "5":
            if self.MAGIC > 0:
                self.HeavyBlow(who)
        elif choice == "6":
            if self.MAGIC > 0:
                self.EndWinner(who)
        else:
            print("选择不正确,重新选择")
            self.Choice(who)


class Mage(OriginMan):
    """
    魔攻高，魔法值高，技能可以多几个防御，另外靠魔攻吃饭，魔攻出场的次数高一点。
    """

    def __init__(self):
        super().__init__()
        self.NAME = "法师"
        self.HEALTHY += 500
        self.MAX_HEALTHY += 500
        self.MAX_ATTACK += 2
        self.MIN_ATTACK += 2
        self.MAX_MAGIC += 750
        self.MAGIC += 750
        self.MAGIC_ATTACK += 12
        self.SOUL_JOB = 0
        self.SHIELD = 0

    def MagicBurst(self, who):
        """
        魔法爆裂,造成魔攻*2+等级*10的伤害
        """
        attack = self.MAGIC_ATTACK * 2 + self.LEVEL * 10
        spend = self.LEVEL * 10
        self.MAGIC -= spend
        who.HEALTHY -= attack
        print(f"魔法-{spend}")
        print(f"{self.NAME}使用了魔能震爆对{who.NAME}造成了{attack}点伤害.")

    def Baptism(self):
        """
        洗礼，纯粹的回蓝技能...
        """
        magic = self.LEVEL * 10 + 10
        self.MAGIC += magic
        print(f"魔法圣光使得{self.NAME}的魔法恢复了{magic}点.")

    def HealthyMagic(self):
        """
        治疗术，纯粹的回血技能
        """
        blood = self.MAX_HEALTHY // 10
        spend = self.MAX_HEALTHY // 40
        self.MAGIC -= spend
        self.HEALTHY += blood
        print(f"魔法-{spend}")
        print(f"{self.NAME}消耗了{spend}点魔法恢复了{blood}点血.")

    def WaterFall(self, who):
        """
        瀑布流,造成伤害并加一个“灵魂印记”
        """
        attack = self.MAGIC_ATTACK + random.randint(self.MIN_ATTACK +
                                                    self.MAGIC_ATTACK,
                                                    self.MAX_ATTACK +
                                                    self.MAGIC_ATTACK) * 5
        spend = 120
        self.MAGIC -= spend
        who.HEALTHY -= attack
        self.SOUL_JOB += 1
        print(f"魔法-{spend}")
        print(f"{self.NAME}强大的魔法使得{who.NAME}失去了{attack}点血并标记了对方灵魂.")

    def SafeSpace(self):
        """
        守护立场,对自身施加一个巨大的魔法护盾并在护盾未消失之前免疫一切伤害.护盾血量为最大生命值
        """
        spend = self.MAX_HEALTHY // 10
        healthy = self.MAX_HEALTHY
        self.SHIELD += healthy
        self.MAGIC -= spend
        print(f"{self.NAME}使用了{spend}点魔法为自己创造了一个{healthy}点血的护盾!")

    def SoulTear(self, who):
        """
        @神技
        灵魂撕裂,伤害依据目前的灵魂标记数量而定(理论上无限高)
        """
        null = self.SOUL_JOB
        attack = random.randint(self.MIN_ATTACK + self.MAGIC_ATTACK,
                                self.MAX_ATTACK + self.MAGIC_ATTACK) + self.MAGIC_ATTACK * 2
        attack *= null + 3
        spend = 10
        self.MAGIC -= spend
        who.HEALTHY -= attack
        self.SOUL_JOB = 0
        print(f"魔法-{spend}")
        print(f"{self.NAME}使用灵魂印记对{who.NAME}造成了{attack}点伤害!")

    def show(self):
        print(
            f"""
{self.NAME}:
生命值:{self.HEALTHY}/{self.MAX_HEALTHY},攻击力:{self.MIN_ATTACK}~{self.MAX_ATTACK}
魔法值:{self.MAGIC}/{self.MAX_MAGIC},力量:{self.STRONG}
防御:{self.HIDE},等级:{self.LEVEL},经验{self.EXP}/{self.UP_EXP}
灵魂印记数:{self.SOUL_JOB},护盾血量:{self.SHIELD}
    """)

    def Choice(self, who):
        """
        选择如何攻击,这个判断有点骚.
        """
        print(
            """
你的选择:
0.普通攻击
1.魔能爆裂/2.洗礼
3.治疗术/4.瀑布流
5.守护立场/6.灵魂撕裂
            """
        )
        choice = str(input("你的选择:"))
        if choice == "0":
            self.Attack(who)
        elif choice == "1":
            if self.MAGIC > 0:
                self.MagicBurst(who)
        elif choice == "2":
            self.Baptism()
        elif choice == "3":
            if self.MAGIC > 0:
                self.HealthyMagic()
        elif choice == "4":
            if self.MAGIC > 0:
                self.WaterFall(who)
        elif choice == "5":
            if self.MAGIC > 0:
                self.SafeSpace()
        elif choice == "6":
            if self.MAGIC > 0:
                self.SoulTear(who)
        else:
            print("选择不正确,重新选择")
            self.Choice(who)

    def LevelUp(self):
        if self.EXP >= self.UP_EXP:
            print("你升级了!你的力量,生命值,灵敏度,魔法等级都提高了!")
            self.MAX_HEALTHY += self.LEVEL * 10 + self.STRONG * 5
            self.HEALTHY += self.MAX_HEALTHY // 10
            self.MIN_ATTACK += self.LEVEL
            self.MAX_ATTACK += self.LEVEL
            self.STRONG += self.LEVEL - 1
            self.MAX_MAGIC += 10
            self.MAGIC += self.MAX_MAGIC // 10
            self.MAGIC_ATTACK += self.LEVEL * 2
            self.EXP = 0
            self.LEVEL += 1
            self.UP_EXP += self.LEVEL * 1.5 // 2


class Ranger(OriginMan):
    """
    浪就对了，不要防御技能，攻击的技能狠狠堆起来，魔法和物理双攻，吸血技能至少2个。但生命往死里减。
    """

    def __init__(self):
        super().__init__()
        self.NAME = "游侠"
        self.HEALTHY += 200
        self.MAX_HEALTHY += 200
        self.MAX_MAGIC += 350
        self.MAGIC += 350
        self.MAGIC_ATTACK += random.randint(2, 16)
        self.MAX_ATTACK += 8
        self.MIN_ATTACK += 9
        self.SPEED += 5
        self.DRINK_FORGET_DRINK = 0

    def ShadowJump(self, who):
        """
        暗影之跃,攻击力取决于速度.
        """
        attack = random.randint(self.MIN_ATTACK, self.MAX_ATTACK) - who.HIDE
        attack *= self.SPEED - 4
        self.MAGIC -= self.SPEED * 5
        who.HEALTHY -= attack
        print(f"魔法-{self.SPEED * 5}")
        print(f"{self.NAME}对{who.NAME}造成了{attack}点伤害")

    def KillSwirl(self, who):
        """
        刀刃漩涡,攻击力和魔法夹杂着攻击且加一枚湮灭汲取勋章.
        """
        attack = random.randint(self.MIN_ATTACK, self.MAX_ATTACK)
        spend = attack // 10
        self.MAGIC -= spend
        self.DRINK_FORGET_DRINK += 1
        who.HEALTHY -= attack
        print(f"魔法-{spend}")
        print(f"{self.NAME}随意地攻击了{who.NAME}并造成了{attack}点伤害")

    def HealthyJump(self, who):
        """
        @神技
        生命跃动,属于暴击吸血流
        """
        attack = random.randint(self.MIN_ATTACK,
                                self.MAX_ATTACK) + self.MAGIC_ATTACK
        healthy = random.randint(1, 6) * attack
        spend = 50
        self.MAGIC -= spend
        who.HEALTHY -= attack
        self.HEALTHY += healthy
        print(f"{self.NAME}造成了{attack}点伤害,并恢复了{healthy}滴血")

    def NormalBlow(self, who):
        """
        @神技
        正常·普通·最简单的·攻击
        """
        attack = random.randint(self.MIN_ATTACK, self.MAX_ATTACK *
                                random.randint(1, 8))
        spend = attack // 10
        self.MAGIC -= spend
        who.HEALTHY -= attack
        print(f"魔法-{spend}")
        print(f"{self.NAME}不经意的对{who.NAME}造成了{attack}点伤害.")

    def OneEgg(self, who):
        """
        @神技
        秉承了随机的神奇理念,但是这个要扣血的.
        """
        healthy = self.MAX_HEALTHY // 10
        attack = random.randint(1, self.MAX_ATTACK * 10) * 2
        self.HEALTHY -= healthy
        who.HEALTHY -= attack
        print(f"生命-{healthy}")
        print(f"{self.NAME}孤注一掷地攻击了{who.NAME}并造成了{attack}点伤害!")

    def DrinkForget(self, who):
        """
        @神技
        湮灭汲取,吸取巨量的各种属性(看DRINK_FORGET_DRINK)
        """
        angry = self.DRINK_FORGET_DRINK
        self.DRINK_FORGET_DRINK = 0
        attack = random.randint(10, self.MAX_ATTACK) * angry
        healthy = attack // 10
        magic = attack // 20
        self.HEALTHY += healthy
        self.MAGIC += magic
        who.HEALTHY -= attack
        print(f"{self.NAME}对{who.NAME}造成了{attack}点伤害.")

    def show(self):
        print(
            f"""
{self.NAME}:
生命值:{self.HEALTHY}/{self.MAX_HEALTHY},攻击力:{self.MIN_ATTACK}~{self.MAX_ATTACK}
魔法值:{self.MAGIC}/{self.MAX_MAGIC},力量:{self.STRONG}
防御:{self.HIDE},等级:{self.LEVEL},经验{self.EXP}/{self.UP_EXP}
速度:{self.SPEED},湮灭印记:{self.DRINK_FORGET_DRINK}
        """)

    def Choice(self, who):
        print(
            """
你的选择:
0.普通攻击
1.暗影之跃/2.刀刃漩涡
3.生命跃动/4.正常攻击
5.孤注一掷/6.湮灭汲取
            """
        )
        choice = str(input("你的选择:"))
        if choice == "0":
            self.Attack(who)
        elif choice == "1":
            if self.MAGIC > 0:
                self.ShadowJump(who)
        elif choice == "2":
            self.KillSwirl(who)
        elif choice == "3":
            if self.MAGIC > 0:
                self.HealthyJump(who)
        elif choice == "4":
            if self.MAGIC > 0:
                self.NormalBlow(who)
        elif choice == "5":
            if self.MAGIC > 0:
                self.OneEgg(who)
        elif choice == "6":
            self.DrinkForget(who)
        else:
            print("选择不正确,重新选择")
            self.Choice(who)

    def LevelUp(self):
        if self.EXP >= self.UP_EXP:
            print("你升级了!你的力量,生命值,灵敏度,魔法等级都提高了!")
            self.MAX_HEALTHY += self.LEVEL * 10 + self.SPEED * 10
            self.HEALTHY += self.MAX_HEALTHY // 10
            self.MIN_ATTACK += self.LEVEL + 1
            self.MAX_ATTACK += self.LEVEL + 1
            self.STRONG += self.LEVEL // 20
            self.MAX_MAGIC += 10
            self.MAGIC += self.MAX_MAGIC // 10
            self.MAGIC_ATTACK += self.LEVEL
            self.EXP -= self.UP_EXP
            self.LEVEL += 1
            self.UP_EXP += self.LEVEL * 1.7 // 2


class Robot(OriginMan):
    """
    皮糙肉厚(抗伤害)，暴击倍数增加，每回合定期回血，攻击上面相对来说较弱，魔攻较弱，技能类似防御堆砌。
    """

    def __init__(self):
        super().__init__()
        self.NAME = "机器人"
        self.MAX_HEALTHY *= 2
        self.HEALTHY *= 2
        self.MAX_HEALTHY += 500
        self.HEALTHY += 500
        self.MIN_ATTACK += 5
        self.MAX_ATTACK += 5
        self.MAX_MAGIC += 450
        self.MAGIC += 450
        self.GEARS = 0
        self.SHIELD = 0

    def Rolling(self, who):
        """
        碾压,造成攻击力*3的伤害,制造一个齿轮
        """
        attack = random.randint(self.MIN_ATTACK * 3, self.MAX_ATTACK * 3) - who.HIDE
        self.GEARS += 1
        who.HEALTHY -= attack
        spend = self.LEVEL * 20
        self.MAGIC -= spend
        print(f"{self.NAME}造成了{attack}点伤害.")

    def MachineHeart(self, who):
        """
        机器之心,回复大量血量.
        """
        spend = self.MAX_HEALTHY // 20
        self.MAGIC -= spend
        self.HEALTHY += self.MAX_HEALTHY // 10
        who.HEALTHY -= self.MAX_HEALTHY // 20
        print(f"{self.NAME}回复了血量并电流过载对{who.NAME}造成了"
              f"{self.MAX_HEALTHY // 20}点伤害")

    def KILL(self, who):
        """
        密度砍杀,造成当前血量+攻击力的伤害.(扣血)
        """
        attack = random.randint(self.MIN_ATTACK,
                                self.MAX_ATTACK) + self.HEALTHY // 10
        spend = self.MAX_HEALTHY // 10
        self.HEALTHY -= spend
        who.HEALTHY -= attack
        print(f"{self.NAME}对{who.NAME}造成了{attack}点伤害")

    def IronSoul(self):
        """
        钢铁灵魂,制造一个当前最大生命值的护盾(消耗hin大)并制造一个齿轮
        """
        self.GEARS += 1
        self.SHIELD += self.MAX_HEALTHY
        self.MAGIC -= self.MAX_HEALTHY // 5
        print(f"{self.NAME}消耗了{self.MAX_HEALTHY // 5}魔法并制造了一个护盾.")

    def BrokenBlow(self, who):
        """
        破碎攻击,将自己的所有护盾转换为伤害并攻击(消耗1个齿轮)
        """
        self.GEARS -= 1
        attack = self.SHIELD
        self.SHIELD = 0
        who.HEALTHY -= attack
        print(f"{self.NAME}将自己的护盾全部抛了出去对{who.NAME}造成了{attack}点伤害.")

    def AbsoluteDefense(self):
        """
        绝对防御,补满血量的50%并消耗3个齿轮并使得当前护盾生命值*2.(减蓝)
        """
        self.GEARS -= 3
        self.SHIELD *= 2
        self.HEALTHY += self.MAX_HEALTHY // 2
        self.MAGIC -= self.MAX_HEALTHY // 5
        print(f"{self.NAME}强大的意志力使得{self.NAME}的身体变得比钢铁更坚硬.")

    def show(self):
        print(
            f"""
{self.NAME}:
生命值:{self.HEALTHY}/{self.MAX_HEALTHY},攻击力:{self.MIN_ATTACK}~{self.MAX_ATTACK}
魔法值:{self.MAGIC}/{self.MAX_MAGIC},力量:{self.STRONG}
防御:{self.HIDE},等级:{self.LEVEL},经验{self.EXP}/{self.UP_EXP}
齿轮:{self.GEARS},护盾:{self.SHIELD}
        """)

    def Choice(self, who):
        """
        选择如何攻击,这个判断有点骚.
        """
        print(
            """
你的选择:
0.普通攻击
1.碾压/2.机器之心
3.密度砍杀/4.钢铁之灵
5.破碎攻击/6.绝对防御
            """
        )
        choice = str(input("你的选择:"))
        if choice == "0":
            self.Attack(who)
            self.MAGIC += self.MAX_MAGIC // 50
        elif choice == "1":
            if self.MAGIC > 0:
                self.Rolling(who)
                self.MAGIC += self.MAX_MAGIC // 50
        elif choice == "2":
            if self.MAGIC > 0:
                self.MachineHeart(who)
                self.MAGIC += self.MAX_MAGIC // 50
        elif choice == "3":
            if self.MAGIC > 0:
                self.KILL(who)
                self.MAGIC += self.MAX_MAGIC // 50
        elif choice == "4":
            if self.MAGIC > 0:
                self.IronSoul()
                self.MAGIC += self.MAX_MAGIC // 50
        elif choice == "5":
            self.BrokenBlow(who)
            self.MAGIC += self.MAX_MAGIC // 50
        elif choice == "6":
            if self.MAGIC > 0:
                self.AbsoluteDefense()
                self.MAGIC += self.MAX_MAGIC // 50
        else:
            print("选择不正确,重新选择")
            self.Choice(who)

    def LevelUp(self):
        if self.EXP >= self.UP_EXP:
            print("你升级了!你的力量,生命值,灵敏度,魔法等级都提高了!")
            self.MAX_HEALTHY += self.LEVEL * 10 + self.SPEED * 5
            self.HEALTHY += self.MAX_HEALTHY // 10
            self.MIN_ATTACK += self.LEVEL + 1
            self.MAX_ATTACK += self.LEVEL + 1
            self.STRONG += self.LEVEL - 1
            self.MAX_MAGIC += 10
            self.MAGIC += self.MAX_MAGIC // 10
            self.MAGIC_ATTACK += self.LEVEL
            self.EXP = 0
            self.LEVEL += 1
            self.UP_EXP += self.LEVEL * 1.5 // 2


Warrior = Warrior()
Mage = Mage()
Ranger = Ranger()
Robot = Robot()


def NormalDungeon(chapter):
    global FLOOR, SEARCH_TURNS, MAX_SEARCH_TURNS
    print(f"第{FLOOR}层")
    print(
        f"""
本层你已经探索了{SEARCH_TURNS}次,最高探索{MAX_SEARCH_TURNS}次
        """)
    print("你可以选择:\n1.探索\n2.查看状态\n3.下楼\n'rename':换一个名字")
    choice = str(input("选择你的命运:"))
    if SEARCH_TURNS < MAX_SEARCH_TURNS:
        if choice == "1":
            a = next(Fate())
            if a == "获得治疗":
                print("你获得了治愈")
                chapter.HEALTHY += chapter.MAX_HEALTHY // 10
                SEARCH_TURNS += 1
            if a == "踩中陷阱":
                print("你踩到了陷阱")
                chapter.HEALTHY -= chapter.MAX_HEALTHY // 20
                SEARCH_TURNS += 1
            if a == "怪物来袭":
                a = Choice()
                a.__init__()
                print(f"你遇上了{a.NAME}")
                while a.HEALTHY > 0 and chapter.HEALTHY > 0:
                    a.show()
                    chapter.show()
                    chapter.Choice(a)
                    time.sleep(0.1)
                    a.show()
                    chapter.LevelUp()
                    if a.HEALTHY <= 0:
                        print(f"你打败了{a.NAME}!")
                        a.restart(chapter)
                        SEARCH_TURNS += 1
                        break
                    a.Attack(chapter)
                    time.sleep(0.2)
                    chapter.show()
                    if chapter.HEALTHY <= 0:
                        print("你死了...")
                        sys.exit()
    else:
        print("这一层已经被你清空了...")

    if choice == "2":
        chapter.show()

    if choice == "3":
        print("你更加深入地牢,地牢也更加危险了...")
        SEARCH_TURNS = 0
        FLOOR += 1

    if choice == "666":
        chapter.MAGIC += 5000000000000

    if choice == "rename":
        you = str(input("Name:"))
        chapter.NAME = you


def BossDungeon(chapter):
    global FLOOR
    master = Choose()
    chapter.MAX_ATTACK += chapter.MIN_ATTACK * 10
    chapter.MIN_ATTACK += 100
    chapter.HEALTHY += 10000
    master.__init__()
    print("这个房间的气息变得十分凝重...")
    time.sleep(0.4)
    print("一个庞大的身影在房间尽头伸展着...")
    time.sleep(0.5)
    print(f"{FLOOR}层BOSS:{master.NAME}!")
    print(master)
    while chapter.HEALTHY > 0 and master.HEALTHY > 0:
        chapter.Choice(master)
        time.sleep(0.1)
        master.show()
        if master.HEALTHY <= 0:
            if master.NAME != "陨落的半神":
                print(f"你打败了{master.NAME}!")
                master.restart(chapter)
                FLOOR += 1
                break
            if master.NAME == "陨落的半神":
                if not master.TWICE:
                    master.ATTACK_TURNS = master.BOSS_ATTACK_TURNS + 1
                if master.TWICE:
                    print(f"你打败了{master.NAME}!")
                    master.restart(chapter)
                    FLOOR += 1
                    break
        master.Attack(chapter)
        time.sleep(0.2)
        chapter.show()
        if chapter.HEALTHY <= 0:
            print("你死了...")
            sys.exit()


def Fate():
    while True:
        random.shuffle(FATE_LIST)
        xx = random.choice(FATE_LIST)
        yield xx


oop = str(input("""选择角色:
1.战士:血越少攻击越高,卖血攻击吊炸天
2.法师:回血回蓝,超高魔法攻击
3.游侠:快乐,快乐和快乐,吸血伤害很高
4.机器人:血厚的一批
选择?>"""))
play = object
if oop == "1":
    play = Warrior
if oop == "2":
    play = Mage
if oop == "3":
    play = Ranger
if oop == "4":
    play = Robot


def main():
    while True:
        if (FLOOR % 20) != 0:
            NormalDungeon(play)
        else:
            BossDungeon(play)


if __name__ == '__main__':
    main()
