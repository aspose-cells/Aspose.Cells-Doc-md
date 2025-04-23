---
title: Modifiche all API pubblica in Aspose.Cells 8.6.3
type: docs
weight: 230
url: /it/java/public-api-changes-in-aspose-cells-8-6-3/
---

{{% alert color="primary" %}} 

Questo documento descrive le modifiche all'API di Aspose.Cells dalla versione 8.6.2 alla 8.6.3 che potrebbero interessare agli sviluppatori di moduli/applicazioni. Include non solo nuovi e aggiornati metodi pubblici, classi aggiunte, ma anche una descrizione di eventuali cambiamenti nel comportamento dietro le quinte in Aspose.Cells.

{{% /alert %}} 
## **API aggiunte**
### **Supporto per l'analisi HTML durante l'importazione dei dati**
Questo rilascio dell'API Aspose.Cells for Java ha esposto l'attributo ImportTableOptions.setHtmlString che indica all'API di analizzare i tag HTML durante l'importazione dei dati nel foglio di lavoro e di impostare il risultato analizzato come valore della cella.

Ecco il caso d'uso più semplice.

**Java**

{{< highlight csharp >}}

 //create an instance of ImportTableOptions

ImportTableOptions importOptions = new ImportTableOptions();

//Set IsHtmlString to true so that the API can parse the HTML

importOptions.setHtmlString(true);

//Import data from DataTable while passing instance of ImportTableOptions

cells.importData(iTable, 0, 0, importOptions);

{{< /highlight >}}
### **Aggiunto il metodo Workbook.createBuiltinStyle**
Aspose.Cells for Java 8.6.3 ha esposto il metodo Workbook.createBuiltinStyle che può essere utilizzato per creare un oggetto della classe Style corrispondente a uno degli stili predefiniti offerti dall'applicazione Excel.

Di seguito è riportato il semplice scenario d'uso.

**Java**

{{< highlight csharp >}}

 //Create an instance of Workbook

//Optionally load a spreadsheet

Workbook book = new Workbook();

//Create a built-in style of type Title

Style style = book.createBuiltinStyle(BuiltinStyleType.TITLE);

{{< /highlight >}}
### **Aggiunta la proprietà LoadDataOption.OnlyVisibleWorksheet**
Aspose.Cells for Java 8.6.3 ha esposto la proprietà LoadDataOption.OnlyVisibleWorksheet che influenzerà il meccanismo di caricamento dell'API, facendo sì che vengano caricati solo i fogli di lavoro visibili da un determinato foglio di calcolo.

Di seguito è riportato il semplice scenario d'uso.

**Java**

{{< highlight csharp >}}

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
## **API deprecate**
### **Metodo Workbook.copyConditionalFormatting reso obsoleto**
Come alternativa al metodo Worksheet.copyConditionalFormatting, è consigliabile utilizzare uno qualsiasi dei metodi Cells.copyRows o Range.copy.
### **Proprietà Cells.End resa obsoleta**
Si prega di utilizzare la proprietà Cells.LastCell come alternativa alla proprietà Cells.End.
{{< app/cells/assistant language="java" >}}
