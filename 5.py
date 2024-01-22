def func(banks):
    dp = [0] * (len(banks)+1)

    for i in range(1, len(banks)+1):
        dp[i] = max(dp[i-1], dp[i-2] + banks[i-1][1])

    money = dp[-1]
    selected_banks = []

    i = len(banks)
    while i > 0:
        if dp[i] == dp[i-1]:
            i -= 1
        else:
            selected_banks.append(banks[i-1])
            i -= 2

    selected_banks.reverse()
    return [money, selected_banks]

if __name__=='__main__':
    k = int(input("Введите количество банков на улице: "))
    banks = []
    for i in range(k):
        bank_name, money = input("Введите название банка и сумму денег в сейфе через пробел: ").split()
        banks.append((bank_name, int(money)))
    print(func(banks))
