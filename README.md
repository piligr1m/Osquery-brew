## Описание проекта.
Osquery-расширение для менджера пакетов Homebrew. Данное расшиерние позволяет пользователю получать спискок установаленных пакетов, корневых пакетов и доступные обновления. Так же пользователь может получить список существующих CVE по формуле и список закрытых issue и pull-request для репозитория. Работает только на OS Linux.
## Доступные функции:
- [x] Получить список пакетов.
- [x] Получить список корневых пакетов.
- [x] Получить список обновлений.
- [x] Получить список закрытых issue и pull-request для репозитория.
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
Чтобы получить все существующие CVE для формулы введите:
```ShellSession
$ ./cvesearch.py -s "формула"
```
Пример использования скрипта для получения закрытых issue и pull-request для репозитория.  
Все необходимые пакеты для работы скрипта можно установить с помощью команды:
```ShellSession
$ sudo pip3 install -r requirements.txt
```
Чтобы получить закрытые issue и pull-request для репозитория введите:
```ShellSession
$ ./import_issues.py
$ ./process_issues.py
```
После выполенния этих команд в папке со скриптами появиться файл `result.tsv`, в котором будет таблица с количеством закрытых issue и pull-request.
## Демонстрационные видео
- [Получение CVE](https://asciinema.org/a/Zc0PM2hUcPeyVNjIqSDUS9V1I)  
- [Получение issue и pull-request](https://asciinema.org/a/Zc0PM2hUcPeyVNjIqSDUS9V1I)   
[![asciicast](https://asciinema.org/a/KTgP7sDCdCmkQoFsKSXKyhhXw.svg)](https://asciinema.org/a/KTgP7sDCdCmkQoFsKSXKyhhXw)
## Полезные ссылки
- [Менедер пакетов для Python](https://pypi.org/project/pip/)
- [Официальный сайт osquery](https://osquery.io)
- [Homebrew](https://brew.sh/index_ru)
- [NATIONAL VULNERABILITY DATABASE](https://nvd.nist.gov)

