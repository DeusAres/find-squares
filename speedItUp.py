from PIL import Image

import time
start_time = time.time()

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

        if len(toRemove) != 0:
            self.entries = [self.entries[i] for i in range(len(self.entries)) if i not in toRemove]


class check():
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def inside(self, x, y):
        if x >= self.x1 and x < self.x2:
            if y >= self.y1 and y < self.y2:
                return self.y2-self.y1
        elif x > self.x2:
            return 'remove'

if __name__ == '__main__':
    template = "./test.png"
    template = Image.open(template)
    W, H = template.size
    template = template.load()

    coordinates = []
    checkList = listCheck()

    x = 0
    while x < W:
        y = 0
        while y < H:
            if x == 177 and y == 72: 
                print('found')

            result = checkList.checking(x,y)
            if type(result) == int:
                y += result
                continue

            if template[x,y] != (255, 255, 255):
                y1 = y
                while template[x,y1] != (255, 255, 255):
                    y1 += 1
                    if y1>H : break
                x1 = x
                while template[x1,y] != (255, 255, 255):
                    x1 += 1
                    if x1>W : break

                coordinates.append([x,y,x1,y1])

                checkList.append([x,y,x1,y1])
            y+=1
        x+=1

    print("--- %s seconds ---" % (time.time() - start_time))