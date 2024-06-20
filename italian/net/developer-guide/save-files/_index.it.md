---
title: Diversi modi per salvare i file
linktitle: Salva file
type: docs
weight: 40
url: /it/net/different-ways-to-save-files/
description: Aspose.Cells for .NET può salvare file in formati diversi. Salva file in PDF. Salva file in HTML. Salva file in DOCX. Salva file in PPTX. Salva file in JSON. Salva file in MHTML.
keywords: Aspose.Cells Salva Excel in PDF, HTML, JSON, CSV, TXT, XML, DOCX, PPTX, MHT, MHTML e così via utilizzando C#, Salva o converti il foglio di lavoro in PDF HTML JSON TXT SQL in C#.
---

{{% alert color="primary" %}}

Aspose.Cells rende possibile creare e salvare file. Questo articolo spiega i vari modi in cui i file possono essere salvati.

{{% /alert %}}

## **Diversi modi per salvare i file**

Aspose.Cells fornisce il [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) che rappresenta un file di Microsoft Excel e fornisce le proprietà e i metodi necessari per lavorare con i file di Excel. La classe [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) fornisce il metodo [**Save**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index) utilizzato per salvare i file di Excel. Il metodo [**Save**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index) ha molte sovraccarichi che vengono utilizzati per salvare file in modi diversi.

Il formato del file in cui il file viene salvato è deciso dall'enumerazione [**SaveFormat**](https://reference.aspose.com/cells/net/aspose.cells/saveformat)

|**Tipi di formato file**|**Descrizione**|
| :- | :- |
| CSV | Rappresenta un file CSV |
|Excel97To2003| Rappresenta un file Excel 97 - 2003 |
|Xlsx| Rappresenta un file Excel 2007 XLSX |
|Xlsm| Rappresenta un file Excel 2007 XLSM |
|Xltx| Rappresenta un modello di Excel 2007 XLTX |
|Xltm|Rappresenta un file XLTM abilitato per macro di Excel 2007|
|Xlsb|Rappresenta un file XLSB binario di Excel 2007|
|SpreadsheetML|Rappresenta un file XML di fogli di calcolo|
|TSV|Rappresenta un file di valori separati da tabulazione|
|TabDelimited|Rappresenta un file di testo delimitato da tabulazioni|
|ODS|Rappresenta un file ODS|
|Html|Rappresenta file HTML|
|MHtml|Rappresenta file MHTML|
|Pdf|Rappresenta un file PDF|
|XPS|Rappresenta un documento XPS|
|TIFF|Rappresenta il formato di file immagine TIFF (Tagged Image File Format)|

## **Come Salvare File in Diversi Formati**

Per salvare i file in una posizione di archiviazione, specificare il nome del file (completo di percorso di archiviazione) e il formato desiderato del file (dall'enumerazione [**SaveFormat**](https://reference.aspose.com/cells/net/aspose.cells/saveformat)) durante la chiamata del metodo [**Save**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index) dell'oggetto [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SavingFiletoSomeLocation-1.cs" >}}

## **Come Salvare un Workbook in Pdf**
Il formato di file Portable Document Format (PDF) è un tipo di documento creato da Adobe negli anni '90. Lo scopo di questo formato di file era introdurre uno standard per la rappresentazione di documenti e di altro materiale di riferimento in un formato indipendente dal software dell'applicazione, dall'hardware e dal Sistema Operativo. Il formato di file PDF ha la piena capacità di contenere informazioni come testo, immagini, collegamenti ipertestuali, campi modulo, media ricca, firme digitali, allegati, metadati, funzionalità geospaziali e oggetti 3D che possono diventare parte del documento di origine.

I seguenti codici mostrano come salvare il workbook in formato pdf con Aspose.Cells:
{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Save-As-Pdf.cs" >}}

## **Come Salvare un Workbook in Formato Testo o CSV**

A volte si desidera convertire o salvare un workbook con più fogli di lavoro in formato testo. Per i formati di testo (ad esempio TXT, TabDelim, CSV, ecc.), sia Microsoft Excel che Aspose.Cells di default salvano solo i contenuti del foglio di lavoro attivo.

L'esempio di codice seguente spiega come salvare un intero workbook in formato testo. Carica il workbook di origine che potrebbe essere un file di fogli di calcolo Microsoft Excel o OpenOffice (quindi XLS, XLSX, XLSM, XLSB, ODS e così via) con un qualsiasi numero di fogli di lavoro.

Quando il codice viene eseguito, converte i dati di tutti i fogli nel workbook nel formato TXT.

È possibile modificare lo stesso esempio per salvare il file in formato CSV. Per impostazione predefinita, [**TxtSaveOptions.Separator**](https://reference.aspose.com/cells/net/aspose.cells/txtsaveoptions/properties/separator) è la virgola, quindi non specificare un separatore se si salva in formato CSV.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SaveWorkbookToTextCSVFormat-1.cs" >}}

## **Come salvare un file in file di testo con un separatore personalizzato**

I file di testo contengono dati del foglio di calcolo senza formattazione. Il file è una sorta di file di testo semplice che può avere alcuni delimitatori personalizzati tra i suoi dati.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SavingTextFilewithCustomSeparator-1.cs" >}}

## **Come salvare un file in uno stream**

Per salvare i file in uno stream, creare un oggetto *MemoryStream* o *FileStream* e salvare il file su quell'oggetto stream chiamando il metodo [**Save**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index) dell'oggetto [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook). Specificare il formato del file desiderato utilizzando l'enumerazione [**SaveFormat**](https://reference.aspose.com/cells/net/aspose.cells/saveformat) al momento della chiamata del metodo [**Save**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SavingFiletoStream-1.cs" >}}

## **Come salvare un file di Excel in file Html e Mht**
Aspose.Cells può semplicemente salvare un file di Excel, JSON, CSV o altri file che potrebbero essere caricati da Aspose.Cells come file .html e .mht.
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Excel-to-MHTML.cs" >}}


## **Come salvare un file di Excel in OpenOffice (ODS, SXC, FODS, OTS)**
Possiamo salvare i file in formato open office: ODS, SXC, FODS, OTS ecc.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Excel-to-ODS.cs" >}}

## **Come salvare un file di Excel in JSON o XML**

JSON (JavaScript Object Notation) è un formato file standard aperto per la condivisione di dati che utilizza testo leggibile dall'uomo per memorizzare e trasmettere dati. I file JSON sono memorizzati con l'estensione .json. JSON richiede meno formattazione ed è una buona alternativa per XML. JSON deriva da JavaScript, ma è un formato di dati indipendente dal linguaggio. La generazione e l'analisi di JSON sono supportate da molti linguaggi di programmazione moderni. application/json è il tipo di supporto usato per JSON.

Aspose.Cells supporta il salvataggio dei file in JSON o XML.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Excel-to-JSON.cs" >}}


## **Argomenti avanzati**
- [Regola il livello di compressione del workbook](/cells/it/net/adjust-workbook-compression-level/)
- [Salva il foglio di lavoro nel formato Strict Open XML Spreadsheet](/cells/it/net/save-workbook-to-strict-open-xml-spreadsheet-format/)
- [Salvataggio del file nell'oggetto di risposta](/cells/it/net/saving-file-to-response-object/)
