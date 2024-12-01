class Solution:
    def checkIfExist(self, arr: list[int]) -> bool:
        d = dict()

        for e in arr:
            if e % 2 == 0:
                if d.get(e//2):
                    return True
                
            if d.get(e*2):
                return True

            d[e] = True
        
        return False
           

        