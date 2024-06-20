---
title: Modifiche all API pubblica in Aspose.Cells 8.9.1
type: docs
weight: 310
url: /it/net/public-api-changes-in-aspose-cells-8-9-1/
---

{{% alert color="primary" %}} 

Questo documento descrive le modifiche all'API Aspose.Cells dalla versione 8.9.0 alla 8.9.1 che potrebbero interessare agli sviluppatori dei moduli/applicazioni. Include non solo nuovi metodi pubblici e aggiornati, classi aggiunte e rimosse, ma anche una descrizione di eventuali modifiche nel comportamento dietro le quinte in Aspose.Cells.

{{% /alert %}} 
## **API aggiunte**
### **Sorgenti dei caratteri configurabili**
Aspose.Cells for .NET ha esposto una serie di classi per fornire il supporto per le fonti di caratteri configurabili per la visualizzazione dei fogli di calcolo. Ecco l'elenco delle classi aggiunte con Aspose.Cells for .NET 8.9.1.

1. La classe FontConfigs specifica le impostazioni del carattere.
1. La classe FontSourceBase è una classe di base astratta per le classi che consentono all'utente di specificare varie fonti di caratteri.
1. La classe FileFontSource rappresenta il singolo file di caratteri TrueType memorizzato nel file system.
1. La classe FolderFontSource rappresenta la cartella che contiene file di caratteri TrueType.
1. La classe MemoryFontSource rappresenta il singolo file di caratteri TrueType memorizzato in memoria.
1. L'enumerazione FontSourceType specifica il tipo di una fonte di caratteri.

Con le modifiche sopra menzionate, il Aspose.Cells for .NET consente di impostare i caratteri come dettagliato di seguito.

1. Imposta una cartella di caratteri personalizzata durante l'utilizzo del metodo FontConfigs.SetFontFolder.
1. Imposta più cartelle di caratteri personalizzate durante l'utilizzo del metodo FontConfigs.SetFontFolders.
1. Imposta le fonti di caratteri da una cartella di caratteri personalizzata, un singolo file di caratteri o dati di caratteri da un array di byte durante l'utilizzo del metodo FontConfigs.SetFontSources.

Ecco uno scenario di utilizzo semplice dei metodi menzionati in precedenza.

**C#**

{{< highlight csharp >}}

 // Defining string variables to store paths to font folders & font file

string fontFolder1 = "D:/Arial";

string fontFolder2 = "D:/Calibri";

string fontFile = "D:/Arial/arial.ttf";

// Setting first font folder with SetFontFolder method

// Second parameter directs the API to search the subfolders for font files

FontConfigs.SetFontFolder(fontFolder1, true);

// Setting both font folders with SetFontFolders method

// Second parameter prohibits the API to search the subfolders for font files

FontConfigs.SetFontFolders(new string[] { fontFolder1, fontFolder2 }, false);

// Defining FolderFontSource

FolderFontSource sourceFolder = new FolderFontSource(fontFolder1, false);

// Defining FileFontSource

FileFontSource sourceFile = new FileFontSource(fontFile);

// Defining MemoryFontSource

MemoryFontSource sourceMemory = new MemoryFontSource(System.IO.File.ReadAllBytes(fontFile));

//Setting font sources

FontConfigs.SetFontSources(new FontSourceBase[] { sourceFolder, sourceFile, sourceMemory});

{{< /highlight >}}

{{% alert color="primary" %}} 

Entrambi i metodi FontConfigs.SetFontFolder e FontConfigs.SetFontFolders accettano un secondo parametro di tipo Boolean. Passare true come secondo parametro indirizzerà le API Aspose.Cells a cercare le sottocartelle per i file dei caratteri.

{{% /alert %}} 

