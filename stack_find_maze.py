maps=[['1','1','1','1','1','1'],
    ['e','0','0','0','0','1'],
    ['1','0','1','0','1','1'],
    ['1','1','1','0','0','x'],
    ['1','1','1','0','1','1'],
    ['1','1','1','1','1','1']
    ]
MAZE_SIZE=6
class Stack():
    def __init__(self):
        self.top=[]
    def isEmpty(self):
        return len(self.top)==0
    def size(self):
        return len(self.top)
    def Clear(self):
        self.top=[]
    def push(self,item):
        self.top.append(item)
    def pop(self):
        if  not self.isEmpty():
            return self.top.pop(-1)
    def peek(self):
        if not self.isEmpty():
            return self.top[-1]
    def __str__(self) -> str:
        return str(self.top)
def isValidPos(x,y):
    if x<0 or y<0 or x>=MAZE_SIZE or y>=MAZE_SIZE:
        return False
    else:
        return maps[y][x] == '0' or maps[y][x]=='x'

def DFS():
    stack=Stack()
    stack.push((0,1))
    print('DFS: ')
    while not stack.isEmpty():
        here=stack.pop()
        print(here,end="->")
        (x,y)=here
        if maps[y][x] =='x':
            return True
        else:
            maps[y][x]="."
            if isValidPos(x,y-1):
                stack.push((x,y-1))
            if isValidPos(x,y+1):
                stack.push((x,y+1))
            if isValidPos(x-1,y):
                stack.push((x-1,y))
            if isValidPos(x+1,y):
                stack.push((x+1,y))
        print("현재스택: ",stack)
    return False
print(DFS())
