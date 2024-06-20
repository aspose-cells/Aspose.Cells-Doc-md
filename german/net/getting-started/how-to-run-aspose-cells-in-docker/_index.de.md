---
title: So führen Sie Aspose.Cells in Docker aus
type: docs
description: Führen Sie Aspose.Cells in einem Docker Container für Linux, Windows Server und jedes Betriebssystem aus.
weight: 139
url: /de/net/how-to-run-aspose-cells-in-docker/
---

Microservices in Verbindung mit Containerisierung ermöglichen es, Technologien einfach zu kombinieren. Docker ermöglicht es Ihnen, die Funktionalität von Aspose.Cells leicht in Ihre Anwendung zu integrieren, unabhängig davon, welche Technologie in Ihrem Entwicklungsstack verwendet wird.

Falls Sie auf Microservices abzielen oder wenn die Haupttechnologie in Ihrem Stack nicht .NET, C++ oder Java ist, Sie jedoch die Funktionalität von Aspose.Cells benötigen oder wenn Sie bereits Docker in Ihrem Stack verwenden, dann könnten Sie daran interessiert sein, Aspose.Cells in einem Docker-Container zu nutzen.

## Voraussetzungen

- Docker muss auf Ihrem System installiert sein. Informationen zur Installation von Docker unter Windows oder Mac finden Sie in den Links im Abschnitt "Siehe auch".

- Beachten Sie auch, dass Visual Studio 2019, .NET Core 3.1 SDK im unten bereitgestellten Beispiel verwendet werden.


## Hello World Anwendung

In diesem Beispiel erstellen Sie eine einfache Hello World Konsolenanwendung, die ein "Hello World!"-Dokument erstellt und in allen unterstützten Formaten speichert. Die Anwendung kann dann in Docker erstellt und ausgeführt werden.

### Erstellen der Konsolenanwendung

Um das Hello World-Programm zu erstellen, befolgen Sie die folgenden Schritte:
1. Sobald Docker installiert ist, stellen Sie sicher, dass es Linux-Container (standardmäßig) verwendet. Wählen Sie bei Bedarf die Option "Zu Linux-Containern wechseln" im Menü von Docker Desktop aus.
1. In Visual Studio, create a .NET Core console application.<br>
![todo:image_alt_text](create-a-new-project.png)<br>
1. Install the latest Aspose.Cells version from NuGet. System.Drawing.Common and System.Text.Encoding.CodePages will be installed as a dependency of Aspose.Cells.<br>
![todo:image_alt_text](nuget-aspose-cells.png)<br>
1. Da die Anwendung auf Linux ausgeführt wird, müssen die entsprechenden nativen Linux-Ressourcen installiert sein. Beginnen Sie mit dem dotnet core sdk 3.1 Basisimage und installieren Sie libgdiplus libc6-dev.
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

Beachten Sie, dass der Ordner „TestOut“ als Ausgabeordner zum Speichern von Ausgabedokumenten festgelegt ist. Wenn die Anwendung in Docker ausgeführt wird, wird ein Ordner auf dem Host-Computer mit diesem Ordner im Container verbunden. Dadurch können Sie die von Aspose.Cells im Docker-Container generierte Ausgabe leicht anzeigen.

### Konfigurieren eines Dockerfiles

Der nächste Schritt besteht darin, das Dockerfile zu erstellen und zu konfigurieren.

1. Erstellen Sie das Dockerfile und platzieren Sie es neben der Lösungsdatei Ihrer Anwendung. Behalten Sie den Dateinamen ohne Erweiterung (Standardmäßig) bei.
1. Geben Sie im Dockerfile an:

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

Das obige ist ein einfaches Dockerfile, das die folgenden Anweisungen enthält:

