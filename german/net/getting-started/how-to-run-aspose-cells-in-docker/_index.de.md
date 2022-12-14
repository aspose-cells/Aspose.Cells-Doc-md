---
title: So führen Sie Aspose.Cells in Docker aus
type: docs
description: Führen Sie Aspose.Cells in einem Docker-Container für Linux, Windows Server und jedes Betriebssystem aus.
weight: 139
url: /de/net/how-to-run-aspose-cells-in-docker/
---
Microservices in Verbindung mit Containerisierung ermöglichen es, Technologien einfach zu kombinieren. Docker ermöglicht Ihnen die einfache Integration der Aspose.Cells-Funktionalität in Ihre Anwendung, unabhängig davon, welche Technologie sich in Ihrem Entwicklungsstack befindet.

Falls Sie auf Microservices abzielen oder wenn die Haupttechnologie in Ihrem Stack nicht .NET, C++ oder Java ist, Sie aber die Aspose.Cells-Funktionalität benötigen oder wenn Sie Docker bereits in Ihrem Stack verwenden, dann könnten Sie daran interessiert sein, Aspose.Cells in einem Docker zu verwenden Container.

## Voraussetzungen

- Docker muss auf Ihrem System installiert sein. Informationen zur Installation von Docker auf Windows oder Mac finden Sie unter den Links im Abschnitt „Siehe auch“.

- Beachten Sie außerdem, dass Visual Studio 2019, .NET Core 3.1 SDK in dem unten bereitgestellten Beispiel verwendet wird.


## Hello World Anwendung

In diesem Beispiel erstellen Sie eine einfache Hello World-Konsolenanwendung, die ein „Hello World!“ Dokument und speichert es in allen unterstützten Speicherformaten. Die Anwendung kann dann in Docker erstellt und ausgeführt werden.

### Erstellen der Konsolenanwendung

Gehen Sie wie folgt vor, um das Programm Hello World zu erstellen:
1. Stellen Sie nach der Installation von Docker sicher, dass es Linux-Container verwendet (Standard). Wählen Sie bei Bedarf die Option Zu Linux-Containern wechseln im Menü Docker-Desktops aus.
1. Erstellen Sie in Visual Studio eine .NET Core-Konsolenanwendung.<br>
![todo: Bild_alt_Text](create-a-new-project.png)<br>
1. Installieren Sie die neueste Aspose.Cells-Version von NuGet. System.Drawing.Common und System.Text.Encoding.CodePages werden als Abhängigkeit von Aspose.Cells installiert.<br>
![todo: Bild_alt_Text](nuget-aspose-cells.png)<br>
1. Da die Anwendung unter Linux ausgeführt wird, müssen die entsprechenden nativen Linux-Assets installiert werden. Beginnen Sie mit dem dotnet Core SDK 3.1-Basisimage und installieren Sie libgdiplus libc6-dev.
1. Wenn alle erforderlichen Abhängigkeiten hinzugefügt sind, schreiben Sie ein einfaches Programm, das ein „Hello World!“ erstellt. Arbeitsmappe und speichert sie in allen unterstützten Speicherformaten:<br>
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

Beachten Sie, dass der Ordner „TestOut“ als Ausgabeordner zum Speichern von Ausgabedokumenten angegeben ist. Beim Ausführen der Anwendung in Docker wird ein Ordner auf dem Hostcomputer in diesen Ordner im Container gemountet. Dadurch können Sie die von Aspose.Cells generierte Ausgabe einfach im Docker-Container anzeigen.

### Dockerfile konfigurieren

Der nächste Schritt besteht darin, das Dockerfile zu erstellen und zu konfigurieren.

1. Erstellen Sie das Dockerfile und platzieren Sie es neben der Lösungsdatei Ihrer Anwendung. Behalten Sie diesen Dateinamen ohne Erweiterung bei (Standardeinstellung).
1. Geben Sie in der Dockerfile Folgendes an:

