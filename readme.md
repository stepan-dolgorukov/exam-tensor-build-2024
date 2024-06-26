# Решение тестового задания в отдел сборки ПО

Ознакомьтесь, пожалуйста, с содержимым &laquo;прочитайки&raquo; перед проверкой решения. В этом файле содержатся комментарии, инструкции по запуску решений задач.

Часть &laquo;A&raquo; &mdash; это задания по Bash, часть &laquo;B&raquo; &mdash; задания по Python.

Решения не требуют установки зависимостей. Применяются GNU Bash версии 5.2.26(1), Python версии 3.11.8.

## A.1

```shell
cd A
chmod u+x 1.bash
./1.bash "каталог" "версия"
```

Будут удалены каталоги продуктов, чья версия меньше указанной (bound-версия).

## A.2

Задание составлено неточно. Непонятно, какое взаимодействие будет с хостами. Поэтому я просто распечатываю считанные хосты. Тело цикла обхода легко модифицируется под необходимое взаимодействие.

```shell
cd A
chmod u+x 2.bash
```

Запуск:

```shell
./2.bash < "файл, представляющий список хостов"
```

либо

```shell
./2.bash
```

и вводим хосты построчно.

## A.3

```shell
cd A
chmod u+x 3.bash
./3.bash "каталог"
```

## A.4

```shell
cd A
chmod u+x 4.bash
./3.bash "каталог-источник" "каталог-назначение"
```

## B.1

```shell
cd B
chmod u+x 1.py
./1.py "файл журнала"
```

## B.2

```shell
cd B
chmod u+x 2.py
./2.py "каталог"
```

Выполнено замедление каждого шага: задержка 1 секунда, чтобы было видно заполнение прогресс-бара.