# 装饰器用法
import time

def trimmer(func):
    def deco():
        start_time = time.time()
        func()
        end_time = time.time()
        print(end_time-start_time)
    return deco()
@trimmer
def test1():
    print("this is test1")

if __name__ == "__main__":
    test1