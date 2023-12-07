a = int(input())
ch = list(input())
s_ch = ch.copy()
s_ch.sort()

print(ch, s_ch)
re = ""
for x in s_ch:
    re += str(ch[ch.index(x)])

print(re)