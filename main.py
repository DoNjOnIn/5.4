def s0(n,s):
    for k in range(1,n+1):
        s+=1/(2*k+1)**2
    return s
def s1(n,k):
    if k>n:
        return 0
    else:
        return 1/(2*k+1)**2 + s1(n,k+1)

def s2(n,k):
    if k<1:
        return 0
    else:
        return 1/(2*k+1)**2 + s2(n,k-1)

def s3(n,k,s):
    s+=1/(2*k+1)**2
    if k>=n:
        return s
    else:
        return s3(n,k+1,s)

def s4(n,k,s):
    s+=1/(2*k+1)**2
    if k<=1:
        return s
    else:
        return s4(n,k-1,s)

def main():
    n=int(input('n='))
    print('Iter=    '+str(s0(n,0)))
    print('Rec up++ = '+str(s1(n, 1)))
    print('Rec up-- = '+str(s2(n, n)))
    print('Rec down++ ='+str(s3(n, 1,0)))
    print('Rec down-- ='+str(s4(n, n,0)))

if __name__=='__main__':
    main()