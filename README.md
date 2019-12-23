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
Обязательным условием работы данных трех скриптов является наличие менеджера пакетов Pacman.
P.S данный пример приведен для получения списка установленных пакетов.
```ShellSession
$ cd Packages 
$ ./run.sh
```
После того как скрипт завершит работу введите команду:
```ShellSession
$ dumper dump
$ dumper ls
```
На выходе вы получите SQL-таблицу с нужными данными.  
Пример использования скрипта для получиния списка существующих CVE по формуле.  
Все необходимые пакеты для работы скрипта можно установить с помощью команды:
```ShellSession
$  pip3 install requests untangle
```
Чтобы получить все существующие CVE для формулы введите:
```ShellSession
$ ./cvesearch.py -s "формула"
```
Пример использования скрипта для получения закрытых issue и pull-request для репозитория.  
В файлах `import_issues.py` и `process_issues.py` вставьте свой токен и замените автора и название репозитория.   
Все необходимые пакеты для работы скрипта можно установить с помощью команды:
```ShellSession
$ sudo pip3 install -r requirements.txt
```
Чтобы получить закрытые issue и pull-request для репозитория введите:
```ShellSession
$ ./import_issues.py
$ ./process_issues.py
```
После выполенния этих команд в директории со скриптами появится файл `result.tsv`, в котором будет таблица с количеством закрытых issue и pull-request.
## Демонстрационные видео.
- [Получение CVE](https://asciinema.org/a/Zc0PM2hUcPeyVNjIqSDUS9V1I)  
- [Получение issue и pull-request](https://asciinema.org/a/KTgP7sDCdCmkQoFsKSXKyhhXw)
- [Получение установленных пакетов](https://www.youtube.com/watch?v=j9WaYU-zj1U&feature=youtu.be)
- [Получение корневых пакетов](https://youtu.be/65YdzjlJ6bg)

## Полезные ссылки.
- [Менедер пакетов для Python](https://pypi.org/project/pip/)
- [Официальный сайт osquery](https://osquery.io)
- [Homebrew](https://brew.sh/index_ru)
- [NATIONAL VULNERABILITY DATABASE](https://nvd.nist.gov)
- [Github3.py](https://pypi.org/project/github3.py/)
- [Github API](https://developer.github.com/v3/)
- [Pacman](https://wiki.archlinux.org/index.php/Pacman_(Русский))

