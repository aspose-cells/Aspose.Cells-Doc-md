---
title: Pubblico API Modifiche Aspose.Cells 8.8.1
type: docs
weight: 270
url: /it/net/public-api-changes-in-aspose-cells-8-8-1/
---
{{% alert color="primary" %}} 

Questo documento descrive le modifiche allo Aspose.Cells API dalla versione 8.8.0 alla 8.8.1 che potrebbero interessare gli sviluppatori di moduli/applicazioni. Include non solo metodi pubblici nuovi e aggiornati, classi aggiunte e rimosse ecc., ma anche una descrizione di eventuali cambiamenti nel comportamento dietro le quinte in Aspose.Cells.

{{% /alert %}} 
## **API aggiunte**
### **Filtrare i dati per il caricamento**
Aspose.Cells for .NET 8.8.1 ha esposto l'enumerazione LoadDataFilterOptions insieme alla proprietà LoadOptions.LoadDataFilterOptions che può essere utilizzata per specificare il tipo di dati da caricare durante la creazione della cartella di lavoro da un file modello. Il filtraggio dei dati caricati può migliorare le prestazioni per scopi speciali, soprattutto quando si utilizzano le API LightCells.

L'enumerazione LoadDataFilterOptions fornisce le selezioni seguenti.

1. Tutto per caricare tutto dal foglio di calcolo.
1. Nessuno per non caricare nulla dal foglio di calcolo.
1. CellBlank carica le celle i cui valori sono vuoti.
1. CellBool carica le celle i cui valori sono booleani.
1. CellData carica i dati delle celle inclusi valori, formule e formattazione.
1. CellError carica le celle i cui valori sono errore.
1. CellNumeric carica le celle i cui valori sono numerici (incluse data e ora).
1. CellString carica le celle i cui valori sono testo/stringa.
1. CellValue carica solo i valori delle celle (tutti i tipi).
1. Grafico carica solo i grafici.
1. ConditionalFormatting carica solo le regole di formattazione condizionale.
1. DataValidation carica solo le regole di convalida dei dati.
1. DocumentProperties carica solo le proprietà del documento.
1. Formula carica le formule inclusi i nomi definiti.
1. MergedArea carica solo le celle unite.
1. PivotTable carica le tabelle pivot.
1. Impostazioni carica solo le impostazioni della cartella di lavoro e del foglio di lavoro.
1. Shape carica solo le forme.
1. Stile carica la formattazione delle celle.
1. Tabella carica tabelle Excel/Elenco oggetti.

{{% alert color="primary" %}} 

 Per maggiori dettagli su questa funzione, consultare l'articolo dettagliato su[Filtra i dati per il caricamento](/cells/it/net/filtering-the-kind-of-data-while-loading-the-workbook-from-template-file/).

{{% /alert %}} 

Di seguito è riportato il semplice scenario di utilizzo.

**C#**

{{< highlight "csharp" >}}

 //Create an instance of LoadOptions & initialize it with type of template to be loaded

var options = new LoadOptions(LoadFormat.Xlsx);

//Set LoadDataFilterOptions to load only shapes

options.LoadDataFilterOptions = LoadDataFilterOptions.Shape;

//Create an instance of Workbook from a existing spreadsheet using instance of LoadOptions

var book = new Workbook(filePath, options);

{{< /highlight >}}


### **Converti direttamente il grafico in PDF**
Le API Aspose.Cells hanno già fornito la possibilità di eseguire il rendering dei grafici su PDF durante l'utilizzo del metodo Chart.ToPdf. Con questa versione, lo API ha esposto un'altra versione sovraccaricata del suddetto metodo che potrebbe accettare un'istanza di Stream, consentendo agli utenti di salvare lo PDF del grafico in un'istanza di MemoryStream.

Di seguito è riportato il semplice scenario di utilizzo.

**C#**

{{< highlight "csharp" >}}

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


### **Aggiunta proprietà WorkbookSettings.PaperSize**
Aspose.Cells for .NET 8.8.1 ha esposto la proprietà WorkbookSettings.PaperSize per impostare la dimensione della carta di stampa predefinita per l'intero foglio di calcolo. La proprietà WorkbookSettings.PaperSize accetta un valore dall'enumerazione PaperSizeType che contiene le dimensioni predefinite per i tipi di carta da stampa più utilizzati.

**C#**

{{< highlight "csharp" >}}

 //Create an instance of Workbook

//Optionally load an existing spreadsheet

var book = new Workbook();

//Access WorkbookSettings from the Workbook

var settings = book.Settings;

//Set the default printing paper size for the Workbook

settings.PaperSize = PaperSizeType.PaperA4;

{{< /highlight >}}


### **Aggiunta la proprietà Shape.TextBody**
Questa versione di Aspose.Cells for .NET API ha esposto Shape.TextBody per manipolare gli aspetti del testo in una forma. Il seguente frammento utilizza la suddetta proprietà per impostare l'effetto ombra del testo in un TextBox.

{{% alert color="primary" %}} 

 Per maggiori dettagli su questa funzione, consultare l'articolo dettagliato su[Impostazione dell'effetto ombra per il testo](/cells/it/net/setting-shadow-of-text-effects-of-shape-or-textbox/).

{{% /alert %}} 

**C#**

{{< highlight "csharp" >}}

 //Crea un'istanza di Workbook

var libro = nuova cartella di lavoro();

//Accedi al primo foglio di lavoro della cartella di lavoro

var foglio = libro.Fogli di lavoro[0];

//Aggiungi un TextBox a ShapeCollection

var textBox = sheet.Shapes.AddTextBox(2, 0, 2, 0, 100, 400);

//Imposta il testo del TextBox

textBox.Text = "Questo testo ha le seguenti impostazioni.\n\nEffetti di testo > Ombra > Offset in basso";

//Imposta l'effetto ombra per il testo

 per (int i = 0; i< textBox.TextBody.Count; i++)

{

    textBox.TextBody[i].ShapeFont.FillFormat.ShadowEffect.PresetType = PresetShadowType.OffsetBottom;

}

{{< /highlight >}}


### **Aggiunto il metodo Worksheet.CalculateFormula(string formula, CalculationOptions opts).**
Aspose.Cells for .NET 8.8.1 ha esposto un altro sovraccarico per il metodo CalculateFormula che fornisce la possibilità di calcolare una data formula direttamente con opzioni personalizzate.

{{% alert color="primary" %}} 

 Per maggiori dettagli su questa funzione, consultare l'articolo dettagliato su[Calcolo diretto della funzione personalizzata](/cells/it/net/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/).

{{% /alert %}} 
### **Aggiunto il metodo GridCell.CreateValidation**
Aspose.Cells.GridWeb ha fornito la possibilità di aggiungere direttamente la regola di convalida a una singola cella durante l'utilizzo del metodo GridCell.CreateValidation. Il suddetto metodo richiede 2 parametri. Il primo è di tipo GridValidationType che determina il tipo di validazione, mentre il secondo parametro (isRequied) è di tipo Boolean.



**C#**

{{< highlight "csharp" >}}

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
Aspose.Cells.GridWeb ha anche fornito la possibilità di rimuovere la regola di convalida dei dati da un GridCell durante l'utilizzo del metodo GridCell.RemoveValidation.
## **API obsolete**
### **Proprietà Shape.TextFrame obsoleta**
Si consiglia invece di utilizzare la proprietà Shape.TextBody.TextAlignment.
