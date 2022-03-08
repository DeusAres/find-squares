from PIL import Image

class listCheck():
    def __init__(self):
        self.entries = []
    def append(self, args):
        self.entries.append(check(*args))
    def checking(self, x,y):
        toRemove = []
        for i in range(len(self.entries)):
            result = self.entries[i].inside(x,y)
            if type(result) == int:
                return result
            elif result == 'remove':
                toRemove.append(i)
            
class check():
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def inside(self, x, y):
        if x >= self.x1 and x<= self.x2:
            if y >= self.y1 and y <= self.y2:
                return self.y2-self.y1
        elif x > self.x2:
            return 'remove'

if __name__ == '__main__':
    template = "test.png"
    template = Image.open(template)
    W, H = template.size
    template = template.load()

    coordinates = []
    checkList = listCheck()

    for x in range(W):
        for y in range(H):
            result = checkList.checking(x,y)
            if type(result) == int:
                y += result-1
                continue

            if template[x,y] == (0,0,0):
                y1 = y
                while y1<H and template[x,y1] == (0,0,0) :
                    y1 += 1
                x1 = x
                while x1<W and template[x1,y] == (0,0,0) :
                    x1 += 1

                coordinates.append([x,y,x1-1,y1-1])

                checkList.append([x,y,x1-1,y1-1])