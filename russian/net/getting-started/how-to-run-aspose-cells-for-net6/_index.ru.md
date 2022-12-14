---
title: Как запустить Aspose.Cells для .Net6
type: docs
description: Как запустить Aspose.Cells для .Net6
weight: 138
url: /ru/net/how-to-run-aspose-cells-for-net6/
---
## Обзор

 Для платформ .NET6 (или более поздних версий) по сравнению с предыдущими платформами (.netcore31 или более ранними) важным отличием является графическая библиотека.
 В этом официальном[Microsoft Документ](https://learn.microsoft.com/en-gb/dotnet/core/compatibility/core-libraries/6.0/system-drawing-common-windows-only), поясняется, что для .NET6 или более поздних версий графическая библиотека «System.Drawing.Common» будет поддерживаться только на Windows, и даются рекомендации по замене графической библиотеки.

Для продукта Apose.Cells мы провели оценку и завершили миграцию графической библиотеки. Мы используем SkiaSharp вместо System.Drawing.Common в системах, отличных от Windows, как это предлагается в официальной документации Microsoft. Обратите внимание, что это критическое изменение вступит в силу в версии Aspose.Cells 22.10.1 или более поздней версии для .Net6.

Для .netcore31 или более ранних версий для совместимости и стабильности в настоящее время мы по-прежнему используем графическую библиотеку «System.Drawing.Common». Зависимости для .netcore31 или более ранних версий следующие:
- System.Drawing.Common, 4.7.0.
- System.Security.Cryptography.Pkcs, 5.0.1.
- Система.Текст.Кодировка.Кодовые страницы, 4.7.0.

## Запустите Aspose.Cells для .Net6 на Windows.

Сначала вы можете создать приложение .net6 с VS2022, затем вы можете выбрать следующие варианты установки:

### Установить через nuget

1.  Поиск Aspose.Cells из NuGet:[Aspose.Cells for .NET NuGet Пакет](https://www.nuget.org/packages/Aspose.Cells/). 
Вы также можете установить Aspose.Cells из диспетчера пакетов Nuget в VS2022.

2. «SkiaSharp» или «System.Drawing.Common» будут установлены автоматически как зависимость Aspose.Cells 22.10.1 или более поздней версии для платформ .Net6, что зависит от конфигурации «Целевая ОС» в вашем проекте.
- Установите «Целевая ОС» на «Windows» для вашего проекта, вы будете использовать «System.Drawing.Common» в качестве зависимости от вашей системы Windows для проекта .Net6. В этой конфигурации результат отрисовки ближе к .netcore31 или раньше.
**![Конфигурация целевой ОС](TargetOS.png)**
- Установите «Целевая ОС» на «Нет» или другие параметры для вашего проекта, вы будете использовать «SkiaSharp» в качестве зависимости от вашей системы Windows для проекта .Net6. Обратите внимание, что в настоящее время SkiaSharp не поддерживает такие форматы, как EMF, в Windows.

### Установить через msi или DLL

1. [Загрузите Aspose.Cells.msi или DLL](https://releases.aspose.com/cells/net/)

2. Откройте каталог установки или каталог DLL, затем выберите шаг 3 или 4 ниже:

3. найдите подкаталог «net6.0-windows», добавьте в него файл Aspose.Cells.dll к вашему приложению .net6. Вручную добавьте следующие пакеты nuget в ваш проект .net6:
- System.Drawing.Common, 4.7.0.
- Система.Безопасность.Криптография.Pkcs, 6.0.1.
- Система.Текст.Кодировка.Кодовые страницы, 4.7.0.

Таким образом, вы будете использовать «System.Drawing.Common» в качестве зависимости от вашей системы Windows для проекта .Net6. В этой конфигурации результат отрисовки ближе к .netcore31 или раньше.

4. найдите подкаталог «net6.0», добавьте в него Aspose.Cells.dll к вашему приложению .net6. Вручную добавьте следующие пакеты nuget в ваш проект .net6:
- СкиаШарп, 2.88.3.
- Система.Безопасность.Криптография.Pkcs, 6.0.1.
- Система.Текст.Кодировка.Кодовые страницы, 4.7.0.

Таким образом, вы будете использовать «SkiaSharp» в качестве зависимости от вашей системы Windows для проекта .Net6. Обратите внимание, что в настоящее время SkiaSharp не поддерживает такие форматы, как EMF, в Windows.

## Запустите Aspose.Cells для .Net6 в Linux.

Обратитесь к методу установки по телефону Windows, вы можете выбрать SkiaSharp только в качестве зависимости графической библиотеки от системы Linux.

Вам необходимо выполнить следующие дополнительные операции, чтобы обеспечить правильное использование SkiaSharp под Linux:

1. Запустите следующую команду в вашей системе Linux:
```
apt-get update && apt-get install -y libfontconfig1
```
ИЛИ ЖЕ
```
apk update && apk add fontconfig 
```

2. Добавьте пакеты nuget «SkiaSharp.NativeAssets.Linux 2.88.3» в свой проект .net6.

3. Или вы можете добавить пакеты nuget «SkiaSharp.NativeAssets.Linux.NoDependencies 2.88.3» в свой проект .net6 вместо двух шагов, описанных выше.

### Пример Dockerfile для Ubuntu

1. Добавьте пакеты nuget «SkiaSharp.NativeAssets.Linux 2.88.3» в свой проект .net6.

2. Используйте следующий Dockerfile:
{{< highlight "plain" >}}
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
COPY ["Ubuntu_Docker.csproj", "."]RUN dotnet restore "./Ubuntu_Docker.csproj"
COPY . .
WORKDIR "/src/."
RUN dotnet build "Ubuntu_Docker.csproj" -c Release -o /app/build

FROM build AS publish
RUN dotnet publish "Ubuntu_Docker.csproj" -c Release -o /app/publish

FROM base AS final
WORKDIR /app
COPY --from=publish /app/publish .
ENTRYPOINT ["dotnet", "Ubuntu_Docker.dll"]{{< /highlight >}}

### Пример Dockerfile для Alpine

1. Добавьте пакеты nuget «SkiaSharp.NativeAssets.Linux 2.88.3» в свой проект .net6.

2. Используйте следующий Dockerfile:
{{< highlight "plain" >}}
# Alpine 3.16
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
COPY ["Alpine_Docker.csproj", "."]RUN dotnet restore "./Alpine_Docker.csproj"
COPY . .
WORKDIR "/src/."
RUN dotnet build "Alpine_Docker.csproj" -c Release -o /app/build

FROM build AS publish
RUN dotnet publish "Alpine_Docker.csproj" -c Release -o /app/publish

FROM base AS final
WORKDIR /app
COPY --from=publish /app/publish .
ENTRYPOINT ["dotnet", "Alpine_Docker.dll"]{{< /highlight >}}
