def gcd(a,b):
        x=a
        y=b
        r=x%y
        blr=0 # Before Last Remainder
        l=[]
        print("Step 1:")
        while r != 0:
            blr=r
            r=x%y
            q=x//y
            print("{0} = {1} x {2} + {3}".format(x,q,y,r))
            x=y
            y=r
        print("GCD is {0}".format(blr))
        print("=========================")
        print("=== working backwards ===")
        for i in range :
            blr =






gcd(252,198)
