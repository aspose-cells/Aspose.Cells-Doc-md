---
title: Как запустить Aspose.Cells в Docker
type: docs
description: Запустите Aspose.Cells в контейнере Docker для Linux, Windows Server и любой ОС.
weight: 139
url: /ru/net/how-to-run-aspose-cells-in-docker/
---
Микросервисы в сочетании с контейнеризацией позволяют легко комбинировать технологии. Docker позволяет легко интегрировать функции Aspose.Cells в ваше приложение, независимо от того, какая технология используется в вашем стеке разработки.

Если вы нацелены на микросервисы, или если основная технология в вашем стеке не .NET, C++ или Java, но вам нужна функциональность Aspose.Cells, или если вы уже используете Docker в своем стеке, то вам может быть интересно использовать Aspose.Cells в Docker. контейнер.

## Предпосылки

- Докер должен быть установлен в вашей системе. Чтобы узнать, как установить Docker на Windows или Mac, перейдите по ссылкам в разделе «См. также».

- Также обратите внимание, что Visual Studio 2019, .NET Core 3.1 SDK используется в приведенном ниже примере.


## Hello World Заявление

В этом примере вы создаете простое консольное приложение Hello World, которое делает «Hello World!» документ и сохраняет его во всех поддерживаемых форматах сохранения. Затем приложение можно собрать и запустить в Docker.

### Создание консольного приложения

Чтобы создать программу Hello World, выполните следующие действия:
1. После установки Docker убедитесь, что он использует контейнеры Linux (по умолчанию). При необходимости выберите параметр «Переключиться на контейнеры Linux» в меню «Рабочие столы Docker».
1. В Visual Studio создайте консольное приложение .NET Core.<br>
![дело:изображение_альтернативный_текст](create-a-new-project.png)<br>
1. Установите последнюю версию Aspose.Cells из NuGet. System.Drawing.Common и System.Text.Encoding.CodePages будут установлены как зависимость Aspose.Cells.<br>
![дело:изображение_альтернативный_текст](nuget-aspose-cells.png)<br>
1. Поскольку приложение будет работать в Linux, необходимо установить соответствующие исходные ресурсы Linux. Начните с базового образа dotnet core sdk 3.1 и установите libgdiplus libc6-dev.
1. Когда все необходимые зависимости будут добавлены, напишите простую программу, которая создает «Hello World!» книгу и сохраняет ее во всех поддерживаемых форматах сохранения:<br>
**.NET**<br>
{{< highlight "csharp" >}}
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

Обратите внимание, что папка «TestOut» указана как выходная папка для сохранения выходных документов. При запуске приложения в Docker в эту папку в контейнере будет смонтирована папка на хост-машине. Это позволит вам легко просматривать выходные данные, созданные Aspose.Cells, в контейнере Docker.

### Настройка Dockerfile

Следующим шагом будет создание и настройка Dockerfile.

1. Создайте файл Dockerfile и поместите его рядом с файлом решения вашего приложения. Оставьте это имя файла без расширения (по умолчанию).
1. В Dockerfile укажите:

