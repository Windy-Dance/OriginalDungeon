#             Coding : Utf-8              #
#         Created By : Parallel           #
#         Created On : 2020/7/24 20:00    #
#           Language : Python             #
#       Last Updated : 2020/7/24 20:00    #

# ____            _              ____
# | __ ) _ __ ___ | | _____ _ __ |  _ \ _   _ _ __   __ _  ___  ___  _ __
# |  _ \| '__/ _ \| |/ / _ \ '_ \| | | | | | | '_ \ / _` |/ _ \/ _ \| '_ \
# | |_) | | | (_) |   <  __/ | | | |_| | |_| | | | | (_| |  __/ (_) | | | |
# |____/|_|  \___/|_|\_\___|_| |_|____/ \__,_|_| |_|\__, |\___|\___/|_| |_|
#                                                   |___/

__name__ = 'wears'


class HELMET(object):
    """
    The Helmets' Father object
    """
    __slots__ = ["NAME", "DEFENSE", "DESCRIPTION"]

    def __init__(self, name: str, defense: int, description: str):
        self.NAME: str = name
        self.DEFENSE: int = defense
        self.DESCRIPTION: str = description


class ARMOR(object):
    """
    The Armors' Father object
    """
    __slots__ = ["NAME", "DEFENSE", "DESCRIPTION", "HEALTHY"]

    def __init__(self, name: str, defense: int, description: str, healthy: int = 0):
        self.NAME: str = name
        self.DEFENSE: int = defense
        self.DESCRIPTION: str = description
        self.HEALTHY: int = healthy


class PANTS(object):
    """
    The Pants' Father object
    """
    __slots__ = ["NAME", "DEFENSE", "DESCRIPTION"]

    def __init__(self, name: str, defense: int, description: str):
        self.NAME: str = name
        self.DEFENSE: int = defense
        self.DESCRIPTION: str = description


class SHOES(object):
    """
    The Shoes' Father object
    """
    __slots__ = ["NAME", "DEFENSE", "DESCRIPTION"]

    def __init__(self, name: str, defense: int, description: str):
        self.NAME: str = name
        self.DEFENSE: int = defense
        self.DESCRIPTION: str = description


class ATTACKER(object):
    """
    The Attackers' Father object
    """
    __slots__ = ["NAME", "DEFENSE", "MAX_ATTACK", "MIN_ATTACK", "DESCRIPTION"]

    def __init__(self, name: str, max_attack: int, min_attack: int, description: str):
        self.NAME: str = name
        self.MAX_ATTACK: int = max_attack
        self.MIN_ATTACK: int = min_attack
        self.DESCRIPTION: str = description


# ============ Helmets ============ #
GrassHelmet = HELMET(name = "草质头盔", defense = 1,
                     description = "一个绿油油的头盔,闻上去是一股青草的味道...")
LeatherHelmet = HELMET(name = "皮革头盔", defense = 2,
                       description = "稍微正常一点的皮革头盔.")
WordHelmet = HELMET(name = "木制头盔", defense = 3,
                    description = "梦开始的头盔,采用原木制作!")
BetterWordHelmet = HELMET(name = "精致木头盔", defense = 5,
                          description = "更精良的木制头盔")
IronHelmet = HELMET(name = "铁盔", defense = 6,
                    description = "这才是真正的开始...")
IronWordHelmet = HELMET(name = "铁箍木盔", defense = 5,
                        description = "用铁箍把木头牢牢地捆在一起.")
JackalHelmet = HELMET(name = "豺狼人头盔", defense = 7,
                      description = "这些豺狼人的装备可真是精良啊...")
NinjaHelmet = HELMET(name = "忍者头盔", defense = 3,
                     description = "忍者会怎么做?")
RealWordHelmet = HELMET(name = "真正的木头盔", defense = 12,
                        description = "是时候让你瞧瞧木头的厉害了...")
BrokenHelmet = HELMET(name = "破碎头盔", defense = 12,
                      description = "会破碎的可就不是头盔了...")
BetterIronHelmet = HELMET(name = "精良的铁头盔", defense = 15,
                          description = "来自铁匠一锤一锤的防御!")
DarkIronHelmet = HELMET(name = "黑铁头盔", defense = 25,
                        description = "见识一下什么叫做铁!")