{{< highlight "plain" >}}
FROM mcr.microsoft.com/dotnet/core/sdk:3.1-buster 
COPY fonts/* /usr/share/fonts/
WORKDIR /app
COPY . ./
RUN apt-get update && \
    apt-get install -y --allow-unauthenticated libgdiplus libc6-dev
RUN dotnet publish "Aspose.Cells.Docker.csproj" -c Release -o /app/publish
ENTRYPOINT ["dotnet", "publish/Aspose.Cells.Docker.dll"]{{< /highlight >}}

Das Obige ist ein einfaches Dockerfile, das die folgenden Anweisungen enthält:

- Das zu verwendende SDK-Image. Hier ist es das .Net Core SDK 3.1-Image. Docker lädt es herunter, wenn der Build ausgeführt wird. Die Version des SDK wird als Tag angegeben.
- Installieren Sie Schriftarten, da das SDK-Image nur sehr wenige Schriftarten enthält. Der Befehl kopiert Schriftartdateien von lokal in das Docker-Image. Stellen Sie sicher, dass Sie über ein lokales „Fonts“-Verzeichnis verfügen, das alle Schriftarten enthält, die Sie installieren müssen. In diesem Beispiel wird das lokale „fonts“-Verzeichnis in dasselbe Verzeichnis wie die Dockerfile gestellt.
- Das Arbeitsverzeichnis, das in der nächsten Zeile angegeben wird.
- Der Befehl, alles in den Container zu kopieren, die Anwendung zu veröffentlichen und den Einstiegspunkt anzugeben.
- Der Befehl zum Installieren von libgdiplus wird im Container ausgeführt. Dies wird von System.Drawing.Common benötigt.

### Erstellen und Ausführen der Anwendung in Docker

Jetzt kann die Anwendung in Docker erstellt und ausgeführt werden. Öffnen Sie Ihre bevorzugte Eingabeaufforderung, wechseln Sie in das Verzeichnis mit der Anwendung (Ordner, in dem sich die Lösungsdatei und die Dockerfile befinden) und führen Sie den folgenden Befehl aus:

{{< highlight "plain" >}}
docker build -t actest .
{{< /highlight >}}

Die erste Ausführung dieses Befehls kann länger dauern, da Docker die erforderlichen Bilder herunterladen muss. Führen Sie nach Abschluss des vorherigen Befehls den folgenden Befehl aus:

{{< highlight "plain" >}}
docker run --mount type=bind,source=C:\Temp,target=/TestOut --rm actest from Docker
{{< /highlight >}}

{{% alert color="primary" %}} 

Achten Sie auf das Argument mount, da, wie bereits erwähnt, ein Ordner auf dem Hostcomputer in den Ordner des Containers eingehängt wird, um die Ergebnisse der Anwendungsausführung einfach anzuzeigen. Bei Pfaden in Linux wird zwischen Groß- und Kleinschreibung unterschieden.

{{% /alert %}}

## Bilder, die Aspose.Cells unterstützen

- Aspose.Cells for .NET Standard unterstützt EMF und TIFF unter Linux nicht.


## Mehr Beispiele

***1. So führen Sie die Anwendung in Windows Server 2019 aus***

- Dockerfile

{{< highlight "plain" >}}
FROM microsoft/dotnet-framework:4.7.2-sdk-windowsservercore-ltsc2019
WORKDIR /app
COPY . ./
RUN dotnet publish "Aspose.Cells.Docker.csproj" -c Release -o /app/publish
ENTRYPOINT ["dotnet", "publish/Aspose.Cells.Docker.dll"]{{< /highlight >}}

- Docker-Image erstellen

{{< highlight "plain" >}}
docker build -t actest .
{{< /highlight >}}

- Führen Sie das Docker-Image aus

{{< highlight "plain" >}}
docker run --mount type=bind,source=C:\Temp,target=c:\TestOut --rm actest from Docker
{{< /highlight >}}


***2. Um die Anwendung unter Linux auszuführen***

- Schreiben Sie ein einfaches Programm, das den Schriftartordner festlegt und eine „Hello World!“ erstellt. Arbeitsmappe und speichert sie.

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
- Dockerfile

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

- Docker-Image erstellen

{{< highlight "plain" >}}
docker build -t actest .
{{< /highlight >}}

- Führen Sie das Docker-Image aus

{{< highlight "plain" >}}
docker run --mount type=bind,source=C:\Windows\Fonts,target=/Fonts  --mount type=bind,source=C:\Temp,target=/TestOut --rm actest from Docker
{{< /highlight >}}


## Siehe auch

- [Installieren Sie Docker Desktop unter Windows](https://docs.docker.com/docker-for-windows/install/)
- [Installieren Sie Docker Desktop auf dem Mac](https://docs.docker.com/docker-for-mac/install/)
- [Visual Studio 2019, .NET Core 3.1-SDK](https://docs.microsoft.com/en-us/dotnet/core/install/windows?tabs=netcore31#dependencies)
- [Wechseln Sie zu Linux-Containern](https://docs.docker.com/docker-for-windows/#switch-between-windows-and-linux-containers) Möglichkeit
-  Weitere Informationen auf[.NET Kern-SDK](https://hub.docker.com/_/microsoft-dotnet-sdk)
