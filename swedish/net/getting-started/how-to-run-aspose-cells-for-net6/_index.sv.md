---
title: Hur man kör Aspose.Cells för .Net6
type: docs
description: Hur man kör Aspose.Cells för .Net6
weight: 138
url: /sv/net/how-to-run-aspose-cells-for-net6/
---
##  Översikt

 För .NET6 (eller senare) plattformar, jämför med tidigare plattformar (.netcore31 eller tidigare), är en viktig skillnad om grafikbiblioteket.
 I denna tjänsteman[Microsoft Dokument](https://learn.microsoft.com/en-gb/dotnet/core/compatibility/core-libraries/6.0/system-drawing-common-windows-only), förklarar det för .NET6 eller senare versioner att grafikbiblioteket "System.Drawing.Common" endast stöds på Windows, och ger rekommendationer för att ersätta grafikbiblioteket.

För produkten Apose.Cells har vi genomfört utvärderingen och har slutfört migreringen av grafikbiblioteket. Vi använder SkiaSharp istället för System.Drawing.Common i icke-Windows system, som föreslås i Microsoft:s officiella dokumentation. Observera att denna kritiska ändring kommer att träda i kraft Aspose.Cells 22.10.1 eller senare för .Net6.

För .netcore31 eller tidigare, för kompatibilitet och stabilitet, använder vi för närvarande fortfarande grafikbiblioteket "System.Drawing.Common". Beroendena för .netcore31 eller tidigare är följande:
- System.Drawing.Common, 4.7.0.
- System.Security.Cryptography.Pkcs, 5.0.1.
- System.Text.Encoding.CodePages, 4.7.0.

##  Kör Aspose.Cells för .Net6 på Windows

Först kan du skapa en .net6-applikation med VS2022, sedan kan du välja följande installationsalternativ:

###  Installera via nuget

1.  Sök efter Aspose.Cells från NuGet:[Aspose.Cells for .NET NuGet Paket](https://www.nuget.org/packages/Aspose.Cells/). 
Du kan också installera Aspose.Cells från pakethanteraren Nuget i VS2022.

2. "SkiaSharp" eller "System.Drawing.Common" kommer att installeras automatiskt som ett beroende av Aspose.Cells 22.10.1 eller senare för .Net6-plattformar, vilket beror på "Target OS"-konfigurationen i ditt projekt.
- Ställ in "Target OS" till "Windows" för ditt projekt, du kommer att använda "System.Drawing.Common" som ett beroende av ditt Windows-system för .Net6-projektet. I den här konfigurationen är resultatet av ritningen närmare .netcore31 eller tidigare.
**![Config target OS](TargetOS.png)**
-  Ställ in "Target OS" till "None" eller andra alternativ för ditt projekt, du kommer att använda "SkiaSharp" som ett beroende av ditt Windows-system för .Net6-projektet.*Observera att versionen som använder "SkiaSharp" som ett beroende inte stöder funktionen för utskrift till skrivare.*

###  Installera via msi eller DLL

1. [Ladda ner Aspose.Cells.msi eller DLL](https://releases.aspose.com/cells/net/)

2. Öppna installationskatalogen eller DLL-katalogen och välj sedan steg 3 eller 4 nedan:

3. hitta underkatalogen "net6.0-windows", lägg till Aspose.Cells.dll i den i ditt .net6-program. Lägg manuellt till följande nuget-paket till ditt .net6-projekt:
- System.Drawing.Common, 4.7.0.
- System.Security.Cryptography.Pkcs, 6.0.3.
- System.Text.Encoding.CodePages, 4.7.0.

På detta sätt kommer du att använda "System.Drawing.Common" som ett beroende av ditt Windows-system för .Net6-projektet. I den här konfigurationen är resultatet av ritningen närmare .netcore31 eller tidigare.

4. hitta underkatalogen "net6.0", lägg till Aspose.Cells.dll i den i ditt .net6-program. Lägg manuellt till följande nuget-paket till ditt .net6-projekt:
- SkiaSharp, 2.88.6.
- System.Security.Cryptography.Pkcs, 6.0.3.
- System.Text.Encoding.CodePages, 4.7.0.

 På detta sätt kommer du att använda "SkiaSharp" som ett beroende av ditt Windows-system för .Net6-projektet.*Observera att versionen som använder "SkiaSharp" som ett beroende inte stöder funktionen för utskrift till skrivare.*
##  Kör Aspose.Cells för .Net6 på Linux

Se installationsmetoden på Windows, du kan bara välja SkiaSharp som ett grafikbiblioteksberoende på Linux-system.

Du måste göra följande ytterligare operationer för att säkerställa korrekt användning av SkiaSharp under Linux:

1. Kör följande kommando i ditt Linux-system:
```
apt-get update && apt-get install -y libfontconfig1
```
OR
```
apk update && apk add fontconfig 
```

2. Lägg till nuget-paketen "SkiaSharp.NativeAssets.Linux 2.88.6" till ditt .net6-projekt.

3. Eller så kan du välja att lägga till nuget-paket "SkiaSharp.NativeAssets.Linux.NoDependencies 2.88.6" till ditt .net6-projekt, istället för de två stegen ovan.

###  Exempel Dockerfile för Ubuntu

1. Lägg till nuget-paketen "SkiaSharp.NativeAssets.Linux 2.88.6" till ditt .net6-projekt.

2. Använd följande Dockerfil:
{{< highlight "plain" >}}
#  Ubuntu 20.04
FROM mcr.microsoft.com/dotnet/runtime:6.0-focal AS base
WORKDIR /app

#  add "libfontconfig1" package if using "SkiaSharp.NativeAssets.Linux" in your project
#  Or you need to use "SkiaSharp.NativeAssets.Linux.NoDependencies" in your project
RUN apt-get update && apt-get install -y libfontconfig1

#  Copy fonts from local to docker
#  For example, put a "fonts" folder in your project folder, and put the font files in it,
#  then, use the following line:
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

###  Exempel Dockerfile för Alpine

1. Lägg till nuget-paketen "SkiaSharp.NativeAssets.Linux 2.88.6" till ditt .net6-projekt.

2. Använd följande Dockerfil:
{{< highlight "plain" >}}
# Alpine 3.16
FROM mcr.microsoft.com/dotnet/runtime:6.0-alpine3.16 AS base
WORKDIR /app

#  add "fontconfig" package if using "SkiaSharp.NativeAssets.Linux" in your project
#  Or you need to use "SkiaSharp.NativeAssets.Linux.NoDependencies" in your project
RUN apk update && apk add fontconfig 

#  Copy fonts from local to docker
#  For example, put a "fonts" folder in your project folder, and put the font files in it,
#  then, use the following line:
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
