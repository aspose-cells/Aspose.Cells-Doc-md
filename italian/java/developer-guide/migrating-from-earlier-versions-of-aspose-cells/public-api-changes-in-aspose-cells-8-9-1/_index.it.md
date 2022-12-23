---
title: Pubblico API Modifiche Aspose.Cells 8.9.1
type: docs
weight: 320
url: /it/java/public-api-changes-in-aspose-cells-8-9-1/
---
{{% alert color="primary" %}} 

Questo documento descrive le modifiche allo Aspose.Cells API dalla versione 8.9.0 alla 8.9.1 che potrebbero interessare gli sviluppatori di moduli/applicazioni. Include non solo metodi pubblici nuovi e aggiornati, classi aggiunte e rimosse ecc., ma anche una descrizione di eventuali cambiamenti nel comportamento dietro le quinte in Aspose.Cells.

{{% /alert %}} 
## **API aggiunte**
### **Fonti di caratteri configurabili**
Aspose.Cells for Java ha esposto un numero di classi per fornire il supporto per fonti di font configurabili per il rendering di fogli di calcolo. Ecco l'elenco delle classi che sono state aggiunte con Aspose.Cells for Java 8.9.1.

1. La classe FontConfigs specifica le impostazioni dei caratteri.
1. La classe FontSourceBase è una classe di base astratta per le classi che consentono all'utente di specificare varie fonti di font.
1. La classe FileFontSource rappresenta il singolo file di font TrueType memorizzato nel file system.
1. La classe FolderFontSource rappresenta la cartella che contiene i file dei caratteri TrueType.
1. La classe MemoryFontSource rappresenta il singolo file di font TrueType archiviato in memoria.
1. L'enumerazione FontSourceType specifica il tipo di un'origine font.

Con le modifiche sopra menzionate, Aspose.Cells for Java consente di impostare i caratteri come descritto di seguito.

1. Imposta una cartella di caratteri personalizzati durante l'utilizzo del metodo FontConfigs.setFontFolder.
1. Imposta più cartelle di caratteri personalizzati durante l'utilizzo del metodo FontConfigs.setFontFolders.
1. Imposta le origini dei caratteri da una cartella di caratteri personalizzata, un singolo file di caratteri o dati di caratteri da una matrice di byte durante l'utilizzo del metodo FontConfigs.setFontSources.

Ecco un semplice scenario di utilizzo dei metodi di cui sopra.

**Java**

{{< highlight "csharp" >}}

 //Defining string variables to store paths to font folders & font file

String fontFolder1 = "D:/Arial";

String fontFolder2 = "D:/Calibri";

String fontFile = "D:/Arial/arial.ttf";

//Setting first font folder with setFontFolder method

//Second parameter directs the API to search the sub folders for font files

FontConfigs.setFontFolder(fontFolder1, true);

//Setting both font folders with setFontFolders method

//Second parameter prohibits the API to search the sub folders for font files

FontConfigs.setFontFolders(new String[]{ fontFolder1, fontFolder2 }, false);

//Defining FolderFontSource

FolderFontSource sourceFolder = new FolderFontSource(fontFolder1, false);

//Defining FileFontSource

FileFontSource sourceFile = new FileFontSource(fontFile);

//Defining MemoryFontSource

byte[]bytes = Files.readAllBytes(new File(fontFile).toPath());

MemoryFontSource sourceMemory = new MemoryFontSource(bytes);

//Setting font sources

FontConfigs.setFontSources(new FontSourceBase[]{ sourceFolder, sourceFile, sourceMemory});

{{< /highlight >}}

{{% alert color="primary" %}} 

 Entrambi i metodi FontConfigs.setFontFolder e FontConfigs.setFontFolders accettano un secondo parametro di tipo booleano. Il passaggio di true come secondo parametro indirizzerà le API Aspose.Cells a cercare nelle sottocartelle i file dei caratteri.

{{% /alert %}} 

Aspose.Cells for Java permette anche di configurare la sostituzione dei caratteri. Questo meccanismo è utile quando un font richiesto non è disponibile sulla macchina in cui deve avvenire la conversione. Gli utenti possono fornire un elenco di nomi di caratteri in alternativa al carattere originariamente richiesto. Per ottenere ciò, le API Aspose.Cells hanno esposto il metodo FontConfigs.setFontSubstitutes che accetta 2 parametri. Il primo parametro è di tipo stringa, che dovrebbe essere il nome del carattere che deve essere sostituito. Il secondo parametro è un array di tipo stringa. Gli utenti possono fornire un elenco di nomi di font in sostituzione del nome del font originale (specificato nel primo parametro).

Ecco un semplice scenario di utilizzo del metodo FontConfigs.SetFontSubstitutes.

**Java**

{{< highlight "csharp" >}}

 //Substituting the Arial font with Times New Roman & Calibri

FontConfigs.setFontSubstitutes("Arial", new String[]{ "Times New Roman", "Calibri" });

{{< /highlight >}}

