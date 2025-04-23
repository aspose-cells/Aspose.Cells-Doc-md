---
title: Как запустить Aspose.Cells в Docker
type: docs
description: "Запустите Aspose.Cells в контейнере Docker для Linux, Windows Server и любой ОС."
weight: 139
url: /ru/net/how-to-run-aspose-cells-in-docker/
---

Микросервисы, в сочетании с контейнеризацией, позволяют легко объединять технологии. Docker позволяет легко интегрировать функциональность Aspose.Cells в ваше приложение, независимо от используемой технологии в вашем стеке разработки.

Если вы планируете использовать микросервисы или основную технологию в вашем стеке не .NET, C++ или Java, но вам нужна функциональность Aspose.Cells, или если вы уже используете Docker в своем стеке, вас может заинтересовать использование Aspose.Cells в контейнере Docker.

## Предварительные требования

- Docker должен быть установлен на вашей системе. Для получения информации о том, как установить Docker в Windows или Mac, обратитесь к ссылкам в разделе 'См. также'.

- Также обратите внимание, что в данном примере используется Visual Studio 2019, .NET Core 3.1 SDK.


## Приложение Hello World

В этом примере вы создаете простое консольное приложение Hello World, которое создает документ 'Hello World!' и сохраняет его во всех поддерживаемых форматах. Затем приложение может быть построено и запущено в Docker.

### Создание консольного приложения

Для создания программы Hello World выполните указанные ниже шаги:
1. После установки Docker убедитесь, что он использует контейнеры Linux (по умолчанию). При необходимости выберите опцию Переключиться на контейнеры Linux из меню Docker Desktop.
1. In Visual Studio, create a .NET Core console application.<br>
![todo:image_alt_text](create-a-new-project.png)<br>
1. Install the latest Aspose.Cells version from NuGet. System.Drawing.Common and System.Text.Encoding.CodePages will be installed as a dependency of Aspose.Cells.<br>
![todo:image_alt_text](nuget-aspose-cells.png)<br>
1. Поскольку приложение будет запускаться в Linux, необходимо установить соответствующие средства разработки для Linux. Начните с образа базового образа dotnet core sdk 3.1 и установите libgdiplus libc6-dev.
1. When all required dependencies are added, write a simple program that creates a “Hello World!” workbook and saves it in all supported save formats:<br>
**.NET**<br>
{{< highlight csharp >}}
using System;
namespace Aspose.Cells.Docker
{
    class Program
    {
        static void Main(string[] args)
        {
            Workbook workbook = new Workbook();
            workbook.Worksheets[0].Cells[0, 0].PutValue("Hello from Aspose.Cells!!!");
            foreach (SaveFormat sf in Enum.GetValues(typeof(SaveFormat)))
            {
                if (sf != SaveFormat.Unknown)
                {
                    try
                    {
                        // The folder specified will be mounted as a volume when run the application in Docker image.
                        var fileName = string.Format("out{0}", FileFormatUtil.SaveFormatToExtension(sf));
                        workbook.Save(fileName, sf);
                        Console.WriteLine("Saving {0}\t\t[OK]", sf);
                    }
                    catch
                    {
                        Console.WriteLine("Saving {0}\t\t[FAILED]", sf);
                    }
                }
            }
        }
    }
}

{{< /highlight >}}

Обратите внимание, что папка "TestOut" указывается как папка для сохранения выходных документов. При запуске приложения в Docker папка на хост-машина будет примонтирована к этой папке в контейнере. Это позволит легко просматривать выходные данные, сгенерированные Aspose.Cells в контейнере Docker.

### Настройка Dockerfile

Следующим шагом является создание и настройка Dockerfile.

1. Создайте Dockerfile и разместите его рядом с файлом решения вашего приложения. Сохраните это имя файла без расширения (по умолчанию).
1. В Dockerfile укажите:

