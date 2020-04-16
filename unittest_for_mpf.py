import unittest

def mpf(x):
    tax = 0
    perMon = round(x/12,1)
    if perMon < 7100:
        ftax = tax
        return ftax

    elif 7100 < perMon < 30000:
        tax = perMon*0.05
        ftax = round(tax*12,1)
        return ftax
        
    elif perMon > 30000 :
        tax = 1500
        ftax = round(tax*12,1)
        return ftax

    else:
        print('...Error...')
        return ftax

class TestStringMethods(unittest.TestCase):

    def test_lower(self):
        self.assertEqual(mpf(85188),0)
    def test_mid(self):
        self.assertEqual(mpf(216000),10800)
    def test_upperclass(self):
        self.assertEqual(mpf(360012),18000)






if __name__ == '__main__':
    unittest.main()