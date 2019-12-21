## Описание проекта.
Osquery-расширение для менджера пакетов Homebrew. Данное расшиерние позволяет пользователю получать спискок установаленных пакетов, корневых пакетов и доступные обновления. Так же пользователь может получить список существующих CVE по формуле и список закрытых issue для репозитория.
## Доступные функции:
- [x] Получить список пакетов.
- [x] Получить список корневых пакетов.
- [x] Получить список обновлений.
- [x] Получить список открытых и закрытых issue.
- [x] Получить список существующих CVE.
## Инструкции по запуску скриптов.
В зависимости от того, что вы хотите сделать, выберите нужный скрипт и скачайте его.  
Пример использования скриптов для получения списков установаленных пакетов, корневых пакетов и доступные обновления.  
P.S данный пример приведен для получения списка установленных пакетов.
```ShellSession
$ cd List of packages 
$ cd Script for "brew list"
$ ./run.sh
```
После того как скрипт завершит работу введите команду:
```ShellSession
$ dumer dump
```
На выходе вы получите SQL-таблицу с нужными данными.  
Пример использования скрипта для получиния списка существующих CVE по формуле.  
Все необходимые пакеты для работы скрипта можно установить с помощью команды:
```ShellSession
$ sudo pip3 install -r requirements.txt
```
Для первого запуска нужно ввести следующие команды:
```ShellSession
$ ./sbin/db_mgmt_cpe_dictionary.py -p
$ ./sbin/db_mgmt_json.py -p
$ ./sbin/db_updater.py -c // может занять много времени.
```
Чтобы получить все существующие CVE для формулы введите:
```ShellSession
$ ./bin/search.py -p webex: -o csv  -v "формула"
```
## Демонстрационные видео
Получение CVE:  
[![asciicast](https://asciinema.org/a/Zc0PM2hUcPeyVNjIqSDUS9V1I.svg)](https://asciinema.org/a/Zc0PM2hUcPeyVNjIqSDUS9V1I)
Получение issue:
## Полезные ссылки
- [Менедер пакетов для Python](https://pypi.org/project/pip/)
- [Официальный сайт osquery](https://osquery.io)
- [Homebrew](https://brew.sh/index_ru)

