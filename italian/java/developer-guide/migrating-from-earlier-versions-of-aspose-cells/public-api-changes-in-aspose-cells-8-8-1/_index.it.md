---
title: Pubblico API Modifiche Aspose.Cells 8.8.1
type: docs
weight: 280
url: /it/java/public-api-changes-in-aspose-cells-8-8-1/
---
{{% alert color="primary" %}} 

Questo documento descrive le modifiche allo Aspose.Cells API dalla versione 8.8.0 alla 8.8.1 che potrebbero interessare gli sviluppatori di moduli/applicazioni. Include non solo metodi pubblici nuovi e aggiornati, classi aggiunte e rimosse ecc., ma anche una descrizione di eventuali cambiamenti nel comportamento dietro le quinte in Aspose.Cells.

{{% /alert %}} 
## **API aggiunte**
### **Filtrare i dati per il caricamento**
Aspose.Cells for Java 8.8.1 ha esposto l'enumerazione LoadDataFilterOptions insieme alla proprietà LoadOptions.LoadDataFilterOptions che può essere utilizzata per specificare il tipo di dati da caricare durante la creazione della cartella di lavoro da un file modello. Il filtraggio dei dati caricati può migliorare le prestazioni per scopi speciali, soprattutto quando si utilizzano le API LightCells.

L'enumerazione LoadDataFilterOptions fornisce le selezioni seguenti.

1. ALL per caricare tutto dal foglio di calcolo.
1. NONE per non caricare nulla dal foglio di calcolo.
1. CELL_BLANK carica le celle i cui valori sono vuoti.
1. CELL_BOOL carica le celle i cui valori sono booleani.
1. CELL_DATA carica i dati delle celle inclusi valori, formule e formattazione.
1. CELL_ERROR carica le celle i cui valori sono errore.
1. CELL_NUMERIC carica le celle i cui valori sono numerici (incluse data e ora).
1. CELL_STRING carica le celle i cui valori sono testo/stringa.
1. CELL_VALUE carica solo i valori delle celle (tutti i tipi).
1. CHART carica solo i grafici.
1. CONDITIONAL_FORMATTING carica solo le regole di formattazione condizionale.
1. DATA_VALIDATION carica solo le regole di convalida dei dati.
1. DOCUMENT_PROPERTIES carica solo le proprietà del documento.
1. FORMULA carica le formule inclusi i nomi definiti.
1. MERGED_AREA carica solo le celle unite.
1. PIVOT_TABLE carica le tabelle pivot.
1. IMPOSTAZIONI carica solo le impostazioni della cartella di lavoro e del foglio di lavoro.
1. SHAPE carica solo le forme.
1. STYLE carica la formattazione delle celle.
1. TABLE carica tabelle Excel/Elenco oggetti.

{{% alert color="primary" %}} 

 Per maggiori dettagli su questa funzione, consultare l'articolo dettagliato su[Filtra i dati per il caricamento](/cells/it/java/filtering-the-kind-of-data-while-loading-the-workbook-from-template-file/).

{{% /alert %}} 

Di seguito è riportato il semplice scenario di utilizzo.

**Java**

{{< highlight "csharp" >}}

 //Create an instance of LoadOptions & initialize it with type of template to be loaded

LoadOptions options = new LoadOptions(LoadFormat.XLSX);

//Set LoadDataFilterOptions to load only shapes

options.setLoadDataFilterOptions(LoadDataFilterOptions.SHAPE);

//Create an instance of Workbook from a existing spreadsheet using instance of LoadOptions

Workbook book = new Workbook(filePath, options);

{{< /highlight >}}
### **Converti direttamente il grafico in PDF**
Aspose.Cells Le API hanno già fornito la possibilità di eseguire il rendering dei grafici in PDF durante l'utilizzo del metodo Chart.toPdf. Con questa versione, lo API ha esposto un'altra versione sovraccaricata del suddetto metodo che potrebbe accettare un'istanza di OutputStream, consentendo agli utenti di salvare il PDF del grafico in un'istanza di ByteArrayOutputStream.

Di seguito è riportato il semplice scenario di utilizzo.

**Java**

{{< highlight "csharp" >}}

 //Create an instance of Workbook and load an existing spreadsheet with a chart

Workbook workbook = new Workbook(filePath);

//Access first worksheet containing a chart

Worksheet worksheet = workbook.getWorksheets().get(0);

//Access first chart from the worksheet

Chart chart = worksheet.getCharts().get(0);

//Save the chart to PDF as Stream

