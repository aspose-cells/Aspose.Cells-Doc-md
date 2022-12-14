---
title: Pubblico API Modifiche Aspose.Cells 8.6.3
type: docs
weight: 230
url: /it/java/public-api-changes-in-aspose-cells-8-6-3/
---
{{% alert color="primary" %}} 

Questo documento descrive le modifiche allo Aspose.Cells API dalla versione 8.6.2 alla 8.6.3 che potrebbero interessare gli sviluppatori di moduli/applicazioni. Include non solo metodi pubblici nuovi e aggiornati, classi aggiunte, ma anche una descrizione di eventuali cambiamenti nel comportamento dietro le quinte in Aspose.Cells.

{{% /alert %}} 
## **API aggiunte**
### **Supporto per l'analisi HTML durante l'importazione dei dati**
Questa versione di Aspose.Cells for Java API ha esposto l'attributo ImportTableOptions.setHtmlString che indica a API di analizzare i tag HTML durante l'importazione dei dati nel foglio di lavoro e di impostare il risultato analizzato come valore della cella. Tieni presente che le API Aspose.Cells forniscono già l'attributo Cell.setHtmlString per eseguire questa attività per una singola cella, tuttavia, durante l'importazione di dati in blocco, l'attributo ImportTableOptions.setHtmlString (se impostato su true) tenta di analizzare tutti i tag e i set HTML supportati i risultati analizzati nelle celle corrispondenti.

Ecco lo scenario di utilizzo più semplice.

**Java**

{{< highlight "csharp" >}}

 //create an instance of ImportTableOptions

ImportTableOptions importOptions = new ImportTableOptions();

//Set IsHtmlString to true so that the API can parse the HTML

importOptions.setHtmlString(true);

//Import data from DataTable while passing instance of ImportTableOptions

cells.importData(iTable, 0, 0, importOptions);

{{< /highlight >}}
### **Metodo Workbook.createBuiltinStyle Aggiunto**
Aspose.Cells for Java 8.6.3 ha esposto il metodo Workbook.createBuiltinStyle che può essere utilizzato per creare un oggetto della classe Style che corrisponde a una delle[stili incorporati offerti dall'applicazione Excel](/cells/it/java/using-built-in-styles/). Il metodo Workbook.createBuiltinStyle accetta una costante dall'enumerazione BuiltinStyleType. Si noti che con le versioni precedenti delle API Aspose.Cells, la stessa attività potrebbe essere eseguita tramite il metodo StyleCollection.createBuiltinStyle ma poiché le recenti versioni delle API Aspose.Cells hanno rimosso la classe StyleCollection, pertanto il metodo Workbook.createBuiltinStyle appena esposto può essere considerato un approccio alternativo a ottenere lo stesso.

Di seguito è riportato il semplice scenario di utilizzo.

**Java**

{{< highlight "csharp" >}}

 //Create an instance of Workbook

//Optionally load a spreadsheet

Workbook book = new Workbook();

//Create a built-in style of type Title

Style style = book.createBuiltinStyle(BuiltinStyleType.TITLE);

{{< /highlight >}}
### **Proprietà LoadDataOption.OnlyVisibleWorksheet aggiunta**
Aspose.Cells for Java 8.6.3 ha esposto la proprietà LoadDataOption.OnlyVisibleWorksheet che se impostata su true influenzerà il meccanismo di caricamento di Aspose.Cells for Java API, di conseguenza verranno caricati solo i fogli di lavoro visibili da un determinato foglio di calcolo.

Di seguito è riportato il semplice scenario di utilizzo.

**Java**

{{< highlight "csharp" >}}

 //Create an instance of LoadDataOption

LoadDataOption loadDataOptions = new LoadDataOption();

//Set OnlyVisibleWorksheet property to true

loadDataOptions.setOnlyVisibleWorksheet(true);

//Create an instance of LoadOptions

LoadOptions loadOptions = new LoadOptions();

//Set LoadDataOptions property to the instance of LoadDataOption created earlier

loadOptions.setLoadDataOptions(loadDataOptions);

//Create an instance of Workbook & load an existing spreadsheet

//while passing the instance of LoadOptions created earlier

Workbook book = new Workbook(inputFilePath, loadOptions);

{{< /highlight >}}
## **API obsolete**
### **Metodo Worksheet.copyConditionalFormatting Obsoleto**
In alternativa al metodo Worksheet.copyConditionalFormatting, si consiglia di utilizzare uno dei metodi Cells.copyRows o Range.copy.
### **Immobile Cells.Fine Obsoleto**
Utilizzare la proprietà Cells.LastCell come alternativa alla proprietà Cells.End.
