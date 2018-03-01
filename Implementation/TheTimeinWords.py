def int2letter(m):
    minutes = [
        'one', 'two', 'three', 'four', 'five',
        'six', 'seven', 'eight', 'nine', 'ten',
        'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen',
        'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty'
    ]

    if m <= 20:
        return minutes[m-1]
    else:
        return 'twenty %s' % (minutes[m-21],)


if __name__ == '__main__':
    H = int(input().strip())
    M = int(input().strip())

    hours = ['one', 'two', 'three', 'four', 'five', 'six', 'seven',
             'eight', 'nine', 'ten', 'eleven']

    if M == 0:
        msg = "%s o'  clock" % (hours[H-1], )
    elif M == 15:
        msg = "quarter past %s" % (hours[H-1],)
    elif M == 45:
        msg = "quarter to %s" % (hours[H],)
    elif 0 < M < 30:
        if M == 1:
            msg = 'one minute past %s' % (hours[H-1],)
        else:
            msg = "%s minutes past %s" % (int2letter(M), hours[H-1])
    elif M == 30:
        msg = "half past %s" % (hours[H-1])
    else:
        left_time = 60 - M
        if left_time == 1:
            msg = 'one minute to %s' % (hours[H],)
        else:
            msg = "%s minutes to %s" % (int2letter(left_time), hours[H])
    print(msg)
