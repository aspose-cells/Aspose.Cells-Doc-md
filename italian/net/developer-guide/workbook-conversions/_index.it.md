---
title: Converti Excel in Pdf, Immagine e altri formati
linktitle: Conversioni della cartella di lavoro
type: docs
weight: 65
url: /it/net/convert-workbook-to-different-formats/
description: Converti file Excel in Word, Excel, PowerPoint, PDF, CSV, JPG, HTML, MHT, ODS, BMP, PNG, SVG, TIFF, XPS, JSON, SQL, XML e altro.
---
{{% alert color="primary" %}}

Aspose.Cells supporta la conversione tra molti formati. Tecnicamente, la conversione significa caricare una cartella di lavoro in un formato di file e salvarla in un altro.

{{% /alert %}}

## **Converti la cartella di lavoro di Excel in PDF**

I file PDF sono ampiamente utilizzati per lo scambio di documenti tra organizzazioni, settori governativi e individui. È un formato di documento standard e agli sviluppatori di software viene spesso chiesto di trovare un modo per convertire i file Excel Microsoft in documenti PDF.

Aspose.Cells supporta la conversione di file Excel in PDF e mantiene un'elevata fedeltà visiva nella conversione.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Excel-to-PDF.cs" >}}

## **Converti la cartella di lavoro di Excel in JPG**
Aspose.Cells supporta la conversione di file Excel in JPG.
L'esempio di codice seguente mostra come salvare una cartella di lavoro come JPG.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Excel-to-JPG.cs" >}}

## **Converti la cartella di lavoro di Excel in immagine**
Aspose.Cells supporta la conversione di file Excel in immagini.
L'esempio di codice seguente mostra come salvare una cartella di lavoro come immagini.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Excel-to-Image.cs" >}}

## **Conversione della cartella di lavoro di Excel in XPS**

Il formato del documento XPS è costituito da markup XML strutturato che definisce il layout di un documento e l'aspetto visivo di ogni pagina, insieme alle regole di rendering per la distribuzione, l'archiviazione, il rendering, l'elaborazione e la stampa dei documenti.

Il linguaggio di markup per XPS è un sottoinsieme di XAML che consente di incorporare elementi di grafica vettoriale nei documenti, utilizzando XAML per contrassegnare le primitive Windows Presentation Foundation (WPF). Gli elementi utilizzati sono descritti in termini di percorsi e altre primitive geometriche.

Un file XPS è, infatti, un archivio ZIP unicode che utilizza le Open Packaging Conventions, contenente i file che compongono il documento. Questi includono un file di markup XML per ogni pagina, testo, caratteri incorporati, immagini raster, grafica vettoriale 2D, nonché informazioni sulla gestione dei diritti digitali. Il contenuto di un file XPS può essere esaminato semplicemente aprendolo in un'applicazione che supporti i file ZIP.

Da Aspose.Cells 6.0.0, Microsoft è supportata la conversione da Excel a XPS.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-ConvertingToXPS-1.cs" >}}

## **Converti Excel in Ods, Sxc e Fods (OpenOffice / LibreOffice Calc)**
Aspose.Cells supporta la conversione di file Excel in file Ods, Sxc e Fods. L'esempio di codice seguente mostra come convertire il file[template](book1.xlsx) al file Ods, Sxc e Fods.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Excel-to-ODS.cs" >}}


## **Conversione della cartella di lavoro di Excel in file MHTML**

MHTML combina l'HTML normale con risorse esterne (ovvero, contenuto che di solito è collegato, come immagini, animazioni, audio e così via) in un unico file. Sono utilizzati per le e-mail con estensione file .mht.

Aspose.Cells supporta la lettura e la scrittura di file MHTML.

L'esempio di codice seguente mostra come salvare una cartella di lavoro come file MHTML.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-ConvertingToMHTMLFiles-1.cs" >}}