{{< highlight "plain" >}}
FROM mcr.microsoft.com/dotnet/core/sdk:3.1-buster 
COPY fonts/* /usr/share/fonts/
WORKDIR /app
COPY . ./
RUN apt-get update && \
    apt-get install -y --allow-unauthenticated libgdiplus libc6-dev
RUN dotnet publish "Aspose.Cells.Docker.csproj" -c Release -o /app/publish
ENTRYPOINT ["dotnet", "publish/Aspose.Cells.Docker.dll"]{{< /highlight >}}

Выше приведен простой Dockerfile, который содержит следующие инструкции:

- Образ SDK, который будет использоваться. Вот образ .Net Core SDK 3.1. Docker загрузит его при запуске сборки. Версия SDK указывается в виде тега.
- Установите шрифты, так как образ SDK содержит очень мало шрифтов. Команда копирует файлы шрифтов из локального в образ докера. Убедитесь, что у вас есть локальный каталог «fonts», содержащий все шрифты, которые вам нужно установить. В этом примере локальный каталог «fonts» помещается в тот же каталог, что и Dockerfile.
- Рабочий каталог, указанный в следующей строке.
- Команда скопировать все в контейнер, опубликовать приложение и указать точку входа.
- Команда для установки libgdiplus запускается в контейнере. Это требуется System.Drawing.Common.

### Сборка и запуск приложения в Docker

Теперь приложение можно собрать и запустить в Docker. Откройте вашу любимую командную строку, измените каталог на папку с приложением (папка, в которой находится файл решения и Dockerfile) и выполните следующую команду:

{{< highlight "plain" >}}
docker build -t actest .
{{< /highlight >}}

При первом выполнении этой команды это может занять больше времени, так как Docker необходимо загрузить необходимые образы. После завершения предыдущей команды выполните следующую команду:

{{< highlight "plain" >}}
docker run --mount type=bind,source=C:\Temp,target=/TestOut --rm actest from Docker
{{< /highlight >}}

{{% alert color="primary" %}} 

Обратите внимание на аргумент mount, потому что, как упоминалось ранее, папка на хост-компьютере монтируется в папку контейнера, чтобы легко увидеть результаты выполнения приложения. Пути в Linux чувствительны к регистру.

{{% /alert %}}

## Поддержка изображений Aspose.Cells

- Aspose.Cells for .NET Стандарт не поддерживает EMF и TIFF в Linux.


## Дополнительные примеры

***1. Запустить приложение в Windows Server 2019***

- Докерфайл

{{< highlight "plain" >}}
FROM microsoft/dotnet-framework:4.7.2-sdk-windowsservercore-ltsc2019
WORKDIR /app
COPY . ./
RUN dotnet publish "Aspose.Cells.Docker.csproj" -c Release -o /app/publish
ENTRYPOINT ["dotnet", "publish/Aspose.Cells.Docker.dll"]{{< /highlight >}}

- Собрать образ Docker

{{< highlight "plain" >}}
docker build -t actest .
{{< /highlight >}}

- Запустить образ Docker

{{< highlight "plain" >}}
docker run --mount type=bind,source=C:\Temp,target=c:\TestOut --rm actest from Docker
{{< /highlight >}}


***2. Запустить приложение в Linux***

- Напишите простую программу, которая устанавливает папку шрифта, создает «Hello World!» книгу и сохраняет ее.

{{< highlight "csharp" >}}
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
- Докерфайл

{{< highlight "plain" >}}
FROM mcr.microsoft.com/dotnet/core/sdk:3.1-buster 
WORKDIR /app
COPY . ./
RUN apt-get update && \
    apt-get install -y --allow-unauthenticated libgdiplus libc6-dev
WORKDIR /app
COPY . ./
RUN dotnet publish "Aspose.Cells.Docker.Fonts.csproj" -c Release -o /app/publish
ENTRYPOINT ["dotnet", "publish/Aspose.Cells.Docker.Fonts.dll"]{{< /highlight >}}

- Собрать образ Docker

{{< highlight "plain" >}}
docker build -t actest .
{{< /highlight >}}

- Запустить образ Docker

{{< highlight "plain" >}}
docker run --mount type=bind,source=C:\Windows\Fonts,target=/Fonts  --mount type=bind,source=C:\Temp,target=/TestOut --rm actest from Docker
{{< /highlight >}}


## Смотрите также

- [Установите рабочий стол Docker на Windows.](https://docs.docker.com/docker-for-windows/install/)
- [Установите рабочий стол Docker на Mac](https://docs.docker.com/docker-for-mac/install/)
- [Visual Studio 2019, .NET Core 3.1 SDK](https://docs.microsoft.com/en-us/dotnet/core/install/windows?tabs=netcore31#dependencies)
- [Переключиться на контейнеры Linux](https://docs.docker.com/docker-for-windows/#switch-between-windows-and-linux-containers) вариант
-  Дополнительная информация о[.NET Основной SDK](https://hub.docker.com/_/microsoft-dotnet-sdk)
