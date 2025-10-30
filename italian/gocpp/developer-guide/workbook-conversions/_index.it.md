---
title: Converti Excel in Pdf, Immagine e altri formati con Golang via C++
linktitle: Conversione di cartelle di lavoro
type: docs
weight: 65
url: /it/go-cpp/convert-workbook-to-different-formats/
description: Converti file Excel in Word, Excel, PowerPoint, PDF, CSV, JPG, HTML, MHT, ODS, BMP, PNG, SVG, TIFF, XPS, JSON, SQL, XML e altro ancora usando Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Aspose.Cells supporta la conversione tra molti formati.Tecnicamente, la conversione significa caricare un workbook in un formato di file e salvarlo in un altro.

{{% /alert %}}

## **Converti il foglio di lavoro di Excel in PDF**

I file PDF sono ampiamente utilizzati per lo scambio di documenti tra organizzazioni, settori governativi e individui. È un formato di documento standard e gli sviluppatori di software spesso devono trovare un modo per convertire i file Microsoft Excel in documenti PDF.

Aspose.Cells supporta la conversione di file Excel in PDF e mantiene un'elevata fedeltà visiva nella conversione.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-WorkbookConversions.go" >}}
## **Converti cartella di lavoro Excel in JPG**
Aspose.Cells supporta la conversione dei file Excel in JPG.
L'esempio di codice qui sotto mostra come salvare una cartella di lavoro come JPG.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-WorkbookConversions-1.go" >}}
## **Converti cartella di lavoro Excel in immagine**
Aspose.Cells supporta la conversione dei file Excel in immagini.
L'esempio di codice qui sotto mostra come salvare una cartella di lavoro come immagini.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-WorkbookConversions-2.go" >}}
## **Conversione della cartella di lavoro Excel in XPS**

Il formato del documento XPS consiste in markup XML strutturato che definisce la disposizione di un documento e l'aspetto visuale di ogni pagina, insieme alle regole di rendering per distribuire, archiviare, rendere, elaborare e stampare documenti.

Il linguaggio di markup per XPS è un sottoinsieme di XAML, che consente di incorporare elementi grafici vettoriali nei documenti, usando XAML per contrassegnare le primitive di Windows Presentation Foundation (WPF). Gli elementi utilizzati sono descritti in termini di percorsi e altre primitive geometriche.

Un file XPS è, in effetti, un archivio ZIP Unicode che utilizza le Open Packaging Conventions, contenente i file che compongono il documento. Questi includono un file di markup XML per ogni pagina, testo, font incorporati, immagini raster, grafica vettoriale 2D e informazioni di gestione dei diritti digitali. Il contenuto di un file XPS può essere esaminato semplicemente aprendolo in un’applicazione che supporta ZIP.

A partire da Aspose.Cells 6.0.0, è supportata la conversione di Microsoft Excel in XPS.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-WorkbookConversions-3.go" >}}
## **Converti Excel in Ods, Sxc e Fods (OpenOffice / LibreOffice Calc)**
Aspose.Cells supporta la conversione di file Excel in file Ods, Sxc e Fods. L'esempio di codice seguente mostra come convertire il [modello](book1.xlsx) in file Ods, Sxc e Fods.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-WorkbookConversions-4.go" >}}
## **Conversione della cartella di lavoro Excel in file MHTML**

MHTML combina HTML normale con risorse esterne (cioè contenuti che di solito sono collegati, come immagini, animazioni, audio, e così via) in un unico file. Sono utilizzati per le email con l'estensione del file .mht.

Aspose.Cells supporta la lettura e la scrittura dei file MHTML.

L'esempio di codice sotto mostra come salvare un workbook come file MHTML.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-WorkbookConversions-5.go" >}}
## **Conversione di un Workbook Excel in HTML**

L’API Aspose.Cells supporta l’esportazione di fogli di calcolo in formato HTML. Per questo scopo, Aspose.Cells utilizza la classe [**HtmlSaveOptions**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/) per fornire la flessibilità di controllare vari aspetti dell’HTML di output.

L'esempio di codice sotto mostra come salvare un workbook come file HTML.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-WorkbookConversions-6.go" >}}
## **Impostazione delle Preferenze Immagine per HTML**

