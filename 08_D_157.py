class Stack(object):
    def __init__(self):
        self.items=[]

    def isEmpty(self):
        return len(self)==0

    def __len__(self):
        return len(self.items)

    def peek(self):
        assert not self.isEmpty()
        return self.items[-1]

    def pop(self):
        assert not self.isEmpty()
        return self.items.pop()

    def push(self,data):
        self.items.append(data)

'''s=Stack()
s.push(3)
s.push(7)
s.push(4)
s.push(15)
s.push(25)
print(s.items)
print(s.pop())'''

print("No. 1")
def cetakHexa(data):
    s = Stack()
    ss = "0123456789ABCDEF"
    while data != 0:
        sisa = data%16
        data = data//16
        s.push(ss[sisa])
    st=""
    for i in range(len(s)):
        st = st + str(s.pop())
    return st

print(cetakHexa(12))
print(cetakHexa(31))
print(cetakHexa(299))
print(cetakHexa(255))
print(cetakHexa(31519))

print("No. 2")
nilai = Stack()
for i in range(16):
    if i%3 == 0:
        nilai.push(i)
        print(nilai.items)

print("No. 3")
nilai = Stack()
for i in range(16):
    if i%3 == 0:
        nilai.push(i)
    elif i%4 == 0:
        nilai.pop()
print(nilai.items)
