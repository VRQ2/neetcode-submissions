class Solution:
    def isValid(self, s: str) -> bool:
        dic = {')': '(', ']': '[', '}': '{'} 
        heap = []
    
        for i in s:
            if i in dic:
                t = heap.pop() if heap else "#"

                if(dic[i] != t):
                    return False
            else:
                heap.append(i)   

        if not heap: 
            return True 
        return False