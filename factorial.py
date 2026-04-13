def factorial(n):
    #codizione terminale
    if n==0 or n==0:
        return 1
    #condizione non terminale
    else:
        return n*factorial(n-1)

if __name__ == "__main__":
    N = 5
    print(factorial(N))

