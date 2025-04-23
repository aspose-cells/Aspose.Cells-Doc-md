---
title: как запустить Aspose.Cells.GridWeb в Dockerе
type: docs
weight: 250
url: /ru/net/aspose-cells-gridweb/how-to-build-online-excel-editor/
keywords: GridWeb, Docker
description: Эта статья вводит в способы запуска GridWeb в Docker для создания онлайн редактора или просмотрщика Excel.
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

Убедитесь, что Docker установлен на вашем компьютере. Вы можете скачать и установить Docker с [официального сайта Docker](https://www.docker.com/get-started).

## Шаг 1: Создайте Dockerfile

Создайте файл с именем `Dockerfile` в вашей папке проекта [директории](https://github.com/aspose-cells/Aspose.Cells-for-.NET/blob/master/Examples_GridWeb/). В `Dockerfile` должны быть инструкции по созданию вашего Docker-образа.

## Шаг 2: Написание Dockerfile для GridWeb

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
Создайте образ Docker: В терминале выполните следующую команду для сборки вашего образа Docker:
```bash
docker build -t gridweb-demo-net6 .
```
вы можете заменить gridweb-demo-net6 на имя, которое вы хотите дать вашему образу Docker.

## Шаг 4: Запуск контейнера Docker
После создания образа, вы можете запустить контейнер с помощью следующей команды:

```bash
docker run -d -p 24262:80 --name gridweb-demo-container  gridweb-demo-net6
```
Объяснение опций команды Docker Run
-d: Запустить контейнер в фоновом режиме (отделенно).
-p 24262:80: Назначьте порт 80 внутри контейнера на порт 24262 на хост-машине.
--name gridweb-demo-container: Назначьте имя контейнеру.

## Шаг 5: Проверка, что контейнер запущен
Чтобы проверить, запущен ли ваш контейнер, используйте следующую команду:

```bash
docker ps
```
Это выведет список всех запущенных контейнеров. Вы должны увидеть ваш контейнер с его именем и статусом.

## Шаг 6: Доступ к веб-приложению

Откройте веб-браузер и перейдите по адресу `http://localhost:24262/`. Вы должны увидеть ваше приложение.

вы увидите общее руководство по разработке для GridWeb 

щелкните [демо](http://localhost:24262/grid/index1 "демо") на странице, чтобы выполнить операцию редактирования файла таблицы.

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
docker rmi gridweb-demo-net6
```




