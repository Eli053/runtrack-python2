s = "abcdefghijklmnopqrstuvwxyz" * 10
n = 1
while n * (n + 1) // 2 <= len(s):
    print(s[(n * (n - 1)) // 2 : (n * (n + 1)) // 2])
    n += 1