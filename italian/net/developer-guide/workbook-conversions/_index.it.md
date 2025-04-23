---
title: Converti Excel in Pdf, immagine e altri formati
linktitle: Conversione di cartelle di lavoro
type: docs
weight: 65
url: /it/net/convert-workbook-to-different-formats/
description: Converti file Excel in Word, Excel, PowerPoint, PDF, CSV, JPG, HTML, MHT, ODS, BMP, PNG, SVG, TIFF, XPS, JSON, SQL, XML e altro ancora.
---

{{% alert color="primary" %}}

Aspose.Cells supporta la conversione tra molti formati. Tecnicamente, la conversione significa caricare una cartella di lavoro in un formato di file e salvarla in un altro.

{{% /alert %}}

## **Converti il foglio di lavoro di Excel in PDF**

I file PDF sono ampiamente utilizzati per lo scambio di documenti tra organizzazioni, settori governativi e individui. È un formato di documento standard e spesso agli sviluppatori software viene chiesto di trovare un modo per convertire i file Microsoft Excel in documenti PDF.

Aspose.Cells supporta la conversione di file Excel in PDF e mantiene un'elevata fedeltà visiva nella conversione.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Excel-to-PDF.cs" >}}

## **Converti cartella di lavoro Excel in JPG**
Aspose.Cells supporta la conversione dei file Excel in JPG.
L'esempio di codice qui sotto mostra come salvare una cartella di lavoro come JPG.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Excel-to-JPG.cs" >}}

## **Converti cartella di lavoro Excel in immagine**
Aspose.Cells supporta la conversione dei file Excel in immagini.
L'esempio di codice qui sotto mostra come salvare una cartella di lavoro come immagini.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Excel-to-Image.cs" >}}

## **Conversione della cartella di lavoro Excel in XPS**

Il formato del documento XPS consiste in markup XML strutturato che definisce la disposizione di un documento e l'aspetto visuale di ogni pagina, insieme alle regole di rendering per distribuire, archiviare, rendere, elaborare e stampare documenti.

Il linguaggio di markup per XPS è un sottoinsieme di XAML che consente di incorporare elementi grafici vettoriali nei documenti, utilizzando XAML per contrassegnare i primitivi della Windows Presentation Foundation (WPF). Gli elementi utilizzati sono descritti in termini di percorsi e altri primitivi geometrici.

Un file XPS è, in realtà, un archivio ZIP unicode utilizzando le Convenzioni per l'Imballaggio Aperto, contenente i file che compongono il documento. Questi includono un file di markup XML per ogni pagina, testo, font integrati, immagini raster, grafica vettoriale 2D, nonché le informazioni sulla gestione dei diritti digitali. Il contenuto di un file XPS può essere esaminato semplicemente aprendolo in un'applicazione che supporta file ZIP.

A partire da Aspose.Cells 6.0.0, è supportata la conversione di Microsoft Excel in XPS.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-ConvertingToXPS-1.cs" >}}

## **Converti Excel in Ods, Sxc e Fods (OpenOffice / LibreOffice Calc)**
Aspose.Cells supporta la conversione dei file Excel in file Ods, Sxc e Fods. L'esempio di codice qui sotto mostra come convertire il [modello](book1.xlsx) in file Ods, Sxc e Fods.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Excel-to-ODS.cs" >}}


## **Conversione della cartella di lavoro Excel in file MHTML**

MHTML combina HTML normale con risorse esterne (cioè contenuti che di solito sono collegati, come immagini, animazioni, audio, e così via) in un unico file. Sono utilizzati per le email con l'estensione del file .mht.

Aspose.Cells supporta la lettura e la scrittura dei file MHTML.

L'esempio di codice sotto mostra come salvare un workbook come file MHTML.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-ConvertingToMHTMLFiles-1.cs" >}}

## **Conversione di un Workbook Excel in HTML**

L'API Aspose.Cells fornisce supporto per l'esportazione di fogli di calcolo nel formato HTML. A questo scopo, Aspose.Cells utilizza la classe [**HtmlSaveOptions**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions) per fornire la flessibilità di controllare vari aspetti dell'HTML di output.

L'esempio di codice sotto mostra come salvare un workbook come file HTML.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-ConvertingToHTMLFiles -1.cs" >}}

## **Impostazione delle Preferenze Immagine per HTML**

A partire dalla versione 8.0.2, Aspose.Cells ha esposto [**ImageOptions**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/imageoptions) per la classe [**HtmlSaveOptions**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions), permettendo agli sviluppatori di specificare le preferenze delle immagini durante il salvataggio dei fogli di calcolo nel formato HTML.