Aspose.Cells for .NET consente anche di configurare la sostituzione dei caratteri. Questo meccanismo è utile quando un carattere richiesto non è disponibile sulla macchina dove deve avvenire la conversione. Gli utenti possono fornire un elenco di nomi di caratteri come alternativa al carattere originariamente richiesto. Per ottenere questo, le API Aspose.Cells hanno esposto il metodo FontConfigs.SetFontSubstitutes che accetta 2 parametri. Il primo parametro è di tipo stringa, che dovrebbe essere il nome del carattere che deve essere sostituito. Il secondo parametro è un array di tipo stringa. Gli utenti possono fornire un elenco di nomi di caratteri come sostituzione al nome del carattere originale (specificato nel primo parametro).

Ecco uno scenario di utilizzo semplice del metodo FontConfigs.SetFontSubstitutes.

**C#**

{{< highlight csharp >}}

 // Substituting the Arial font with Times New Roman & Calibri

FontConfigs.SetFontSubstitutes("Arial", new string[] { "Times New Roman", "Calibri" });

{{< /highlight >}}



Il Aspose.Cells for .NET ha inoltre fornito i mezzi per raccogliere informazioni su quali fonti e sostituzioni sono state impostate.

1. Il metodo FontConfigs.GetFontSources restituisce un array di tipo FontSourceBase contenente l'elenco delle fonti di caratteri specificate. Nel caso in cui non siano state impostate fonti, il metodo FontConfigs.GetFontSources restituirà un array vuoto.
1. Il metodo FontConfigs.GetFontSubstitutes accetta un parametro di tipo stringa che consente di specificare il nome del carattere per il quale è stata impostata una sostituzione. Nel caso in cui non sia stata impostata alcuna sostituzione per il nome del carattere specificato, il metodo FontConfigs.GetFontSubstitutes restituirà null.

{{% alert color="primary" %}} 

Per maggiori dettagli su FontConfigs, consultare l'articolo su [Configurazione dei caratteri per la visualizzazione dei fogli elettronici](/cells/it/net/configuring-fonts-for-rendering-spreadsheets/).

{{% /alert %}} 
### **Aggiunta dell'interfaccia IFilePathProvider e della proprietà HtmlSaveOptions.FilePathProvider**
Aspose.Cells for .NET 8.9.1 consente di ottenere/impostare l'interfaccia IFilePathProvider per esportare i fogli di lavoro in file HTML separati. Queste nuove API sono utili in scenari in cui i collegamenti ipertestuali in un foglio di lavoro puntano a una posizione in un altro foglio di lavoro, e l'esigenza dell'applicazione è quella di renderizzare ciascun foglio di lavoro in un file HTML separato. Implementando l'interfaccia IFilePathProvider è possibile mantenere i suddetti collegamenti ipertestuali integri, indipendentemente dal fatto che puntino a una posizione in un file HTML risultante separato.

Di seguito è riportato il semplice scenario di utilizzo della proprietà HtmlSaveOptions.FilePathProvider.

**C#**

{{< highlight csharp >}}

 // Load a spreadsheet in an instance of Workbook

var book = new Workbook(dir + "sample.xlsx");

// Save each Worksheet to separate HTML file

for (int i = 0; i < book.Worksheets.Count; i++)

{

    book.Worksheets.ActiveSheetIndex = i;

    // Create an instance of HtmlSaveOptions & set FilePathProvider property

    var options = new HtmlSaveOptions

    {

        ExportActiveWorksheetOnly = true,

        FilePathProvider = new FilePathProvider()

    };

    // Write HTML file to disc

    book.Save(dir + string.Format(@"sheet{0}.html", i), options);

}

{{< /highlight >}}



Ecco come implementare l'interfaccia IFilePathProvider.

**C#**

{{< highlight csharp >}}

 public class FilePathProvider : IFilePathProvider

{

    public FilePathProvider()

    {

    }

    /// <summary>

    /// Gets the full path of the file by Worksheet name when exporting Worksheet to html separately.

    /// So the references among the Worksheets can be exported correctly.

    /// </summary>

