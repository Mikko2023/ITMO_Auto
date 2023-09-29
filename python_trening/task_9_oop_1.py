new*
class Input:

            def __init__(self, loc):
            self.loc = loc

# создаем экземпляры класса
search = Input('input#search')
home = Button('Домой','/home')
title = Button('Каталог', '/msk/catalog')
Link = Button ('Каталог', '/msk/catalog')

print(search.text)
print('Кнопка ' + home.text + ' имеет ссылку ' + home.link)

print(Button.text)
print('Кнопка ' + home.text + ' имеет ссылку ' + home.link)

print(Title.text)
print('Кнопка ' + home.text + ' имеет ссылку ' + home.link)

print(Link.text)
print('Кнопка ' + home.text + ' имеет ссылку ' + home.link)

print('\n')


print(home.text)

print(search.click())


