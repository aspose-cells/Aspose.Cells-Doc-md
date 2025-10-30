---
title: Hur man kör Aspose.Cells i Docker
type: docs
description: Kör Aspose.Cells i en Docker container för Linux, Windows Server och vilket som helst operativsystem.
weight: 139
url: /sv/net/how-to-run-aspose-cells-in-docker/
---

Microservices, i kombination med containerisering, gör det möjligt att enkelt kombinera teknologier. Docker gör det möjligt att enkelt integrera Aspose.Cells-funktionalitet i din applikation, oavsett vilken teknik som finns i din utvecklingsstack.

Om du riktar in dig på mikrotjänster eller om huvudtekniken i din stack inte är .NET, C++ eller Java, men du behöver funktionaliteten i Aspose.Cells, eller om du redan använder Docker i din stack, kan du vara intresserad av att använda Aspose.Cells i en Docker-container.

## Förutsättningar

- Docker måste vara installerat på ditt system. För information om hur man installerar Docker på Windows eller Mac, hänvisas till länkarna i avsnittet "Se även".

- Observera också att Visual Studio 2019, .NET Core 3.1 SDK används i exemplet som anges nedan.


## Hello World-applikation

I det här exemplet skapar du en enkel Hello World-konsolapplikation som skapar en ”Hello World!”-dokument och sparar den i alla stödda spara format. Applikationen kan sedan byggas och köras i Docker.

### Skapande av konsolapplikationen

För att skapa Hello World-programmet, följ stegen nedan:
1. När Docker är installerat, se till att det använder Linux-containers (standard). Om det behövs, välj alternativet Växla till Linux-containers från Docker Desktops meny.
1. In Visual Studio, create a .NET Core console application.<br>
![todo:image_alt_text](create-a-new-project.png)<br>
1. Install the latest Aspose.Cells version from NuGet. System.Drawing.Common and System.Text.Encoding.CodePages will be installed as a dependency of Aspose.Cells.<br>
![todo:image_alt_text](nuget-aspose-cells.png)<br>
1. Eftersom programmet kommer att köras på Linux måste de lämpliga nativa Linux-resurserna installeras. Börja med dotnet core sdk 3.1-basbilden och installera libgdiplus libc6-dev.
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

Observera att mappen "TestOut" anges som en utmatningsmapp för att spara utmatningsdokument. När programmet körs i Docker kommer en mapp på värdmaskinen att monteras till denna mapp i containern. Detta gör att du enkelt kan visa utmatningen genererad av Aspose.Cells i Dockercontainern.

### Konfigurering av en Dockerfil

Nästa steg är att skapa och konfigurera Dockerfilen.

1. Skapa Dockerfilen och placera den bredvid lösningen för din applikation. Behåll filnamnet utan tillägg (standard).
1. I Dockerfilen, ange:

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

Ovan är en enkel Dockerfil som innehåller följande instruktioner:

- Den SDK-bild som ska användas. Här är det .Net Core SDK 3.1-bilden. Docker kommer att ladda ner den när byggnaden körs. Versionen av SDK anges som en tagg.
- Installera typsnitt eftersom SDK-bilden innehåller väldigt få typsnitt. Kommandot kopierar typsnittsfilerna från lokal till docker-bilden. Se till att du har en lokal "typsnitt"-mapp som innehåller alla typsnitt du behöver installera. I det här exemplet placeras den lokala "typsnitt"-mappen i samma mapp som Dockerfilen.
- Arbetskatalogen som anges i nästa rad.
- Kommandot för att kopiera allt till containern, publicera applikationen och ange ingångspunkten.
- Kommandot för att installera libgdiplus körs i containern. Detta krävs av System.Drawing.Common.

### Bygga och köra applikationen i Docker

Nu kan programmet byggas och köras i Docker. Öppna din favoritkommandorad, byt katalog till mappen med applikationen (mapp där lösningen och Dockerfilen är placerade) och kör följande kommando:

