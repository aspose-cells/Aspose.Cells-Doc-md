---
title: Convertire tra formati Excel
type: docs
weight: 20
url: /it/net/convert-between-excel-formats/
---

## **Conversione di Excel in PDF**

I file **PDF** sono ampiamente utilizzati per lo scambio di documenti tra organizzazioni, settori governativi e individui. È un formato standard dei documenti e spesso chiesto agli sviluppatori di software di trovare un modo per convertire i file di Microsoft Excel in documenti **PDF**.
**Aspose.Cells** supporta la conversione dei file Excel in PDF e mantiene un'alta fedeltà visiva nella conversione.

Aspose.Cells for .NET supporta la conversione da fogli di calcolo a PDF indipendentemente da altri software. Salvare un file Excel in PDF utilizzando il metodo Save della classe Workbook. Il metodo Save fornisce il membro enum SaveFormat.Pdf che converte i file Excel nativi nel formato PDF.

**Convertire** direttamente da foglio di calcolo a PDF, invece di utilizzare un tool di terze parti o un'API esterna, ha diversi **vantaggi**:

1. La conversione diretta non richiede file temporanei perché l'intero processo può essere eseguito in memoria.
1. Non è necessario un file XML quindi i file di grandi dimensioni possono essere facilmente convertiti.
1. La velocità di conversione è molto più rapida.

**Per convertire i file in PDF:**

1. Istanziare un oggetto della classe **Workbook** chiamando il suo costruttore vuoto.
1. È possibile **aprire/caricare** un file modello esistente o omettere questo passaggio se si sta creando il workbook da zero.
1. Eseguire il lavoro desiderato (inserire dati, applicare formattazione, impostare formule, inserire immagini o altri oggetti grafici, e così via) sul foglio di calcolo utilizzando le API di Aspose.Cells.
1. Quando il codice dello spreadsheet è completo, chiamare il **metodo di salvataggio della classe Workbook** per salvare il foglio di calcolo. Il formato del file dovrebbe essere PDF, quindi selezionare Pdf (un valore predefinito) dall'enumerazione SaveFormat per generare il documento PDF finale.

{{< highlight csharp >}}

  Workbook workbook = new Workbook(openFileDialog1.FileName);

  workbook.Save(saveFileDialog1.FileName, SaveFormat.Pdf);

{{< /highlight >}}

## **Conversione di Excel in MHTML**

**MHTML** combina HTML normale con risorse esterne (cioè, contenuti solitamente collegati, come immagini, animazioni, audio, e così via) in un unico file. Sono utilizzati per le email con l'estensione del file .mht.
Aspose.Cells supporta la lettura e la scrittura dei file MHTML.

{{< highlight csharp >}}

  Workbook workbook = new Workbook(openFileDialog1.FileName);

  //Specify the HTML Saving Options

  HtmlSaveOptions sv = new HtmlSaveOptions(SaveFormat.MHtml);

  workbook.Save(saveFileDialog1.FileName, sv);

{{< /highlight >}}

## **Conversione di Excel in XPS**

A volte si desidera convertire o salvare un workbook con più fogli di lavoro in formato testo. Per i formati di testo (ad esempio TXT, TabDelim, CSV ecc.), sia Microsoft Excel che Aspose.Cells di default salvano solo i contenuti del foglio di lavoro attivo

{{< highlight csharp >}}

  Workbook workbook = new Workbook(openFileDialog1.FileName);

 workbook.Save(saveFileDialog1.FileName, SaveFormat.CSV);

{{< /highlight >}}

## **Scarica il codice di esempio**

- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Convert%20between%20Excel%20formats%20%28Aspose.Cells%29.zip)
