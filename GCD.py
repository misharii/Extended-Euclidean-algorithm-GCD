def gcd(a,b):
        # Initialize lists to hold the sequence of divisions
        quotients =[]
        dividers =[]
        remainders =[]
        y=[]
        print("Step 1:  Euclidean algorithm to find gcd({0},{1}):".format(a, b))
        
        while b != 0:                  # Continue finding remainders until we find 0
            quotients.append(a//b)     # Append quotient list with (a divided by b)
            dividers.append(a)         # Append difiders list with a
            remainders.append(a%b)     # Append remainders list with a,b remainder (a%b)
            y.append(b)                # Append y list with b
            temp = a                   # Temporary storage of current a
            a = b                      # Set a to the current b
            b = temp % a               # Calculate new b as remainder 

        print("=========================")
        
         # Print the results of each division step
        for i in range (len(dividers)) :
            print("{0} = {1} x {2} + {3}".format(dividers[i],quotients[i] , y[i], remainders[i]))
                
        # The second to last remainder before the zero remainder is the GCD
        print("GCD is {0}".format(remainders[-2]))

        # print("=== working backwards ===")
        # for j in range (len(dividers)):



gcd(252,198)
