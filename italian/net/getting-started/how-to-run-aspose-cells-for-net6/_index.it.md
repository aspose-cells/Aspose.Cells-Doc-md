---
title: Come eseguire Aspose.Cells per .Net6
type: docs
description: "Come eseguire Aspose.Cells per .Net6."
weight: 138
url: /it/net/how-to-run-aspose-cells-for-net6/
---

## Panoramica

Per le piattaforme .NET6 (o successive), a differenza delle piattaforme precedenti (.netcore31 o precedenti), una differenza importante riguarda la libreria grafica. 
In questo [Documento ufficiale di Microsoft](https://learn.microsoft.com/en-gb/dotnet/core/compatibility/core-libraries/6.0/system-drawing-common-windows-only), si spiega che per le release di .NET6 o successive la libreria grafica "System.Drawing.Common" sarà supportata solo su Windows e fornisce raccomandazioni per sostituire la libreria grafica.

Per il prodotto Apose.Cells, abbiamo condotto la valutazione e completato la migrazione della libreria grafica. Utilizziamo SkiaSharp invece di System.Drawing.Common nei sistemi non Windows, come suggerito nella documentazione ufficiale di Microsoft. Si prega di notare che questo cambiamento critico avrà effetto in Aspose.Cells 22.10.1 o successivo per .Net6.

Per .netcore31 o precedenti, per compatibilità e stabilità, attualmente utilizziamo ancora la libreria grafica "System.Drawing.Common". Le dipendenze per .netcore31 o precedenti sono le seguenti:
- System.Drawing.Common, 4.7.0.
- System.Security.Cryptography.Pkcs, 5.0.1.
- System.Text.Encoding.CodePages, 4.7.0.

## Eseguire Aspose.Cells per .Net6 su Windows

Prima è possibile creare un'applicazione .net6 con VS2022, quindi è possibile scegliere le seguenti opzioni di installazione:

### Installare attraverso nuget

1. Cerca Aspose.Cells da NuGet: [Pacchetto NuGet Aspose.Cells for .NET](https://www.nuget.org/packages/Aspose.Cells/). 
È inoltre possibile installare Aspose.Cells dal gestore dei pacchetti Nuget in VS2022.

2. "SkiaSharp" o "System.Drawing.Common" verrà installato automaticamente come dipendenza di Aspose.Cells 22.10.1 o successivi per le piattaforme .Net6, che dipendono dalla configurazione "Target OS" nel tuo progetto.
- Imposta il "Target OS" su "Windows" per il tuo progetto, userai "System.Drawing.Common" come dipendenza nel tuo sistema windows per il progetto .Net6. In questa configurazione, il risultato del disegno è più vicino a .netcore31 o precedenti.
**![Configura il sistema operativo di destinazione](TargetOS.png)**
Imposta il "Target OS" su "None" o altre opzioni per il tuo progetto, userai "SkiaSharp" come dipendenza sul tuo sistema Windows per il progetto .Net6. *Si prega di notare che la versione che utilizza "SkiaSharp" come dipendenza non supporta la funzione di stampa su stampante.*

### Installare tramite msi o DLL

1. [Scarica Aspose.Cells.msi o DLL](https://releases.aspose.com/cells/net/)

2. Apri la directory di installazione o la directory DLL, quindi seleziona il passaggio 3 o 4 qui sotto:

3. individua la sottodirectory "net6.0-windows", aggiungi il file Aspose.Cells.dll ad essa per il tuo'applicazione .net6. Aggiungi manualmente i pacchetti nuget seguenti al tuo progetto .net6:
- System.Drawing.Common, 4.7.0.
- System.Security.Cryptography.Pkcs, 6.0.3.
- System.Text.Encoding.CodePages, 4.7.0.

In questo modo, userai "System.Drawing.Common" come dipendenza sul tuo sistema Windows per il progetto .Net6. In questa configurazione, il risultato del disegno è più simile a .netcore31 o precedente.

4. individua la sottodirectory "net6.0", aggiungi il file Aspose.Cells.dll ad essa per il tuo'applicazione .net6. Aggiungi manualmente i pacchetti nuget seguenti al tuo progetto .net6:
- SkiaSharp, 2.88.6.
- System.Security.Cryptography.Pkcs, 6.0.3.
- System.Text.Encoding.CodePages, 4.7.0.

In questo modo, userai "SkiaSharp" come dipendenza sul tuo sistema Windows per il progetto .Net6. *Si prega di notare che la versione che utilizza "SkiaSharp" come dipendenza non supporta la funzione di stampa su stampante.*
## Eseguire Aspose.Cells per .Net6 su Linux

Fai riferimento al metodo di installazione su Windows, puoi solo selezionare SkiaSharp come dipendenza della libreria grafica sul sistema Linux.

Devi eseguire le seguenti operazioni aggiuntive per garantire un corretto utilizzo di SkiaSharp sotto Linux:

1. Esegui il comando seguente nel tuo sistema Linux:
```
apt-get update && apt-get install -y libfontconfig1
```
OPPURE
```
apk update && apk add fontconfig 
```

2. Aggiungi i pacchetti nuget "SkiaSharp.NativeAssets.Linux 2.88.6" al tuo progetto .net6.

3. Oppure puoi scegliere di aggiungere i pacchetti nuget "SkiaSharp.NativeAssets.Linux.NoDependencies 2.88.6" al tuo progetto .net6, invece dei due passaggi sopra.

### Esempio di Dockerfile per Ubuntu

1. Aggiungi i pacchetti nuget "SkiaSharp.NativeAssets.Linux 2.88.6" al tuo progetto .net6.

2. Usa il seguente Dockerfile:
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

### Esempio del file Docker per Alpine

1. Aggiungi i pacchetti nuget "SkiaSharp.NativeAssets.Linux 2.88.6" al tuo progetto .net6.

2. Usa il seguente Dockerfile:
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
