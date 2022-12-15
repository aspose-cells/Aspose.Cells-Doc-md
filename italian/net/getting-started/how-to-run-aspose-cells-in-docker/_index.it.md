---
title: Come eseguire Aspose.Cells in Docker
type: docs
description: Esegui Aspose.Cells in un contenitore Docker per Linux, Windows Server e qualsiasi sistema operativo.
weight: 139
url: /it/net/how-to-run-aspose-cells-in-docker/
---
I microservizi, insieme alla containerizzazione, consentono di combinare facilmente le tecnologie. Docker ti consente di integrare facilmente la funzionalità Aspose.Cells nella tua applicazione, indipendentemente dalla tecnologia presente nel tuo stack di sviluppo.

Se stai prendendo di mira i microservizi o se la tecnologia principale nel tuo stack non è .NET, C++ o Java, ma hai bisogno della funzionalità Aspose.Cells o se utilizzi già Docker nel tuo stack, allora potresti essere interessato a utilizzare Aspose.Cells in un Contenitore Docker.

## Prerequisiti

- Docker deve essere installato sul tuo sistema. Per informazioni su come installare Docker su Windows o Mac, fare riferimento ai collegamenti nella sezione "Vedi anche".

- Si noti inoltre che nell'esempio fornito di seguito viene usato Visual Studio 2019, .NET Core 3.1 SDK.


## Hello World Richiesta

In questo esempio, crei una semplice applicazione console Hello World che crea un messaggio "Hello World!" documento e lo salva in tutti i formati di salvataggio supportati. L'applicazione può quindi essere creata ed eseguita in Docker.

### Creazione dell'applicazione console

Per creare il programma Hello World, attenersi alla seguente procedura:
1. Una volta installato Docker, assicurati che utilizzi i contenitori Linux (impostazione predefinita). Se necessario, seleziona l'opzione Passa ai contenitori Linux dal menu Docker Desktop.
1. In Visual Studio creare un'applicazione console .NET Core.<br>
![cose da fare:immagine_alt_testo](create-a-new-project.png)<br>
1. Installa l'ultima versione Aspose.Cells da NuGet. System.Drawing.Common e System.Text.Encoding.CodePages verranno installati come dipendenza di Aspose.Cells.<br>
![cose da fare:immagine_alt_testo](nuget-aspose-cells.png)<br>
1. Poiché l'applicazione verrà eseguita su Linux, è necessario installare le risorse Linux native appropriate. Iniziare con l'immagine di base dotnet core sdk 3.1 e installare libgdiplus libc6-dev.
1. Quando tutte le dipendenze richieste sono state aggiunte, scrivi un semplice programma che crei un "Hello World!" cartella di lavoro e la salva in tutti i formati di salvataggio supportati:<br>
**.RETE**<br>
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

Si noti che la cartella "TestOut" è specificata come cartella di output per il salvataggio dei documenti di output. Quando si esegue l'applicazione in Docker, una cartella sul computer host verrà montata in questa cartella nel contenitore. Ciò consentirà di visualizzare facilmente l'output generato da Aspose.Cells nel contenitore Docker.

### Configurazione di un Dockerfile

Il passaggio successivo consiste nel creare e configurare il Dockerfile.

1. Crea il Dockerfile e posizionalo accanto al file della soluzione della tua applicazione. Mantieni questo nome file senza estensione (impostazione predefinita).
1. Nel Dockerfile, specificare:

