def weirdNotWeird(n):
    if n % 2 != 0:
        return 'Weird'
    elif n % 2 == 0 and 2 <= n <= 5:
        return 'Not weird'
    elif n % 2 == 0 and 6 <= n <= 20:
        return 'Weird'
