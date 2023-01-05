---
title: Hur man kör Aspose.Cells i Docker
type: docs
description: Kör Aspose.Cells i en Docker-behållare för Linux, Windows Server och valfritt operativsystem.
weight: 139
url: /sv/net/how-to-run-aspose-cells-in-docker/
---
Mikrotjänster i samband med containerisering gör det möjligt att enkelt kombinera teknologier. Docker låter dig enkelt integrera Aspose.Cells-funktionalitet i din applikation, oavsett vilken teknik som finns i din utvecklingsstack.

Om du riktar in dig på mikrotjänster, eller om huvudtekniken i din stack inte är .NET, C++ eller Java, men du behöver Aspose.Cells-funktionalitet, eller om du redan använder Docker i din stack, kan du vara intresserad av att använda Aspose.Cells i en Docker behållare.

## Förutsättningar

- Docker måste vara installerat på ditt system. För information om hur du installerar Docker på Windows eller Mac, se länkarna i avsnittet "Se även".

- Observera också att Visual Studio 2019, .NET Core 3.1 SDK används i exemplet nedan.


## Hello World Ansökan

I det här exemplet skapar du en enkel Hello World konsolapplikation som gör ett "Hello World!" dokument och sparar det i alla sparade format som stöds. Applikationen kan sedan byggas och köras i Docker.

### Skapar konsolapplikationen

För att skapa programmet Hello World, följ stegen nedan:
1. När Docker är installerat, se till att den använder Linux-behållare (standard). Om det behövs, välj alternativet Byt till Linux-behållare från Docker Desktops-menyn.
1. Skapa en .NET Core-konsolapplikation i Visual Studio.<br>
![todo:image_alt_text](create-a-new-project.png)<br>
1. Installera den senaste versionen Aspose.Cells från NuGet. System.Drawing.Common och System.Text.Encoding.CodePages kommer att installeras som ett beroende av Aspose.Cells.<br>
![todo:image_alt_text](nuget-aspose-cells.png)<br>
1. Eftersom programmet kommer att köras på Linux måste lämpliga inbyggda Linux-tillgångar installeras. Börja med dotnet core sdk 3.1 basavbildningen och installera libgdiplus libc6-dev.
1. När alla nödvändiga beroenden har lagts till, skriv ett enkelt program som skapar ett "Hello World!" arbetsbok och sparar den i alla sparade format som stöds:<br>
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

Observera att mappen "TestOut" är angiven som en utdatamapp för att spara utdatadokument. När applikationen körs i Docker, kommer en mapp på värddatorn att monteras till denna mapp i behållaren. Detta gör att du enkelt kan se utdata som genereras av Aspose.Cells i Docker-behållaren.

### Konfigurera en dockerfil

Nästa steg är att skapa och konfigurera Dockerfilen.

1. Skapa Dockerfilen och placera den bredvid lösningsfilen för din applikation. Behåll detta filnamn utan förlängning (standard).
1. I Dockerfilen, ange:

{{< highlight "plain" >}}
FROM mcr.microsoft.com/dotnet/core/sdk:3.1-buster 
COPY fonts/* /usr/share/fonts/
WORKDIR /app
COPY . ./
RUN apt-get update && \
    apt-get install -y --allow-unauthenticated libgdiplus libc6-dev
RUN dotnet publish "Aspose.Cells.Docker.csproj" -c Release -o /app/publish
ENTRYPOINT ["dotnet", "publish/Aspose.Cells.Docker.dll"]{{< /highlight >}}

Ovanstående är en enkel Dockerfil, som innehåller följande instruktioner:

- SDK-bilden som ska användas. Här är det .Net Core SDK 3.1-bilden. Docker kommer att ladda ner det när bygget körs. Versionen av SDK anges som en tagg.
- Installera typsnitt eftersom SDK-bilden innehåller väldigt få typsnitt. Kommandot kopierar teckensnittsfiler från lokal till docker-bild. Se till att du har en lokal "fonts"-katalog som innehåller alla teckensnitt du behöver installera. I det här exemplet placeras den lokala "fonts"-katalogen i samma katalog som Dockerfilen.
- Arbetskatalogen, som anges på nästa rad.
- Kommandot för att kopiera allt till behållaren, publicera programmet och ange startpunkten.
- Kommandot för att installera libgdiplus körs i behållaren. Detta krävs av System.Drawing.Common.

### Bygga och köra applikationen i Docker

Nu kan applikationen byggas och köras i Docker. Öppna din favoritkommandotolk, byt katalog till mappen med programmet (mappen där lösningsfilen och Dockerfilen finns) och kör följande kommando:

{{< highlight "plain" >}}
docker build -t actest .
{{< /highlight >}}

Första gången det här kommandot körs kan det ta längre tid, eftersom Docker behöver ladda ner de nödvändiga bilderna. När det föregående kommandot är klart, kör följande kommando:

{{< highlight "plain" >}}
docker run --mount type=bind,source=C:\Temp,target=/TestOut --rm actest from Docker
{{< /highlight >}}

{{% alert color="primary" %}} 

Var uppmärksam på mount-argumentet, eftersom, som nämnts tidigare, en mapp på värddatorn monteras i containerns mapp, för att enkelt se resultatet av applikationskörningen. Sökvägar i Linux är skiftlägeskänsliga.

{{% /alert %}}

## Bilder som stöder Aspose.Cells

- Aspose.Cells for .NET Standard stöder inte EMF och TIFF på Linux.


## Fler exempel

***1. För att köra applikationen i Windows Server 2019***

- Dockerfil

{{< highlight "plain" >}}
FROM microsoft/dotnet-framework:4.7.2-sdk-windowsservercore-ltsc2019
WORKDIR /app
COPY . ./
RUN dotnet publish "Aspose.Cells.Docker.csproj" -c Release -o /app/publish
ENTRYPOINT ["dotnet", "publish/Aspose.Cells.Docker.dll"]{{< /highlight >}}

- Bygg Docker-bild

{{< highlight "plain" >}}
docker build -t actest .
{{< /highlight >}}

- Kör Docker Image

{{< highlight "plain" >}}
docker run --mount type=bind,source=C:\Temp,target=c:\TestOut --rm actest from Docker
{{< /highlight >}}


***2. För att köra programmet i Linux***

- Skriv ett enkelt program som ställer in teckensnittsmapp, skapar en "Hello World!" arbetsbok och sparar den.

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
- Dockerfil

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

- Bygg Docker-bild

{{< highlight "plain" >}}
docker build -t actest .
{{< /highlight >}}

- Kör Docker Image

{{< highlight "plain" >}}
docker run --mount type=bind,source=C:\Windows\Fonts,target=/Fonts  --mount type=bind,source=C:\Temp,target=/TestOut --rm actest from Docker
{{< /highlight >}}


## Se även

- [Installera Docker Desktop på Windows](https://docs.docker.com/docker-for-windows/install/)
- [Installera Docker Desktop på Mac](https://docs.docker.com/docker-for-mac/install/)
- [Visual Studio 2019, .NET Core 3.1 SDK](https://docs.microsoft.com/en-us/dotnet/core/install/windows?tabs=netcore31#dependencies)
- [Byt till Linux-behållare](https://docs.docker.com/docker-for-windows/#switch-between-windows-and-linux-containers) alternativ
-  Ytterligare information om[.NET Core SDK](https://hub.docker.com/_/microsoft-dotnet-sdk)