    /// <param name="sheetName">Worksheet name</param>

    /// <returns>the full path of the file</returns>

    public string GetFullName(string sheetName)

    {

        if ("Sheet2".Equals(sheetName))

        {

            return "sheet1.html";

        }

        else if ("Sheet3".Equals(sheetName))

        {

            return "sheet2.html";

        }

        return "";

    }

}

{{< /highlight >}}

{{% alert color="primary" %}} 

Per maggiori dettagli su questo miglioramento, consultare l'articolo su [Implementare l'interfaccia IFilePathProvider](/cells/it/net/provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface/).

{{% /alert %}} 
### **Aggiunta della proprietà CopyOptions.ReferToDestinationSheet e sovraccarico per il metodo Cells.CopyRows**
Aspose.Cells for .NET API ha esposto la proprietà di tipo booleano CopyOptions.ReferToDestinationSheet insieme a un sovraccarico del metodo Cells.CopyRows al fine di facilitare l'operazione di copia delle righe quando le righe da copiare contengono anche un grafico e il relativo origine dati. Gli sviluppatori possono utilizzare queste nuove API per puntare l'origine dati del grafico ai fogli di lavoro di origine o destinazione.

Di seguito è riportato il semplice scenario d'uso.

**C#**

{{< highlight csharp >}}

 // Load a sample spreadsheet in an instance of Workbook

var book = new Workbook(dir + "sample.xlsx");

// Access the worksheet containing the chart & its data source

var source = book.Worksheets[0];

// Add a new worksheet to the collection

var destination = book.Worksheets[book.Worksheets.Add()];

// Initialize CopyOptions and set its ReferToDestinationSheet property to true

CopyOptions options = new CopyOptions();

options.ReferToDestinationSheet = true;

// Copy the rows

destination.Cells.CopyRows(source.Cells, 0, 0, source.Cells.MaxDisplayRange.RowCount, options);

// Save the result on disc

book.Save(dir + "output.xlsx");

{{< /highlight >}}

{{% alert color="primary" %}} 

Per maggiori dettagli su questa funzionalità, consultare l'articolo su [Controllare l'origine dati del grafico durante la copia delle righe](/cells/it/net/change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range/).

{{% /alert %}} 
### **Aggiunta della proprietà CalculationOptions.Recursive**
Aspose.Cells for .NET 8.9.1 ha esposto la proprietà di tipo booleano CalculationOptions.Recursive. Impostando la proprietà CalculationOptions.Recursive su true e passando l'oggetto al metodo Workbook.CalculateFormula, le API di Aspose.Cells calcoleranno in modo ricorsivo le celle dipendenti quando calcolano le celle che dipendono da altre celle.

Di seguito è riportato il semplice scenario d'uso.

**C#**

{{< highlight csharp >}}

 // Load a sample spreadsheet in an instance of Workbook

var book = new Workbook(dir + "sample.xlsx");

// Initialize CalculationOptions & set Recursive property to true

var options = new CalculationOptions();

options.Recursive = true;

// Recalculate formulas

book.CalculateFormula(options);

{{< /highlight >}}

{{% alert color="primary" %}} 

Per maggiori dettagli su questa funzionalità, consultare l'articolo su [Ottimizzare il tempo di calcolo](/cells/it/net/decrease-the-calculation-time-of-cell-calculate-method/).

{{% /alert %}}
## **API deprecate**
### **Proprietà CellsHelper.FontDir obsoleta**
Si consiglia di utilizzare il metodo FontConfigs.SetFontFolder(string, bool) con ricorsività della cartella impostata su false.
### **Proprietà CellsHelper.FontDirs obsoleta**
Utilizzare il metodo FontConfigs.SetFontFolders(string[], bool) con ricorsività della cartella impostata su false al posto.
### **Proprietà Obsoleta CellsHelper.FontFiles**
Utilizzare invece il metodo FontConfigs.SetFontSources(FontSourceBase[]).
