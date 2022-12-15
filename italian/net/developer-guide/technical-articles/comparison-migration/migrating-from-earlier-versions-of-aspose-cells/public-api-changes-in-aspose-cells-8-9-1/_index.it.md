---
title: Modifiche all'API pubblica in Aspose.Cells 8.9.1
type: docs
weight: 310
url: /it/net/public-api-changes-in-aspose-cells-8-9-1/
---
{{% alert color="primary" %}} 

Questo documento descrive le modifiche all'API Aspose.Cells dalla versione 8.9.0 alla 8.9.1 che potrebbero interessare gli sviluppatori di moduli/applicazioni. Include non solo metodi pubblici nuovi e aggiornati, classi aggiunte e rimosse ecc., ma anche una descrizione di eventuali cambiamenti nel comportamento dietro le quinte in Aspose.Cells.

{{% /alert %}} 
## **API aggiunte**
### **Fonti di caratteri configurabili**
Aspose.Cells for .NET ha esposto un numero di classi per fornire il supporto per fonti di font configurabili per il rendering di fogli di calcolo. Ecco l'elenco delle classi che sono state aggiunte con Aspose.Cells for .NET 8.9.1.

1. La classe FontConfigs specifica le impostazioni dei caratteri.
1. La classe FontSourceBase è una classe di base astratta per le classi che consentono all'utente di specificare varie fonti di font.
1. La classe FileFontSource rappresenta il singolo file di font TrueType memorizzato nel file system.
1. La classe FolderFontSource rappresenta la cartella che contiene i file dei caratteri TrueType.
1. La classe MemoryFontSource rappresenta il singolo file di font TrueType archiviato in memoria.
1. L'enumerazione FontSourceType specifica il tipo di un'origine font.

Con le modifiche sopra menzionate, Aspose.Cells for .NET consente di impostare i caratteri come descritto di seguito.

1. Imposta una cartella di caratteri personalizzati durante l'utilizzo del metodo FontConfigs.SetFontFolder.
1. Imposta più cartelle di caratteri personalizzati durante l'utilizzo del metodo FontConfigs.SetFontFolders.
1. Imposta le origini dei caratteri da una cartella di caratteri personalizzata, un singolo file di caratteri o dati di caratteri da una matrice di byte durante l'utilizzo del metodo FontConfigs.SetFontSources.

Ecco un semplice scenario di utilizzo dei metodi di cui sopra.

**C#**

{{< highlight "csharp" >}}

 // Defining string variables to store paths to font folders & font file

string fontFolder1 = "D:/Arial";

string fontFolder2 = "D:/Calibri";

string fontFile = "D:/Arial/arial.ttf";

// Setting first font folder with SetFontFolder method

// Second parameter directs the API to search the subfolders for font files

FontConfigs.SetFontFolder(fontFolder1, true);

// Setting both font folders with SetFontFolders method

// Second parameter prohibits the API to search the subfolders for font files

FontConfigs.SetFontFolders(new string[]{ fontFolder1, fontFolder2 }, false);

// Defining FolderFontSource

FolderFontSource sourceFolder = new FolderFontSource(fontFolder1, false);

// Defining FileFontSource

FileFontSource sourceFile = new FileFontSource(fontFile);

// Defining MemoryFontSource

MemoryFontSource sourceMemory = new MemoryFontSource(System.IO.File.ReadAllBytes(fontFile));

//Setting font sources

FontConfigs.SetFontSources(new FontSourceBase[]{ sourceFolder, sourceFile, sourceMemory});

{{< /highlight >}}

{{% alert color="primary" %}} 

Entrambi i metodi FontConfigs.SetFontFolder e FontConfigs.SetFontFolders accettano un secondo parametro di tipo booleano. Il passaggio di true come secondo parametro indirizzerà le API Aspose.Cells a cercare nelle sottocartelle i file dei caratteri.

{{% /alert %}} 

Aspose.Cells for .NET permette anche di configurare la sostituzione dei caratteri. Questo meccanismo è utile quando un font richiesto non è disponibile sulla macchina in cui deve avvenire la conversione. Gli utenti possono fornire un elenco di nomi di caratteri in alternativa al carattere originariamente richiesto. Per ottenere ciò, le API Aspose.Cells hanno esposto il metodo FontConfigs.SetFontSubstitutes che accetta 2 parametri. Il primo parametro è di tipo stringa, che dovrebbe essere il nome del carattere che deve essere sostituito. Il secondo parametro è un array di tipo stringa. Gli utenti possono fornire un elenco di nomi di font in sostituzione del nome del font originale (specificato nel primo parametro).

Ecco un semplice scenario di utilizzo del metodo FontConfigs.SetFontSubstitutes.

**C#**

{{< highlight "csharp" >}}

 // Substituting the Arial font with Times New Roman & Calibri

FontConfigs.SetFontSubstitutes("Arial", new string[]{ "Times New Roman", "Calibri" });

{{< /highlight >}}