## **Conversione della cartella di lavoro di Excel in HTML**

 Il Aspose.Cells API fornisce supporto per l'esportazione di fogli di calcolo in formato HTML. A tale scopo Aspose.Cells utilizza il**[HtmlSaveOptions](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions)**class per fornire la flessibilità necessaria per controllare diversi aspetti dell'output HTML.

L'esempio di codice seguente mostra come salvare una cartella di lavoro come file HTML.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-ConvertingToHTMLFiles -1.cs" >}}

## **Impostazione delle preferenze immagine per HTML**

 A partire dalla 8.0.2, Aspose.Cells ha esposto**[ImageOptions](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/imageoptions)** per il**[HtmlSaveOptions](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions)**class, consentendo agli sviluppatori di specificare le preferenze delle immagini durante il salvataggio dei fogli di calcolo in formato HTML.

Di seguito sono riportati i dettagli di alcune delle impostazioni dell'immagine che possono essere applicate,

- **[ImageType](https://reference.aspose.com/cells/net/aspose.cells.drawing/imagetype)**: specifica il tipo di immagine. Tieni presente che tutte le forme, inclusi i grafici, vengono visualizzate come immagini nell'HTML di output.
- **[Modalità levigatura](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/smoothingmode)**: specifica l'anti-aliasing per linee, curve e bordi delle aree piene.
- **[Suggerimento per il rendering del testo](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/hint per il rendering del testo)**: Specifica la qualità del rendering del testo.
- **[Qualità](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/quality)** : Specifica la qualità dell'immagine tra 0 e 100, quando**[ImageType](https://reference.aspose.com/cells/net/aspose.cells.drawing/imagetype)**è specificato come Jpeg.
- **[Risoluzione verticale](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/verticalresolution)**: Ottiene o imposta la risoluzione verticale dell'immagine in punti per pollice.
- **[Risoluzione orizzontale](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/horizontalresolution)**: Ottiene o imposta la risoluzione orizzontale dell'immagine in punti per pollice.
- **[TiffCompression](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/tiffcompression)** : Ottiene o imposta il tipo di compressione per le immagini quando**[ImageType](https://reference.aspose.com/cells/net/aspose.cells.drawing/imagetype)**è specificato come Tiff.
- **[Trasparente](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/transparent)**Indica se lo sfondo di un'immagine deve essere trasparente quando ImageFormat è specificato come Png.

 Il codice seguente mostra come utilizzare**[HtmlSaveOptions.ImageOptions](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/imageoptions)**per specificare preferenze diverse.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-SettingImagePrefrencesforHTML-1.cs" >}}

## **Converti la cartella di lavoro di Excel in Markdown**

Il Aspose.Cells API fornisce supporto per l'esportazione di fogli di calcolo in formato Markdown. Per esportare il foglio di lavoro attivo in Markdown, passare**[SaveFormat.Markdown](https://reference.aspose.com/cells/net/aspose.cells/saveformat)** come secondo parametro di**[Workbook.Save](https://reference.aspose.com/cells/net/aspose.cells.workbook/save/methods/3)** metodo. Puoi anche usare**[MarkdownSaveOptions](https://reference.aspose.com/cells/net/aspose.cells/markdownsaveoptions)** class per specificare impostazioni aggiuntive per l'esportazione del foglio di lavoro in Markdown.

 L'esempio di codice seguente illustra l'esportazione del foglio di lavoro attivo in Markdown utilizzando**[SaveFormat.Markdown](https://reference.aspose.com/cells/net/aspose.cells/saveformat)** membro di enumerazione. Si prega di consultare il[output file Markdown](md_sample.txt)generato dal codice per riferimento.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-ConvertExcelFileToMarkdown-1.cs" >}}

## **Converti la cartella di lavoro di Excel in JSON**

Aspose.Cells supporta la conversione di una cartella di lavoro in un file Json (JavaScript Object Notation).

 L'esempio di codice seguente illustra l'esportazione del foglio di lavoro attivo in Json utilizzando[**SaveFormat.Json**](https://reference.aspose.com/cells/net/aspose.cells/saveformat) membro di enumerazione. Si prega di consultare il codice per convertire[file sorgente](Book1.xlsx) al[file Json di output](Book1.Json)generato dal codice per riferimento.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Excel-to-JSON.cs" >}}

## **Converti Excel in XML**
Aspose.Cells supporta la conversione di una cartella di lavoro in foglio di calcolo XML di Excel 2003 e dati XML semplici.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Excel-to-XML.cs" >}}

## **Converti la cartella di lavoro di Excel in TIFF**
Aspose.Cells supporta la conversione di una cartella di lavoro in file TIFF.

Il frammento di codice seguente mostra come convertire Excel in TIFF:

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Excel-to-TIFF.cs" >}}

## **Converti la cartella di lavoro di Excel in DOCX**

Il Aspose.Cells API fornisce il supporto per la conversione di fogli di calcolo in formato DOCX. Per esportare la cartella di lavoro in DOCX, passare[**SaveFormat.Docx**](https://reference.aspose.com/cells/net/aspose.cells/saveformat) come secondo parametro di[**Cartella di lavoro.Salva**](https://reference.aspose.com/cells/net/aspose.cells.workbook/save/methods/3) metodo. Puoi anche usare[**DocxSaveOptions**](https://reference.aspose.com/cells/net/aspose.cells/docxsaveoptions) class per specificare impostazioni aggiuntive per l'esportazione del foglio di lavoro in DOCX.

 L'esempio di codice seguente illustra l'esportazione del foglio di lavoro attivo in DOCX utilizzando[**SaveFormat.Docx**](https://reference.aspose.com/cells/net/aspose.cells/saveformat) membro di enumerazione. Si prega di consultare il[file DOCX di output](Book1.docx)generato dal codice per riferimento.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-ConvertExcelFileToDocx-1.cs" >}}

## **Converti la cartella di lavoro di Excel in PPTX**

Il Aspose.Cells API fornisce il supporto per la conversione di fogli di calcolo in formato PPTX. Per esportare la cartella di lavoro in PPTX, passare[**SaveFormat.Pptx**](https://reference.aspose.com/cells/net/aspose.cells/saveformat) come secondo parametro di[**Cartella di lavoro.Salva**](https://reference.aspose.com/cells/net/aspose.cells.workbook/save/methods/3) metodo. Puoi anche usare[**PptxSaveOptions**](https://reference.aspose.com/cells/net/aspose.cells/pptxsaveoptions) class per specificare impostazioni aggiuntive per l'esportazione del foglio di lavoro in PPTX.

 L'esempio di codice seguente illustra l'esportazione del foglio di lavoro attivo in PPTX utilizzando[**SaveFormat.Pptx**](https://reference.aspose.com/cells/net/aspose.cells/saveformat) membro di enumerazione. Si prega di consultare il[file di output PPTX](Book1.pptx)generato dal codice per riferimento.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-ConvertExcelFileToPptx-1.cs" >}}

## **Argomenti avanzati**
- [Converti la revisione di XLSB in XLSM](/cells/it/net/convert-revision-of-xlsb-to-xlsm/)
- [HTML](/cells/it/net/convert-excel-to-html/)
- [Immagine](/cells/it/net/convert-excel-to-image/)
- [Json](/cells/it/net/convert-workbook-to-json/)
- [Converti la cartella di lavoro di Excel in Ods, Sxc e Fods (OpenOffice / LibreOffice calc).](/cells/it/net/convert-excel-to-ods/)
- [PDF](/cells/it/net/convert-excel-workbook-to-pdf/)
- [Converti Excel in CSV, TSV e Txt](/cells/it/net/convert-excel-to-csv-tsv-and-txt/)
- [Tieni traccia dell'avanzamento della conversione del documento](/cells/it/net/track-document-conversion-progress/)
- [Converti CSV, TSV e TXT in Excel](/cells/it/net/convert-csv-tsv-and-txt-to-excel/)
