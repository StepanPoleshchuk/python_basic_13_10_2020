def my_range(stop, start=0, step=1):
    '''Мой range, start и stop именованные параметры'''
    try:
        while stop > start:
            yield start
            start += step
    except ValueError:
        print('my_range принимает только числа')
