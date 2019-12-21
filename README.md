## Osquery for brew
## Описание проекта.
Osquery-расширение для менджера пакетов Homebrew. Данное расшиерние позволяет пользователю получать спискок установаленных пакетов, корневых пакетов и доступные обновления. Так же пользователь может получить список существующих CVE по формуле и список закрытых issue для репозитория.
## Доступные функции:
- [x] Получить список пакетов.
- [x] Получить список корневых пакетов.
- [x] Получить список обновлений.
- [x] Получить список закрытых issue.
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
Необходмиые пакеты для работы скрипта:
1.Python 3.6 or later
2.MongoDB 2.2 or later
3.redis server
4.Pip3
   click
   feedformater (for RSS and Atom dump_last) 
   Flask
   Flask-Login
   Flask-PyMongo
   irc
   itsdangerous
   Jinja2
   lxml
   passlib
   PyMongo
   Python-dateutil
   Pytz
   Redis
   requests
   requirements-parser
   six
   sleekxmpp
   Tornado
   Werkzeug
   Whoosh 
   xlrd
Все необходимые пакеты можно установить с помощью команды:
```ShellSession
$ sudo pip3 install -r requirements.txt
```
Для первого запуска нужно ввести следующие команды:
```ShellSession
$ ./sbin/db_mgmt_cpe_dictionary.py -p
$ ./sbin/db_mgmt_json.py -p
$ ./sbin/db_updater.py -c // может занять много времени.
```
Чтобы получить все существующие CVE введите:
```ShellSession
$ ./bin/search.py -p webex: -o csv  -v "формула"
```

