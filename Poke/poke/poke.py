import random


class Card(object):
    """一张牌"""

    def __init__(self, suite, face):
        self._suite = suite
        self._face = face

    @property
    def face(self):
        return self._face

    @property
    def suite(self):
        return self._suite

    def __str__(self):
        if self._face == 14:
            face_str = 'A'
        elif self._face == 10:
            face_str = 'T'
        elif self._face == 11:
            face_str = 'J'
        elif self._face == 12:
            face_str = 'Q'
        elif self._face == 13:
            face_str = 'K'
        else:
            face_str = str(self._face)
        return '%c%c' % (face_str, self._suite)

    def __repr__(self):
        return self.__str__()


class Poker(object):
    """一副牌"""

    def __init__(self):
        self._cards = [Card(suite, face)
                       for suite in 'DSHC'
                       for face in range(2, 15)]
        self._current = 0

    @property
    def cards(self):
        return self._cards

    def shuffle(self):
        """洗牌(随机乱序)"""
        self._current = 0
        random.shuffle(self._cards)

    @property
    def next(self):
        """发牌"""
        card = str(self._cards[self._current])
        self._current += 1
        return card

    @property
    def has_next(self):
        """还有没有牌"""
        return self._current < len(self._cards)


def suff(ini):
    # 玩家整理手牌
    cmp = ''.join(ini)
    cmp1 = []
    cmp2 = []
    dic = {}
    for i in range(10):
        if i % 2 == 0:
            if cmp[i] == 'T':
                cmp1.append(10)
            elif cmp[i] == 'J':
                cmp1.append(11)
            elif cmp[i] == 'Q':
                cmp1.append(12)
            elif cmp[i] == 'K':
                cmp1.append(13)
            elif cmp[i] == 'A':
                cmp1.append(14)
            else:
                cmp1.append(int(cmp[i]))
        else:
            cmp2.append(cmp[i])
    for i in cmp1:
        dic[i] = cmp1.count(i)
    cmp1.sort(key=lambda x: (dic[x], x), reverse=True)
    return (cmp1, cmp2)


def judge(cmp1, cmp2):
    # 牌型判定
    p = 1
    q = 1
    count = []
    for i in range(4):
        if cmp2[i] == cmp2[i + 1]:
            q *= 1
        else:
            q *= 0
    for i in range(4):
        p *= cmp1[i] - cmp1[i + 1]
        count.append(cmp1.count(cmp1[i]))

    if p == 1 and q == 1:
        return 1
    elif q == 1:
        return 4
    elif p == 1:
        return 5
    elif p == 0:
        if 4 in count:
            return 2
        elif 3 in count:
            if 2 in count:
                return 3
            else:
                return 6
        elif 2 in count:
            if count.count(2) > 2:
                return 7
            else:
                return 8
    else:
        return 9


def compara(white, black):
    # 牌型大小比较
    white1, white2 = suff(white)
    black1, black2 = suff(black)
    whitep = judge(white1, white2)
    blackp = judge(black1, black2)

    if whitep < blackp:
        return 'w'
    elif blackp < whitep:
        return 'b'
    else:
        for i in range(5):
            if white1[i] > black1[i]:
                return 'w'
            elif black1[i] > white1[i]:
                return 'b'
        return 't'


def main():
    p = Poker()
    p.shuffle()
    white = []
    black = []
    for _ in range(5):
        white.append(p.next)
        black.append(p.next)
    print(white)
    print(black)
    print(compara(white, black))


if __name__ == '__main__':
    main()