{{< highlight plain >}}
FROM mcr.microsoft.com/dotnet/core/sdk:3.1-buster 
COPY fonts/* /usr/share/fonts/
WORKDIR /app
COPY . ./
RUN apt-get update && \
    apt-get install -y --allow-unauthenticated libgdiplus libc6-dev
RUN dotnet publish "Aspose.Cells.Docker.csproj" -c Release -o /app/publish
ENTRYPOINT ["dotnet", "publish/Aspose.Cells.Docker.dll"]
{{< /highlight >}}

Приведенный выше Dockerfile содержит следующие инструкции:

- Используемый образ SDK. В данном случае это образ .Net Core SDK 3.1. Docker загрузит его при запуске сборки. Версия SDK указана в виде тега.
- Установка шрифтов, потому что образ SDK содержит очень мало шрифтов. Команда копирует файлы шрифтов из локальной директории в образ Docker. Убедитесь, что у вас есть локальная директория "fonts", содержащая все необходимые шрифты для установки. В этом примере локальная директория "fonts" помещена в ту же директорию, что и Dockerfile.
- Рабочий каталог, указанный в следующей строке.
- Команда для копирования всего в контейнер, публикации приложения и указания точки входа.
- Команда для запуска установки libgdiplus в контейнере. Это требуется для System.Drawing.Common.

### Сборка и запуск приложения в Docker

Теперь приложение можно собрать и запустить в Docker. Откройте вашу любимую командную строку, перейдите в каталог с приложением (в каталог, где размещены файл решения и Dockerfile) и выполните следующую команду:

{{< highlight plain >}}
docker build -t actest .
{{< /highlight >}}

При первом выполнении этой команды может потребоваться больше времени, так как Docker должен загрузить необходимые образы. После завершения предыдущей команды выполните следующую:

{{< highlight plain >}}
docker run --mount type=bind,source=C:\Temp,target=/TestOut --rm actest from Docker
{{< /highlight >}}

{{% alert color="primary" %}} 

Обратите внимание на аргумент mount, потому что, как уже упоминалось, папка на хост-машине примонтирована в папку контейнера, чтобы легко увидеть результаты выполнения приложения. Пути в Linux чувствительны к регистру.

{{% /alert %}}

## Изображения, поддерживаемые Aspose.Cells

- Aspose.Cells for .NET Standard не поддерживает EMF и TIFF в Linux.


## Дополнительные примеры

***1. Запустите приложение в Windows Server 2019***

- Dockerfile

{{< highlight plain >}}
FROM microsoft/dotnet-framework:4.7.2-sdk-windowsservercore-ltsc2019
WORKDIR /app
COPY . ./
RUN dotnet publish "Aspose.Cells.Docker.csproj" -c Release -o /app/publish
ENTRYPOINT ["dotnet", "publish/Aspose.Cells.Docker.dll"]
{{< /highlight >}}

- Собрать образ Docker

{{< highlight plain >}}
docker build -t actest .
{{< /highlight >}}

- Запустить образ Docker

{{< highlight plain >}}
docker run --mount type=bind,source=C:\Temp,target=c:\TestOut --rm actest from Docker
{{< /highlight >}}


***2. Запустить приложение в Linux***

- Написать простую программу, которая устанавливает папку шрифтов, создает книгу "Hello World!" и сохраняет ее.

{{< highlight csharp >}}
namespace Aspose.Cells.Docker.Fonts
{
    using System;
    using System.IO;

    class Program
    {
        static void Main(string[] args)
        {
            try
            {
                // Set font folders on linux.
                string[] fonts = { "/Fonts" };
                FontConfigs.SetFontFolders(fonts, true);
                // build workbook
                Workbook workbook = new Workbook();
                MemoryStream memoryStream = new MemoryStream();
                workbook.Worksheets[0].Cells[0, 0].PutValue("Hello from Aspose.Cells!!!");
                Style style = workbook.CreateStyle();
                style.Font.Name = "Arial";
                style.Font.Size = 16;
                workbook.Worksheets[0].Cells[0, 0].SetStyle(style);
                workbook.Save("/TestOut/TestFontsOut.xlsx");
            }
            catch (Exception e)
            {
                Console.WriteLine("Saving outfonts.xlsx\t\t[FAILED],{0}", e.Message);
            }

        }
    }
}

{{< /highlight >}}
- Dockerfile

{{< highlight plain >}}
FROM mcr.microsoft.com/dotnet/core/sdk:3.1-buster 
WORKDIR /app
COPY . ./
RUN apt-get update && \
    apt-get install -y --allow-unauthenticated libgdiplus libc6-dev
WORKDIR /app
COPY . ./
RUN dotnet publish "Aspose.Cells.Docker.Fonts.csproj" -c Release -o /app/publish
ENTRYPOINT ["dotnet", "publish/Aspose.Cells.Docker.Fonts.dll"]
{{< /highlight >}}

- Собрать образ Docker

{{< highlight plain >}}
docker build -t actest .
{{< /highlight >}}

- Запустить образ Docker

{{< highlight plain >}}
docker run --mount type=bind,source=C:\Windows\Fonts,target=/Fonts  --mount type=bind,source=C:\Temp,target=/TestOut --rm actest from Docker
{{< /highlight >}}


## См. также

- [Установите Docker Desktop на Windows](https://docs.docker.com/docker-for-windows/install/)
- [Установите Docker Desktop на Mac](https://docs.docker.com/docker-for-mac/install/)
- [Visual Studio 2019, .NET Core 3.1 SDK](https://docs.microsoft.com/en-us/dotnet/core/install/windows?tabs=netcore31#dependencies)
- [Переключитесь на контейнеры Linux](https://docs.docker.com/docker-for-windows/#switch-between-windows-and-linux-containers) параметр
- Дополнительная информация о [.NET Core SDK](https://hub.docker.com/_/microsoft-dotnet-sdk)
{{< app/cells/assistant language="csharp" >}}
