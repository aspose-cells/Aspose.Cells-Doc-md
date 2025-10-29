---
title: как запустить Aspose.Cells.GridJs в Docker
type: docs
weight: 250
url: /ru/java/aspose-cells-gridjs/how-to-build-online-excel-editor/
keywords: GridJs, Docker
description: Эта статья описывает, как запускать GridJs в Docker для создания онлайн редактора или просмотрщика Excel.
aliases:
  - /java/aspose-cells-gridjs/docker/
  - /java/aspose-cells-gridjs/run-aspose-cells-gridjs-in-docker/
  - /java/aspose-cells-gridjs/run-gridjs-in-docker/
  - /java/aspose-cells-gridjs/how-to-build-online-excel-editor-using-gridjs/
  - /java/aspose-cells-gridjs/how-to-build-web-spreadsheet-editor-using-gridjs/
  - /java/aspose-cells-gridjs/how-to-build-web-excel-editor-using-gridjs/
  - /java/aspose-cells-gridjs/how-to-build-online-excel-viewer-using-gridjs/
  - /java/aspose-cells-gridjs/how-to-build-web-spreadsheet-viewer-using-gridjs/
  - /java/aspose-cells-gridjs/how-to-build-web-excel-viewer-using-gridjs/
---

# Руководство по Docker

## Предварительные требования

Убедитесь, что Docker установлен на вашем компьютере. Вы можете скачать и установить Docker с [официального сайта Docker](https://www.docker.com/get-started).

## Шаг 1: Создайте Dockerfile

Создайте файл с именем `Dockerfile` в вашей [директории](https://github.com/aspose-cells/Aspose.Cells.Grid-for-Java/tree/master/Examples.GridJs). `Dockerfile` должен содержать инструкции по сборке вашего Docker-образа.

## Шаг 2: Напишите Dockerfile для GridJs

Вот пример [`Dockerfile`](https://github.com/aspose-cells/Aspose.Cells.Grid-for-Java/tree/master/Examples.GridJs/Dockerfile) для демонстрации GridJs с java-приложением:

```dockerfile
# Use the maven image to build jar file
FROM maven:3.8.6-amazoncorretto-17 AS build
WORKDIR /usr/src/app


# copy local Maven files to container
COPY .mvn .mvn
COPY pom.xml .
COPY src src

# build application with maven
RUN mvn  package -DskipTests


# Use the jdk8 image as the basic docker image
FROM eclipse/ubuntu_jdk8
WORKDIR /app
# copy build jar file to target container 
COPY --from=build /usr/src/app/target/*.jar /app/app.jar

# web port
EXPOSE 8080
# if you want display better like in windows ,you need to install kinds of fonts in /usr/share/fonts/ 
# then the application can parse and render the fonts which is used in the spread sheet file
# here we don't provide extra fonts resource
# Install Fonts because the SDK image contains very few fonts. The command copies font files from local to docker image. Make sure you have a local “fonts” directory that contains all the fonts you need to install. In this example, the local “fonts” directory is put in the same directory as the Dockerfile.
# COPY fonts/* /usr/share/fonts/
# the basic file path which contains the spread sheet files 
RUN mkdir -p /app/wb
# the file path to store the uploaded files
RUN mkdir -p /app/uploads
# the cache file path for GridJs
RUN mkdir -p /app/grid_cache/streamcache
# we provide some sample spread sheet files in demo 
COPY wb/*.xlsx /app/wb/

# set the start command for the docker image 
ENTRYPOINT ["java","-Djava.security.egd=file:/dev/./urandom","-jar","/app/app.jar"]
```

## Шаг 3: Создание образа Docker
Создайте образ Docker: В терминале выполните следующую команду для сборки вашего образа Docker:
```bash
docker build -t gridjs-demo-java .
```
вы можете заменить gridjs-demo-java на название, которое хотите дать вашему образу Docker.

## Шаг 4: Запуск контейнера Docker
После создания образа, вы можете запустить контейнер с помощью следующей команды:

```bash
docker run -d -p 8080:80   -v C:/path/to/license.txt:/app/license --name gridjs-demo-container  gridjs-demo-java
```

или просто запустите демонстрацию в режиме пробного использования:


```bash
docker run -d -p 8080:80  --name gridjs-demo-container  gridjs-demo-java
```

Объяснение опций команды Docker Run
-d: Запустить контейнер в фоновом режиме (отделенно).
-p 8080:80: сопоставить порт 80 в контейнере с портом 8080 на хосте.
-v C:/path/to/license.txt:/app/license: Привязка файла лицензии с хост-машины внутри контейнера.
--name gridjs-demo-container: Назначить имя контейнеру.

## Шаг 5: Проверка, что контейнер запущен
Чтобы проверить, запущен ли ваш контейнер, используйте следующую команду:

```bash
docker ps
```
Это выведет список всех запущенных контейнеров. Вы должны увидеть ваш контейнер с его именем и статусом.

## Шаг 6: Доступ к веб-приложению

Откройте веб-браузер и перейдите по адресу `http://localhost:8080/gridjsdemo/index`. Вы должны увидеть ваше приложение запущенным.

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
docker rmi gridjs-demo-java
```




