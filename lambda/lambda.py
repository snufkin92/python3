""" ラムダ関数 """


def lambda_func(word, func):
    print(func(word))


# Pen
lambda_func("pen", lambda wd: wd.capitalize())
