import unittest

def mpf(x):
    tax = 0
    perMon = round(x/12,1) # year total income / 12 month = income per month
    
    if perMon < 7100: # less then $7100 no need to pay MPF
        ftax = tax
        return ftax
    
    elif 7100 < perMon < 30000: # less then $30000 but more then $7100
        tax = perMon*0.05       # mpf = 5% per month
        ftax = round(tax*12,1)
        return ftax
        
    elif perMon > 30000 : # more then $30000
        tax = 1500        # mpf = $1500 per month
        ftax = round(tax*12,1)
        return ftax

    else:
        print('...Error...')
        return ftax

def sumTax(fin,flag):
    finSum = 0
    error = 0
    if flag == 1:
        
        fin = fin - 132000

    elif flag == 2:
        
        fin = fin - 264000

    else:
        print('...Flag Error...')
        error = 1
        
    if error == 1:
        return 0
    
    else:
        if fin > 50000:
            finSum = finSum + 1000
            fin = fin - 50000

            if fin > 50000:
                finSum = finSum + 3000
                fin = fin - 50000

                if fin > 50000:
                    finSum = finSum + 5000
                    fin = fin - 50000

                    if fin > 50000:
                        finSum = finSum + 7000
                        fin = fin - 50000

                        finSum = finSum + round(fin*0.17,1)
                            
                    else:
                        finSum = finSum + round(fin*0.14,1)
                        
                else:
                    finSum = finSum + round(fin*0.10,1)
                    
            else:
                finSum = finSum + round(fin*0.06,1)
                
        else:
            finSum = finSum + round(fin*0.02,1)

        if finSum < 0:
            finSum = 0

        return finSum

class TestStringMethods(unittest.TestCase):

    def test_sin_lower(self):
        self.assertEqual(sumTax(85188 - 0,1),0)
    def test_sin_mid(self):
        self.assertEqual(sumTax(216000 - 10800,1), 2392)
    def test_sin_upperclass(self):
        self.assertEqual(sumTax(360012- 18000,1), 17702)
    def test_marr_lower(self):
        self.assertEqual(sumTax(116376 - 0,2), 0)
    def test_marr_mid(self):
        self.assertEqual(sumTax(432000 - 36000,2),7200)
    def test_marr_upperclass(self):
        self.assertEqual(sumTax(720024 - 36000,2),53404.1)

if __name__ == '__main__':
    unittest.main()