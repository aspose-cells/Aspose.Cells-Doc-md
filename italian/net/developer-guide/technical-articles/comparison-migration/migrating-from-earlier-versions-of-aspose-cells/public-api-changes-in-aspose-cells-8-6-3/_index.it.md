---
title: Pubblico API Modifiche Aspose.Cells 8.6.3
type: docs
weight: 220
url: /it/net/public-api-changes-in-aspose-cells-8-6-3/
---
{{% alert color="primary" %}} 

Questo documento descrive le modifiche allo Aspose.Cells API dalla versione 8.6.2 alla 8.6.3 che potrebbero interessare gli sviluppatori di moduli/applicazioni. Include non solo metodi pubblici nuovi e aggiornati, classi aggiunte, ma anche una descrizione di eventuali cambiamenti nel comportamento dietro le quinte in Aspose.Cells.

{{% /alert %}} 
## **API aggiunte**
### **Supporto per l'analisi HTML durante l'importazione dei dati**
Questa versione di Aspose.Cells for .NET API ha esposto la proprietà ImportTableOptions.IsHtmlString che indica a API di analizzare i tag HTML durante l'importazione dei dati nel foglio di lavoro e di impostare il risultato analizzato come valore della cella. Tieni presente che le API Aspose.Cells forniscono già Cell.HtmlString per eseguire questa attività per una singola cella, tuttavia, durante l'importazione di dati in blocco, ad esempio da un DataTable, la proprietà ImportTableOptions.IsHtmlString (se impostata su true) tenta di analizzare tutte le Tag HTML e imposta i risultati analizzati nelle celle corrispondenti.

Ecco lo scenario di utilizzo più semplice.

**C#**

{{< highlight "csharp" >}}

 //create an instance of ImportTableOptions

var importOptions = new ImportTableOptions();

//Set IsHtmlString to true so that the API can parse the HTML

importOptions.IsHtmlString = true;

//Import data from DataTable while passing instance of ImportTableOptions

cells.ImportData(table, 0, 0, importOptions);

{{< /highlight >}}


### **Metodo Workbook.CreateBuiltinStyle Aggiunto**
 Aspose.Cells for .NET 8.6.3 ha esposto il metodo Workbook.CreateBuiltinStyle che può essere utilizzato per creare un oggetto della classe Style che corrisponde ad una delle[stili incorporati offerti dall'applicazione Excel](/cells/it/net/using-built-in-styles/)Il metodo Workbook.CreateBuiltinStyle accetta una costante dall'enumerazione BuiltinStyleType. Si noti che con le versioni precedenti delle API Aspose.Cells, la stessa attività potrebbe essere eseguita tramite il metodo StyleCollection.CreateBuiltinStyle ma poiché le recenti versioni delle API Aspose.Cells hanno rimosso la classe StyleCollection, pertanto il metodo Workbook.CreateBuiltinStyle appena esposto può essere considerato come un approccio alternativo a ottenere lo stesso.

Di seguito è riportato il semplice scenario di utilizzo.

**C#**

{{< highlight "csharp" >}}

 //Create an instance of Workbook

//Optionally load a spreadsheet

var book = new Workbook();

//Create a built-in style of type Title

var style = book.CreateBuiltinStyle(BuiltinStyleType.Title);

{{< /highlight >}}


### **Metodo Cells.ImportGridView aggiunto**
Aspose.Cells for .NET 8.6.3 ha esposto una versione sovraccaricata di Cells.ImportGridView che ora può accettare un'istanza di ImportTableOptions per fornire un maggiore controllo sul processo di importazione.

Di seguito è riportato il semplice scenario di utilizzo.

**C#**

{{< highlight "csharp" >}}

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


### **Proprietà ImportTableOptions.ConvertGridStyle Aggiunta**
In riferimento ai miglioramenti sopra menzionati, l'ultima versione di Aspose.Cells for .NET API ha anche esposto la proprietà ImportTableOptions.ConvertGridStyle. Questa proprietà di tipo booleano consente agli sviluppatori di controllare l'aspetto dei dati importati, dove l'impostazione della proprietà ImportTableOptions.ConvertGridStyle su true indica che API applicherà lo stile di GridView alle celle in cui sono stati importati i dati.

Di seguito è riportato il semplice scenario di utilizzo.

**C#**

{{< highlight "csharp" >}}

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


### **Proprietà LoadDataOption.OnlyVisibleWorksheet aggiunta**
 Aspose.Cells for .NET 8.6.3 ha esposto la proprietà LoadDataOption.OnlyVisibleWorksheet che se impostata su true influenzerà il meccanismo di caricamento di Aspose.Cells for .NET API, di conseguenza verranno caricati solo i fogli di lavoro visibili da un determinato foglio di calcolo. Si prega di controllare[articolo dettagliato](/cells/it/net/different-ways-to-open-files/) su questo argomento.

Di seguito è riportato il semplice scenario di utilizzo.

**C#**

{{< highlight "csharp" >}}

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
## **API obsolete**
### **Metodo Worksheet.CopyConditionalFormatting Obsoleto**
In alternativa al metodo Worksheet.CopyConditionalFormatting, si consiglia di utilizzare uno dei metodi Cells.CopyRows o Range.Copy.
### **Immobile Cells.Fine Obsoleto**
Utilizzare la proprietà Cells.LastCell come alternativa alla proprietà Cells.End.
