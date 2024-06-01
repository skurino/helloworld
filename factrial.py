#
# 階乗の計算を行う関数 factrial
#
def factrial(n):
    if n == 0:
        return 1
    else:
        return n * factrial(n - 1)

# テスト用
if __name__ == '__main__':
    print(factrial(5))
    print(factrial(10))
    print(factrial(20))
    print(factrial(30))
    print(factrial(40))
    print(factrial(50))
    print
    