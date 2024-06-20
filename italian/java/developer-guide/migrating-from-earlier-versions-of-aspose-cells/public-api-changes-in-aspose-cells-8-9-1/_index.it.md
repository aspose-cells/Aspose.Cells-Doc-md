---
title: Modifiche all API pubblica in Aspose.Cells 8.9.1
type: docs
weight: 320
url: /it/java/public-api-changes-in-aspose-cells-8-9-1/
---

{{% alert color="primary" %}} 

Questo documento descrive le modifiche all'API Aspose.Cells dalla versione 8.9.0 alla 8.9.1 che potrebbero interessare agli sviluppatori dei moduli/applicazioni. Include non solo nuovi metodi pubblici e aggiornati, classi aggiunte e rimosse, ma anche una descrizione di eventuali modifiche nel comportamento dietro le quinte in Aspose.Cells.

{{% /alert %}} 
## **API aggiunte**
### **Sorgenti dei caratteri configurabili**
Aspose.Cells for Java ha esposto un numero di classi per fornire il supporto per le origini dei caratteri configurabili per la visualizzazione delle cartelle di lavoro. Ecco l'elenco delle classi che sono state aggiunte con Aspose.Cells for Java 8.9.1.

1. La classe FontConfigs specifica le impostazioni del carattere.
1. La classe FontSourceBase è una classe di base astratta per le classi che consentono all'utente di specificare varie fonti di caratteri.
1. La classe FileFontSource rappresenta il singolo file di caratteri TrueType memorizzato nel file system.
1. La classe FolderFontSource rappresenta la cartella che contiene file di caratteri TrueType.
1. La classe MemoryFontSource rappresenta il singolo file di caratteri TrueType memorizzato in memoria.
1. L'enumerazione FontSourceType specifica il tipo di una fonte di caratteri.

Con i cambiamenti sopra citati, il Aspose.Cells for Java consente di impostare i caratteri come dettagliato di seguito.

1. Imposta una cartella dei caratteri personalizzata utilizzando il metodo FontConfigs.setFontFolder.
1. Imposta più cartelle di caratteri personalizzate utilizzando il metodo FontConfigs.setFontFolders.
1. Imposta le origini dei caratteri da una cartella dei caratteri personalizzata, da un singolo file di carattere o da dati di carattere da un array di byte utilizzando il metodo FontConfigs.setFontSources.

Ecco uno scenario di utilizzo semplice dei metodi menzionati in precedenza.

**Java**

{{< highlight csharp >}}

 //Defining string variables to store paths to font folders & font file

String fontFolder1 = "D:/Arial";

String fontFolder2 = "D:/Calibri";

String fontFile = "D:/Arial/arial.ttf";

//Setting first font folder with setFontFolder method

//Second parameter directs the API to search the sub folders for font files

FontConfigs.setFontFolder(fontFolder1, true);

//Setting both font folders with setFontFolders method

//Second parameter prohibits the API to search the sub folders for font files

FontConfigs.setFontFolders(new String[] { fontFolder1, fontFolder2 }, false);

//Defining FolderFontSource

FolderFontSource sourceFolder = new FolderFontSource(fontFolder1, false);

//Defining FileFontSource

FileFontSource sourceFile = new FileFontSource(fontFile);

//Defining MemoryFontSource

byte[] bytes = Files.readAllBytes(new File(fontFile).toPath());

MemoryFontSource sourceMemory = new MemoryFontSource(bytes);

//Setting font sources

FontConfigs.setFontSources(new FontSourceBase[] { sourceFolder, sourceFile, sourceMemory});

{{< /highlight >}}

{{% alert color="primary" %}} 

Entrambi i metodi FontConfigs.setFontFolder e FontConfigs.setFontFolders accettano un secondo parametro di tipo Boolean. Passare true come secondo parametro indirizzerà le API di Aspose.Cells a cercare le sottocartelle per i file di carattere. 

