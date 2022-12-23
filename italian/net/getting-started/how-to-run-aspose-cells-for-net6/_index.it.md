---
title: Come eseguire Aspose.Cells per .Net6
type: docs
description: Come eseguire Aspose.Cells per .Net6
weight: 138
url: /it/net/how-to-run-aspose-cells-for-net6/
---
## Panoramica

 Per le piattaforme .NET6 (o successive), rispetto alle piattaforme precedenti (.netcore31 o precedenti), una differenza importante riguarda la libreria grafica.
 In questo ufficiale[Microsoft Documento](https://learn.microsoft.com/en-gb/dotnet/core/compatibility/core-libraries/6.0/system-drawing-common-windows-only), spiega che per .NET6 o versioni successive la libreria grafica "System.Drawing.Common" sarà supportata solo su Windows e fornisce consigli per sostituire la libreria grafica.

Per il prodotto Apose.Cells, abbiamo condotto la valutazione e completato la migrazione della libreria grafica. Usiamo SkiaSharp invece di System.Drawing.Common nei sistemi non-Windows, come suggerito nella documentazione ufficiale di Microsoft. Tieni presente che questa modifica critica avrà effetto in Aspose.Cells 22.10.1 o versioni successive per .Net6.

Per .netcore31 o precedenti, per compatibilità e stabilità, attualmente utilizziamo ancora la libreria grafica "System.Drawing.Common". Le dipendenze per .netcore31 o precedenti sono le seguenti:
- System.Drawing.Common, 4.7.0.
- System.Security.Cryptography.Pkcs, 5.0.1.
- System.Text.Encoding.CodePages, 4.7.0.

## Esegui Aspose.Cells per .Net6 su Windows

Per prima cosa puoi creare un'applicazione .net6 con VS2022, quindi puoi scegliere le seguenti opzioni di installazione:

### Installa tramite nuget

1.  Cerca Aspose.Cells da NuGet:[Aspose.Cells for .NET NuGet Confezione](https://www.nuget.org/packages/Aspose.Cells/). 
Puoi anche installare Aspose.Cells dal gestore pacchetti Nuget in VS2022.

2. "SkiaSharp" o "System.Drawing.Common" verrà installato automaticamente come dipendenza di Aspose.Cells 22.10.1 o successivo per le piattaforme .Net6, che dipende dalla configurazione del "sistema operativo di destinazione" nel progetto.
- Imposta il "sistema operativo di destinazione" su "Windows" per il tuo progetto, utilizzerai "System.Drawing.Common" come dipendenza dal tuo sistema Windows per il progetto .Net6. In questa configurazione, il risultato del disegno è più vicino a .netcore31 o precedente.
**![Configura sistema operativo di destinazione](TargetOS.png)**
- Imposta "Sistema operativo di destinazione" su "Nessuno" o altre opzioni per il tuo progetto, utilizzerai "SkiaSharp" come dipendenza dal tuo sistema Windows per il progetto .Net6. Tieni presente che attualmente SkiaSharp non supporta formati come EMF in Windows.

### Installa tramite msi o DLL

1. [Scarica Aspose.Cells.msi o DLL](https://releases.aspose.com/cells/net/)

2. Aprire la directory di installazione o la directory DLL, quindi selezionare il passaggio 3 o 4 di seguito:

3. individuare la sottodirectory "net6.0-windows", aggiungere Aspose.Cells.dll all'applicazione .net6. Aggiungi manualmente i seguenti pacchetti nuget al tuo progetto .net6:
- System.Drawing.Common, 4.7.0.
- System.Security.Cryptography.Pkcs, 6.0.1.
- System.Text.Encoding.CodePages, 4.7.0.

In questo modo, utilizzerai "System.Drawing.Common" come dipendenza dal tuo sistema Windows per il progetto .Net6. In questa configurazione, il risultato del disegno è più vicino a .netcore31 o precedente.

4. individuare la sottodirectory "net6.0", aggiungere il file Aspose.Cells.dll all'applicazione .net6. Aggiungi manualmente i seguenti pacchetti nuget al tuo progetto .net6:
- SkiaSharp, 2.88.3.
- System.Security.Cryptography.Pkcs, 6.0.1.
- System.Text.Encoding.CodePages, 4.7.0.

In questo modo, utilizzerai "SkiaSharp" come dipendenza dal tuo sistema Windows per il progetto .Net6. Tieni presente che attualmente SkiaSharp non supporta formati come EMF in Windows.

## Esegui Aspose.Cells per .Net6 su Linux

Fare riferimento al metodo di installazione su Windows, è possibile selezionare SkiaSharp solo come dipendenza della libreria grafica su sistema Linux.

È necessario eseguire le seguenti operazioni aggiuntive per garantire un uso corretto di SkiaSharp in Linux:

1. Esegui il seguente comando nel tuo sistema Linux:
```
apt-get update && apt-get install -y libfontconfig1
```
O
```
apk update && apk add fontconfig 
```

2. Aggiungi i pacchetti nuget "SkiaSharp.NativeAssets.Linux 2.88.3" al tuo progetto .net6.

3. Oppure puoi scegliere di aggiungere i pacchetti nuget "SkiaSharp.NativeAssets.Linux.NoDependencies 2.88.3" al tuo progetto .net6, invece dei due passaggi precedenti.

### Esempio Dockerfile per Ubuntu

1. Aggiungi i pacchetti nuget "SkiaSharp.NativeAssets.Linux 2.88.3" al tuo progetto .net6.

2. Utilizzare il seguente file Docker:
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

### Esempio Dockerfile per Alpine

1. Aggiungi i pacchetti nuget "SkiaSharp.NativeAssets.Linux 2.88.3" al tuo progetto .net6.

2. Utilizzare il seguente file Docker:
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
