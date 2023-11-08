def gcd(a,b):
        quotients =[]
        dividers =[]
        remainders =[]
        y=[]
        print("Step 1:  Euclidean algorithm to find gcd({0},{1}):".format(a, b))
        while b != 0:
            quotients.append(a//b)
            dividers.append(a)
            remainders.append(a%b)
            y.append(b)
            temp  = a
            a=b
            b=temp%a

        print("=========================")
        for i in range (len(dividers)) :
            print("{0} = {1} x {2} + {3}".format(dividers[i],quotients[i] , y[i], remainders[i]))

        print("GCD is {0}".format(remainders[-2]))

        # print("=== working backwards ===")
        # for j in range (len(dividers)):



gcd(252,198)
