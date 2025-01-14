class FibonacchiLst:
    def __init__(self, instance) -> None:
        self.instance = instance  
        self.idx = 0              
    
    def __iter__(self):
        return self      
    def __next__(self):
        while True:
            try:
                res = self.instance[self.idx]  
            except IndexError:
                raise StopIteration  
            
            
            if res < 0:
                self.idx += 1
            elif res == 0:  
                self.idx += 1
                return res
            else:
                
                if FibonacchiLst.is_fibonacci(res):
                    self.idx += 1
                    return res
                self.idx += 1

    def is_fibonacci(n):
        
        if n == 0 or n == 1:  
            return True
        
        
        a, b = 0, 1
        while b < n:  
            a, b = b, a + b
        
        return b == n  