---
title: Modifiche all API pubblica in Aspose.Cells 8.6.3
type: docs
weight: 220
url: /it/net/public-api-changes-in-aspose-cells-8-6-3/
---

{{% alert color="primary" %}} 

Questo documento descrive le modifiche all'API di Aspose.Cells dalla versione 8.6.2 alla 8.6.3 che potrebbero interessare agli sviluppatori di moduli/applicazioni. Include non solo nuovi e aggiornati metodi pubblici, classi aggiunte, ma anche una descrizione di eventuali cambiamenti nel comportamento dietro le quinte in Aspose.Cells.

{{% /alert %}} 
## **API aggiunte**
### **Supporto per l'analisi HTML durante l'importazione dei dati**
Questa versione di Aspose.Cells for .NET API ha esposto la proprietà ImportTableOptions.IsHtmlString che indica all'API di analizzare i tag HTML durante l'importazione dei dati nel foglio di lavoro e impostare il risultato analizzato come valore della cella. Si prega di notare che le API Aspose.Cells forniscono già il metodo Cell.HtmlString per eseguire questo compito per una singola cella, tuttavia, durante l'importazione dati in blocco come da un DataTable, la proprietà ImportTableOptions.IsHtmlString (quando impostata su true) cerca di analizzare tutti i tag HTML supportati e imposta i risultati analizzati nelle celle corrispondenti.

Ecco il caso d'uso più semplice.

**C#**

{{< highlight csharp >}}

 //create an instance of ImportTableOptions

var importOptions = new ImportTableOptions();

//Set IsHtmlString to true so that the API can parse the HTML

importOptions.IsHtmlString = true;

//Import data from DataTable while passing instance of ImportTableOptions

cells.ImportData(table, 0, 0, importOptions);

{{< /highlight >}}


### **Metodo Workbook.CreateBuiltinStyle aggiunto**
Aspose.Cells for .NET 8.6.3 ha esposto il metodo Workbook.CreateBuiltinStyle che può essere utilizzato per creare un oggetto della classe Style corrispondente a uno dei [stili predefiniti offerti dall'applicazione Excel](/cells/it/net/using-built-in-styles/). Il metodo Workbook.CreateBuiltinStyle accetta una costante dall'enumerazione BuiltinStyleType. Si prega di notare, con le versioni precedenti delle API Aspose.Cells, lo stesso compito poteva essere svolto tramite il metodo StyleCollection.CreateBuiltinStyle ma poiché le versioni recenti delle API Aspose.Cells hanno rimosso la classe StyleCollection, il metodo Workbook.CreateBuiltinStyle appena esposto può essere considerato come un approccio alternativo per ottenere lo stesso risultato.

Di seguito è riportato il semplice scenario d'uso.

**C#**

{{< highlight csharp >}}

 //Create an instance of Workbook

//Optionally load a spreadsheet

var book = new Workbook();

//Create a built-in style of type Title

var style = book.CreateBuiltinStyle(BuiltinStyleType.Title);

{{< /highlight >}}


### **Metodo Cells.ImportGridView aggiunto**
Aspose.Cells for .NET 8.6.3 ha esposto una versione sovraccaricata del metodo Cells.ImportGridView che ora può accettare un'istanza di ImportTableOptions per avere maggiore controllo sul processo di importazione.

Di seguito è riportato il semplice scenario d'uso.

**C#**

{{< highlight csharp >}}

 //Create an instance of Workbook

//Optionally load a spreadsheet

var book = new Workbook();

//Retrieve the Cells collection of first Worksheet in Workbook

var cells = book.Worksheets[0].Cells;

//create an instance of ImportTableOptions & set its various properties

var importOptions = new ImportTableOptions();

importOptions.IsHtmlString = true;

importOptions.IsFieldNameShown = true;

//Import data from GridView while passing instance of ImportTableOptions

cells.ImportGridView(gridView, 0, 0, importOptions);

{{< /highlight >}}


### **Proprietà LoadDataOption.OnlyVisibleWorksheet aggiunta**
In riferimento alle migliorie sopra menzionate, l'ultima versione di Aspose.Cells for .NET API ha esposto anche la proprietà ImportTableOptions.ConvertGridStyle. Questa proprietà di tipo Boolean consente agli sviluppatori di controllare l'aspetto dei dati importati, impostando la proprietà ImportTableOptions.ConvertGridStyle su true indica che l'API applicherà lo stile del GridView alle celle in cui sono stati importati i dati.

Di seguito è riportato il semplice scenario d'uso.

**C#**

{{< highlight csharp >}}

 //Create an instance of Workbook

//Optionally load a spreadsheet

var book = new Workbook();

//Retrieve the Cells collection of first Worksheet in Workbook

var cells = book.Worksheets[0].Cells;

//create an instance of ImportTableOptions

var importOptions = new ImportTableOptions();

//Set ConvertGridStyle property to true

importOptions.ConvertGridStyle = true;



//Import data from GridView while passing instance of ImportTableOptions

cells.ImportGridView(gridView, 0, 0, importOptions);

{{< /highlight >}}


### **APIs Obsoleted**
Aspose.Cells for .NET 8.6.3 ha esposto la proprietà LoadDataOption.OnlyVisibleWorksheet che, impostandola su true, influenzerà il meccanismo di caricamento dell'API Aspose.Cells for .NET, di conseguenza verranno caricati solo i fogli di lavoro visibili da un determinato foglio di calcolo. Si prega di consultare l'[articolo dettagliato](/cells/it/net/different-ways-to-open-files/) su questo argomento.

Di seguito è riportato il semplice scenario d'uso.

**C#**

{{< highlight csharp >}}

 //Create an instance of LoadDataOption

var loadDataOptions = new LoadDataOption();

//Set OnlyVisibleWorksheet property to true

loadDataOptions.OnlyVisibleWorksheet = true;

//Create an instance of LoadOptions

var loadOptions = new LoadOptions();

//Set LoadDataOptions property to the instance of LoadDataOption created earlier

loadOptions.LoadDataOptions = loadDataOptions;



//Create an instance of Workbook & load an existing spreadsheet

//while passing the instance of LoadOptions created earlier

var book = new Workbook(inputFilePath, loadOptions);

{{< /highlight >}}
## **API deprecate**
### **Si prega di utilizzare la proprietà Cells.LastCell in alternativa alla proprietà Cells.End.**
Come alternativa al metodo Worksheet.CopyConditionalFormatting, si consiglia di utilizzare uno qualsiasi dei metodi Cells.CopyRows o Range.Copy.
### **Proprietà Cells.End resa obsoleta**
Si prega di utilizzare la proprietà Cells.LastCell come alternativa alla proprietà Cells.End.