Lo Aspose.Cells for Java ha anche fornito mezzi per raccogliere informazioni su quali fonti e sostituzioni sono state impostate.

1. Il metodo FontConfigs.getFontSources restituisce un array di tipo FontSourceBase contenente l'elenco delle origini dei font specificate. Nel caso in cui non sia stata impostata alcuna origine, il metodo FontConfigs.getFontSources restituirà un array vuoto.
1. Il metodo FontConfigs.getFontSubstitutes accetta un parametro di tipo stringa che consente di specificare il nome del font per il quale è stata impostata una sostituzione. Nel caso in cui non sia stata impostata alcuna sostituzione per il nome del font specificato, il metodo FontConfigs.getFontSubstitutes restituirà null.

{{% alert color="primary" %}} 

 Per maggiori dettagli su FontConfigs, consultare l'articolo su[Configurazione dei caratteri per il rendering di fogli di calcolo](/cells/it/java/configuring-fonts-for-rendering-spreadsheets/).

{{% /alert %}} 
### **Aggiunta interfaccia IFilePathProvider e proprietà HtmlSaveOptions.FilePathProvider**
Aspose.Cells for Java 8.9.1 consente di ottenere/impostare IFilePathProvider per l'esportazione di fogli di lavoro in file HTML separati. Queste nuove API sono utili negli scenari in cui i collegamenti ipertestuali in un foglio di lavoro puntano a una posizione in un altro foglio di lavoro, in cui il requisito dell'applicazione è eseguire il rendering di ogni foglio di lavoro in un file HTML separato. L'implementazione di IFilePathProvider consente di mantenere intatti i suddetti collegamenti ipertestuali indipendentemente dal fatto che puntino a una posizione in un file HTML risultante separato.

Di seguito è riportato il semplice scenario di utilizzo della proprietà HtmlSaveOptions.FilePathProvider.

**Java**

{{< highlight "csharp" >}}

 //Carica un foglio di calcolo in un'istanza di Workbook

Libro della cartella di lavoro = nuova cartella di lavoro (dir + "sample.xlsx");

//Salva ciascun foglio di lavoro in un file HTML separato

 per (int i = 0; i< book.getWorksheets().getCount(); i++)

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

 Per ulteriori dettagli su questo miglioramento, consultare l'articolo su[Implementazione dell'interfaccia IFilePathProvider](/cells/it/java/provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface/).

{{% /alert %}} 
### **Aggiunta proprietà CopyOptions.ReferToDestinationSheet e sovraccarico per il metodo Cells.copyRows**
Aspose.Cells for Java API ha esposto la proprietà CopyOptions.ReferToDestinationSheet di tipo booleano insieme al metodo un overload di Cells.copyRows per facilitare l'operazione di copia delle righe quando le righe da copiare contengono anche un grafico e la sua origine dati. Gli sviluppatori possono utilizzare queste nuove API per indirizzare l'origine dati del grafico ai fogli di lavoro di origine o di destinazione.

Di seguito è riportato il semplice scenario di utilizzo.

**Java**

{{< highlight "csharp" >}}

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

 Per maggiori dettagli su questa funzione, consultare l'articolo su[Controlla l'origine dati del grafico durante la copia delle righe](/cells/it/java/change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range/).

{{% /alert %}} 
### **Aggiunta la proprietà CalculationOptions.Recursive**
Aspose.Cells for Java 8.9.1 ha esposto la proprietà CalculationOptions.Recursive di tipo booleano. L'impostazione della proprietà CalculationOptions.Recursive su true e il passaggio dell'oggetto al metodo Workbook.calculateFormula indica alle API Aspose.Cells di calcolare le celle dipendenti in modo ricorsivo durante il calcolo delle celle che dipendono da altre celle.

Di seguito è riportato il semplice scenario di utilizzo.

**Java**

{{< highlight "csharp" >}}

 //Load a sample spreadsheet in an instance of Workbook

Workbook book = new Workbook(dir + "sample.xlsx");

//Initialize CalculationOptions & set Recursive property to true

CalculationOptions options = new CalculationOptions();

options.setRecursive(true);

//Recalculate formulas

book.calculateFormula(options);

{{< /highlight >}}

{{% alert color="primary" %}} 

 Per maggiori dettagli su questa funzione, consultare l'articolo su[Ottimizza il tempo di calcolo](/cells/it/java/decrease-the-calculation-time-of-cell-calculate-method/).

{{% /alert %}}
## **API obsolete**
### **Proprietà CellsHelper.FontDir obsoleta**
Si consiglia invece di utilizzare il metodo FontConfigs.setFontFolder(String, boolean) con folder recursive to false.
### **Proprietà CellsHelper.FontDirs obsoleta**
Utilizzare invece il metodo FontConfigs.setFontFolders(String[], boolean) con la cartella ricorsiva su false.
### **Proprietà CellsHelper.FontFiles obsoleta**
Utilizzare invece il metodo FontConfigs.setFontSources(FontSourceBase[]).
