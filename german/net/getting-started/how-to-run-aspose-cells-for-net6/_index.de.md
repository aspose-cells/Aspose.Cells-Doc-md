---
title: Wie man Aspose.Cells für .Net6 ausführt
type: docs
description: Wie man Aspose.Cells für .Net6 ausführt.
weight: 138
url: /de/net/how-to-run-aspose-cells-for-net6/
---

## Übersicht

Für die .NET6-Plattformen (oder später) gibt es im Vergleich zu früheren Plattformen (.netcore31 oder früher) einen wichtigen Unterschied in Bezug auf die Grafikbibliothek. 
In diesem offiziellen [Microsoft-Dokument](https://learn.microsoft.com/en-gb/dotnet/core/compatibility/core-libraries/6.0/system-drawing-common-windows-only) wird erklärt, dass die Grafikbibliothek "System.Drawing.Common" für .NET6 oder spätere Versionen nur auf Windows unterstützt wird, und es werden Empfehlungen zur Ersetzung der Grafikbibliothek gegeben.

Für das Produkt Apose.Cells haben wir die Evaluierung durchgeführt und die Migration der Grafikbibliothek abgeschlossen. Wir verwenden SkiaSharp anstelle von System.Drawing.Common in Nicht-Windows-Systemen, wie in der offiziellen Dokumentation von Microsoft empfohlen. Bitte beachten Sie, dass diese wichtige Änderung ab Aspose.Cells 22.10.1 oder später für .Net6 wirksam wird.

Für .netcore31 oder früher verwenden wir aus Gründen der Kompatibilität und Stabilität weiterhin die Grafikbibliothek "System.Drawing.Common". Die Abhängigkeiten für .netcore31 oder früher sind wie folgt:
- System.Drawing.Common, 5.0.3.
- System.Security.Cryptography.Pkcs, 6.0.5.
- System.Text.Encoding.CodePages, 4.7.0.

## Ausführen von Aspose.Cells für .Net6 (oder höher) unter Windows

Zuerst können Sie eine .net6 (oder höher) Anwendung mit VS2022 erstellen, dann können Sie die folgenden Installationsoptionen wählen:

### Über NuGet installieren

1. Suchen Sie nach Aspose.Cells auf NuGet: [Aspose.Cells for .NET NuGet-Paket](https://www.nuget.org/packages/Aspose.Cells/). 
Sie können Aspose.Cells auch über den NuGet-Paketmanager in VS2022 installieren.

2. "SkiaSharp" oder "System.Drawing.Common" werden automatisch als Abhängigkeit von Aspose.Cells 22.10.1 oder später für .Net6 (oder höher) Plattformen installiert, die von der "Target OS"-Konfiguration in Ihrem Projekt abhängen.
- Stellen Sie die "Target OS" auf "Windows" für Ihr Projekt ein, Sie verwenden "System.Drawing.Common" als Abhängigkeit auf Ihrem Windows-System für das .Net6 (oder höher) Projekt. In dieser Konfiguration ist das Zeichnen-Ergebnis näher an .netcore31 oder früher.
**![Zielbetriebssystem konfigurieren](TargetOS.png)**
- Stellen Sie die "Target OS" auf "None" oder andere Optionen für Ihr Projekt ein, Sie verwenden "SkiaSharp" als Abhängigkeit auf Ihrem Windows-System für das .Net6 (oder höher) Projekt. *Bitte beachten Sie, dass Versionen, die "SkiaSharp" als Abhängigkeit nutzen, die Druckerfunktion nicht unterstützen.*

### Installation über msi oder DLL

1. [Aspose.Cells.msi oder DLL herunterladen](https://releases.aspose.com/cells/net/)

2. Öffnen Sie das Installationsverzeichnis oder das DLL-Verzeichnis, wählen Sie dann Schritt 3 oder 4 aus:

3. Suchen Sie das Unterverzeichnis „net6.0-windows“, fügen Sie die Aspose.Cells.dll hinzu, um sie Ihrer .NET6-Anwendung hinzuzufügen. Fügen Sie manuell die folgenden NuGet-Pakete zu Ihrem .NET6-Projekt hinzu:
- System.Drawing.Common, 6.0.0.
- System.Security.Cryptography.Pkcs, 6.0.5.
- System.Text.Encoding.CodePages, 4.7.0.

Auf diese Weise verwenden Sie "System.Drawing.Common" als Abhängigkeit auf Ihrem Windows-System für das .Net6 (oder höher) Projekt. In dieser Konfiguration ist das Zeichnen-Ergebnis näher an .netcore31 oder früher.

4. Suchen Sie das Unterverzeichnis „net6.0“, fügen Sie die Aspose.Cells.dll hinzu, um sie Ihrer .NET6-Anwendung hinzuzufügen. Fügen Sie manuell die folgenden NuGet-Pakete zu Ihrem .NET6-Projekt hinzu:
- SkiaSharp, 3.116.1.
- System.Security.Cryptography.Pkcs, 6.0.5.
- System.Text.Encoding.CodePages, 4.7.0.

Auf diese Weise verwenden Sie "SkiaSharp" als Abhängigkeit auf Ihrem Windows-System für das .Net6 (oder höher) Projekt. *Bitte beachten Sie, dass Versionen, die "SkiaSharp" als Abhängigkeit nutzen, die Druckerfunktion nicht unterstützen.*

## Ausführen von Aspose.Cells für .Net6 (oder höher) unter Linux

Beachten Sie die Installationsmethode unter Windows, Sie können nur SkiaSharp als Grafikbibliotheksabhängigkeit im Linux-System auswählen.

Sie müssen die folgenden zusätzlichen Operationen durchführen, um eine ordnungsgemäße Verwendung von SkiaSharp unter Linux sicherzustellen:

1. Führen Sie den folgenden Befehl in Ihrem Linux-System aus:
```
apt-get update && apt-get install -y libfontconfig1
```
ODER
```
apk update && apk add fontconfig 
```

2. Fügen Sie das NuGet-Paket "SkiaSharp.NativeAssets.Linux 3.116.1" zu Ihrem .net6 (oder höher) Projekt hinzu.
3. Oder Sie können das NuGet-Paket "SkiaSharp.NativeAssets.Linux.NoDependencies 3.116.1" zu Ihrem .net6 (oder höher) Projekt hinzufügen, anstelle der oben genannten zwei Schritte.

*Bitte beachten Sie, dass die Version des hinzugefügten Pakets "SkiaSharp.NativeAssets.Linux" oder "SkiaSharp.NativeAssets.Linux.NoDependencies" mit der Version von "SkiaSharp" übereinstimmen sollte, die in Aspose.Cells for .NET referenziert wird. Die Versionen von Aspose.Cells for .NET und die entsprechenden referenzierten "SkiaSharp"-Versionen sind wie folgt beschrieben:*

| Aspose.Cells for .NET  |                SkiaSharp                |
| :--------------------: | :-------------------------------------: |
| >= 22.10.1 && <= 22.11 |                 2.88.0                  |
|  >= 22.12 && <= 23.9   |                 2.88.3                  |
|  >= 23.10 && <= 24.12  |                 2.88.6                  |
|        = 25.1.1        |                 3.116.1                 |
|        >=25.1.2        | 2.88.9(net6.0, net8.0), 3.116.1(net9.0) |



### Beispiel Dockerfile für Ubuntu

1. Fügen Sie das NuGet-Paket "SkiaSharp.NativeAssets.Linux 3.116.1" zu Ihrem .net6 (oder höher) Projekt hinzu.

2. Verwenden Sie das folgende Dockerfile:
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

### Beispiel Dockerfile für Alpine

1. Fügen Sie das NuGet-Paket "SkiaSharp.NativeAssets.Linux 3.116.1" zu Ihrem .net6 (oder höher) Projekt hinzu.

2. Verwenden Sie das folgende Dockerfile:
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
