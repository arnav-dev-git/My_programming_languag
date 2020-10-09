import basic

running = True

while running:
    text = input('$basic > ')
    result, error = basic.run('<stdin>', text)

    if text == 'exit!':
        break

    if(error):
        print(error.as_string())
    else:
        print(result)
