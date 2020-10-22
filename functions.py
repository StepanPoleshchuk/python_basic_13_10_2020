def my_range(i, start=0, step=1):
    '''Мой range, start и stop именованные параметры'''
    try:
        i = int(i)
        result = []
        current = start
        while current < i:
            result.append(current)
            current += step
        return result
    except ValueError:
        print('my_range принимает только числа')