A partire dalla versione 8.0.2, Aspose.Cells ha esposto [**GetImageOptions()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getimageoptions/) per la classe [**HtmlSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/), consentendo agli sviluppatori di specificare le preferenze di immagine durante il salvataggio dei fogli di calcolo in formato HTML.

Di seguito sono riportati alcuni dettagli delle impostazioni di immagine che possono essere applicate:

- [**ImageType**](https://reference.aspose.com/cells/go-cpp/imagetype/): Specifica il tipo di immagine. Si noti che tutte le forme, inclusi grafici, vengono rappresentati come immagini nell'HTML di output.
- [**GetQuality()**](https://reference.aspose.com/cells/go-cpp/imageorprintoptions/getquality/): Specifica la qualità dell’immagine tra 0 e 100 quando [**ImageType**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/imagetype/) è specificato come Jpeg.
- [**GetVerticalResolution()**](https://reference.aspose.com/cells/go-cpp/imageorprintoptions/getverticalresolution/): Ottiene o imposta la risoluzione verticale dell'immagine in punti per pollice.
- [**GetHorizontalResolution()**](https://reference.aspose.com/cells/go-cpp/imageorprintoptions/gethorizontalresolution/): Ottiene o imposta la risoluzione orizzontale dell'immagine in punti per pollice.
- [**TiffCompression**](https://reference.aspose.com/cells/go-cpp/tiffcompression/): Ottiene o imposta il tipo di compressione per le immagini quando [**ImageType**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/imagetype/) è specificato come Tiff.
- [**GetTransparent()**](https://reference.aspose.com/cells/go-cpp/imageorprintoptions/gettransparent/): Indica se lo sfondo di un'immagine deve essere trasparente quando ImageFormat è specificato come Png.

Il codice seguente dimostra come utilizzare [**HtmlSaveOptions.GetImageOptions()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getimageoptions/) per specificare diverse preferenze.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-WorkbookConversions-7.go" >}}
## **Converti Workbook Excel in Markdown**

L’API Aspose.Cells supporta l’esportazione di fogli di calcolo in formato Markdown. Per esportare il foglio attivo in Markdown, passare [**SaveFormat.Markdown**](https://reference.aspose.com/cells/go-cpp/saveformat/) come secondo parametro del metodo [**Workbook.Save**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/). È inoltre possibile utilizzare la classe [**MarkdownSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/markdownsaveoptions/) per specificare impostazioni aggiuntive per l’esportazione del foglio in Markdown.

Il seguente esempio di codice dimostra come esportare il foglio attivo in Markdown usando il membro di enumerazione [**SaveFormat.Markdown**](https://reference.aspose.com/cells/go-cpp/saveformat/). Consultare il [file Markdown di output](md_sample.txt) generato dal codice come riferimento.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-WorkbookConversions-8.go" >}}
## **Converti Workbook Excel in JSON**

Aspose.Cells supporta la conversione di un workbook in JSON (JavaScript Object Notation).

Il seguente esempio di codice dimostra come esportare il foglio attivo in JSON usando il membro di enumerazione [**SaveFormat.Json**](https://reference.aspose.com/cells/go-cpp/saveformat/). Consultare il codice per convertire il [file sorgente](Book1.xlsx) nel [file JSON di output](Book1.Json) generato dal codice come riferimento.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-WorkbookConversions-9.go" >}}
## **Converti Excel in XML**
Aspose.Cells supporta la conversione di un workbook in Excel 2003 Spreadsheet XML e dati XML semplici.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-WorkbookConversions-10.go" >}}
## **Converti Workbook di Excel in TIFF**
Aspose.Cells supporta la conversione di un workbook in file TIFF.

Il frammento di codice seguente mostra come convertire Excel in TIFF:

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-WorkbookConversions-11.go" >}}
## **Converti Workbook di Excel in DOCX**

L’API Aspose.Cells supporta la conversione di fogli di calcolo in formato DOCX. Per esportare il workbook in DOCX, passare [**SaveFormat.Docx**](https://reference.aspose.com/cells/go-cpp/saveformat/) come secondo parametro del metodo [**Workbook.Save**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/). È inoltre possibile utilizzare la classe [**DocxSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/docxsaveoptions/) per specificare impostazioni aggiuntive per l’esportazione del foglio in DOCX.

Il seguente esempio di codice dimostra come esportare il foglio attivo in DOCX usando il membro di enumerazione [**SaveFormat.Docx**](https://reference.aspose.com/cells/go-cpp/saveformat/). Consultare il [file DOCX di output](Book1.docx) generato dal codice come riferimento.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-WorkbookConversions-12.go" >}}
## **Converti Workbook di Excel in PPTX**

L’API Aspose.Cells supporta la conversione di fogli di calcolo in formato PPTX. Per esportare il workbook in PPTX, passare [**SaveFormat.Pptx**](https://reference.aspose.com/cells/go-cpp/saveformat/) come secondo parametro del metodo [**Workbook.Save**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/). È inoltre possibile utilizzare la classe [**PptxSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/pptxsaveoptions/) per specificare impostazioni aggiuntive per l’esportazione del foglio in PPTX.

Il seguente esempio di codice dimostra l'esportazione del foglio di lavoro attivo in PPTX utilizzando [**SaveFormat.Pptx**](https://reference.aspose.com/cells/go-cpp/saveformat/) membro dell'enumerazione. Si veda il [file PPTX generato](Book1.pptx) come riferimento.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-WorkbookConversions-13.go" >}}
## **Converti cartella di lavoro Excel in EPUB**

L'API Aspose.Cells supporta la conversione di fogli di calcolo in formato EPUB. Per esportare la cartella di lavoro in EPUB, passare [**SaveFormat.Epub**](https://reference.aspose.com/cells/go-cpp/saveformat/) come secondo parametro del metodo [**Workbook.Save**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/). È inoltre possibile utilizzare la classe [**EBookSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.saving/ebooksaveoptions/) per specificare impostazioni aggiuntive per l'esportazione del foglio di lavoro in EPUB.

Il seguente esempio di codice dimostra l'esportazione del foglio di lavoro attivo in EPUB utilizzando [**SaveFormat.Epub**](https://reference.aspose.com/cells/go-cpp/saveformat/) membro dell'enumerazione.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-WorkbookConversions-14.go" >}}
## **Converti cartella di lavoro Excel in AZW3**

L'API Aspose.Cells supporta la conversione di fogli di calcolo in formato AZW3. Per esportare la cartella di lavoro in AZW3, passare [**SaveFormat.Azw3**](https://reference.aspose.com/cells/go-cpp/saveformat/) come secondo parametro del metodo [**Workbook.Save**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/). È inoltre possibile utilizzare la classe [**EBookSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.saving/ebooksaveoptions/) per specificare impostazioni aggiuntive per l'esportazione del foglio di lavoro in AZW3.

Il seguente esempio di codice dimostra l'esportazione del foglio di lavoro attivo in AZW3 utilizzando [**SaveFormat.Azw3**](https://reference.aspose.com/cells/go-cpp/saveformat/) membro dell'enumerazione.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-WorkbookConversions-15.go" >}}
## **Argomenti avanzati**
- [Converti la revisione di XLSB in XLSM](/cells/it/cpp/convert-revision-of-xlsb-to-xlsm/)
- [HTML](/cells/it/cpp/convert-excel-to-html/)
- [Immagine](/cells/it/cpp/convert-excel-to-image/)
- [Json](/cells/it/cpp/convert-workbook-to-json/)
- [Converti cartella di lavoro Excel in Ods, Sxc e Fods (OpenOffice / LibreOffice calc).](/cells/it/cpp/convert-excel-to-ods/)
- [Pdf](/cells/it/cpp/convert-excel-workbook-to-pdf/)
- [Converti Excel in CSV, TSV e Txt](/cells/it/cpp/convert-excel-to-csv-tsv-and-txt/)
- [Monitorare il progresso della conversione dei documenti](/cells/it/cpp/track-document-conversion-progress/)
- [Converti CSV, TSV e TXT in Excel](/cells/it/cpp/convert-csv-tsv-and-txt-to-excel/)
