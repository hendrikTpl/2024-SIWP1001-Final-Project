class Euclid():
    def __init__(self,a, b):
        self.a = a
        self.b = b 
        
    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a
    
# DO something
# def main():
#     a = 10
#     b =10
#     algo2 = Euclid(a,b)
#     res = algo2.gcd(a,b)
#     print(res)

# if __name__=="__main__":
#     main()