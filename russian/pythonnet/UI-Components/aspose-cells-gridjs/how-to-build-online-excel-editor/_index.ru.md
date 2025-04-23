---
title: как запустить Aspose.Cells.GridJs в Docker
type: docs
weight: 250
url: /ru/python-net/aspose-cells-gridjs/how-to-build-online-excel-editor/
keywords: GridJs, Docker
description: Эта статья описывает, как запускать GridJs в Docker для создания онлайн редактора или просмотрщика Excel.
aliases:
  - /python-net/aspose-cells-gridjs/docker/
  - /python-net/aspose-cells-gridjs/run-aspose-cells-gridjs-in-docker/
  - /python-net/aspose-cells-gridjs/run-gridjs-in-docker/
  - /python-net/aspose-cells-gridjs/how-to-build-online-excel-editor-using-gridjs/
  - /python-net/aspose-cells-gridjs/how-to-build-web-spreadsheet-editor-using-gridjs/
  - /python-net/aspose-cells-gridjs/how-to-build-web-excel-editor-using-gridjs/
  - /python-net/aspose-cells-gridjs/how-to-build-online-excel-viewer-using-gridjs/
  - /python-net/aspose-cells-gridjs/how-to-build-web-spreadsheet-viewer-using-gridjs/
  - /python-net/aspose-cells-gridjs/how-to-build-web-excel-viewer-using-gridjs/
---

# Руководство по Docker

## Предварительные требования

Убедитесь, что Docker установлен на вашем компьютере. Вы можете скачать и установить Docker с [официального сайта Docker](https://www.docker.com/get-started).

## Шаг 1: Создайте Dockerfile

Создайте файл с именем `Dockerfile` в вашей [директории](https://github.com/aspose-cells/Aspose.Cells-for-Python-via-.NET/blob/main/Examples_GridJs_Python_Net/). В `Dockerfile` должны содержаться инструкции по сборке вашего Docker-образа.

## Шаг 2: Напишите Dockerfile для GridJs

Вот пример [`Dockerfile`](https://github.com/aspose-cells/Aspose.Cells-for-Python-via-.NET/blob/main/Examples_GridJs_Python_Net/Dockerfile) для демонстрации GridJs с приложением на Python:

```dockerfile
# use Python 3.13 as parent image
FROM python:3.13-slim
# web port
EXPOSE 2022

# Update the package list and install the   package along with additional related packages
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        libicu-dev \
        icu-devtools \
        pkg-config \
        build-essential \
	fontconfig \ 
        libgdiplus && \
        apt-get clean && \
        rm -rf /var/lib/apt/lists/*

# Set the necessary environment variable  
ENV LD_LIBRARY_PATH=/usr/lib/x86_64-linux-gnu
# Set the System.Globalization.Invariant setting to true
ENV DOTNET_SYSTEM_GLOBALIZATION_INVARIANT=true

WORKDIR /app  

# copy all to  /app  
COPY . /app  


RUN pip install --no-cache-dir -r requirements.txt  
# the basic file path which contains the spread sheet files 
RUN mkdir -p /app/wb
# the file path to store the uploaded files
RUN mkdir -p /app/uploads
# the cache file path for GridJs
RUN mkdir -p /app/grid_cache/  
COPY wb/*.xlsx /app/wb/



# start cmd
CMD [ "python", "./main.py" ]
```

## Шаг 3: Создание образа Docker
Создайте образ Docker: В терминале выполните следующую команду для сборки вашего образа Docker:
```bash
docker build -t gridjs-demo-python .
```
вы можете заменить gridjs-demo-python на название, которое хотите дать своему образу Docker.

## Шаг 4: Запуск контейнера Docker
После создания образа, вы можете запустить контейнер с помощью следующей команды:

```bash
docker run -d -p 2022:2022   -v C:/path/to/license.txt:/app/license  --name gridjs-demo-container  gridjs-demo-python
```

или просто запустите демонстрацию в режиме пробного использования:


```bash
docker run -d -p 2022:2022 --name gridjs-demo-container  gridjs-demo-python
```

Объяснение опций команды Docker Run
-d: Запустить контейнер в фоновом режиме (отделенно).
-p 2022:2022: Пробросить порт 2022 внутри контейнера на порт 2022 на хосте.
-v C:/path/to/license.txt:/app/license: Привязка файла лицензии с хост-машины внутри контейнера.
--name gridjs-demo-container: Назначить имя контейнеру.

## Шаг 5: Проверка, что контейнер запущен
Чтобы проверить, запущен ли ваш контейнер, используйте следующую команду:

```bash
docker ps
```
Это выведет список всех запущенных контейнеров. Вы должны увидеть ваш контейнер с его именем и статусом.

## Шаг 6: Доступ к веб-приложению

Откройте веб-браузер и перейдите по адресу `http://localhost:2022`. Вы должны увидеть ваше приложение в работе.

## Дополнительные команды

### Остановка контейнера

Для остановки запущенного контейнера используйте следующую команду:

```bash
docker stop gridjs-demo-container
```

### Удаление контейнера
Чтобы удалить остановленный контейнер, используйте следующую команду:

```bash
docker rm  gridjs-demo-container
```

### Удаление образа
Чтобы удалить образ, используйте следующую команду:

```bash
docker rmi gridjs-demo-python
```




