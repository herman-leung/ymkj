def function():
    try:
        # print(1/0)
        # print(a)
        # print(str('1'- '0'))
        # print('1' - ';')
        pass
    except Exception as e:
        print(e)
    finally:
        print("程序异常")

def main():
    function()
if __name__ == "__main__":
    function()