SkullHelmet = HELMET(name = "骷髅盔", defense = 15,
                     description = "骷髅头盔看上去居然很拉风...")
GoldenHelmet = HELMET(name = "金闪闪的头盔", defense = 12,
                      description = "看上去金光灿烂,但实际上却抵挡不了多少伤害.")
KingsNewHelmet = HELMET(name = "国王的新头盔", defense = 18,
                        description = "虚无幻境,生死可弃! --老国王")
KingdomHelmet = HELMET(name = "皇家头盔", defense = 24,
                       description = "带上这个头盔,就得做好赴死的准备 --皇家上尉")
ShadowHelmet = HELMET(name = "影盔", defense = 28,
                      description = "半神的杰作")
TenguHelmet = HELMET(name = "天狗面具", defense = 46,
                     description = "天狗之魂附着在这上面")
FortressHelmet = HELMET(name = "堡垒头盔", defense = 63,
                        description = "看上去蛮吓人的")
IronSoulHelmet = HELMET(name = "钢铁之颅", defense = 104,
                        description = "戴上它,仿佛可以抵挡一切")
KrakenHelmet = HELMET(name = "克拉肯头盔", defense = 65,
                      description = "大海的力量源源不断地朝你涌来...")

# ============ Armors ============ #
GrassArmor = ARMOR(name = "草甲", defense = 7,
                   description = "是大自然的味道", healthy = 10)
LeatherArmor = ARMOR(name = "皮甲", defense = 8,
                     description = "祖传的皮质护甲", healthy = 20)
WordArmor = ARMOR(name = "木甲", defense = 10,
                  description = "木头装甲,心理上给了你一点安慰", healthy = 50)
BetterWordArmor = ARMOR(name = "精良木装甲", defense = 12,
                        description = "更好的木装甲,更好的平衡")
IronArmor = ARMOR(name = "铁甲", defense = 15,
                  description = "战士穿的东西", healthy = 100)
IronWordArmor = ARMOR(name = "匠人背心", defense = 14,
                      description = "...")
JackalArmor = ARMOR(name = "豺狼人护甲", defense = 18,
                    description = "豺狼人的气息!", healthy = 150)
NinjaArmor = ARMOR(name = "忍者长袍", defense = 13,
                   description = "忍者为什么会穿长袍?", healthy = 350)
RealWordArmor = ARMOR(name = "真正的木装甲", defense = 21,
                      description = "树木的尊严", healthy = 230)
BrokenArmor = ARMOR(name = "破碎战甲", defense = 23,
                    description = "会破碎的可就不是战甲了...")
BetterIronArmor = ARMOR(name = "精良铁战甲", defense = 23,
                        description = "更加优秀战甲")
DarkIronArmor = ARMOR(name = "黑铁战甲", defense = 25,
                      description = "瞧不起黑铁?")
SkullArmor = ARMOR(name = "骷髅护甲", defense = 12,
                   description = "很轻便,但是却含有强大的生命力!", healthy = 360)
GoldenArmor = ARMOR(name = "花里胡哨的护甲", defense = 15,
                    description = "穿上去很显眼...")
KingsNewArmor = ARMOR(name = "国王的新护甲", defense = 25,
                      description = "在黑暗中闪闪发光", healthy = 250)
KingdomArmor = ARMOR(name = "皇家护甲", defense = 43,
                     description = "这是至高无上的荣耀!", healthy = 300)
ShadowArmor = ARMOR(name = "影甲", defense = 52,
                    description = "竟然在不断地吞噬着阳光!", healthy = -500)
TenguArmor = ARMOR(name = "天狗风衣", defense = 54,
                   description = "天狗的气息混杂在这件衣服里", healthy = 350)
FortressArmor = ARMOR(name = "堡垒护甲", defense = 68,
                      description = "坚固到感受不到普通的拳打脚踢", healthy = 250)
IronSoulArmor = ARMOR(name = "钢铁之心", defense = 126,
                      description = "钢铁之魂被禁锢其中", healthy = 500)
KrakenArmor = ARMOR(name = "克拉肯之躯", defense = 75,
                    description = "克拉肯皮还挺厚的...", healthy = 450)

# ============ Pants ============ #


# ============ Shoes ============ #


# ========== Attackers ========== #
