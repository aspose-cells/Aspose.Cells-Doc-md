---
title: Cambiamenti nell API pubblica in Aspose.Cells 8.8.1
type: docs
weight: 270
url: /it/net/public-api-changes-in-aspose-cells-8-8-1/
---

{{% alert color="primary" %}} 

Questo documento descrive le modifiche all'API Aspose.Cells dalla versione 8.8.0 a 8.8.1 che possono interessare gli sviluppatori di moduli/applicazioni. Include non solo metodi pubblici nuovi e aggiornati, classi aggiunte e rimosse, ma anche una descrizione di eventuali modifiche nel comportamento dietro le quinte in Aspose.Cells.

{{% /alert %}} 
## **API aggiunte**
### **Filtrare i dati per il caricamento**
Aspose.Cells for .NET 8.8.1 ha esposto l'enumerazione LoadDataFilterOptions insieme alla proprietà LoadOptions.LoadDataFilterOptions che può essere utilizzata per specificare il tipo di dati da caricare durante la costruzione del workbook da un file di modello. Filtrare i dati caricati può migliorare le prestazioni per scopi speciali, specialmente quando si utilizzano API LightCells.

L'enumerazione LoadDataFilterOptions fornisce le seguenti selezioni.

1. Tutto per caricare tutto dal foglio di calcolo.
1. Nessuno per non caricare nulla dal foglio di calcolo.
1. CellBlank carica le celle il cui valore è vuoto.
1. CellBool carica celle il cui valore è Booleano.
1. CellData carica dati delle celle inclusi valori, formule e formattazione.
1. CellError carica le celle il cui valore è un errore.
1. CellNumeric carica le celle il cui valore è numerico (inclusa la Data & Ora).
1. CellString carica le celle il cui valore è testo/stringa.
1. CellValue carica solo i valori delle celle (tutti i tipi).
1. Il grafico carica solo i grafici.
1. ConditionalFormatting carica solo le regole di formattazione condizionale.
1. DataValidation carica solo le regole di convalida dei dati.
1. DocumentProperties carica solo le proprietà del documento.
1. Formula carica formule incluse i nomi definiti.
1. MergedArea carica solo le celle unite.
1. PivotTable carica tabelle pivot.
1. Settings carica solo impostazioni del foglio di lavoro e del foglio di lavoro.
1. Shape carica solo le forme.
1. Style carica la formattazione delle celle.
1. Table carica tabelle Excel/Gli oggetti Elenco.

{{% alert color="primary" %}} 

Per ulteriori dettagli su questa funzionalità, si prega di consultare l'articolo dettagliato su [Filtrare i dati per il caricamento](/cells/it/net/filtering-the-kind-of-data-while-loading-the-workbook-from-template-file/).

{{% /alert %}} 

Di seguito è riportato il semplice scenario d'uso.

**C#**

{{< highlight csharp >}}

 //Create an instance of LoadOptions & initialize it with type of template to be loaded

var options = new LoadOptions(LoadFormat.Xlsx);

//Set LoadDataFilterOptions to load only shapes

options.LoadDataFilterOptions = LoadDataFilterOptions.Shape;

//Create an instance of Workbook from a existing spreadsheet using instance of LoadOptions

var book = new Workbook(filePath, options);

{{< /highlight >}}


### **Convertire direttamente il grafico in PDF**
Le API Aspose.Cells hanno già fornito la possibilità di rendere i grafici in PDF utilizzando il metodo Chart.ToPdf. Con questa versione, l'API ha esposto un'altra versione sovraccaricata del suddetto metodo che potrebbe accettare un'istanza di Stream, consentendo agli utenti di salvare il PDF del grafico in un'istanza di MemoryStream.

Di seguito è riportato il semplice scenario d'uso.

**C#**

{{< highlight csharp >}}

 //Create an instance of Workbook and load an existing spreadsheet with a chart

var workbook = new Workbook(filePath);

//Access first worksheet containing a chart

var worksheet = workbook.Worksheets[0];

//Access first chart from the worksheet

var chart = worksheet.Charts[0];

//Save the chart to PDF as Stream

using (MemoryStream stream = new MemoryStream())

{

    chart.ToPdf(stream);

}

