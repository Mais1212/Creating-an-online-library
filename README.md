# Creating-an-online-library
Офлайн библиотека спарсенных книг с сайта tululu.org.

Пример работы [сайта](https://mais1212.github.io/Creating-an-online-library/pages/index1.html).

# Как запустить сайт в оффлайн
- Загрузите репозиторий к себе на компьютер.
- Создайте папку в удобном для вас месте.
- Разархивируйте туда папки из репозитория : `images`, `library`, `pages`, `static`.
- Перейдите в папку `pages`.
- Откройте файл `index1.html`
# Как запустить
- Для запуска библиотеки у вас уже должен быть установлен [Python 3](https://www.python.org/downloads/).
- Установите зависимости командой:
```
pip install -r requirements.txt
```
- Запустите сайт командой:
```
python render_website.py
```
