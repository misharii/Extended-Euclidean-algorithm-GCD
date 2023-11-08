# Extended-Euclidean-algorithm-GCD
The aim of this project is to implement the Extended Euclidean algorithm,
which is an extension to the Euclidean algorithm, that computes in addition to the greatest common divisor gcd(a,b) of integers a and b, 
also the coefficients (s and t) of a and b, such that:

**gcd(𝑎, 𝑏) = 𝑠𝑎 + 𝑡𝑏**, 

gcd(a,b) can be expressed as a Liner Combinaiton with integer coefficients of a and b. For example:

gcd(6, 14) = 2, and 2 = **(−2)** ⋅ 6 + **(1)** ⋅ 14

=============================================================

Here's a explanation of what the code does:

1.	The function gcd takes two integer parameters a and b.
2.	It initializes four lists: quotients, dividers, remainders, and y.
3.	It then prints the beginning of the process, which is to find the GCD of a and b.
4.	It enters a while loop that continues until b becomes 0.
5.	Inside the loop, it calculates the quotient of a divided by b and appends it to the quotients list.
6.	It also appends the current a to the dividers list and the remainder of a divided by b to the remainders list.
7.	The value of b is appended to the y list.
8.	It then updates the values of a and b to continue the algorithm: a takes the value of b, and b takes the remainder of the previous division.
9.	After the loop, it prints a series of equations representing each step of the Euclidean algorithm.
10.	It then prints the GCD, which is the last non zero remainder in the remainders list.