ByteArrayOutputStream outStream = new ByteArrayOutputStream();

chart.toPdf(outStream);

{{< /highlight >}}
### **Aggiunta proprietà WorkbookSettings.PaperSize**
Aspose.Cells for Java 8.8.1 ha esposto la proprietà WorkbookSettings.PaperSize per impostare la dimensione della carta di stampa predefinita per l'intero foglio di calcolo. La proprietà WorkbookSettings.PaperSize accetta un valore dall'enumerazione PaperSizeType che contiene le dimensioni predefinite per i tipi di carta da stampa più utilizzati.

**Java**

{{< highlight "csharp" >}}

 //Create an instance of Workbook

//Optionally load an existing spreadsheet

Workbook book = new Workbook();

//Access WorkbookSettings from the Workbook

WorkbookSettings settings = book.getSettings();

//Set the default printing paper size for the Workbook

settings.setPaperSize(PaperSizeType.PAPER_A_4);

{{< /highlight >}}
### **Aggiunta la proprietà Shape.TextBody**
Questa versione di Aspose.Cells for Java API ha esposto Shape.TextBody per manipolare gli aspetti del testo in una forma. Il seguente frammento utilizza la suddetta proprietà per impostare l'effetto ombra del testo in un TextBox.

{{% alert color="primary" %}} 

 Per maggiori dettagli su questa funzione, consultare l'articolo dettagliato su[Impostazione dell'effetto ombra per il testo](/cells/it/java/setting-shadow-of-text-effects-of-shape-or-textbox/).

{{% /alert %}} 

**Java**

{{< highlight "csharp" >}}

 //Crea un'istanza di Workbook

Libro della cartella di lavoro = nuova cartella di lavoro();

//Accedi al primo foglio di lavoro della cartella di lavoro

Foglio di lavoro = book.getWorksheets().get(0);

//Aggiungi un TextBox a ShapeCollection

int index = sheet.getTextBoxes().add(2, 2, 100, 400);

TextBox textBox = sheet.getTextBoxes().get(index);

//Imposta il testo del TextBox

textBox.setText("Questo testo ha le seguenti impostazioni.\n\nEffetti testo > Ombra > Offset fondo");

//Imposta l'effetto ombra per il testo

 per (int i = 0; i< textBox.getTextBody().getCount(); i++)

{

  textBox.getTextBody().get(i).getShapeFont().getFillFormat().getShadowEffect().setPresetType(PresetShadowType.OFFSET_BOTTOM);

}

{{< /highlight >}}
### **Aggiunto il metodo Worksheet.calculateFormula(string formula, CalculationOptions opts).**
Aspose.Cells for Java 8.8.1 ha esposto un altro sovraccarico per il metodo Worksheet.calculateFormula che fornisce la possibilità di calcolare una data formula direttamente con opzioni personalizzate.

{{% alert color="primary" %}} 

 Per maggiori dettagli su questa funzione, consultare l'articolo dettagliato su[Calcolo diretto della funzione personalizzata](/cells/it/java/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/).

{{% /alert %}} 
### **Aggiunto il metodo GridCell.createValidation**
Aspose.Cells.GridWeb ha fornito la possibilità di aggiungere direttamente la regola di convalida a una singola cella durante l'utilizzo del metodo GridCell.createValidation. Il suddetto metodo richiede 2 parametri. Il primo è di tipo GridValidationType che determina il tipo di validazione, mentre il secondo parametro (isRequied) è di tipo Boolean.

**Java**

{{< highlight "csharp" >}}

 //Access first worksheet

GridWorksheet sheet = gridweb.getWorkSheets().get(0);

//Access cell B3

GridCell cell = sheet.getCells().get("B3");

//Add validation inside the GridCell

//Any value which is not between 20 and 40 will cause error in a GridCell

GridValidation val = cell.createValidation(GridValidationType.WHOLE_NUMBER, true);

val.setFormula1("=20");

val.setFormula2("=40");

val.setOperator(OperatorType.BETWEEN);

val.setShowError(true);

val.setShowInput(true);

{{< /highlight >}}
### **Aggiunto il metodo GridCell.removeValidation**
Aspose.Cells.GridWeb ha anche fornito la possibilità di rimuovere la regola di convalida dei dati da un GridCell durante l'utilizzo del metodo GridCell.removeValidation.
## **API obsolete**
### **Proprietà Shape.TextFrame obsoleta**
Si consiglia invece di utilizzare la proprietà Shape.TextBody.TextAlignment.
