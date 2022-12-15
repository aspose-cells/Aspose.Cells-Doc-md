---
title: Modifiche all'API pubblica in Aspose.Cells 8.9.0
type: docs
weight: 300
url: /it/net/public-api-changes-in-aspose-cells-8-9-0/
---
{{% alert color="primary" %}} 

Questo documento descrive le modifiche all'API Aspose.Cells dalla versione 8.8.3 alla 8.9.0 che potrebbero interessare gli sviluppatori di moduli/applicazioni. Include non solo metodi pubblici nuovi e aggiornati, classi aggiunte e rimosse ecc., ma anche una descrizione di eventuali cambiamenti nel comportamento dietro le quinte in Aspose.Cells.

{{% /alert %}} 
## **API aggiunte**
### **Aggiunta proprietà HtmlSaveOptions.DefaultFontName**
Aspose.Cells for .NET 8.9.0 ha esposto la proprietà DefaultFontName per la classe HtmlSaveOptions che consente di specificare il nome del carattere predefinito durante il rendering dei fogli di calcolo in formato HTML. Il carattere predefinito verrà utilizzato solo quando il carattere di stile non esiste. Il valore predefinito della proprietà HtmlSaveOptions.DefaultFontName è null, il che significa che l'API Aspose.Cells for .NET utilizzerà il carattere universale che ha la stessa famiglia del carattere originale.

{{% alert color="primary" %}} 

 Per maggiori dettagli su questa funzione, consultare l'articolo su[Impostazione del carattere predefinito per il rendering di fogli di calcolo in formato HTML](/cells/it/net/set-default-font-while-rendering-spreadsheet-to/).

{{% /alert %}} 

Di seguito è riportato il semplice scenario di utilizzo.

**C#**

{{< highlight "csharp" >}}

 // Create an instance of HtmlSaveOptions

var options = new HtmlSaveOptions();

// Set default font name for Html rendering

options.DefaultFontName = "Arial";

// Load a spreadsheet in an instance of Workbook

var book = new Workbook(dir + "sample.xlsx");

// Save the spreadsheet in Html format while passing instance of HtmlSaveOptions

book.Save(dir + "output.html", options);

{{< /highlight >}}


### **Aggiunta proprietà ImageOrPrintOptions.DefaultFont**
Aspose.Cells for .NET 8.9.0 consente di impostare il nome del carattere predefinito per la classe ImageOrPrintOptions esponendo la proprietà DefaultFont. La suddetta proprietà può essere utilizzata quando i caratteri Unicode nel foglio di calcolo non sono impostati con il carattere corretto nello stile della cella, pertanto tali caratteri possono apparire come blocchi nelle immagini risultanti.

{{% alert color="primary" %}} 

Imposta la proprietà DefaultFont su MingLiu o MS Gothic per visualizzare i caratteri Unicode. Se la suddetta proprietà non è impostata, Aspose.Cells utilizzerà il carattere predefinito del sistema per mostrare i caratteri Unicode.

{{% /alert %}} {{% alert color="primary" %}} 

 Per maggiori dettagli su questa funzione, consultare l'articolo su[Impostazione del carattere predefinito per il rendering di fogli di calcolo nei formati immagine](/cells/it/net/set-default-font-while-rendering-spreadsheet-to-images/).

{{% /alert %}} 

Di seguito è riportato il semplice scenario di utilizzo.

**C#**

{{< highlight "csharp" >}}

 // Create an instance of ImageOrPrintOptions

var options = new ImageOrPrintOptions();

// Set default font name for image rendering

options.DefaultFont = "Arial";

// Load a spreadsheet in an instance of Workbook

var book = new Workbook(dir + "sample.xlsx");

// Access the worksheet to be rendered

var sheet = book.Worksheets[0];

// Create an instance of SheetRender

var render = new SheetRender(sheet, options);

// Save spreadsheet to image

render.ToImage(0, dir + "output.png");

{{< /highlight >}}


### **Aggiunta proprietà PivotTable.IsExcel2003Compatible**
Aspose.Cells for .NET L'API ha esposto la proprietà IsExcel2003Compatible di tipo booleano per la classe PivotTable che consente di specificare se la tabella pivot è compatibile con Excel 2003 per scopi di aggiornamento. Il valore predefinito della proprietà IsExcel2003Compatible è true, ovvero una stringa deve essere inferiore o uguale a 255 caratteri. Se la stringa è maggiore di 255 caratteri, verrà troncata. Se falso, la suddetta restrizione non sarà imposta.

{{% alert color="primary" %}} 

 Per maggiori dettagli su questa funzione, consultare l'articolo su[Compatibilità per Excel 2003 per l'aggiornamento delle tabelle pivot](https://docs.aspose.com/cells/net/specify-whether-the-pivottable-is-compatible-for-excel2003-while-refreshing-pivottable/).

{{% /alert %}} 

Di seguito è riportato il semplice scenario di utilizzo.

**C#**

{{< highlight "csharp" >}}

 // Load a spreadsheet in an instance of Workbook

var book = new Workbook(dir + "sample.xlsx");

// Access the desired Pivot Table from the spreadsheet

var pivot = book.Worksheets[0].PivotTables[0];

// Set Excel 2003 compatibility to false

pivot.IsExcel2003Compatible = false;

// Refresh & recalculate Pivot Table

pivot.RefreshData();

pivot.CalculateData();

{{< /highlight >}}


### **Aggiunto il metodo GridWeb.GetVersion**
Aspose.Cells.GridWeb for .NET 8.9.0 ha esposto il metodo factory {GetVersion}} che restituisce la versione di rilascio del componente GridWeb.
