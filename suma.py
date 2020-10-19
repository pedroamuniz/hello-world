def suma(*args, **kwargs):
    for a , b in kwargs.items():
        print(a , '->>>>>' , b)
    return sum(args)

if __name__ == "__main__":
    print(suma(1 , 2  ,3 , total=6))