Lo Aspose.Cells for .NET ha anche fornito mezzi per raccogliere informazioni su quali fonti e sostituzioni sono state impostate.

1. Il metodo FontConfigs.GetFontSources restituisce una matrice di tipo FontSourceBase contenente l'elenco delle origini dei caratteri specificate. Nel caso in cui non sia stata impostata alcuna origine, il metodo FontConfigs.GetFontSources restituirà un array vuoto.
1. Il metodo FontConfigs.GetFontSubstitutes accetta un parametro di tipo stringa che consente di specificare il nome del font per il quale è stata impostata una sostituzione. Nel caso in cui non sia stata impostata alcuna sostituzione per il nome del carattere specificato, il metodo FontConfigs.GetFontSubstitutes restituirà null.

{{% alert color="primary" %}} 

 Per maggiori dettagli su FontConfigs, consultare l'articolo su[Configurazione dei caratteri per il rendering di fogli di calcolo](/cells/it/net/configuring-fonts-for-rendering-spreadsheets/).

{{% /alert %}} 
### **Aggiunta interfaccia IFilePathProvider e proprietà HtmlSaveOptions.FilePathProvider**
Aspose.Cells for .NET 8.9.1 consente di ottenere/impostare IFilePathProvider per l'esportazione di fogli di lavoro in file HTML separati. Queste nuove API sono utili negli scenari in cui i collegamenti ipertestuali in un foglio di lavoro puntano a una posizione in un altro foglio di lavoro, dove il requisito dell'applicazione è quello di eseguire il rendering di ogni foglio di lavoro in un file HTML separato. L'implementazione di IFilePathProvider consente di mantenere intatti i suddetti collegamenti ipertestuali indipendentemente dal fatto che puntino a una posizione in un file HTML risultante separato.

Di seguito è riportato il semplice scenario di utilizzo della proprietà HtmlSaveOptions.FilePathProvider.

**C#**

{{< highlight "csharp" >}}

 // Carica un foglio di calcolo in un'istanza di Workbook

var book = new Workbook(dir + "sample.xlsx");

// Salva ogni foglio di lavoro in un file HTML separato

 per (int i = 0; i< book.Worksheets.Count; i++)

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

{{< highlight "csharp" >}}

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

 Per ulteriori dettagli su questo miglioramento, consultare l'articolo su[Implementazione dell'interfaccia IFilePathProvider](/cells/it/net/provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface/).

{{% /alert %}} 
### **Aggiunta proprietà CopyOptions.ReferToDestinationSheet e sovraccarico per il metodo Cells.CopyRows**
Aspose.Cells for .NET L'API ha esposto la proprietà CopyOptions.ReferToDestinationSheet di tipo booleano insieme al metodo un overload di Cells.CopyRows per facilitare l'operazione di copia delle righe quando le righe da copiare contengono anche un grafico e la sua origine dati. Gli sviluppatori possono utilizzare queste nuove API per indirizzare l'origine dati del grafico ai fogli di lavoro di origine o di destinazione.

Di seguito è riportato il semplice scenario di utilizzo.

**C#**

{{< highlight "csharp" >}}

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

 Per maggiori dettagli su questa funzione, consultare l'articolo su[Controlla l'origine dati del grafico durante la copia delle righe](/cells/it/net/change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range/).

{{% /alert %}} 
### **Aggiunta la proprietà CalculationOptions.Recursive**
Aspose.Cells for .NET 8.9.1 ha esposto la proprietà CalculationOptions.Recursive di tipo booleano. L'impostazione della proprietà CalculationOptions.Recursive su true e il passaggio dell'oggetto al metodo Workbook.CalculateFormula indica alle API Aspose.Cells di calcolare le celle dipendenti in modo ricorsivo durante il calcolo delle celle che dipendono da altre celle.

Di seguito è riportato il semplice scenario di utilizzo.

**C#**

{{< highlight "csharp" >}}

 // Load a sample spreadsheet in an instance of Workbook

var book = new Workbook(dir + "sample.xlsx");

// Initialize CalculationOptions & set Recursive property to true

var options = new CalculationOptions();

options.Recursive = true;

// Recalculate formulas

book.CalculateFormula(options);

{{< /highlight >}}

{{% alert color="primary" %}} 

 Per maggiori dettagli su questa funzione, consultare l'articolo su[Ottimizza il tempo di calcolo](/cells/it/net/decrease-the-calculation-time-of-cell-calculate-method/).

{{% /alert %}}
## **API obsolete**
### **Proprietà CellsHelper.FontDir obsoleta**
Si consiglia invece di utilizzare il metodo FontConfigs.SetFontFolder(string, bool) con folder recursive to false.
### **Proprietà CellsHelper.FontDirs obsoleta**
Utilizzare invece il metodo FontConfigs.SetFontFolders(string[], bool) con la cartella ricorsiva su false.
### **Proprietà CellsHelper.FontFiles obsoleta**
Utilizzare invece il metodo FontConfigs.SetFontSources(FontSourceBase[]).
