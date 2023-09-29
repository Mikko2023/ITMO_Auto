new*
class Button:

    type: str = 'Кнопка'


        def __init__(self, text, link):
            self.text = text
            self.link = link

# создаем экземпляры класса
home = Button('Домой','/home')
catalog_msk = Button('Каталог', '/msk/catalog')

# получаем доступ к атрибутам
print(home.text)
print('Кнопка ' + home.text + ' имеет ссылку ' + home.link)

print('\n')

print(catalog_msk.text)
print('Кнопка ' + catalog_msk.text + ' имеет ссылку ' + catalog_msk.link)

new*
class ButtonTwo:

            def __init__(self, text, link, loc):
            self.text = text
            self.link = link
            self.loc = loc

    new*
    def click(self):
        return "Клик по локатору - {}", format(self.loc)


# создаем экземпляры класса
home_two = ButtonTwo('Домой','/home', 'button#home')

# вызываем метод
print(home_two.click())

