---
title: как запустить Aspose.Cells.GridWeb в docker
type: docs
weight: 250
url: /ru/net/aspose-cells-gridweb/how-to-build-online-excel-editor/
keywords: GridWeb, docker
description: Эта статья представляет, как запустить GridWeb в Docker для создания приложения для редактирования или просмотра таблиц Excel онлайн.
aliases:
  - /net/aspose-cells-gridweb/docker/
  - /net/aspose-cells-gridweb/run-aspose-cells-gridweb-in-docker/
  - /net/aspose-cells-gridweb/run-gridweb-in-docker/
  - /net/aspose-cells-gridweb/how-to-build-online-excel-editor-using-gridweb/
  - /net/aspose-cells-gridweb/how-to-build-web-spreadsheet-editor-using-gridweb/
  - /net/aspose-cells-gridweb/how-to-build-web-excel-editor-using-gridweb/
  - /net/aspose-cells-gridweb/how-to-build-online-excel-viewer-using-gridweb/
  - /net/aspose-cells-gridweb/how-to-build-web-spreadsheet-viewer-using-gridweb/
  - /net/aspose-cells-gridweb/how-to-build-web-excel-viewer-using-gridweb/
---

# Руководство по Docker

## Предварительные требования

Убедитесь, что у вас установлен Docker на вашем компьютере. Вы можете скачать и установить Docker с [официального сайта Docker](https://www.docker.com/get-started).

## Шаг 1: Создайте Dockerfile

Создайте файл с именем `Dockerfile` в вашем проекте [directory](https://github.com/aspose-cells/Aspose.Cells-for-.NET/blob/master/Examples_GridWeb/). Файл `Dockerfile` должен содержать инструкции о том, как собрать образ Docker.

## Шаг 2: Написать Dockerfile для GridWeb

Вот пример [`Dockerfile`](https://github.com/aspose-cells/Aspose.Cells-for-.NET/blob/master/Examples_GridWeb/Dockerfile) для демонстрации GridWeb с приложением ASP.NET Core:

```dockerfile
# Use the official .NET6.0 runtime as a parent image
FROM mcr.microsoft.com/dotnet/aspnet:6.0-focal AS base
WORKDIR /app  
EXPOSE 80 


# Use the official .NET6.0 SDK as build enviroment
FROM mcr.microsoft.com/dotnet/sdk:6.0-focal AS build

WORKDIR /src  
#we shall use .net6.0 project
COPY ["GridWeb.Demo.NET6.0.csproj", "."]
RUN dotnet restore "./GridWeb.Demo.NET6.0.csproj"

# Copy everything else and build
COPY . .
WORKDIR "/src/."
RUN dotnet build "GridWeb.Demo.NET6.0.csproj" -c Release -o /app/build

# Publish the app
FROM build AS publish
RUN dotnet publish "GridWeb.Demo.NET6.0.csproj" -c Release -o /app/publish

# Final stage/image
FROM base AS final
WORKDIR /app
# if you want display better like in windows ,you need to install kinds of fonts in /usr/share/fonts/ 
# then the application can parse and render the fonts which is used in the spread sheet file
# here we don't provide extra fonts resource
# Install Fonts because the SDK image contains very few fonts. The command copies font files from local to docker image. Make sure you have a local “fonts” directory that contains all the fonts you need to install. In this example, the local “fonts” directory is put in the same directory as the Dockerfile.
# COPY fonts/* /usr/share/fonts/
# the basic file path which contains the spread sheet files 
RUN mkdir -p /app/wb
# the cache file path for GridWeb
RUN mkdir -p /app/filecache
# the cache picture path for GridWeb
RUN mkdir -p /app/piccache
COPY wwwroot/wb/*.xlsx /app/wb/

COPY --from=publish /app/publish .

# set the start command for the docker image 
ENTRYPOINT ["dotnet", "GridWeb.Demo.NET6.0.dll"]
```

## Шаг 3: Создание образа Docker
Создайте образ Docker: Из терминала выполните следующую команду для создания образа Docker:
```bash
docker build -t gridweb-demo-net6 .
```
Вы можете заменить gridweb-demo-net6 на имя, которое вы хотите дать своему образу Docker.

## Шаг 4: Запуск контейнера Docker
После построения образа вы можете запустить контейнер с помощью следующей команды:

```bash
docker run -d -p 24262:80 --name gridweb-demo-container  gridweb-demo-net6
```
Объяснение опций команды Docker Run
-d: Запустить контейнер в отсоединенном режиме (в фоновом режиме).
-p 24262:80: Сопоставьте порт 80 в контейнере с портом 24262 на хост-машине.
--name gridweb-demo-container: Назначить имя контейнеру.

## Шаг 5: Проверка работы контейнера
Чтобы проверить работу вашего контейнера, используйте следующую команду:

```bash
docker ps
```
Это перечислит все работающие контейнеры. Вы увидите в списке ваш контейнер вместе с его названием и статусом.

## Шаг 6: Доступ к веб-приложению

Откройте веб-браузер и перейдите по адресу `http://localhost:24262/`. Вы должны увидеть работающее приложение.

Вы увидите общее руководство разработчика для GridWeb 

нажмите [демо](http://localhost:24262/grid/index1 "demo") на странице, чтобы редактировать файл таблицы.

## Дополнительные команды

### Остановка контейнера

Чтобы остановить запущенный контейнер, используйте следующую команду:

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
docker rmi gridweb-demo-net6
```