{{< highlight plain >}}
docker build -t actest .
{{< /highlight >}}

Första gången detta kommando körs kan det ta längre tid eftersom Docker behöver ladda ner de nödvändiga bilderna. När det föregående kommandot har utförts kör följande kommando:

{{< highlight plain >}}
docker run --mount type=bind,source=C:\Temp,target=/TestOut --rm actest from Docker
{{< /highlight >}}

{{% alert color="primary" %}} 

Observera monteringsargumentet, eftersom en mapp på värdmaskinen monteras in i containerns mapp, för att enkelt kunna se resultaten av programkörningen. Sökvägar i Linux skiftlägeskänsliga.

{{% /alert %}}

## Bilder som stöder Aspose.Cells

- Aspose.Cells for .NET Standard stöder inte EMF och TIFF på Linux.


## Fler exempel

***1. För att köra applikationen i Windows Server 2019***

- Dockerfile

{{< highlight plain >}}
FROM microsoft/dotnet-framework:4.7.2-sdk-windowsservercore-ltsc2019
WORKDIR /app
COPY . ./
RUN dotnet publish "Aspose.Cells.Docker.csproj" -c Release -o /app/publish
ENTRYPOINT ["dotnet", "publish/Aspose.Cells.Docker.dll"]
{{< /highlight >}}

- Bygg Docker Image

{{< highlight plain >}}
docker build -t actest .
{{< /highlight >}}

- Kör Docker Image

{{< highlight plain >}}
docker run --mount type=bind,source=C:\Temp,target=c:\TestOut --rm actest from Docker
{{< /highlight >}}


***2. För att köra applikationen i Linux***

- Skriv ett enkelt program som anger typsnittsmappen, skapar en "Hello World!"-arbetsbok och sparar den.

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

- Bygg Docker Image

{{< highlight plain >}}
docker build -t actest .
{{< /highlight >}}

- Kör Docker Image

{{< highlight plain >}}
docker run --mount type=bind,source=C:\Windows\Fonts,target=/Fonts  --mount type=bind,source=C:\Temp,target=/TestOut --rm actest from Docker
{{< /highlight >}}

## Rekommenderad lösning

För .Net6 (eller senare) plattformar, jämfört med tidigare plattformar (.netcore31 eller tidigare) är en viktig skillnad gällande grafikbiblioteket. 
I detta officiella [Microsoft-dokument](https://learn.microsoft.com/en-gb/dotnet/core/compatibility/core-libraries/6.0/system-drawing-common-windows-only) förklaras det att för .Net6 eller senare versioner kommer grafikbiblioteket "System.Drawing.Common" endast stödjas på Windows och ger rekommendationer om att ersätta grafikbiblioteket.

Så Aspose.Cells erbjuder en lösning som är beroende av SkiaSharp-ritbiblioteket på icke-Windows plattformar. Vi rekommenderar att använda SkiaSharp som bibliotek på macOS, vilket också innebär att det inte är nödvändigt att installera libgdiplus.

För information om hur man installerar Aspose.Cells på icke-Windows plattformar och använder SkiaSharp som grafikbibliotek, hänvisar vi till följande artikel:
[Hur man kör Aspose.Cells för .Net6](https://docs.aspose.com/cells/net/how-to-run-aspose-cells-for-net6/)

## Se även

- [Installera Docker Desktop på Windows](https://docs.docker.com/docker-for-windows/install/)
- [Installera Docker Desktop på Mac](https://docs.docker.com/docker-for-mac/install/)
- [Visual Studio 2019, .NET Core 3.1 SDK](https://docs.microsoft.com/en-us/dotnet/core/install/windows?tabs=netcore31#dependencies)
- [Byt till Linux-containrar](https://docs.docker.com/docker-for-windows/#switch-between-windows-and-linux-containers)-alternativet
- Ytterligare information om [.NET Core SDK](https://hub.docker.com/_/microsoft-dotnet-sdk)
{{< app/cells/assistant language="csharp" >}}
