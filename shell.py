import basic

running = True

while running:
    text = input('$Neon > ')

    if text == '.out':
        break

    result, error = basic.run('<stdin>', text)

    if(error):
        print(error.as_string())
    else:
        print(result)