{{% /alert %}} 

Aspose.Cells for Java consente anche di configurare la sostituzione dei caratteri. Questo meccanismo è utile quando un carattere richiesto non è disponibile sul computer dove deve avvenire la conversione. Gli utenti possono fornire un elenco di nomi di carattere come alternativa al carattere originariamente richiesto. Per ottenere questo, le API di Aspose.Cells hanno esposto il metodo FontConfigs.setFontSubstitutes che accetta 2 parametri. Il primo parametro è di tipo stringa, che dovrebbe essere il nome del carattere che deve essere sostituito. Il secondo parametro è un array di tipo stringa. Gli utenti possono fornire un elenco di nomi di carattere come sostituzione al nome di carattere originale (specificato nel primo parametro).

Ecco uno scenario di utilizzo semplice del metodo FontConfigs.SetFontSubstitutes.

**Java**

{{< highlight csharp >}}

 //Substituting the Arial font with Times New Roman & Calibri

FontConfigs.setFontSubstitutes("Arial", new String[] { "Times New Roman", "Calibri" });

{{< /highlight >}}

Il Aspose.Cells for Java ha anche fornito i mezzi per raccogliere informazioni su quali fonti e sostituzioni sono state impostate.

1. Il metodo FontConfigs.getFontSources restituisce un array di tipo FontSourceBase contenente l'elenco delle origini dei caratteri specificate. Nel caso in cui non siano state impostate origini, il metodo FontConfigs.getFontSources restituirà un array vuoto.
1. Il metodo FontConfigs.getFontSubstitutes accetta un parametro di tipo stringa che consente di specificare il nome del carattere per il quale è stata impostata una sostituzione. Nel caso in cui non sia stata impostata alcuna sostituzione per il nome del carattere specificato, il metodo FontConfigs.getFontSubstitutes restituirà null.

{{% alert color="primary" %}} 

Per ulteriori dettagli su FontConfigs, si prega di consultare l'articolo su [Configurazione dei caratteri per la visualizzazione delle cartelle di lavoro](/cells/it/java/configurazione-dei-caratteri-per-la-visualizzazione-delle-cartelle-di-lavoro/).

{{% /alert %}} 
### **Aggiunta dell'interfaccia IFilePathProvider e della proprietà HtmlSaveOptions.FilePathProvider**
Aspose.Cells for Java 8.9.1 consente di ottenere/impostare l'IFilePathProvider per esportare le cartelle di lavoro in file HTML separati. Queste nuove API sono utili in scenari in cui i collegamenti ipertestuali in una cartella di lavoro puntano a una posizione in un'altra cartella di lavoro, dove il requisito dell'applicazione è di visualizzare ogni cartella di lavoro in un file HTML separato. Implementare l'IFilePathProvider consente di mantenere i suddetti collegamenti ipertestuali intatti indipendentemente dal fatto che puntino a una posizione in un file HTML risultante separato.

Di seguito è riportato il semplice scenario di utilizzo della proprietà HtmlSaveOptions.FilePathProvider.

**Java**

{{< highlight csharp >}}

 //Load a spreadsheet in an instance of Workbook

Workbook book = new Workbook(dir + "sample.xlsx");

//Save each Worksheet to separate  HTML file

for (int i = 0; i < book.getWorksheets().getCount(); i++)

{

	book.getWorksheets().setActiveSheetIndex(i);

	//Create an instance of HtmlSaveOptions & set FilePathProvider property

	HtmlSaveOptions options = new HtmlSaveOptions();

	options.setExportActiveWorksheetOnly(true);

	options.setFilePathProvider(new IFilePathProvider() 

	{ 

		public String getFullName(String sheetName)

		{

		    if ("Sheet2".equals(sheetName))

		    {

		        return "sheet1.html";

		    }

		    else if ("Sheet3".equals(sheetName))

		    {

		        return "sheet2.html";

		    }



		    return "";

		}

	});



	 //Write HTML file to disc

	 book.save(dir + "sheet"+ i +".html", options);

}

