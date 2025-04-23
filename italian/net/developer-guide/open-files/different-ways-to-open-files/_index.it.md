---
title: Diverse modalità per aprire i file
type: docs
weight: 10
url: /it/net/different-ways-to-open-files/
description: Questo articolo spiega come aprire un file excel utilizzando l API Aspose.Cells for .NET.
keywords: Aprire un file Excel senza Excel in C#, Come posso aprire un file Excel.
---

{{% alert color="primary" %}}

Con Aspose.Cells è semplice aprire file, ad esempio, per recuperare dati o utilizzare un modello di designer per accelerare il processo di sviluppo.

{{% /alert %}}

## **Come aprire un file Excel tramite un percorso**

I programmatori possono aprire un file Microsoft Excel utilizzando il percorso del file sul computer locale specificandolo nel costruttore della classe [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook). Basta passare il percorso nel costruttore come *stringa*. Aspose.Cells rileverà automaticamente il tipo di formato del file.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningFilesThroughPath-1.cs" >}}

## **Come aprire un file Excel tramite uno stream**

È anche semplice aprire un file Excel come uno stream. Per farlo, utilizzare una versione sovraccaricata del costruttore che prende l'oggetto *Stream* che contiene il file.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningFilesThroughStream-1.cs" >}}

## **Come aprire un file con solo dati**

Per aprire un file solo con i dati, utilizza le classi [**LoadOptions**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions) e [**LoadFilter**](https://reference.aspose.com/cells/net/aspose.cells/loadfilter) per impostare l'attributo correlato e le opzioni delle classi per il file modello da caricare.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningFilewithDataOnly-1.cs" >}}

## **Come caricare solo fogli visibili**

Mentre carichi un [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) a volte potresti aver bisogno solo dei dati nei fogli di lavoro visibili in un cartella di lavoro. Aspose.Cells ti permette di saltare i dati nei fogli di lavoro invisibili durante il caricamento di una cartella di lavoro. Per farlo, crea una funzione personalizzata che eredita la classe [**LoadFilter**](https://reference.aspose.com/cells/net/aspose.cells/loadfilter) e passa la sua istanza alla proprietà [**LoadOptions.LoadFilter**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/properties/loadfilter)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-LoadVisibleSheetsOnly-1.cs" >}}

Ecco l'implementazione della classe *CustomnLoad* menzionata nel frammento precedente.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-LoadVisibleSheetsOnly-2.cs" >}}

{{% alert color="primary" %}}

Verrà generata un'eccezione se si tenta di aprire file Excel non nativi o altri formati di file (ad esempio PPT/PPTX, DOC/DOCX, ecc.) con Aspose.Cells.

{{% /alert %}} {{% alert color="primary" %}}

È probabile che il costruttore [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) possa generare *System.OutOfMemoryException* durante il caricamento di fogli di calcolo di grandi dimensioni. Questa eccezione suggerisce che la memoria disponibile non è sufficiente per caricare completamente il foglio di calcolo in memoria quindi il foglio di calcolo deve essere caricato abilitando le Preferenze di memoria.

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}