Di seguito sono riportati i dettagli di alcune delle impostazioni delle immagini che possono essere applicate,

- [**ImageType**](https://reference.aspose.com/cells/net/aspose.cells.drawing/imagetype): Specifica il tipo di immagine. Si noti che tutte le forme, inclusi grafici, vengono rappresentati come immagini nell'HTML di output.
- [**SmoothingMode**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/smoothingmode): Specifica l'anti-aliasing per linee, curve e bordi delle aree riempite.
- [**TextRenderingHint**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/textrenderinghint): Specifica la qualità del rendering del testo.
- [**Quality**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/quality): Specifica la qualità dell'immagine tra 0 e 100, quando [**ImageType**](https://reference.aspose.com/cells/net/aspose.cells.drawing/imagetype) è specificato come Jpeg.
- [**VerticalResolution**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/verticalresolution): Ottiene o imposta la risoluzione verticale dell'immagine in punti per pollice.
- [**HorizontalResolution**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/horizontalresolution): Ottiene o imposta la risoluzione orizzontale dell'immagine in punti per pollice.
- [**TiffCompression**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/tiffcompression): Ottiene o imposta il tipo di compressione per le immagini quando [**ImageType**](https://reference.aspose.com/cells/net/aspose.cells.drawing/imagetype) è specificato come Tiff.
- [**Transparent**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/transparent): Indica se lo sfondo di un'immagine deve essere trasparente quando ImageFormat è specificato come Png.

Il codice sotto dimostra come utilizzare [**HtmlSaveOptions.ImageOptions**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/imageoptions) per specificare diverse preferenze.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-SettingImagePrefrencesforHTML-1.cs" >}}

## **Converti Workbook Excel in Markdown**

L'API Aspose.Cells fornisce supporto per l'esportazione di fogli di calcolo nel formato Markdown. Per esportare il foglio attivo in Markdown, passa [**SaveFormat.Markdown**](https://reference.aspose.com/cells/net/aspose.cells/saveformat) come secondo parametro del metodo [**Workbook.Save**](https://reference.aspose.com/cells/net/aspose.cells.workbook/save/methods/3). Puoi anche utilizzare la classe [**MarkdownSaveOptions**](https://reference.aspose.com/cells/net/aspose.cells/markdownsaveoptions) per specificare impostazioni aggiuntive per l'esportazione del foglio di calcolo in Markdown.

Il seguente esempio di codice dimostra l'esportazione del foglio di lavoro attivo in Markdown utilizzando il membro di enumerazione [**SaveFormat.Markdown**](https://reference.aspose.com/cells/net/aspose.cells/saveformat). Si prega di consultare il [file Markdown di output](md_sample.txt) generato dal codice per riferimento.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-ConvertExcelFileToMarkdown-1.cs" >}}

## **Converti Workbook Excel in JSON**

Aspose.Cells supporta la conversione di un workbook in un file Json (JavaScript Object Notation).

L'esempio di codice seguente dimostra l'esportazione del foglio di lavoro attivo in Json utilizzando il membro di enumerazione [**SaveFormat.Json**](https://reference.aspose.com/cells/net/aspose.cells/saveformat). Si prega di consultare il codice per convertire il [file di origine](Book1.xlsx) nel [file Json di output](Book1.Json) generato dal codice per riferimento.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Excel-to-JSON.cs" >}}

## **Converti Excel in XML**
Aspose.Cells supporta la conversione di un workbook in Excel 2003 Spreadsheet XML e dati XML semplici.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Excel-to-XML.cs" >}}

## **Converti Workbook di Excel in TIFF**
Aspose.Cells supporta la conversione di un workbook in file TIFF.

Il frammento di codice seguente mostra come convertire Excel in TIFF:

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Excel-to-TIFF.cs" >}}

## **Converti Workbook di Excel in DOCX**

L'API di Aspose.Cells fornisce supporto per la conversione di fogli di calcolo nel formato DOCX. Per esportare il workbook in DOCX, passare [**SaveFormat.Docx**](https://reference.aspose.com/cells/net/aspose.cells/saveformat) come secondo parametro del metodo [**Workbook.Save**](https://reference.aspose.com/cells/net/aspose.cells.workbook/save/methods/3). È inoltre possibile utilizzare la classe [**DocxSaveOptions**](https://reference.aspose.com/cells/net/aspose.cells/docxsaveoptions) per specificare impostazioni aggiuntive per l'esportazione del foglio di lavoro in DOCX.

L'esempio di codice seguente dimostra l'esportazione del foglio di lavoro attivo in DOCX utilizzando il membro di enumerazione [**SaveFormat.Docx**](https://reference.aspose.com/cells/net/aspose.cells/saveformat). Si prega di consultare il [file DOCX di output](Book1.docx) generato dal codice per riferimento.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-ConvertExcelFileToDocx-1.cs" >}}

## **Converti Workbook di Excel in PPTX**

L'API di Aspose.Cells fornisce supporto per la conversione di fogli di calcolo nel formato PPTX. Per esportare il workbook in PPTX, passare [**SaveFormat.Pptx**](https://reference.aspose.com/cells/net/aspose.cells/saveformat) come secondo parametro del metodo [**Workbook.Save**](https://reference.aspose.com/cells/net/aspose.cells.workbook/save/methods/3). È inoltre possibile utilizzare la classe [**PptxSaveOptions**](https://reference.aspose.com/cells/net/aspose.cells/pptxsaveoptions) per specificare impostazioni aggiuntive per l'esportazione del foglio di lavoro in PPTX.

L'esempio di codice seguente dimostra l'esportazione del foglio di lavoro attivo in PPTX utilizzando il membro di enumerazione [**SaveFormat.Pptx**](https://reference.aspose.com/cells/net/aspose.cells/saveformat). Si prega di consultare il [file PPTX di output](Book1.pptx) generato dal codice per riferimento.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-ConvertExcelFileToPptx-1.cs" >}}

## **Converti cartella di lavoro Excel in EPUB**

L'API Aspose.Cells supporta la conversione di fogli di calcolo in formato EPUB. Per esportare il workbook in EPUB, passa [**SaveFormat.Epub**](https://reference.aspose.com/cells/net/aspose.cells/saveformat) come secondo parametro del metodo [**Workbook.Save**](https://reference.aspose.com/cells/net/aspose.cells.workbook/save/methods/3). Puoi anche usare la classe [**EBookSaveOptions**](https://reference.aspose.com/cells/net/aspose.cells/ebooksaveoptions) per specificare impostazioni aggiuntive per l'esportazione del foglio di lavoro in Epub.

Il seguente esempio di codice dimostra l'esportazione del foglio attivo in EPUB usando il membro di enumerazione [**SaveFormat.Epub**](https://reference.aspose.com/cells/net/aspose.cells/saveformat).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-ConvertingToEPUB-1.cs" >}}

## **Converti cartella di lavoro Excel in AZW3**

L'API Aspose.Cells supporta la conversione di fogli di calcolo in formato AZW3. Per esportare il workbook in AZW3, passa [**SaveFormat.Azw3**](https://reference.aspose.com/cells/net/aspose.cells/saveformat) come secondo parametro del metodo [**Workbook.Save**](https://reference.aspose.com/cells/net/aspose.cells.workbook/save/methods/3). Puoi anche usare la classe [**EBookSaveOptions**](https://reference.aspose.com/cells/net/aspose.cells/ebooksaveoptions) per specificare impostazioni aggiuntive per l'esportazione del foglio di lavoro in AZW3.

Il seguente esempio di codice dimostra l'esportazione del foglio attivo in AZW3 usando il membro di enumerazione [**SaveFormat.Azw3**](https://reference.aspose.com/cells/net/aspose.cells/saveformat).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-ConvertingToAZW3-1.cs" >}}

## **Argomenti avanzati**
- [Converti la revisione di XLSB in XLSM](/cells/it/net/convert-revision-of-xlsb-to-xlsm/)
- [HTML](/cells/it/net/convert-excel-to-html/)
- [Immagine](/cells/it/net/convert-excel-to-image/)
- [Json](/cells/it/net/convert-workbook-to-json/)
- [Converti il workbook di Excel in Ods, Sxc e Fods (OpenOffice / LibreOffice calc).](/cells/it/net/convert-excel-to-ods/)
- [Pdf](/cells/it/net/convert-excel-workbook-to-pdf/)
- [Converti Excel in CSV, TSV e Txt](/cells/it/net/convert-excel-to-csv-tsv-and-txt/)
- [Monitorare il progresso della conversione dei documenti](/cells/it/net/track-document-conversion-progress/)
- [Converti CSV, TSV e TXT in Excel](/cells/it/net/convert-csv-tsv-and-txt-to-excel/)
{{< app/cells/assistant language="csharp" >}}
