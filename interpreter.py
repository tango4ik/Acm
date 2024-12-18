class acm():
    def __init__(self,code:list[str]):
        self.code :list[str] = code
        self.stack: int = 104
    def do(self):
        i = 0
        while i < len(self.code):
            bit = self.code[i]
            if "&" in bit:
                if self.stack == int(bit.removeprefix("&")):
                    i = i
                else:
                    i += 1
            if "out" in bit:
                print(chr(self.stack),end="")
            elif "in" in bit:
                self.stack = ord(input())
            elif "set" in bit:
                self.stack = int(bit.removeprefix("set "))
            elif "goto" in bit:
                i = int(bit.removeprefix("goto ")) - 1
            elif "end" in bit:
                break
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
