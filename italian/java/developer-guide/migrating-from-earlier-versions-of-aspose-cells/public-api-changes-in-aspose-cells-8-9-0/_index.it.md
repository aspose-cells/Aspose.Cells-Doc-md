---
title: Modifiche all API pubblica in Aspose.Cells 8.9.0
type: docs
weight: 310
url: /it/java/public-api-changes-in-aspose-cells-8-9-0/
---

{{% alert color="primary" %}} 

Questo documento descrive le modifiche all'API Aspose.Cells dalla versione 8.8.3 alla 8.9.0 che potrebbero interessare agli sviluppatori di moduli/applicazioni. Include non solo nuovi metodi pubblici e aggiornati, classi aggiunte e rimosse, ma anche una descrizione di eventuali modifiche nel comportamento interno di Aspose.Cells.

{{% /alert %}} 
## **API aggiunte**
### **Aggiunta la proprietà HtmlSaveOptions.DefaultFontName**
Aspose.Cells for Java 8.9.0 ha esposto la proprietà DefaultFontName per la classe HtmlSaveOptions che consente di specificare il nome del carattere predefinito durante il rendering dei fogli di calcolo in formato HTML. Il carattere predefinito verrà utilizzato solo quando il carattere dello stile non esiste. Il valore predefinito della proprietà HtmlSaveOptions.DefaultFontName è null, ciò significa che la API Aspose.Cells for Java utilizzerà il carattere universale che ha la stessa famiglia del font originale.

{{% alert color="primary" %}} 

Per ulteriori dettagli su questa funzionalità, si prega di consultare l'articolo su [Impostazione del carattere predefinito per la visualizzazione delle cartelle di lavoro nel formato HTML](/cells/it/java/impostazione-del-carattere-predefinito-durante-la-visualizzazione-delle-cartelle-di-lavoro/).

{{% /alert %}} 

Di seguito è riportato il semplice scenario d'uso.

**Java**

{{< highlight csharp >}}

 //Create an instance of HtmlSaveOptions

HtmlSaveOptions options = new HtmlSaveOptions();

//Set default font name for Html rendering

options.setDefaultFontName("Arial");

//Load a spreadsheet in an instance of Workbook

Workbook book = new Workbook(dir + "sample.xlsx");

//Save the spreadsheet in Html format while passing instance of HtmlSaveOptions

book.save(dir + "output.html", options);

{{< /highlight >}}
### **Aggiunta la proprietà ImageOrPrintOptions.DefaultFont**
Aspose.Cells for Java 8.9.0 consente di impostare il nome del carattere predefinito per la classe ImageOrPrintOptions esponendo la proprietà DefaultFont. La suddetta proprietà può essere utilizzata quando i caratteri Unicode nella cartella di lavoro non sono impostati con il carattere corretto nello stile della cella, pertanto tali caratteri potrebbero apparire come blocchi nelle immagini risultanti. 

{{% alert color="primary" %}} 

Impostare la proprietà DefaultFont su MingLiu o MS Gothic per visualizzare i caratteri Unicode. Se la suddetta proprietà non è impostata, Aspose.Cells utilizzerà il carattere predefinito del sistema per mostrare i caratteri Unicode. 

{{% /alert %}} {{% alert color="primary" %}} 

Per ulteriori dettagli su questa funzionalità, si prega di consultare l'articolo su [Impostazione del carattere predefinito per la visualizzazione delle cartelle di lavoro nei formati delle immagini](/cells/it/java/impostazione-del-carattere-predefinito-durante-la-visualizzazione-delle-cartelle-di-lavoro-nelle-immagini/).

{{% /alert %}} 

Di seguito è riportato il semplice scenario d'uso.

**Java**

{{< highlight csharp >}}

 //Create an instance of ImageOrPrintOptions

ImageOrPrintOptions options = new ImageOrPrintOptions();

//Set default font name for image rendering

options.setDefaultFont("Arial");

//Load a spreadsheet in an instance of Workbook

Workbook book = new Workbook(dir + "sample.xlsx");

//Access the worksheet to be rendered

Worksheet sheet = book.getWorksheets().get(0);

//Create an instance of SheetRender

SheetRender render = new SheetRender(sheet, options);

//Save spreadsheet to image

render.toImage(0, dir + "output.png");

{{< /highlight >}}
### **Proprietà PivotTable.Excel2003Compatible aggiunta**
Aspose.Cells for Java API ha esposto la proprietà Excel2003Compatible di tipo Boolean per la classe PivotTable che consente di specificare se il PivotTable sia compatibile con Excel 2003 per scopi di aggiornamento. Il valore predefinito della proprietà Excel2003Compatible è true, il che significa che una stringa deve essere inferiore o uguale a 255 caratteri. Se la stringa è maggiore di 255 caratteri, verrà troncata. Se false, la suddetta restrizione non sarà imposta.

{{% alert color="primary" %}} 

Per ulteriori dettagli su questa funzionalità, si prega di consultare l'articolo su [Compatibilità per Excel 2003 per l'aggiornamento delle tabelle pivot](/cells/it/java/specifica-se-la-tabella-pivot-è-compatibile-con-excel2003-durante-laggiornamento-della-tabella-pivot/).

{{% /alert %}} 

Di seguito è riportato il semplice scenario d'uso.

**Java**

{{< highlight csharp >}}

 //Load a spreadsheet in an instance of Workbook

Workbook book = new Workbook(dir + "sample.xlsx");

//Access the desired Pivot Table from the spreadsheet

PivotTable pivot = book.getWorksheets().get(0).getPivotTables().get(0);

//Set Excel 2003 compatibility to false

pivot.setExcel2003Compatible(false);

//Refresh & recalculate Pivot Table

pivot.refreshData();

pivot.calculateData();

{{< /highlight >}}
