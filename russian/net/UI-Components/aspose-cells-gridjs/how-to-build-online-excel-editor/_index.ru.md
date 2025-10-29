---
title: как запустить Aspose.Cells.GridJs в Docker
type: docs
weight: 250
url: /ru/net/aspose-cells-gridjs/how-to-build-online-excel-editor/
keywords: GridJs, Docker
description: Эта статья описывает, как запускать GridJs в Docker для создания онлайн редактора или просмотрщика Excel.
aliases:
  - /net/aspose-cells-gridjs/docker/
  - /net/aspose-cells-gridjs/run-aspose-cells-gridjs-in-docker/
  - /net/aspose-cells-gridjs/run-gridjs-in-docker/
  - /net/aspose-cells-gridjs/how-to-build-online-excel-editor-using-gridjs/
  - /net/aspose-cells-gridjs/how-to-build-web-spreadsheet-editor-using-gridjs/
  - /net/aspose-cells-gridjs/how-to-build-web-excel-editor-using-gridjs/
  - /net/aspose-cells-gridjs/how-to-build-online-excel-viewer-using-gridjs/
  - /net/aspose-cells-gridjs/how-to-build-web-spreadsheet-viewer-using-gridjs/
  - /net/aspose-cells-gridjs/how-to-build-web-excel-viewer-using-gridjs/
---

# Руководство по Docker

## Предварительные требования

Убедитесь, что Docker установлен на вашем компьютере. Вы можете скачать и установить Docker с [официального сайта Docker](https://www.docker.com/get-started).

## Шаг 1: Создайте Dockerfile

Создайте файл с именем `Dockerfile` в вашей папке проекта [каталоге](https://github.com/aspose-cells/Aspose.Cells.Grid-for-.NET/blob/master/Examples_GridJs/). В `Dockerfile` должны быть инструкции о том, как создать образ Docker.

## Шаг 2: Напишите Dockerfile для GridJs

Вот пример [`Dockerfile`](https://github.com/aspose-cells/Aspose.Cells.Grid-for-.NET/blob/master/Examples_GridJs/Dockerfile) для демонстрации GridJs с приложением ASP.NET Core:

```dockerfile
# Use the official .NET6.0 runtime as a parent image
FROM mcr.microsoft.com/dotnet/aspnet:6.0-focal AS base
WORKDIR /app  
EXPOSE 80 


# Use the official .NET6.0 SDK as build enviroment
FROM mcr.microsoft.com/dotnet/sdk:6.0-focal AS build

WORKDIR /src  
#we shall use .net6.0 project
COPY ["gridjs-demo-.net6.csproj", "."]
RUN dotnet restore "./gridjs-demo-.net6.csproj"

# Copy everything else and build
COPY . .
WORKDIR "/src/."
RUN dotnet build "gridjs-demo-.net6.csproj" -c Release -o /app/build

# Publish the app
FROM build AS publish
RUN dotnet publish "gridjs-demo-.net6.csproj" -c Release -o /app/publish

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
# the file path to store the uploaded files
RUN mkdir -p /app/uploads
# the cache file path for GridJs
RUN mkdir -p /app/grid_cache
# we provide some sample spread sheet files in demo 
COPY wb/*.xlsx /app/wb/

COPY --from=publish /app/publish .

# set the start command for the docker image 
ENTRYPOINT ["dotnet", "gridjs-demo-.net6.dll"]
```

## Шаг 3: Создание образа Docker
Создайте образ Docker: В терминале выполните следующую команду для сборки вашего образа Docker:
```bash
docker build -t gridjs-demo-net6 .
```
вы можете заменить gridjs-demo-net6 на имя, которое хотите присвоить вашему Docker-образу.

## Шаг 4: Запуск контейнера Docker
После создания образа, вы можете запустить контейнер с помощью следующей команды:

```bash
docker run -d -p 24262:80 -v C:/path/to/license.txt:/app/license --name gridjs-demo-container  gridjs-demo-net6
```

или просто запустите демонстрацию в режиме пробного использования:


```bash
docker run -d -p 24262:80 --name gridjs-demo-container  gridjs-demo-net6
```


Объяснение опций команды Docker Run
-d: Запустить контейнер в фоновом режиме (отделенно).
-p 24262:80: Назначьте порт 80 внутри контейнера на порт 24262 на хост-машине.
-v C:/path/to/license.txt:/app/license: Привязка файла лицензии с хост-машины внутри контейнера.
--name gridjs-demo-container: Назначить имя контейнеру.

## Шаг 5: Проверка, что контейнер запущен
Чтобы проверить, запущен ли ваш контейнер, используйте следующую команду:

```bash
docker ps
```
Это выведет список всех запущенных контейнеров. Вы должны увидеть ваш контейнер с его именем и статусом.

## Шаг 6: Доступ к веб-приложению

Откройте веб-браузер и перейдите по адресу `http://localhost:24262/GridJs2/List`. Вы должны увидеть ваше приложение в работе.

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
docker rmi gridjs-demo-net6
```




