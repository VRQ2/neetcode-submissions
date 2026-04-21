class Solution:
    def isPalindrome(self, s: str) -> bool:
        news = re.sub(r'[^a-zA-Z0-9]', '',s)
        news = news.lower()
        wynik = []
        for i in range(len(news)-1,-1,-1):
            wynik.append(news[i])
        wynikstr = "".join(wynik)
        if(wynikstr == news):
            return True
        return False