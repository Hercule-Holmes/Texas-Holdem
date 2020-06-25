from poke import poke
import unittest

class test_Poke(unittest.TestCase):
    def test_Getcard(self):
        poke.main()

    def test_isSflush(self):
        cmp1,cmp2 = poke.suff(['2D','3D','4D','5D','6D'])
        result = poke.judge(cmp1,cmp2)
        self.assertEqual(result,1)

    def test_isFour(self):
        cmp1, cmp2 = poke.suff(['TD','TH','TD','TD','JD'])
        result = poke.judge(cmp1, cmp2)
        self.assertEqual(result,2)

    def test_isFullh(self):
        cmp1, cmp2 = poke.suff(['TD','TH','TD','JD','JD'])
        result = poke.judge(cmp1, cmp2)
        self.assertEqual(result,3)

    def test_isFlush(self):
        cmp1, cmp2 = poke.suff(['3D','5D','9D','1D','JD'])
        result = poke.judge(cmp1, cmp2)
        self.assertEqual(result,4)

    def test_isStrai(self):
        cmp1, cmp2 = poke.suff(['3D','4D','5H','6D','7D'])
        result = poke.judge(cmp1, cmp2)
        self.assertEqual(result,5)

    def test_isThree(self):
        cmp1, cmp2 = poke.suff(['3D','3D','3H','6D','7D'])
        result = poke.judge(cmp1, cmp2)
        self.assertEqual(result,6)

    def test_isTwo(self):
        cmp1, cmp2 = poke.suff(['3D','3D','6H','6D','7D'])
        result = poke.judge(cmp1, cmp2)
        self.assertEqual(result,7)

    def test_isOne(self):
        cmp1, cmp2 = poke.suff(['3D','3D','8H','6D','7D'])
        result = poke.judge(cmp1, cmp2)
        self.assertEqual(result,8)

    def test_isHigh(self):
        cmp1, cmp2 = poke.suff(['TD','3D','8H','6D','7D'])
        result = poke.judge(cmp1, cmp2)
        self.assertEqual(result,9)

    def test_winner1(self):
        result = poke.compara(['3D','3D','8H','6D','7D'],['TD','3D','8H','6D','7D'])
        self.assertEqual(result,'w')

    def test_winner2(self):
        result = poke.compara(['3D', '3D', '8H', '6D', '7D'], ['3D', '3D', '8H', '6D', '7D'])
        self.assertEqual(result, 't')

    def test_winner3(self):
        result = poke.compara(['2H', '3D', '5S', '9C', 'KD'], ['2D', '3H', '5C', '9S', 'KH'])
        self.assertEqual(result, 't')

if __name__ == '__main__':
    unittest.main()