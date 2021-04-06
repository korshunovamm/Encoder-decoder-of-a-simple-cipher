import heapq
from AbstractClassEncryptor import AbsCodeClass


class AutomaticCesarClass(AbsCodeClass):
    def code(self):
        count = {chr(x): 0 for x in range(self.smallstartletter, self.smallstartletter + self.letters - 1)}
        heap = []
        for char in self.text:
            if char.isalpha():
                count[char.lower()] += 1
                heapq.heappush(heap, (count[char.lower()], char.lower()))
        key_cesar_encrypt = abs(ord(heapq.heappop(heap)[1]) - self.smallstartletter)
        print(key_cesar_encrypt)


