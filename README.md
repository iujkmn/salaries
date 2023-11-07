# Сравниваем зарплаты программистов
Программа берёт данные по вакансиям по разным языкам программирования и анализирует их.Затем выдаёт таблицу с языком программирования и соответсвующую ему усреднённую зарплату.
## Как установить
Python3 должен быть уже установлен. Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей и установить зависимости.

Установите зависимости командой:

```
pip install -r requirements.txt
```
Рекомендуется использовать [virtuaienv/venv] для изоляции проекта.
## Пример запуска скрипта
Для запуска скрипта у вас уже должен быть установлен Python3.

Для получения необходимых изображений необходимо написать один из вариантов:

```
python main.py
```
## Переменные окружения
Часть настроек проекта берётся из переменных окружения. Переменные окружения-это переменные,значение которых присваиваются программе Python извне. Чтобы их определить,создайте файл `.env` рядом с `main.py` и запишите туда данные в таком формате:ПЕРЕМЕННАЯ=значение.

Пример содержания файла `.env`:
```
TOKEN = "token"
```
Получить токен `TOKEN` можно на сайте [SuperJob](https://www.superjob.ru).
## Пример запуска скрипта
Для запуска скрипта у вас уже должен быть установлен Python3.

Для запуска скрипта необходимо написать:
```
python main.py
```
## Цель проекта
Код написан в образовательных целях на онлайн-курсе для веб-разработчиков dvmn.org.