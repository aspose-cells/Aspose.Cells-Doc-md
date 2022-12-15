---
title: Diversi modi per salvare i file
linktitle: Salva file
type: docs
weight: 40
url: /it/net/different-ways-to-save-files/
---
{{% alert color="primary" %}}

Aspose.Cells consente di creare e salvare file. Questo articolo spiega i vari modi in cui i file possono essere salvati.

{{% /alert %}}

## **Diversi modi per salvare i file**

 Aspose.Cells fornisce il**[Workbook](https://reference.aspose.com/cells/net/aspose.cells/workbook)** che rappresenta un file Microsoft Excel e fornisce le proprietà e i metodi necessari per lavorare con i file Excel. Il**[Workbook](https://reference.aspose.com/cells/net/aspose.cells/workbook)** la classe fornisce il**[Salva](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index)** metodo utilizzato per salvare i file Excel. Il**[Salva](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index)**Il metodo ha molti overload che vengono utilizzati per salvare i file in modi diversi.

 Il formato di file in cui viene salvato il file è deciso dal file**[SaveFormat](https://reference.aspose.com/cells/net/aspose.cells/saveformat)**enumerazione

|**Tipi di formati di file**|**Descrizione**|
|:- |:- |
|CSV|Rappresenta un file CSV|
|Excel97To2003|Rappresenta un file Excel 97 - 2003|
|Xlsx|Rappresenta un file XLSX di Excel 2007|
|XLSM|Rappresenta un file XLSM di Excel 2007|
|XLTX|Rappresenta un file XLTX modello Excel 2007|
|Xltm|Rappresenta un file XLTM con attivazione macro di Excel 2007|
|Xlsb|Rappresenta un file XLSB binario di Excel 2007|
|Foglio di calcoloML|Rappresenta un file XML di foglio di calcolo|
|TSV|Rappresenta un file di valori separati da tabulazioni|
|Tab Delimitato|Rappresenta un file di testo delimitato da tabulazioni|
|ODS|Rappresenta un file ODS|
|HTML|Rappresenta i file HTML|
|HTML|Rappresenta uno o più file MHTML|
|PDF|Rappresenta un file PDF|
|XPS|Rappresenta un documento XPS|
|TIPO|Rappresenta il formato file immagine con tag (TIFF)|

## **Salvataggio di file in diversi formati**

 Per salvare i file in una posizione di archiviazione, specificare il nome del file (completo di percorso di archiviazione) e il formato file desiderato (da**[SaveFormat](https://reference.aspose.com/cells/net/aspose.cells/saveformat)**enumerazione) quando si chiama il**[Workbook](https://reference.aspose.com/cells/net/aspose.cells/workbook)** dell'oggetto**[Salva](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index)**metodo.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SavingFiletoSomeLocation-1.cs" >}}

## **Salvataggio cartella di lavoro in pdf**
Portable Document Format (PDF) è un tipo di documento creato da Adobe negli anni '90. Lo scopo di questo formato di file era introdurre uno standard per la rappresentazione di documenti e altro materiale di riferimento in un formato indipendente dal software applicativo, dall'hardware e dal sistema operativo. Il formato di file PDF ha la piena capacità di contenere informazioni come testo, immagini, collegamenti ipertestuali, campi modulo, rich media, firme digitali, allegati, metadati, caratteristiche geospaziali e oggetti 3D che possono diventare parte del documento di origine.

I seguenti codici mostrano come salvare la cartella di lavoro come file pdf con Aspose.Cells:
{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Save-As-Pdf.cs" >}}

## **Salvataggio della cartella di lavoro in formato testo o CSV**

volte, vuoi convertire o salvare una cartella di lavoro con più fogli di lavoro in formato testo. Per i formati di testo (ad esempio TXT, TabDelim, CSV, ecc.), per impostazione predefinita sia Microsoft Excel che Aspose.Cells salvano solo il contenuto del foglio di lavoro attivo.

L'esempio di codice seguente spiega come salvare un'intera cartella di lavoro in formato testo. Carica la cartella di lavoro di origine che potrebbe essere qualsiasi file di foglio di calcolo di Microsoft Excel o OpenOffice (quindi XLS, XLSX, XLSM, XLSB, ODS e così via) con qualsiasi numero di fogli di lavoro.

Quando il codice viene eseguito, converte i dati di tutti i fogli nella cartella di lavoro nel formato TXT.

 Puoi modificare lo stesso esempio per salvare il tuo file in formato CSV. Per impostazione predefinita,**[TxtSaveOptions.Separator](https://reference.aspose.com/cells/net/aspose.cells/txtsaveoptions/properties/separator)**è una virgola, quindi non specificare un separatore se si salva in formato CSV.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SaveWorkbookToTextCSVFormat-1.cs" >}}

## **Salvataggio di file di testo con separatore personalizzato**

I file di testo contengono dati del foglio di calcolo senza formattazione. Il file è una sorta di file di testo semplice che può avere alcuni delimitatori personalizzati tra i suoi dati.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SavingTextFilewithCustomSeparator-1.cs" >}}

## **Salvataggio di file in un flusso**

 Per salvare i file in un flusso, creare un file*MemoryStream* o*FileStream* oggetto e salva il file in quell'oggetto flusso chiamando il metodo**[Workbook](https://reference.aspose.com/cells/net/aspose.cells/workbook)** dell'oggetto**[Salva](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index)** metodo. Specificare il formato di file desiderato utilizzando il file**[SaveFormat](https://reference.aspose.com/cells/net/aspose.cells/saveformat)** enumerazione quando si chiama il**[Salva](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index)**metodo.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SavingFiletoStream-1.cs" >}}

## **Salvataggio di file come file Html e Mht**
Aspose.Cells può semplicemente salvare un file Excel, JSON, CSV o altri file che potrebbero essere caricati da Aspose.Cells come file .html e .mht.
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Excel-to-MHTML.cs" >}}
 

## **Salvataggio come OpenOffice (ODS, SXC, FODS, OTS)**
Possiamo salvare i file in formato open office: ODS, SXC, FODS, OTS ecc.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Excel-to-ODS.cs" >}}

## **Salvataggio del file Excel come JSON o XML**

JSON (JavaScript Object Notation) è un formato di file standard aperto per la condivisione di dati che utilizza testo leggibile dall'uomo per archiviare e trasmettere dati. I file JSON vengono archiviati con l'estensione .json. JSON richiede meno formattazione ed è una buona alternativa per XML. JSON deriva da JavaScript ma è un formato di dati indipendente dalla lingua. La generazione e l'analisi di JSON è supportata da molti linguaggi di programmazione moderni. application/json è il tipo di supporto utilizzato per JSON.

Aspose.Cells supporta il salvataggio di file in JSON o XML.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Excel-to-JSON.cs" >}}


## **Argomenti avanzati**
- [Regola il livello di compressione della cartella di lavoro](/cells/it/net/adjust-workbook-compression-level/)
- [Salva cartella di lavoro in formato foglio di calcolo XML aperto rigoroso](/cells/it/net/save-workbook-to-strict-open-xml-spreadsheet-format/)
- [Salvataggio del file nell'oggetto risposta](/cells/it/net/saving-file-to-response-object/)
