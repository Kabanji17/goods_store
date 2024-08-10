# goods_store

## Описание проекта

В рамках этих домашних заданий мы проработаем использование классов и объектов на основе популярной темы e-commerce.

E-commerce  — электронная торговля, или электронная коммерция. На данном этапе работы мы не будем реализовывать систему платежей, однако подготовим всё для того, чтобы у нас появилось ядро для интернет-магазина. В дальнейшем для этого ядра возможно будет реализовать любой интерфейс — от сайта до телеграм-бота.

Проект в рамках выполнения домашних заданий в блоке ООП. Созданы:

- класс представления продуктов с тестами;
- класс представления категорий продуктов с тестами;
- модуль по заполнению представителей классов данными из файла формата json;
- некоторые атрибуты разработанных классов сделаны приватными;
- добавлены сеттеры и геттеры для приватных атрибутов;
- добавлен запрос к пользователю на уменьшение цены;
- добавлен поиск аналогичных товаров в списке товаров в категории, при совпадении количество складывается, цена берётся большая;
- добавлен функционал в части складывания объектов товара;
- добавлен функционал в части строкового отображения;
- добавлен функционал в части перебора списка продуктов в объекте категории;

## Установка:

1. Клонируйте репозиторий:
```
git clone git@github.com:Kabanji17/goods_store.git
```
2. Установите зависимости:
```
pip install -r requirements.txt
```
## Использование:

Раздел будет дополняться по мере разработки.

## Тесты:
1. Для тестирования используются фикстуры в модуле ```conftest.py```.
2. Программа покрыта тестами на 93%

### Покрытие тестами 

проверка:

Сначала заходим в папку ```tests``` и из нее включаем тесты:
```
cd tests
```
```
pytest --cov
```
```
Name                      Stmts   Miss  Cover
---------------------------------------------
src\__init__.py               0      0   100%
src\category.py              30      0   100%
src\product.py               44     11    75%
src\product_iterator.py      13      0   100%
tests\__init__.py             0      0   100%
tests\conftest.py            19      0   100%
tests\test_category.py       23      0   100%
tests\test_product.py        25      0   100%
---------------------------------------------
TOTAL                       154     11    93%
```
## Документация:

Для получения дополнительной информации обратитесь к [документации](docs/README.md).

## Лицензия:

Этот проект лицензирован по [лицензии MIT](LICENSE).