- Das zu verwendende SDK-Image. Hier handelt es sich um das .Net Core SDK 3.1-Image. Docker wird es beim Ausführen des Builds herunterladen. Die Version des SDK wird als Tag angegeben.
- Installieren von Schriftarten, da das SDK-Image nur sehr wenige Schriftarten enthält. Der Befehl kopiert Schriftdateien von lokal zum Docker-Image. Stellen Sie sicher, dass Sie ein lokales „Schriftarten“-Verzeichnis haben, das alle Schriftarten enthält, die Sie installieren müssen. In diesem Beispiel wird das lokale „Schriftarten“-Verzeichnis im selben Verzeichnis wie das Dockerfile platziert.
- Das Arbeitsverzeichnis, das in der nächsten Zeile angegeben ist.
- Der Befehl zum Kopieren von allem in den Container, zum Veröffentlichen der Anwendung und zum Festlegen des Einstiegspunkts.
- Der Befehl zum Installieren von libgdiplus wird im Container ausgeführt. Dies wird von System.Drawing.Common benötigt.

### Bauen und Ausführen der Anwendung in Docker

Nun kann die Anwendung in Docker gebaut und ausgeführt werden. Öffnen Sie Ihre bevorzugte Eingabeaufforderung, wechseln Sie zum Verzeichnis mit der Anwendung (Verzeichnis, in dem die Lösungsdatei und das Dockerfile platziert sind) und führen Sie den folgenden Befehl aus:

{{< highlight plain >}}
docker build -t actest .
{{< /highlight >}}

Das erste Mal, wenn dieser Befehl ausgeführt wird, kann es länger dauern, da Docker die erforderlichen Images herunterladen muss. Sobald der vorherige Befehl abgeschlossen ist, führen Sie den folgenden Befehl aus:

{{< highlight plain >}}
docker run --mount type=bind,source=C:\Temp,target=/TestOut --rm actest from Docker
{{< /highlight >}}

{{% alert color="primary" %}} 

Beachten Sie das Mount-Argument, da, wie zuvor erwähnt, ein Ordner auf dem Host-Computer in den Ordner des Containers eingebunden wird, um die Ergebnisse der Anwendungs-Ausführung leicht zu sehen. Pfade in Linux sind Groß- und Kleinschreibung beachtend.

{{% /alert %}}

## Bilder die Aspose.Cells unterstützen

- Aspose.Cells for .NET Standard unterstützt EMF und TIFF nicht unter Linux.


## Weitere Beispiele

***1. Zum Ausführen der Anwendung in Windows Server 2019***

- Dockerfile

{{< highlight plain >}}
FROM microsoft/dotnet-framework:4.7.2-sdk-windowsservercore-ltsc2019
WORKDIR /app
COPY . ./
RUN dotnet publish "Aspose.Cells.Docker.csproj" -c Release -o /app/publish
ENTRYPOINT ["dotnet", "publish/Aspose.Cells.Docker.dll"]
{{< /highlight >}}

- Docker-Image erstellen

{{< highlight plain >}}
docker build -t actest .
{{< /highlight >}}

- Docker-Image ausführen

{{< highlight plain >}}
docker run --mount type=bind,source=C:\Temp,target=c:\TestOut --rm actest from Docker
{{< /highlight >}}


***2. Anwendung in Linux ausführen***

- Ein einfaches Programm schreiben, das den Schriftartenordner einrichtet, eine Arbeitsmappe mit dem Text 'Hallo Welt!' erstellt und speichert.

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

- Docker-Image erstellen

{{< highlight plain >}}
docker build -t actest .
{{< /highlight >}}

- Docker-Image ausführen

{{< highlight plain >}}
docker run --mount type=bind,source=C:\Windows\Fonts,target=/Fonts  --mount type=bind,source=C:\Temp,target=/TestOut --rm actest from Docker
{{< /highlight >}}


## Siehe auch

- [Docker Desktop auf Windows installieren](https://docs.docker.com/docker-for-windows/install/)
- [Docker Desktop auf Mac installieren](https://docs.docker.com/docker-for-mac/install/)
- [Visual Studio 2019, .NET Core 3.1 SDK](https://docs.microsoft.com/en-us/dotnet/core/install/windows?tabs=netcore31#dependencies)
- Option zum Wechseln zu Linux-Containern
- Zusätzliche Informationen zum .NET Core SDK
