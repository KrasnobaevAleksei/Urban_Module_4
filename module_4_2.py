def test_function():
    def inner_function():
        print("Я внутри функции test_function")
    inner_function()
test_function()
#inner_function() при вызове этой функции пишет что она не определена