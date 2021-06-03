"""　関数内関数 """


def outer_func(outer_arg):
    def inner_func(inner_arg):
        return print(f"outer_arg:{outer_arg}, inner_arg:{inner_arg}")

    return inner_func(outer_arg * 2)


# outer_func arg:2, inner_func arg:4
outer_func(2)

"""　クロージャ """


def closure_outer_func(outer_arg):
    def closure_inner_func(inner_arg):
        return print(f"closure_outer_arg:{outer_arg}, closure_inner_arg:{inner_arg * 2}")

    # 関数の戻り値ではなく関数を返却している事に注目
    return closure_inner_func


# outer_func arg:2, inner_func arg:4
closure_func = closure_outer_func(2)

# 内部関数の引数が動的になっている事に注目
# closure_outer_arg:2, closure_inner_arg:6
closure_func(3)
