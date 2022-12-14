---
title: Conversione tra formati Excel
type: docs
weight: 20
url: /it/net/convert-between-excel-formats/
---
## **Conversione di Excel in PDF**

**PDF** i file sono ampiamente utilizzati per lo scambio di documenti tra organizzazioni, settori governativi e individui. È un formato di documento standard e agli sviluppatori di software viene spesso chiesto di trovare un modo per convertire i file Excel Microsoft in**PDF** documenti.
**Aspose.Cells** supporta la conversione di file Excel in PDF e mantiene un'elevata fedeltà visiva nella conversione.

Aspose.Cells for .NET supporta la conversione da fogli di calcolo a PDF indipendentemente da altri software. Salva un file Excel in PDF utilizzando il metodo Save della classe Workbook. Il metodo Save fornisce il membro enum SaveFormat.Pdf che converte i file Excel nativi in formato PDF.

**Conversione** direttamente dal foglio di calcolo al PDF, invece di utilizzare uno strumento di terze parti o esterno API, ha diversi**vantaggi**:

1. La conversione diretta non richiede file temporanei perché l'intero processo può essere eseguito in memoria.
1. Non è necessario alcun file XML, quindi i file di grandi dimensioni possono essere facilmente convertiti.
1. La velocità di conversione è molto più veloce.

**Per convertire i file in PDF:**

1.  Istanziare un oggetto di**Cartella di lavoro** class chiamando il suo costruttore vuoto.
1.  Potresti**apri/carica** un file modello esistente o saltare questo passaggio se si crea la cartella di lavoro da zero.
1. Esegui il lavoro desiderato (inserisci dati, applica formattazione, imposta formule, inserisci immagini o altri oggetti di disegno e così via) sul foglio di calcolo utilizzando le API Aspose.Cells.
1. Quando il codice del foglio di calcolo è completo, chiama il**Metodo di salvataggio della classe della cartella di lavoro** per salvare il foglio di calcolo. Il formato del file deve essere PDF, quindi selezionare Pdf (un valore predefinito) dall'enumerazione SaveFormat per generare il documento PDF finale.

{{< highlight "csharp" >}}

  Workbook workbook = new Workbook(openFileDialog1.FileName);

  workbook.Save(saveFileDialog1.FileName, SaveFormat.Pdf);

{{< /highlight >}}

## **Conversione di Excel in MHTML**

**HTML** combina l'HTML normale con risorse esterne (ovvero, contenuto che di solito è collegato, come immagini, animazioni, audio e così via) in un unico file. Sono utilizzati per le e-mail con estensione file .mht.
Aspose.Cells supporta la lettura e la scrittura di file MHTML.

{{< highlight "csharp" >}}

  Workbook workbook = new Workbook(openFileDialog1.FileName);

  //Specify the HTML Saving Options

  HtmlSaveOptions sv = new HtmlSaveOptions(SaveFormat.MHtml);

  workbook.Save(saveFileDialog1.FileName, sv);

{{< /highlight >}}

## **Conversione di Excel in XPS**

A volte, vuoi convertire o salvare una cartella di lavoro con più fogli di lavoro in formato testo. Per i formati di testo (ad esempio TXT, TabDelim, CSV ecc.), per impostazione predefinita sia Microsoft Excel che Aspose.Cells salvano solo il contenuto del foglio di lavoro attivo.

{{< highlight "csharp" >}}

  Workbook workbook = new Workbook(openFileDialog1.FileName);

 workbook.Save(saveFileDialog1.FileName, SaveFormat.CSV);

{{< /highlight >}}

## **Scarica il codice di esempio**

- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Convert%20between%20Excel%20formats%20%28Aspose.Cells%29.zip)
