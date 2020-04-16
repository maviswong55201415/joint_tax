# Pair Programming : Tax Calculator
# Code by Wong Yat Cheong Jacky, 18/3/2020
#v1.1 update more try and except cases, 8/4/2020


def main(): # program progess main part
    while True:
        start()
        x = input()
        
        if x=='1' :   # one
            basic()
            main()
            
        elif x=='2' : # two
            married()
            main()

        elif x=='e' :
            print('GoodBye')
            break
            
        else:
            print('...wrong input...')
            main()

def start(): # starting part
    print('...Welcome to tax calculator...')
    print('- Press 1 for one person ')
    print('- Press 2 for two person ')


def basic(): # progress on basic tax cal method (single person)
    print('Please input your income Per Year :')

    try:
        x = input()
        
        y = float(x) # Test input is number or float
        if y <= 0:   # Test input is not 0 or negative number
            print("...wrong input...<press 'e' to Exit> (e1)")
            
        else:
            ss = mpf(float(x)) # cal MPF
            print('* MPF  is $'+str(ss))
            print()
            sfs = sumTax(float(x)-ss,1) # cal total all tax
            print('**** Under Separate Taxation, you need to pay for $'+str(sfs))
            print('\n')
            
    except Exception as e:
        print("...wrong input...<press 'e' to Exit>",e)
        
        
def married(): # progress on couple tax cal method (a couple)
    
    # Test input is number or float
    print('Please input your Husband income Per Year :')
    x = input()
    
    print('Please input your Wife income Per Year :')
    y = input()

    yy=float(x)
    xx=float(y)

    if yy <= 0 or xx <= 0: # Test input is not 0 or negative number
        print("...wrong input...<press 'e' to Exit> (e1)")
        
    else:
        try:
            # progress on Joint method on both hus and wife income
            sumP = float(x)+float(y) # their total income
            hh = mpf(float(x))
            ww = mpf(float(y))
            print('* MPF for Husband is $'+str(hh)+' , wife is $'+str(ww))
            print()
            sumP = sumP - hh - ww  # their total income - their total mpf
            joint = sumTax(sumP,2) # cal total all tax
            print('**** Under Joint Assessment you may need to pay for $'+str(joint))
            print()

            # progress on Single method on both hus and wife income
            hs = sumTax(float(x)-hh,1) # already cal the mpf, so need to cal again. X = mpf
            ws = sumTax(float(y)-ww,1)
            print('** Under Separate Taxation, Husband need to pay for $'+str(hs))
            print('** Under Separate Taxation, Wife need to pay for $'+str(ws))
            print('**** Total need to pay for $'+str(hs+ws))
            print()

            if (hs+ws) > joint: # comparing
                print('   *** Use Joint Assessment may pay less $'+str((hs+ws)-joint))
            else:
                print('   *** Use Separate Taxation may pay less $'+str(joint-(hs+ws)))

            print('\n')
            
        except Exception as e:
            print("...wrong input...<press 'e' to Exit>",e)
    
# cal on mpf
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

# cal on total all tax
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

#run the program
main()
