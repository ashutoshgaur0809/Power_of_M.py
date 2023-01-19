T = int(input("Enter no. of test case = "))
for i in range(T):
    x = int(input("Enter the value of x="))
    m = int(input("Enter the value of m="))
    s = ""
    for j in range(len(str(x))):

        # for last figit
        a = x % 10
        mod = pow(a, m) % 10
        # we store in string
        s = str(mod) + s
        x = x // 10
    print("the no which made by remainder=", s)  # our remainder in form of str
    # reverse str
    rev = s[::-1]
    rev = int(rev)
    print("the reverse of no is=", rev)
    if (rev % 7 == 0):
        print("Yes")
    else:
        print("No")
