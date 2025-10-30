---
title: Hur man kör Aspose.Cells för .Net6
type: docs
description: "Hur man kör Aspose.Cells för .Net6."
weight: 138
url: /sv/net/how-to-run-aspose-cells-for-net6/
---

## Översikt

För .Net6 (eller senare) plattformar, jämfört med tidigare plattformar (.netcore31 eller tidigare) är en viktig skillnad gällande grafikbiblioteket. 
I detta officiella [Microsoft-dokument](https://learn.microsoft.com/en-gb/dotnet/core/compatibility/core-libraries/6.0/system-drawing-common-windows-only) förklaras det att för .Net6 eller senare versioner kommer grafikbiblioteket "System.Drawing.Common" endast stödjas på Windows och ger rekommendationer om att ersätta grafikbiblioteket.

För Apose.Cells-produkten har vi genomfört utvärderingen och slutfört migreringen av grafikbiblioteket. Vi använder SkiaSharp istället för System.Drawing.Common i icke-Windows-system, som föreslagits i Microsofts officiella dokumentation. Observera att denna kritiska ändring kommer att träda i kraft i Aspose.Cells 22.10.1 eller senare för .Net6.

För .netcore31 eller tidigare, för kompatibilitet och stabilitet, använder vi fortfarande "System.Drawing.Common" som grafikbibliotek. Beroendena för .netcore31 eller tidigare är följande:
- System.Drawing.Common, 5.0.3.
- System.Security.Cryptography.Pkcs, 6.0.5.
- System.Text.Encoding.CodePages, 4.7.0.

## Kör Aspose.Cells för .Net6 (eller senare) på Windows

Först kan du skapa en .net6 (eller senare) applikation med VS2022, sedan kan du välja följande installationsalternativ:

### Installera via nuget

1. Sök efter Aspose.Cells från NuGet: [Aspose.Cells for .NET NuGet-paket](https://www.nuget.org/packages/Aspose.Cells/). 
Du kan också installera Aspose.Cells från Nuget-paketet i VS2022.

2. "SkiaSharp" eller "System.Drawing.Common" installeras automatiskt som ett beroende av Aspose.Cells 22.10.1 eller senare för .Net6 (eller senare) plattformar, vilket beror på "Target OS"-konfigurationen i ditt projekt.
- Sätt "Target OS" till "Windows" för ditt projekt, du kommer att använda "System.Drawing.Common" som ett beroende på ditt Windows-system för .Net6 (eller senare) projekt. I denna konfiguration är resultatet av ritningen närmare .netcore31 eller tidigare.
**![Konfigurera målos](TargetOS.png)**
- Sätt "Target OS" till "None" eller andra alternativ för ditt projekt, du kommer att använda "SkiaSharp" som ett beroende på ditt Windows-system för .Net6 (eller senare) projekt. *Observera att versionen som använder "SkiaSharp" som ett beroende inte stödjer utskriftsfunktion.*

### Installera via msi eller DLL

1. [Ladda ner Aspose.Cells.msi eller DLL](https://releases.aspose.com/cells/net/)

2. Öppna installationskatalogen eller DLL-katalogen, välj sedan steg 3 eller 4 nedan:

3. Lokalisera delkatalogen "net6.0-windows", lägg till Aspose.Cells.dll i den till din .net6-applikation. Lägg manuellt till följande nuget-paket till ditt .net6-projekt:
- System.Drawing.Common, 6.0.0.
- System.Security.Cryptography.Pkcs, 6.0.5.
- System.Text.Encoding.CodePages, 4.7.0.

På detta sätt kommer du att använda "System.Drawing.Common" som ett beroende på ditt Windows-system för .Net6 (eller senare) projekt. I denna konfiguration är resultatet av ritningen närmare .netcore31 eller tidigare.

4. Lokalisera delkatalogen "net6.0", lägg till Aspose.Cells.dll i den till din .net6-applikation. Lägg manuellt till följande nuget-paket till ditt .net6-projekt:
- SkiaSharp, 3.116.1.
- System.Security.Cryptography.Pkcs, 6.0.5.
- System.Text.Encoding.CodePages, 4.7.0.

På detta sätt kommer du att använda "SkiaSharp" som ett beroende på ditt Windows-system för .Net6 (eller senare) projekt. *Observera att versionen som använder "SkiaSharp" som ett beroende inte stödjer utskriftsfunktion.*

## Kör Aspose.Cells för .Net6 (eller senare) på Linux

Referera till installationsmetoden på Windows, kan du endast välja SkiaSharp som ett grafikbiblioteksberoende på Linux-system.

Du måste göra följande ytterligare åtgärder för att säkerställa korrekt användning av SkiaSharp under Linux:

1. Kör följande kommando i ditt Linux-system:
```
apt-get update && apt-get install -y libfontconfig1
```
ELLER
```
apk update && apk add fontconfig 
```

2. Lägg till NuGet paketet "SkiaSharp.NativeAssets.Linux 3.116.1" i ditt .net6 (eller senare) projekt.
3. Eller kan du välja att lägga till NuGet paketen "SkiaSharp.NativeAssets.Linux.NoDependencies 3.116.1" i ditt .net6 (eller senare) projekt, istället för de två stegen ovan.

*Observera att versionen av det tillagda paketet "SkiaSharp.NativeAssets.Linux" eller "SkiaSharp.NativeAssets.Linux.NoDependencies" bör motsvara versionen av "SkiaSharp" som refereras av Aspose.Cells for .NET. Versionerna av Aspose.Cells for .NET och den motsvarande refererade "SKiaSharp"-versionen beskrivs som följande:*

| Aspose.Cells for .NET  |                SkiaSharp                |
| :--------------------: | :-------------------------------------: |
| >= 22.10.1 && <= 22.11 |                 2.88.0                  |
|  >= 22.12 && <= 23.9   |                 2.88.3                  |
|  >= 23.10 && <= 24.12  |                 2.88.6                  |
|        = 25.1.1        |                 3.116.1                 |
|        >=25.1.2        | 2.88.9(net6.0, net8.0), 3.116.1(net9.0) |



### Exempel på Dockerfil för Ubuntu

1. Lägg till NuGet paketet "SkiaSharp.NativeAssets.Linux 3.116.1" i ditt .net6 (eller senare) projekt.

2. Använd följande Dockerfil:
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

### Exempel på Dockerfil för Alpine

1. Lägg till NuGet paketet "SkiaSharp.NativeAssets.Linux 3.116.1" i ditt .net6 (eller senare) projekt.

2. Använd följande Dockerfil:
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
