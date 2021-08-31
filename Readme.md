# Запуск Rest api

## Инструкция по запуску(на примере Ubuntu)
Для запуска данного rest api Вам потребуется:
1. Открыть терминал.
2. Создать папку, например, mkdir BostonGene
3. Перейти в нее cd BostonGene
4. Склонировать в нее данный репозиторий  git clone https://github.com/DmitriyLush/Boston_test_fastapi.git
5. Перейти в папку Boston_test_fastapi
6. Выполнить команду sudo docker-compose up --build
## Проверка работоспособности.
После выполнения инструкции, вы должны будете увидеть нечто подобное:

signatures_1  | INFO:     Will watch for changes in these directories: ['/app']
signatures_1  | INFO:     Uvicorn running on http://0.0.0.0:80 (Press CTRL+C to quit)
signatures_1  | INFO:     Started reloader process [1] using statreload
signatures_1  | INFO:     Started server process [9]
signatures_1  | INFO:     Waiting for application startup.
signatures_1  | INFO:     Application startup complete.

Откройте браузер, перейдите по ссылке http://0.0.0.0:80/docs
# Готово, можно тестировать функционал.
Чтобы остановить docker-compose, нажимите ctrl+c, а затем sudo docker-compose down ( это остановит запущенные docker-контейнеры и удалит их, а также все docker-сети, созданные при запуске связки контейнеров из файла docker-compose.yml.
