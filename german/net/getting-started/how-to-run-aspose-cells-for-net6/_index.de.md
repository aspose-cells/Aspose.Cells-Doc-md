---
title: So führen Sie Aspose.Cells für .Net6 aus
type: docs
description: So führen Sie Aspose.Cells für .Net6 aus
weight: 138
url: /de/net/how-to-run-aspose-cells-for-net6/
---
## Überblick

 Bei den .NET6-Plattformen (oder höher) besteht im Vergleich zu früheren Plattformen (.netcore31 oder früher) ein wichtiger Unterschied in der Grafikbibliothek.
 In diesem Beamten[Microsoft Dokument](https://learn.microsoft.com/en-gb/dotnet/core/compatibility/core-libraries/6.0/system-drawing-common-windows-only), erklärt es für .NET6 oder neuere Versionen, dass die Grafikbibliothek „System.Drawing.Common“ nur am Windows unterstützt wird, und gibt Empfehlungen zum Ersetzen der Grafikbibliothek.

Für das Produkt Apose.Cells haben wir die Evaluierung durchgeführt und die Migration der Grafikbibliothek abgeschlossen. Wir verwenden SkiaSharp anstelle von System.Drawing.Common in Nicht-Windows-Systemen, wie in der offiziellen Dokumentation von Microsoft vorgeschlagen. Bitte beachten Sie, dass diese wichtige Änderung ab Aspose.Cells 22.10.1 für .Net6 wirksam wird.

Für .netcore31 oder früher verwenden wir aus Kompatibilitäts- und Stabilitätsgründen derzeit noch die Grafikbibliothek "System.Drawing.Common". Die Abhängigkeiten für .netcore31 oder früher lauten wie folgt:
- System.Drawing.Common, 4.7.0.
- System.Security.Cryptography.Pkcs, 5.0.1.
- System.Text.Encoding.CodePages, 4.7.0.

## Führen Sie Aspose.Cells für .Net6 auf Windows aus

Zuerst können Sie mit VS2022 eine .net6-Anwendung erstellen, dann können Sie die folgenden Installationsoptionen auswählen:

### Installieren Sie über nuget

1.  Suche nach Aspose.Cells aus NuGet:[Aspose.Cells for .NET NuGet Paket](https://www.nuget.org/packages/Aspose.Cells/). 
Sie können Aspose.Cells auch aus dem Nuget-Paketmanager in VS2022 installieren.

2. „SkiaSharp“ oder „System.Drawing.Common“ wird automatisch als Abhängigkeit von Aspose.Cells 22.10.1 oder höher für .Net6-Plattformen installiert, was von der „Zielbetriebssystem“-Konfiguration in Ihrem Projekt abhängt.
- Stellen Sie das „Zielbetriebssystem“ für Ihr Projekt auf „Windows“ ein, Sie verwenden „System.Drawing.Common“ als Abhängigkeit von Ihrem Windows-System für .Net6-Projekte. In dieser Konfiguration ist das Ergebnis der Ziehung näher an .netcore31 oder früher.
**![Zielbetriebssystem konfigurieren](TargetOS.png)**
- Stellen Sie das „Zielbetriebssystem“ auf „Keine“ oder andere Optionen für Ihr Projekt ein, Sie verwenden „SkiaSharp“ als Abhängigkeit von Ihrem Windows-System für das .Net6-Projekt. Bitte beachten Sie, dass Skiasharp derzeit keine Formate wie EMF in Windows unterstützt.

### Installieren Sie über MSI oder DLL

1. [Laden Sie Aspose.Cells.msi oder DLL herunter](https://releases.aspose.com/cells/net/)

2. Öffnen Sie das Installationsverzeichnis oder das DLL-Verzeichnis und wählen Sie dann Schritt 3 oder 4 unten aus:

3. Suchen Sie das Unterverzeichnis „net6.0-windows“ und fügen Sie die Datei Aspose.Cells.dll darin zu Ihrer .net6-Anwendung hinzu. Fügen Sie die folgenden nuget-Pakete manuell zu Ihrem .net6-Projekt hinzu:
- System.Drawing.Common, 4.7.0.
- System.Security.Cryptography.Pkcs, 6.0.1.
- System.Text.Encoding.CodePages, 4.7.0.

Auf diese Weise verwenden Sie „System.Drawing.Common“ als Abhängigkeit von Ihrem Windows-System für das .Net6-Projekt. In dieser Konfiguration ist das Ergebnis der Ziehung näher an .netcore31 oder früher.

4. Suchen Sie das Unterverzeichnis „net6.0“ und fügen Sie die Datei Aspose.Cells.dll darin zu Ihrer .net6-Anwendung hinzu. Fügen Sie die folgenden nuget-Pakete manuell zu Ihrem .net6-Projekt hinzu:
- SkiaSharp, 2.88.3.
- System.Security.Cryptography.Pkcs, 6.0.1.
- System.Text.Encoding.CodePages, 4.7.0.

Auf diese Weise verwenden Sie „SkiaSharp“ als Abhängigkeit von Ihrem Windows-System für das .Net6-Projekt. Bitte beachten Sie, dass Skiasharp derzeit keine Formate wie EMF in Windows unterstützt.

## Führen Sie Aspose.Cells für .Net6 unter Linux aus

Beziehen Sie sich auf die Installationsmethode unter Windows, Sie können Skiasharp nur als Grafikbibliotheksabhängigkeit auf einem Linux-System auswählen.

Sie müssen die folgenden zusätzlichen Vorgänge ausführen, um die ordnungsgemäße Verwendung von Skiasharp unter Linux sicherzustellen:

1. Führen Sie den folgenden Befehl in Ihrem Linux-System aus:
```
apt-get update && apt-get install -y libfontconfig1
```
ODER
```
apk update && apk add fontconfig 
```

2. Fügen Sie Ihrem .net6-Projekt die nuget-Pakete „SkiaSharp.NativeAssets.Linux 2.88.3“ hinzu.

3. Oder Sie können nuget-Pakete „Skiasharp.NativeAssets.Linux.NoDependencies 2.88.3“ zu Ihrem .net6-Projekt hinzufügen, anstatt die beiden obigen Schritte auszuführen.

### Beispiel Dockerfile für Ubuntu

1. Fügen Sie Ihrem .net6-Projekt die nuget-Pakete „Skiasharp.NativeAssets.Linux 2.88.3“ hinzu.

2. Verwenden Sie das folgende Dockerfile:
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

### Beispiel Dockerfile für Alpine

1. Fügen Sie Ihrem .net6-Projekt die nuget-Pakete „Skiasharp.NativeAssets.Linux 2.88.3“ hinzu.

2. Verwenden Sie das folgende Dockerfile:
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
