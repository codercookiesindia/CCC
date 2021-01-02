import sys

positive_set = set()
negative_set = set()
positive_map = {}
negative_map = {}

found = False


def search_str(s, x, y, step, flag, mp):
    global found
    global positive_map
    global negative_map

    if found:
        return

    if step == 0:
        if flag:
            positive_set.add(s)
        else:
            if s in positive_set:
                ret = []
                ret1 = []
                step = 0
                ss = s
                while True:
                    if not (str(step) + ss) in negative_map:
                        break
                    r = negative_map[str(step) + ss]
                    ret.append(r)
                    ss = r.split()[2]
                    step += 1
                ret1 = []
                step = 0
                ss = s
                while True:
                    if not (str(step) + ss) in positive_map:
                        break
                    r = positive_map[str(step) + ss]
                    ret1.append(r.split()[0] + ' ' + r.split()[1] + ' ' + ss)
                    ss = r.split()[2]
                    step += 1
                print('\n'.join(ret1[::-1] + ret))
                found = True

        return

    for i in range(3):
        xx = x[i]
        yy = y[i]
        for j in range(len(s) - len(xx) + 1):
            if s[j:j + len(xx)] == xx:
                next_s = s[:j] + yy + s[j + len(xx):]
                if not str(step - 1) + next_s in mp:
                    mp[str(step - 1) + next_s] = str(i + 1) + \
                        ' ' + str(j + 1) + ' ' + s
                    search_str(s[:j] + yy + s[j + len(xx):],
                               x, y, step - 1, flag, mp)


x = []
y = []
for i in range(3):
    a, b = input().split()
    x.append(a)
    y.append(b)
step, s, e = input().split()
step = int(step)

half_step = (step + 1) // 2
search_str(s, x, y, half_step, True, positive_map)
search_str(e, y, x, step - half_step, False, negative_map)
