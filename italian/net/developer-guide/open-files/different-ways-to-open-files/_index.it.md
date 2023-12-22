---
title: Diversi modi per aprire i file
type: docs
weight: 10
url: /it/net/different-ways-to-open-files/
description: Questo articolo spiega come aprire un file Excel utilizzando Aspose.Cells for .NET API.
keywords: C# Open an Excel file without Excel, How do I open an Excel File.
---
{{% alert color="primary" %}}

Con Aspose.Cells è semplice aprire file, ad esempio, recuperare dati o utilizzare un modello di progettazione per accelerare il processo di sviluppo.

{{% /alert %}}

##  **Come aprire un file Excel tramite un percorso**

 Gli sviluppatori possono aprire un file Excel Microsoft utilizzando il relativo percorso file sul computer locale specificandolo nel campo**[Cartella di lavoro](https://reference.aspose.com/cells/net/aspose.cells/workbook)**costruttore di classi. Passa semplicemente il percorso nel costruttore come *string*. Aspose.Cells rileverà automaticamente il tipo di formato del file.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningFilesThroughPath-1.cs" >}}

##  **Come aprire un file Excel tramite uno stream**

 È anche semplice aprire un file Excel come flusso. Per fare ciò, utilizzare una versione sovraccaricata del costruttore che accetta il file*Flusso*oggetto che contiene il file.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningFilesThroughStream-1.cs" >}}

##  **Come aprire un file solo con dati**

 Per aprire un file contenente solo dati, utilizzare il file**[Opzioni di caricamento](https://reference.aspose.com/cells/net/aspose.cells/loadoptions)** E**[LoadFilter](https://reference.aspose.com/cells/net/aspose.cells/loadfilter)**classi per impostare l'attributo correlato e le opzioni delle classi per il file modello da caricare.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningFilewithDataOnly-1.cs" >}}

##  **Come caricare solo i fogli visibili**

 Durante il caricamento di a**[Cartella di lavoro](https://reference.aspose.com/cells/net/aspose.cells/workbook)**a volte potresti aver bisogno solo dei dati nei fogli di lavoro visibili in una cartella di lavoro. Aspose.Cells ti consente di saltare i dati in fogli di lavoro invisibili durante il caricamento di una cartella di lavoro. Per fare ciò, crea una funzione personalizzata che erediti il file**[LoadFilter](https://reference.aspose.com/cells/net/aspose.cells/loadfilter)**class e passarne l'istanza a**[LoadOptions.LoadFilter](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/properties/loadfilter)**proprietà.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-LoadVisibleSheetsOnly-1.cs" >}}

Ecco l'implementazione del*Caricamento personalizzato*classe a cui si fa riferimento nello snippet sopra.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-LoadVisibleSheetsOnly-2.cs" >}}

{{% alert color="primary" %}}

Verrà generata un'eccezione se si tenta di aprire file Excel non nativi o altri formati di file (ad esempio PPT/PPTX, DOC/DOCX, ecc.) tramite Aspose.Cells.

{{% /alert %}} {{% alert color="primary" %}}

 Ci sono buone probabilità che il**[Cartella di lavoro](https://reference.aspose.com/cells/net/aspose.cells/workbook)**il costruttore può lanciare*System.OutOfMemoryException* durante il caricamento di fogli di calcolo di grandi dimensioni. Questa eccezione suggerisce che la memoria disponibile non è sufficiente per caricare completamente il foglio di calcolo nella memoria, pertanto il foglio di calcolo deve essere caricato abilitando le Preferenze di memoria.

{{% /alert %}}
