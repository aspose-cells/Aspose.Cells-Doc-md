---
title: как запустить Aspose.Cells.GridWeb для создания онлайн редактора или просмотрщика таблиц в Docker
type: docs
weight: 250
url: /ru/java/aspose-cells-gridweb/how-to-build-online-excel-editor/
keywords: GridWeb, Docker
description: Эта статья вводит в способы запуска GridWeb в Docker для создания онлайн редактора или просмотрщика Excel.
aliases:
  - /java/aspose-cells-gridweb/docker/
  - /java/aspose-cells-gridweb/run-aspose-cells-gridweb-in-docker/
  - /java/aspose-cells-gridweb/run-gridweb-in-docker/
  - /java/aspose-cells-gridweb/how-to-build-online-excel-editor-using-gridweb/
  - /java/aspose-cells-gridweb/how-to-build-web-spreadsheet-editor-using-gridweb/
  - /java/aspose-cells-gridweb/how-to-build-web-excel-editor-using-gridweb/
  - /java/aspose-cells-gridweb/how-to-build-online-excel-viewer-using-gridweb/
  - /java/aspose-cells-gridweb/how-to-build-web-spreadsheet-viewer-using-gridweb/
  - /java/aspose-cells-gridweb/how-to-build-web-excel-viewer-using-gridweb/
---

# Руководство по Docker

## Предварительные требования

Убедитесь, что Docker установлен на вашем компьютере. Вы можете скачать и установить Docker с [официального сайта Docker](https://www.docker.com/get-started).

## Шаг 1: Создайте Dockerfile

Создайте файл с именем `Dockerfile` в вашей [директории](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Examples.GridWeb/springboot3.3demo/). `Dockerfile` должен содержать инструкции о том, как создать образ Docker.

## Шаг 2: Написание Dockerfile для GridWeb

Вот пример [`Dockerfile`](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Examples.GridWeb/springboot3.3demo/Dockerfile) для демонстрации GridWeb с Java-приложением:

```dockerfile
#spring boot3.3 shall use jdk17 above 
FROM openjdk:17-jdk-slim  AS build

# set work dir
WORKDIR /usr/src/app

# copy with maven
COPY mvnw .
COPY .mvn .mvn
COPY pom.xml .
COPY src src

RUN chmod +x mvnw
# build with maven
RUN ./mvnw package -DskipTests


RUN ls -l target

# Stage 2: Create the final image
FROM openjdk:17-jdk-slim

# Set the working directory in the container
WORKDIR /app

# Copy the built JAR file from the build stage
COPY --from=build /usr/src/app/target/*.jar /app/app.jar

# web port
EXPOSE 8080
# Install Fonts because the SDK image contains very few fonts. The command copies font files from local to docker image. Make sure you have a local “fonts” directory that contains all the fonts you need to install. In this example, the local “fonts” directory is put in the same directory as the Dockerfile.
# COPY fonts/* /usr/share/fonts/

# Install necessary dependencies for font management,because we use jdk-slim ,we need to install it
RUN apt-get update && apt-get install -y fontconfig libfreetype6 && rm -rf /var/lib/apt/lists/*

# Set the environment variable for headless mode,no need to use display
ENV JAVA_OPTS="-Djava.awt.headless=true"
# create [log dir](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Examples.GridWeb/springboot3.3demo/src/main/resources/application.properties)
RUN mkdir -p /app/log
# create [cache dir](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Examples.GridWeb/springboot3.3demo/src/main/resources/application.properties)
RUN mkdir -p /app/grid_cache

# RUN ls -l /app/
# run java application
CMD ["sh", "-c", "java $JAVA_OPTS -jar /app/app.jar"]

```

## Шаг 3: Создание образа Docker
Создайте образ Docker: В терминале выполните следующую команду для сборки вашего образа Docker:
```bash
docker build -t gridweb-demo-java .
```
вы можете заменить gridweb-demo-java на название, которое хотите дать вашему образу Docker.

## Шаг 4: Запуск контейнера Docker
После создания образа, вы можете запустить контейнер с помощью следующей команды:

```bash
docker run -d -p 8080:8080 --name gridweb-demo-container  gridweb-demo-java
```
Объяснение опций команды Docker Run
-d: Запустить контейнер в фоновом режиме (отделенно).
-p 8080:8080: сопоставить порт 8080 в контейнере с портом 8080 на хосте.
--name gridweb-demo-container: Назначьте имя контейнеру.

## Шаг 5: Проверка, что контейнер запущен
Чтобы проверить, запущен ли ваш контейнер, используйте следующую команду:

```bash
docker ps
```
Это выведет список всех запущенных контейнеров. Вы должны увидеть ваш контейнер с его именем и статусом.

## Шаг 6: Доступ к веб-приложению

Откройте веб-браузер и перейдите по адресу `http://localhost:8080/gridwebdemo/index`. Вы должны увидеть ваше приложение, запущенным.



## Дополнительные команды

### Остановка контейнера

Для остановки запущенного контейнера используйте следующую команду:

```bash
docker stop gridweb-demo-container
```

### Удаление контейнера
Чтобы удалить остановленный контейнер, используйте следующую команду:

```bash
docker rm  gridweb-demo-container
```

### Удаление образа
Чтобы удалить образ, используйте следующую команду:

```bash
docker rmi gridweb-demo-java
```