{{< /highlight >}}


### **Aggiunta della proprietà WorkbookSettings.PaperSize**
Aspose.Cells for .NET 8.8.1 ha esposto la proprietà WorkbookSettings.PaperSize al fine di impostare la dimensione predefinita della carta per l'intero foglio di calcolo. La proprietà WorkbookSettings.PaperSize accetta un valore dall'enumerazione PaperSizeType che contiene le dimensioni predefinite per la maggior parte dei tipi di carta da stampa utilizzati.

**C#**

{{< highlight csharp >}}

 //Create an instance of Workbook

//Optionally load an existing spreadsheet

var book = new Workbook();

//Access WorkbookSettings from the Workbook

var settings = book.Settings;

//Set the default printing paper size for the Workbook

settings.PaperSize = PaperSizeType.PaperA4;

{{< /highlight >}}


### **Aggiunta della proprietà Shape.TextBody**
Questa versione dell'API Aspose.Cells for .NET ha esposto Shape.TextBody al fine di manipolare gli aspetti del testo in una forma. Il seguente snippet utilizza la suddetta proprietà per impostare l'effetto ombra del testo in una casella di testo.

{{% alert color="primary" %}} 

Per ulteriori dettagli su questa funzionalità, si prega di consultare l'articolo dettagliato su [Impostazione Effetto Ombra per Testo](/cells/it/net/setting-shadow-of-text-effects-of-shape-or-textbox/).

{{% /alert %}} 

**C#**

{{< highlight csharp >}}

 //Create an instance of Workbook

var book = new Workbook();

//Access first worksheet of the Workbook

var sheet = book.Worksheets[0];

//Add a TextBox to the ShapeCollection

var textBox = sheet.Shapes.AddTextBox(2, 0, 2, 0, 100, 400);

//Set the text of the TextBox

textBox.Text = "This text has the following settings.\n\nText Effects > Shadow > Offset Bottom";

//Set shadow effect for text

for (int i = 0; i < textBox.TextBody.Count; i++)

{

    textBox.TextBody[i].ShapeFont.FillFormat.ShadowEffect.PresetType = PresetShadowType.OffsetBottom;

}

{{< /highlight >}}


### **Aggiunto il metodo Worksheet.CalculateFormula(string formula, CalculationOptions opts)**
Aspose.Cells for .NET 8.8.1 ha esposto un ulteriore sovraccarico per il metodo CalculateFormula che fornisce la capacità di calcolare una data formula direttamente con opzioni personalizzate.

{{% alert color="primary" %}} 

Per ulteriori dettagli su questa funzionalità, si prega di consultare l'articolo dettagliato su [Calcolo Diretto di Funzione Personalizzata](/cells/it/net/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/).

{{% /alert %}} 
### **Aggiunto il metodo GridCell.CreateValidation**
Aspose.Cells.GridWeb ha fornito la capacità di aggiungere direttamente la regola di convalida a una singola cella utilizzando il metodo GridCell.CreateValidation. Tale metodo richiede 2 parametri. Il primo è di tipo GridValidationType che determina il tipo di convalida, mentre il secondo parametro (isRequied) è di tipo Booleano.



**C#**

{{< highlight csharp >}}

 //Access first worksheet

GridWorksheet sheet = GridWeb1.WorkSheets[0];

//Access cell B3

GridCell cell = sheet.Cells["B3"];

//Add validation inside the GridCell

//Any value which is not between 20 and 40 will cause error in a GridCell

GridValidation val = cell.CreateValidation(GridValidationType.WholeNumber, true);

val.Formula1 = "=20";

val.Formula2 = "=40";

val.Operator = GridOperatorType.Between;

val.ShowError = true;

val.ShowInput = true;

{{< /highlight >}}


### **Aggiunto il metodo GridCell.RemoveValidation**
Aspose.Cells.GridWeb ha fornito anche la capacità di rimuovere la regola di convalida dei dati da una GridCell utilizzando il metodo GridCell.RemoveValidation.
## **API deprecate**
### **Proprietà Shape.TextFrame deprecata**
Si consiglia di utilizzare la proprietà Shape.TextBody.TextAlignment al suo posto.
