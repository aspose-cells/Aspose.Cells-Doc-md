---
title: Come eseguire Aspose.Cells in Docker
type: docs
description: "Esegui Aspose.Cells in un contenitore Docker per Linux, Windows Server e qualsiasi altro sistema operativo."
weight: 139
url: /it/net/how-to-run-aspose-cells-in-docker/
---

I microservizi, in combinazione con la containerizzazione, rendono possibile combinare facilmente le tecnologie. Docker ti consente di integrare facilmente la funzionalità Aspose.Cells nella tua applicazione, indipendentemente dalla tecnologia utilizzata nel tuo stack di sviluppo.

Nel caso tu stia puntando ai servizi micro o se la tecnologia principale nel tuo stack non è .NET, C++ o Java, ma hai bisogno della funzionalità di Aspose.Cells, oppure se già utilizzi Docker nel tuo stack, potresti essere interessato a utilizzare Aspose.Cells in un contenitore Docker.

## Prerequisiti

- Docker deve essere installato sul tuo sistema. Per informazioni su come installare Docker su Windows o Mac, consulta i collegamenti nella sezione "Vedi anche".

- Nota anche che nell'esempio viene utilizzato Visual Studio 2019, .NET Core 3.1 SDK.


## Applicazione Hello World

In questo esempio, crei una semplice applicazione console Hello World che crea un documento "Hello World!" e lo salva in tutti i formati di salvataggio supportati. L'applicazione può quindi essere compilata ed eseguita in Docker.

### Creazione dell'applicazione Console

Per creare il programma Hello World, segui i passaggi seguenti:
1. Una volta installato Docker, assicurati che utilizzi i contenitori Linux (impostazione predefinita). Se necessario, seleziona l'opzione Passa a contenitori Linux dal menu Docker Desktop.
1. In Visual Studio, create a .NET Core console application.<br>
![todo:image_alt_text](create-a-new-project.png)<br>
1. Install the latest Aspose.Cells version from NuGet. System.Drawing.Common and System.Text.Encoding.CodePages will be installed as a dependency of Aspose.Cells.<br>
![todo:image_alt_text](nuget-aspose-cells.png)<br>
1. Poiché l'applicazione verrà eseguita su Linux, è necessario installare le risorse native appropriate per Linux. Inizia con l'immagine di base del SDK di dotnet core sdk 3.1 e installa libgdiplus libc6-dev.
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

Nota che la cartella "TestOut" è specificata come cartella di output per il salvataggio dei documenti di output. Quando si esegue l'applicazione in Docker, una cartella sulla macchina host verrà montata su questa cartella nel contenitore. Ciò ti consentirà di visualizzare facilmente l'output generato da Aspose.Cells nel contenitore Docker.

### Configurare un file Dockerfile

Il passo successivo è creare e configurare il Dockerfile.

1. Crea il Dockerfile e posizionalo accanto al file di soluzione della tua applicazione. Mantieni questo nome file senza estensione (il predefinito).
1. Nel Dockerfile, specifica:

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

Quello precedente è un semplice Dockerfile, che contiene le seguenti istruzioni:

- L'immagine SDK da utilizzare. Qui è presente l'immagine .Net Core SDK 3.1. Docker la downloaderà durante l'esecuzione della build. La versione del SDK è specificata come tag.
- Installa i caratteri perché l'immagine SDK contiene pochi caratteri. Il comando copia i file dei caratteri da locale all'immagine docker. Assicurati di avere una directory locale "fonts" che contenga tutti i caratteri che devi installare. In questo esempio, la directory locale "fonts" è posta nella stessa directory del Dockerfile.
- La directory di lavoro, che è specificata nella riga successiva.
- Il comando per copiare tutto nel container, pubblicare l'applicazione e specificare il punto di ingresso.
- Viene eseguito il comando per installare libgdiplus nel container. Questo è richiesto da System.Drawing.Common.

### Costruzione ed Esecuzione dell'Applicazione in Docker

Ora l'applicazione può essere compilata ed eseguita in Docker. Apri il tuo prompt dei comandi preferito, cambia directory nella cartella dell'applicazione (cartella in cui sono posizionati il file di soluzione e il Dockerfile) ed esegui il seguente comando:

{{< highlight plain >}}
docker build -t actest .
{{< /highlight >}}

La prima volta che questo comando viene eseguito, potrebbe richiedere più tempo, poiché Docker ha bisogno di scaricare le immagini richieste. Una volta completato il comando precedente, esegui il seguente comando:

{{< highlight plain >}}
docker run --mount type=bind,source=C:\Temp,target=/TestOut --rm actest from Docker
{{< /highlight >}}

{{% alert color="primary" %}} 

Presta attenzione all'argomento di mount, poiché, come già accennato, una cartella sulla macchina host viene montata nella cartella del container, per vedere facilmente i risultati dell'esecuzione dell'applicazione. I percorsi in Linux sono sensibili alle maiuscole e minuscole.

{{% /alert %}}

## Immagini con supporto Aspose.Cells

- Aspose.Cells for .NET Standard non supporta EMF e TIFF su Linux.


## Altri Esempi

***1. Per eseguire l'applicazione in Windows Server 2019***

- Dockerfile

{{< highlight plain >}}
FROM microsoft/dotnet-framework:4.7.2-sdk-windowsservercore-ltsc2019
WORKDIR /app
COPY . ./
RUN dotnet publish "Aspose.Cells.Docker.csproj" -c Release -o /app/publish
ENTRYPOINT ["dotnet", "publish/Aspose.Cells.Docker.dll"]
{{< /highlight >}}

- Costruisci l'immagine Docker

{{< highlight plain >}}
docker build -t actest .
{{< /highlight >}}

- Esegui l'immagine Docker

{{< highlight plain >}}
docker run --mount type=bind,source=C:\Temp,target=c:\TestOut --rm actest from Docker
{{< /highlight >}}


***2. Per eseguire l'applicazione in Linux***

- Scrivi un semplice programma che imposta la cartella dei font, crea un foglio di lavoro con scritto “Hello World!” e lo salva.

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

- Costruisci l'immagine Docker

{{< highlight plain >}}
docker build -t actest .
{{< /highlight >}}

- Esegui l'immagine Docker

{{< highlight plain >}}
docker run --mount type=bind,source=C:\Windows\Fonts,target=/Fonts  --mount type=bind,source=C:\Temp,target=/TestOut --rm actest from Docker
{{< /highlight >}}


## Vedi Anche

- [Installa Docker Desktop su Windows](https://docs.docker.com/docker-for-windows/install/)
- [Installa Docker Desktop su Mac](https://docs.docker.com/docker-for-mac/install/)
- [Visual Studio 2019, .NET Core 3.1 SDK](https://docs.microsoft.com/en-us/dotnet/core/install/windows?tabs=netcore31#dependencies)
- Opzione [Passa ai contenitori Linux](https://docs.docker.com/docker-for-windows/#switch-between-windows-and-linux-containers)
- Informazioni aggiuntive su [.NET Core SDK](https://hub.docker.com/_/microsoft-dotnet-sdk)
