import argparse
import math
parser = argparse.ArgumentParser()
parser.add_argument("-t", "--type", type=str, help="Type de Crédit")
parser.add_argument("-p", "--principal", type=float, help="The loan principal")
parser.add_argument("-per", "--periods", type=float, help="Number of months")
parser.add_argument("-i", "--interest", type=float, help="annual interest")
parser.add_argument("-pay", "--payment", type=float, help="annuity monthly payment")
args = parser.parse_args()
i = args.interest
n = args.periods
p = args.principal
a = args.payment
if i is not None and i > 0:
    i /= 1200
    if args.type == 'annuity':
        # calculs étape précédente
        if p is None:
            # calcul du principal
            if (n and a) and (n > 0 and a > 0):
                p = a / ((i * math.pow(1 + i, n)) / (math.pow(1 + i, n) - 1))
                p = math.ceil(p)
                print("Your loan principal = {}!".format(p))
                ove = math.ceil((n * a) - p)
                print("OverPayment = {}".format(ove))
            else:
                print("Incorrect parameters")
        elif a is None:
            # calcul de l'annuity
            if (p and n) and (n > 0 and p > 0):
                a = p * (i * math.pow(1 + i, n)) / (math.pow(1 + i, n) - 1)
                a = math.ceil(a)
                print("Your annuity payment = {}!".format(a))
                ove = math.ceil((n*a)-p)
                print("OverPayment = {}".format(ove))
            else:
                print("Incorrect parameters")
        elif n is None:
            # calcul du nb de mois de remboursement
            if (a and p) and (p > 0 and a > 0):
                n = math.ceil(math.log(a / (a - i * p), 1 + i))
                year = n // 12
                mois = n % 12
                if year == 0:
                    if mois == 1:
                        print("It will take 1 month to repay this loan!")
                    else:
                        print("It will take {} months to repay this loan!".format(mois))
                elif year == 1:
                    if mois == 0:
                        print("It will take 1 year to repay this loan!")
                    elif mois == 1:
                        print("It will take 1 year and 1 month to repay this loan!")
                    else:
                        print("It will take 1 year and {} months to repay this loan!".format(mois))
                else:
                    if mois == 0:
                        print("It will take {} years to repay this loan!".format(year))
                    elif mois == 1:
                        print("It will take {} years and 1 month to repay this loan!".format(year))
                    else:
                        print("It will take {} years and {} months to repay this loan!".format(year, mois))
                ove = math.ceil((n * a) - p)
                print("OverPayment = {}".format(ove))
            else:
                print("Incorrect parameters")
        else:
            print("Incorrect parameters")
    elif args.type == 'diff':
        if a is None:  # paiement fixe mensuel
            if (p is not None and p > 0) and (n is not None and n > 0):
                # credit differentiel
                ove = - p
                for m in range(1, int(n) + 1):
                    D = (p / n) + i * (p - (p * (m - 1) / n))
                    D = math.ceil(D)
                    print('Month {0}: payment is {1}'.format(m, D))
                    ove += D
                ove = math.ceil(ove)
                print("\nOverPayment = {}".format(ove))
            else:
                print('Incorrect parameters')
        else:
            print('Incorrect parameters')
    else:
        print('Incorrect parameters')
else:
    print('Incorrect parameters')
