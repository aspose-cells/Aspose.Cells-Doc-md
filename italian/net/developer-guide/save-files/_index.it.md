---
title: Diversi modi per salvare i file
linktitle: Salva file
type: docs
weight: 40
url: /it/net/different-ways-to-save-files/
description: Aspose.Cells for .NET possono salvare file in diversi formati. Salva File allo PDF. Salva File allo HTML. Salva File allo DOCX. Salva File allo PPTX. Salva File allo JSON. Salva File allo MHTML.
keywords: Aspose.Cells Save Excel to PDF, HTML, JSON, CSV, TXT, XML, DOCX, PPTX, MHT, MHTML and so on using C#, Save or Convert Workbook to PDF HTML JSON TXT SQL in C#.
---
{{% alert color="primary" %}}

Aspose.Cells permette di creare e salvare file. In questo articolo vengono spiegati i vari modi in cui è possibile salvare i file.

{{% /alert %}}

##  **Diversi modi per salvare i file**

 Aspose.Cells fornisce il**[Cartella di lavoro](https://reference.aspose.com/cells/net/aspose.cells/workbook)** che rappresenta un file Excel Microsoft e fornisce le proprietà e i metodi necessari per lavorare con i file Excel. IL**[Cartella di lavoro](https://reference.aspose.com/cells/net/aspose.cells/workbook)** la classe fornisce il file**[Salva](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index)** metodo utilizzato per salvare file Excel. IL**[Salva](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index)**Il metodo ha molti sovraccarichi utilizzati per salvare i file in diversi modi.

 Il formato file in cui viene salvato il file viene deciso da**[SaveFormat](https://reference.aspose.com/cells/net/aspose.cells/saveformat)**enumerazione

|**Tipi di formato file**|**Descrizione**|
| :- | :- |
|CSV|Rappresenta un file CSV|
|Excel97To2003|Rappresenta un file Excel 97 - 2003|
|Xlsx|Rappresenta un file Excel 2007 XLSX|
|Xlsm|Rappresenta un file Excel 2007 XLSM|
|Xltx|Rappresenta un file modello Excel 2007 XLTX|
|Xltm|Rappresenta un file XLTM abilitato per le macro di Excel 2007|
|Xlsb|Rappresenta un file binario XLSB di Excel 2007|
|SpreadsheetML|Rappresenta un file XML del foglio di calcolo|
|TSV|Rappresenta un file di valori separati da tabulazioni|
|TabDelimited|Rappresenta un file di testo delimitato da tabulazioni|
|ODS|Rappresenta un file ODS|
|HTML|Rappresenta HTML file(i)|
|MHTML|Rappresenta uno o più file MHTML|
|PDF|Rappresenta un file PDF|
|XPS|Rappresenta un documento XPS|
|TIFF|Rappresenta il formato file immagine contrassegnato (TIFF)|

##  **Come salvare file in formati diversi**

Per salvare i file in una posizione di archiviazione, specificare il nome del file (completo di percorso di archiviazione) e il formato file desiderato (da**[SaveFormat](https://reference.aspose.com/cells/net/aspose.cells/saveformat)** enumerazione) quando si chiama il file**[Cartella di lavoro](https://reference.aspose.com/cells/net/aspose.cells/workbook)** dell'oggetto**[Salva](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index)**metodo.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SavingFiletoSomeLocation-1.cs" >}}

##  **Come salvare la cartella di lavoro in PDF**
Portable Document Format (PDF) è un tipo di documento creato da Adobe negli anni '90. Lo scopo di questo formato di file era quello di introdurre uno standard per la rappresentazione di documenti e altro materiale di riferimento in un formato indipendente dal software applicativo, dall'hardware e dal sistema operativo. Il formato file PDF ha la piena capacità di contenere informazioni come testo, immagini, collegamenti ipertestuali, campi modulo, rich media, firme digitali, allegati, metadati, caratteristiche geospaziali e oggetti 3D che possono diventare parte del documento sorgente.

I seguenti codici mostrano come salvare la cartella di lavoro come file PDF con Aspose.Cells:
{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Save-As-Pdf.cs" >}}

##  **Come salvare la cartella di lavoro in formato testo o CSV**

A volte, vuoi convertire o salvare una cartella di lavoro con più fogli di lavoro in formato testo. Per i formati di testo (ad esempio TXT, TabDelim, CSV, ecc.), per impostazione predefinita sia Microsoft Excel che Aspose.Cells salvano solo il contenuto del foglio di lavoro attivo.

Nell'esempio di codice seguente viene illustrato come salvare un'intera cartella di lavoro in formato testo. Carica la cartella di lavoro di origine che potrebbe essere qualsiasi file di foglio di calcolo Excel o OpenOffice Microsoft (quindi XLS, XLSX, XLSM, XLSB, ODS e così via) con un numero qualsiasi di fogli di lavoro.

Quando il codice viene eseguito, converte i dati di tutti i fogli della cartella di lavoro nel formato TXT.

 Puoi modificare lo stesso esempio per salvare il file su CSV. Per impostazione predefinita,**[TxtSaveOptions.Separator](https://reference.aspose.com/cells/net/aspose.cells/txtsaveoptions/properties/separator)**è una virgola, quindi non specificare un separatore se si salva nel formato CSV.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SaveWorkbookToTextCSVFormat-1.cs" >}}

##  **Come salvare file in file di testo con separatore personalizzato**

I file di testo contengono dati del foglio di calcolo senza formattazione. Il file è una sorta di file di testo semplice che può avere alcuni delimitatori personalizzati tra i suoi dati.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SavingTextFilewithCustomSeparator-1.cs" >}}

##  **Come salvare il file in un flusso**

 Per salvare i file in uno stream, crea un file*MemoryStream* O*FileStream*object e salva il file su quell'oggetto stream chiamando il file**[Cartella di lavoro](https://reference.aspose.com/cells/net/aspose.cells/workbook)** dell'oggetto**[Salva](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index)** metodo. Specificare il formato file desiderato utilizzando il file**[SaveFormat](https://reference.aspose.com/cells/net/aspose.cells/saveformat)** enumerazione quando si chiama il file**[Salva](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index)**metodo.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SavingFiletoStream-1.cs" >}}

##  **Come salvare file Excel in file Html e Mht**
Aspose.Cells può semplicemente salvare un file Excel, JSON, CSV o altri file che potrebbero essere caricati da Aspose.Cells come file .html e .mht.
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Excel-to-MHTML.cs" >}}
 

##  **Come salvare file Excel su OpenOffice (ODS, SXC, FODS, OTS)**
Possiamo salvare i file come formato open office: ODS, SXC, FODS, OTS ecc.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Excel-to-ODS.cs" >}}

##  **Come salvare il file Excel su JSON o XML**

JSON (JavaScript Object Notation) è un formato file standard aperto per la condivisione di dati che utilizza testo leggibile dall'uomo per archiviare e trasmettere dati. I file JSON vengono archiviati con l'estensione .json. JSON richiede meno formattazione ed è una buona alternativa a XML. JSON deriva da JavaScript ma è un formato dati indipendente dalla lingua. La generazione e l'analisi di JSON sono supportate da molti linguaggi di programmazione moderni. application/json è il tipo di supporto utilizzato per JSON.

Aspose.Cells supporta il salvataggio di file in JSON o XML.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Excel-to-JSON.cs" >}}


##  **Argomenti avanzati**
- [Regola il livello di compressione della cartella di lavoro](/cells/it/net/adjust-workbook-compression-level/)
- [Salva la cartella di lavoro in un formato di foglio di calcolo XML aperto rigoroso](/cells/it/net/save-workbook-to-strict-open-xml-spreadsheet-format/)
- [Salvataggio del file nell'oggetto di risposta](/cells/it/net/saving-file-to-response-object/)