{{< /highlight >}}

{{% alert color="primary" %}} 

Per ulteriori dettagli su questo miglioramento, si prega di consultare l'articolo su [Implementazione dell'interfaccia IFilePathProvider](/cells/it/java/fornire-il-percorso-del-file-html-della-cartella-di-lavoro-esportata-tramite-linterfaccia-ifilepathprovider/).

{{% /alert %}} 
### **Proprietà CopyOptions.ReferToDestinationSheet aggiunta e sovraccarico per il metodo Cells.copyRows.**
Aspose.Cells for Java API ha esposto il tipo Boolean CopyOptions.ReferToDestinationSheet insieme a un sovraccarico del metodo Cells.copyRows al fine di facilitare l'operazione di copia righe quando le righe da copiare contengono anche un grafico e il suo origine dei dati. Gli sviluppatori possono utilizzare queste nuove API per puntare l'origine dei dati del grafico ai fogli di lavoro di origine o destinazione.

Di seguito è riportato il semplice scenario d'uso.

**Java**

{{< highlight csharp >}}

 //Load a sample spreadsheet in an instance of Workbook

Workbook book = new Workbook(dir + "sample.xlsx");

//Access the worksheet containing the chart & its data source

Worksheet source = book.getWorksheets().get(0);

//Add a new worksheet to the collection

Worksheet destination = book.getWorksheets().get(book.getWorksheets().add());

//Initialize CopyOptions and set its ReferToDestinationSheet property to true

CopyOptions options = new CopyOptions();

options.setReferToDestinationSheet(true);

//Copy the rows

destination.getCells().copyRows(source.getCells(), 0, 0, source.getCells().getMaxDisplayRange().getRowCount(), options);

//Save the result on disc

book.save(dir + "output.xlsx");

{{< /highlight >}}

{{% alert color="primary" %}} 

Per ulteriori dettagli su questa funzionalità, si prega di consultare l'articolo su [Controllare l'origine dei dati del grafico durante la copia delle righe](/cells/it/java/change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range/).

{{% /alert %}} 
### **Aggiunta della proprietà CalculationOptions.Recursive**
Aspose.Cells for Java 8.9.1 ha esposto il tipo Boolean CalculationOptions.Recursive. Impostando il valore CalculationOptions.Recursive su true e passando l'oggetto al metodo Workbook.calculateFormula indica alle API di Aspose.Cells di calcolare in modo ricorsivo le celle dipendenti durante il calcolo delle celle che dipendono da altre celle.

Di seguito è riportato il semplice scenario d'uso.

**Java**

{{< highlight csharp >}}

 //Load a sample spreadsheet in an instance of Workbook

Workbook book = new Workbook(dir + "sample.xlsx");

//Initialize CalculationOptions & set Recursive property to true

CalculationOptions options = new CalculationOptions();

options.setRecursive(true);

//Recalculate formulas

book.calculateFormula(options);

{{< /highlight >}}

{{% alert color="primary" %}} 

Per ulteriori dettagli su questa funzionalità, si prega di consultare l'articolo su [Ottimizzare il tempo di calcolo](/cells/it/java/decrease-the-calculation-time-of-cell-calculate-method/).

{{% /alert %}}
## **API deprecate**
### **Proprietà CellsHelper.FontDir obsoleta**
Si consiglia di utilizzare il metodo FontConfigs.setFontFolder(String, boolean) con ricorsività della cartella impostata su false.
### **Proprietà CellsHelper.FontDirs obsoleta**
Utilizzare il metodo FontConfigs.setFontFolders(String[], boolean) con ricorsività della cartella impostata su false.
### **Proprietà Obsoleta CellsHelper.FontFiles**
Utilizzare invece il metodo FontConfigs.setFontSources(FontSourceBase[]).
