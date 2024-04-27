# Решение тестового задания в отдел сборки ПО

Ознакомьтесь, пожалуйста, с содержимым &laquo;прочитайки&raquo; перед проверкой решения. В этом файле содержатся комментарии, инструкции по запуску решений задач.

Часть &laquo;A&raquo; &mdash; это задания по Bash, часть &laquo;B&raquo; &mdash; задания по Python.

## 1.A

```shell
cd A
chmod u+x 1.bash
./1.bash "каталог" "версия"
```

Будут удалены каталоги продуктов, чья версия меньше указанной (bound-версия).

## 2.A

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

## 3.A

```shell
cd A
chmod u+x 3.bash
./3.bash "каталог"
```

## 4.A

```shell
cd A
chmod u+x 4.bash
./3.bash "каталог-источник" "каталог-назначение"
```
