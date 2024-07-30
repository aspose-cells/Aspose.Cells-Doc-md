---
title: как запустить Aspose.Cells.GridJs в docker
type: docs
weight: 250
url: /ru/java/aspose-cells-gridjs/how-to-build-online-excel-editor/
keywords: GridJs, docker
description: Эта статья расскажет, как запустить GridJs в docker для создания онлайн приложения для редактирования или просмотра excel файлов.
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

Убедитесь, что у вас установлен Docker на вашем компьютере. Вы можете скачать и установить Docker с [официального сайта Docker](https://www.docker.com/get-started).

## Шаг 1: Создайте Dockerfile

Создайте файл `Dockerfile` в вашем проекте [directory](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Examples.GridJs). `Dockerfile` должен содержать инструкции о том, как создать ваш образ Docker.

## Шаг 2: Написать Dockerfile для GridJs

Вот пример [`Dockerfile`](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Examples.GridJs/Dockerfile) для демонстрации GridJs с java-приложением:

```dockerfile
# Use the jdk8 image
FROM eclipse/ubuntu_jdk8
WORKDIR /usr/src/app


# copy local Maven files to container
COPY mvnw .
COPY .mvn .mvn
COPY pom.xml .
COPY src src

# build application with maven
RUN ./mvnw package -DskipTests

# Set the user
USER root

#RUN ls -l *

# copy the build output jar to container
COPY  target/*.jar /app/app.jar

# delete build source to reduce storage usage
RUN rm -rf target && rm -rf .mvn && rm -rf src
# web port
EXPOSE 8080
# if you want display better like in windows ,you need to install kinds of fonts in /usr/share/fonts/ 
# then the application can parse and render the fonts which is used in the spread sheet file
# here we don't provide extra fonts resource
# Install Fonts because the SDK image contains very few fonts. The command copies font files from local to docker image. Make sure you have a local “fonts” directory that contains all the fonts you need to install. In this example, the local “fonts” directory is put in the same directory as the Dockerfile.
# COPY fonts/* /usr/share/fonts/
# the basic file path which contains the spread sheet files 
RUN mkdir -p /app/wb
# the cache file path for GridJs
RUN mkdir -p /app/grid_cache/streamcache
# we provide some sample spread sheet files in demo 
COPY wb/*.xlsx /app/wb/

# set the start command for the docker image 
ENTRYPOINT ["java","-Djava.security.egd=file:/dev/./urandom","-jar","/app/app.jar"]
```

## Шаг 3: Создание образа Docker
Создайте образ Docker: Из терминала выполните следующую команду для создания образа Docker:
```bash
docker build -t gridjs-demo-java .
```
вы можете заменить gridjs-demo-java на название, которое вы хотите дать вашему образу Docker.

## Шаг 4: Запуск контейнера Docker
После построения образа вы можете запустить контейнер с помощью следующей команды:

```bash
docker run -d -p 8080:80 --name gridjs-demo-container  gridjs-demo-java
```
Объяснение опций команды Docker Run
-d: Запустить контейнер в отсоединенном режиме (в фоновом режиме).
-p 8080:80: Сопоставление порта 80 в контейнере с портом 8080 на рабочей машине.
--name gridjs-demo-container: Присвоить имя контейнеру.

## Шаг 5: Проверка работы контейнера
Чтобы проверить работу вашего контейнера, используйте следующую команду:

```bash
docker ps
```
Это перечислит все работающие контейнеры. Вы увидите в списке ваш контейнер вместе с его названием и статусом.

## Шаг 6: Доступ к веб-приложению

Откройте веб-браузер и перейдите по адресу `http://localhost:8080/gridjsdemo/index`. Вы увидите, что ваше приложение работает.

## Дополнительные команды

### Остановка контейнера

Чтобы остановить запущенный контейнер, используйте следующую команду:

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




