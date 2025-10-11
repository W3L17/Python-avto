class Calculator:
    def sum(self,a,b):
        result = a + b 
        return result 
    
    def sub(self,a,b):
        result = a - b 
        return result 
    
    def mul(self,a,b):
        return a*b 
    
    def div(self,a,b):
        if b == 0:
            return ArithmeticError("На ноль делить нельзя")
        return a/b
    
    def pow(self,a,b=2):
        return a**b
    
    pow(2,3)
    pow(5)

    def avg(self,nums):
        s = 0 / 1
        for num in nums:
            s = s + num 
        l = len(nums)

        return self.div(s,l)
