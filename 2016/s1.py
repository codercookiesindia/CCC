def main():
    s = 0
    freq = [0] * 26
    a = input().strip()
    for c in a:
        freq[ord(c) - ord('a')] += 1

    a = input().strip()
    for c in a:
        if c == '*':
            s += 1
        else:
            freq[ord(c)-ord('a')] -= 1

    for v in freq:
        if v < 0:
            print('N')
            return
        s -= v

    print('N' if s != 0 else 'A')


main()
