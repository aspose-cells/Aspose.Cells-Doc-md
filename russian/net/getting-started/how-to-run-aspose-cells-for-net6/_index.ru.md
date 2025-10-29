---
title: Как запустить Aspose.Cells для .Net6
type: docs
description: «Как запустить Aspose.Cells для .Net6.»
weight: 138
url: /ru/net/how-to-run-aspose-cells-for-net6/
---

## Обзор

Для платформ .NET6 (или позднее) основное отличие по сравнению с предыдущими платформами (.netcore31 или ранее) заключается в графической библиотеке. 
В этом официальном [документе Microsoft](https://learn.microsoft.com/en-gb/dotnet/core/compatibility/core-libraries/6.0/system-drawing-common-windows-only) объясняется, что для .NET6 или более поздних релизов графическая библиотека "System.Drawing.Common" будет поддерживаться только в Windows и даются рекомендации по замене графической библиотеки.

Для продукта Apose.Cells мы провели оценку и завершили миграцию графической библиотеки. Мы используем SkiaSharp вместо System.Drawing.Common в системах, отличных от Windows, как предложено в официальной документации от Microsoft. Обратите внимание, что это важное изменение начнет действовать в Aspose.Cells 22.10.1 или более поздних версиях для .Net6.

Для .netcore31 или ранее, для совместимости и стабильности в настоящее время мы все еще используем графическую библиотеку "System.Drawing.Common". Зависимости для .netcore31 или ранее следующие:
- System.Drawing.Common, 5.0.3.
- System.Security.Cryptography.Pkcs, 6.0.5.
- System.Text.Encoding.CodePages, 4.7.0.

## Запуск Aspose.Cells для .Net6 (или новее) на Windows

Сначала вы можете создать приложение .net6 (или новее) с помощью VS2022, затем выбрать следующие параметры установки:

### Установка через NuGet

1. Поиск Aspose.Cells в NuGet: [Aspose.Cells for .NET Набор NuGet](https://www.nuget.org/packages/Aspose.Cells/). 
Вы также можете установить Aspose.Cells через менеджер пакетов NuGet в VS2022.

2. "SkiaSharp" или "System.Drawing.Common" будут установлены автоматически как зависимость Aspose.Cells 22.10.1 или более новой для платформ .Net6 (или новее), которые зависят от конфигурации "Target OS" в вашем проекте.
- Установите "Target OS" как "Windows" для вашего проекта, вы будете использовать "System.Drawing.Common" как зависимость в вашей системе Windows для проекта .Net6 (или новее). В этой конфигурации результат рисования ближе к .netcore31 или раньше.
**![Настройка целевой ОС](TargetOS.png)**
- Установите "Target OS" как "None" или другие параметры для вашего проекта, вы будете использовать "SkiaSharp" как зависимость в вашей системе Windows для проекта .Net6 (или новее). *Обратите внимание, что версия, использующая "SkiaSharp" как зависимость, не поддерживает функцию печати на принтер.*

### Установка через msi или DLL

1. [Загрузить Aspose.Cells.msi или DLL](https://releases.aspose.com/cells/net/)

2. Откройте директорию установки или директорию DLL, затем выберите шаг 3 или 4 ниже:

3. Найдите подкаталог "net6.0-windows", добавьте Aspose.Cells.dll в него в ваше приложение .net6. Вручную добавьте следующие пакеты NuGet в ваш проект .net6:
- System.Drawing.Common, 6.0.0.
- System.Security.Cryptography.Pkcs, 6.0.5.
- System.Text.Encoding.CodePages, 4.7.0.

Таким образом, вы будете использовать "System.Drawing.Common" как зависимость в вашей системе Windows для проекта .Net6 (или новее). В этой конфигурации результат рисования ближе к .netcore31 или раньше.

4. Найдите подкаталог "net6.0", добавьте Aspose.Cells.dll в него в ваше приложение .net6. Вручную добавьте следующие пакеты NuGet в ваш проект .net6:
- SkiaSharp, 3.116.1.
- System.Security.Cryptography.Pkcs, 6.0.5.
- System.Text.Encoding.CodePages, 4.7.0.

Таким образом, вы будете использовать "SkiaSharp" как зависимость в вашей системе Windows для проекта .Net6 (или новее). *Обратите внимание, что версия, использующая "SkiaSharp" как зависимость, не поддерживает функцию печати на принтер.*

## Запуск Aspose.Cells для Linux

Ссылка на метод установки в Windows, вы можете выбрать только SkiaSharp в качестве зависимости графической библиотеки в системе Linux.

Вам нужно выполнить следующие дополнительные операции, чтобы обеспечить правильное использование SkiaSharp в Linux:

1. Выполните следующую команду в вашей системе Linux:
```
apt-get update && apt-get install -y libfontconfig1
```
ИЛИ
```
apk update && apk add fontconfig 
```

2. Добавьте пакет nuget "SkiaSharp.NativeAssets.Linux 3.116.1" в ваш проект .net6 (или новее).
3. Или можете выбрать добавление пакета nuget "SkiaSharp.NativeAssets.Linux.NoDependencies 3.116.1" в ваш проект .net6 (или новее), вместо двух шагов выше.

*Обратите внимание, что версия добавляемого пакета "SkiaSharp.NativeAssets.Linux" или "SkiaSharp.NativeAssets.Linux.NoDependencies" должна соответствовать версии "SkiaSharp", указанной в Aspose.Cells for .NET. Варианты версий Aspose.Cells for .NET и связанные с ними версии "SKiaSharp" представлены ниже:*

| Aspose.Cells for .NET  |                SkiaSharp                |
| :--------------------: | :-------------------------------------: |
| >= 22.10.1 && <= 22.11 |                 2.88.0                  |
|  >= 22.12 && <= 23.9   |                 2.88.3                  |
|  >= 23.10 && <= 24.12  |                 2.88.6                  |
|        = 25.1.1        |                 3.116.1                 |
|        >=25.1.2        | 2.88.9 (net6.0, net8.0), 3.116.1 (net9.0) |



### Пример Dockerfile для Ubuntu

1. Добавьте пакет nuget "SkiaSharp.NativeAssets.Linux 3.116.1" в ваш проект .net6 (или новее).

2. Используйте следующий Dockerfile:
{{< highlight plain >}}
# Ubuntu 20.04
FROM mcr.microsoft.com/dotnet/runtime:6.0-focal AS base
WORKDIR /app

# add "libfontconfig1" package if using "SkiaSharp.NativeAssets.Linux" in your project
# Or you need to use "SkiaSharp.NativeAssets.Linux.NoDependencies" in your project
RUN apt-get update && apt-get install -y libfontconfig1

# Copy fonts from local to docker
# For example, put a "fonts" folder in your project folder, and put the font files in it,
# then, use the following line:
COPY fonts/ /usr/share/fonts

FROM mcr.microsoft.com/dotnet/sdk:6.0-focal AS build
WORKDIR /src
COPY ["Ubuntu_Docker.csproj", "."]
RUN dotnet restore "./Ubuntu_Docker.csproj"
COPY . .
WORKDIR "/src/."
RUN dotnet build "Ubuntu_Docker.csproj" -c Release -o /app/build

FROM build AS publish
RUN dotnet publish "Ubuntu_Docker.csproj" -c Release -o /app/publish

FROM base AS final
WORKDIR /app
COPY --from=publish /app/publish .
ENTRYPOINT ["dotnet", "Ubuntu_Docker.dll"]
{{< /highlight >}}

### Пример Dockerfile для Alpine

1. Добавьте пакет nuget "SkiaSharp.NativeAssets.Linux 3.116.1" в ваш проект .net6 (или новее).

2. Используйте следующий Dockerfile:
{{< highlight plain >}}
#Alpine 3.16
FROM mcr.microsoft.com/dotnet/runtime:6.0-alpine3.16 AS base
WORKDIR /app

# add "fontconfig" package if using "SkiaSharp.NativeAssets.Linux" in your project
# Or you need to use "SkiaSharp.NativeAssets.Linux.NoDependencies" in your project
RUN apk update && apk add fontconfig 

# Copy fonts from local to docker
# For example, put a "fonts" folder in your project folder, and put the font files in it,
# then, use the following line:
COPY fonts/ /usr/share/fonts

FROM mcr.microsoft.com/dotnet/sdk:6.0-alpine3.16 AS build
WORKDIR /src
COPY ["Alpine_Docker.csproj", "."]
RUN dotnet restore "./Alpine_Docker.csproj"
COPY . .
WORKDIR "/src/."
RUN dotnet build "Alpine_Docker.csproj" -c Release -o /app/build

FROM build AS publish
RUN dotnet publish "Alpine_Docker.csproj" -c Release -o /app/publish

FROM base AS final
WORKDIR /app
COPY --from=publish /app/publish .
ENTRYPOINT ["dotnet", "Alpine_Docker.dll"]
{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
