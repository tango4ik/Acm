class acm():
    def __init__(self,code:list[str]):
        self.code :list[str] = code
        self.stack : list[int] = []
    def do(self):
        i = 0
        while i < len(self.code):
            bit = self.code[i]
            if "out" in bit:
                print(chr(self.stack.pop()),end="")
            elif "inc" in bit:
                self.stack.append(ord(input()))
            elif "ini" in bit:
                self.stack.append(int(input()))
            elif "set" in bit:
                self.stack.append(int(bit.removeprefix("set ")))
            elif "goto" in bit:
                i = int(bit.removeprefix("goto ")) - 1
            elif "add" in bit:
                self.stack.append(self.stack.pop() + self.stack.pop())
            elif "mul" in bit:
                self.stack.append(self.stack.pop() * self.stack.pop())
            elif "div" in bit:
                self.stack.append(self.stack.pop() / self.stack.pop())
            elif "rem" in bit:
                self.stack.remove(int(bit.removeprefix("rem ")))
            elif "sub" in bit:
                self.stack.append(self.stack.pop() - self.stack.pop())
            elif "." in bit:
                print(self.stack.pop())
            elif "end" in bit:
                break
            if "&" in bit:
                temp = self.stack[len(self.stack) - 1]
                if temp == int(bit.removeprefix("&")):
                    temp = self.stack.pop()
                else:
                    i += 1
            i += 1
code = []
program = input()
with open(program + '.acm') as f:
    code = f.readlines()
inp = None
#while inp != "end":
#   inp = input()
#   if inp != "end":
#     code.append(inp)
comp = acm(code)
comp.do()