{{< highlight "plain" >}}
FROM mcr.microsoft.com/dotnet/core/sdk:3.1-buster 
COPY fonts/* /usr/share/fonts/
WORKDIR /app
COPY . ./
RUN apt-get update && \
    apt-get install -y --allow-unauthenticated libgdiplus libc6-dev
RUN dotnet publish "Aspose.Cells.Docker.csproj" -c Release -o /app/publish
ENTRYPOINT ["dotnet", "publish/Aspose.Cells.Docker.dll"]{{< /highlight >}}

Quanto sopra è un semplice Dockerfile, che contiene le seguenti istruzioni:

- L'immagine SDK da utilizzare. Ecco l'immagine .Net Core SDK 3.1. Docker lo scaricherà quando viene eseguita la build. La versione dell'SDK è specificata come tag.
- Installa i caratteri perché l'immagine dell'SDK contiene pochissimi caratteri. Il comando copia i file dei font dall'immagine locale all'immagine docker. Assicurati di avere una directory "fonts" locale che contenga tutti i font che devi installare. In questo esempio, la directory "fonts" locale viene inserita nella stessa directory del Dockerfile.
- La directory di lavoro, specificata nella riga successiva.
- Il comando per copiare tutto nel contenitore, pubblicare l'applicazione e specificare il punto di ingresso.
- Il comando per installare libgdiplus viene eseguito nel contenitore. Ciò è richiesto da System.Drawing.Common.

### Creazione ed esecuzione dell'applicazione in Docker

Ora l'applicazione può essere creata ed eseguita in Docker. Apri il tuo prompt dei comandi preferito, cambia la directory nella cartella con l'applicazione (cartella in cui sono posizionati il file della soluzione e il Dockerfile) ed esegui il seguente comando:

{{< highlight "plain" >}}
docker build -t actest .
{{< /highlight >}}

La prima volta che questo comando viene eseguito potrebbe richiedere più tempo, poiché Docker deve scaricare le immagini richieste. Una volta completato il comando precedente, eseguire il seguente comando:

{{< highlight "plain" >}}
docker run --mount type=bind,source=C:\Temp,target=/TestOut --rm actest from Docker
{{< /highlight >}}

{{% alert color="primary" %}} 

Prestare attenzione all'argomento mount, perché, come accennato in precedenza, una cartella sulla macchina host viene montata nella cartella del contenitore, per vedere facilmente i risultati dell'esecuzione dell'applicazione. I percorsi in Linux fanno distinzione tra maiuscole e minuscole.

{{% /alert %}}

## Immagini che supportano Aspose.Cells

- Aspose.Cells for .NET Standard non supporta EMF e TIFF su Linux.


## Altri esempi

***1. Per eseguire l'applicazione in Windows Server 2019***

- Dockerfile

{{< highlight "plain" >}}
FROM microsoft/dotnet-framework:4.7.2-sdk-windowsservercore-ltsc2019
WORKDIR /app
COPY . ./
RUN dotnet publish "Aspose.Cells.Docker.csproj" -c Release -o /app/publish
ENTRYPOINT ["dotnet", "publish/Aspose.Cells.Docker.dll"]{{< /highlight >}}

- Crea immagine Docker

{{< highlight "plain" >}}
docker build -t actest .
{{< /highlight >}}

- Eseguire l'immagine Docker

{{< highlight "plain" >}}
docker run --mount type=bind,source=C:\Temp,target=c:\TestOut --rm actest from Docker
{{< /highlight >}}


***2. Per eseguire l'applicazione in Linux***

- Scrivi un semplice programma che imposta la cartella dei caratteri, crea un "Hello World!" cartella di lavoro e la salva.

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

- Crea immagine Docker

{{< highlight "plain" >}}
docker build -t actest .
{{< /highlight >}}

- Eseguire l'immagine Docker

{{< highlight "plain" >}}
docker run --mount type=bind,source=C:\Windows\Fonts,target=/Fonts  --mount type=bind,source=C:\Temp,target=/TestOut --rm actest from Docker
{{< /highlight >}}


## Guarda anche

- [Installa Docker Desktop su Windows](https://docs.docker.com/docker-for-windows/install/)
- [Installa Docker Desktop su Mac](https://docs.docker.com/docker-for-mac/install/)
- [Visual Studio 2019, .NET Core 3.1 SDK](https://docs.microsoft.com/en-us/dotnet/core/install/windows?tabs=netcore31#dependencies)
- [Passa ai container Linux](https://docs.docker.com/docker-for-windows/#switch-between-windows-and-linux-containers) opzione
-  Ulteriori informazioni su[.NET Core SDK](https://hub.docker.com/_/microsoft-dotnet-sdk)
