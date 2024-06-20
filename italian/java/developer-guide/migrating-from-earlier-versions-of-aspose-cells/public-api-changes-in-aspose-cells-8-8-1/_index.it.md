---
title: Cambiamenti nell API pubblica in Aspose.Cells 8.8.1
type: docs
weight: 280
url: /it/java/public-api-changes-in-aspose-cells-8-8-1/
---

{{% alert color="primary" %}} 

Questo documento descrive le modifiche all'API Aspose.Cells dalla versione 8.8.0 a 8.8.1 che possono interessare gli sviluppatori di moduli/applicazioni. Include non solo metodi pubblici nuovi e aggiornati, classi aggiunte e rimosse, ma anche una descrizione di eventuali modifiche nel comportamento dietro le quinte in Aspose.Cells.

{{% /alert %}} 
## **API aggiunte**
### **Filtrare i dati per il caricamento**
Aspose.Cells for Java 8.8.1 ha esposto l'enumerazione LoadDataFilterOptions insieme alla proprietà LoadOptions.LoadDataFilterOptions che può essere utilizzata per specificare il tipo di dati che dovrebbe essere caricato durante la costruzione del foglio di calcolo da un file modello. Filtrare i dati caricati può migliorare le prestazioni per scopi speciali, specialmente quando si utilizzano le API LightCells.

L'enumerazione LoadDataFilterOptions fornisce le seguenti selezioni.

1. TUTTO per caricare tutto dal foglio di calcolo.
1. NULL per caricare nulla dal foglio di calcolo.
1. CELL_BLANK carica le celle il cui valore è vuoto.
1. CELL_BOOL carica celle il cui valore è Booleano.
1. CELL_DATA carica dati delle celle inclusi valori, formule e formattazioni.
1. CELL_ERROR carica celle il cui valore è un errore.
1. CELL_NUMERIC carica celle il cui valore è numerico (inclusa Data e Ora).
1. CELL_STRING carica celle il cui valore è testo/stringa.
1. CELL_VALUE carica solo i valori delle celle (tutti i tipi).
1. CHART carica solo grafici.
1. CONDITIONAL_FORMATTING carica solo regole di formattazione condizionale.
1. DATA_VALIDATION carica solo regole di convalida dei dati.
1. DOCUMENT_PROPERTIES carica solo proprietà del documento.
1. FORMULA carica formule inclusi nomi definiti.
1. MERGED_AREA carica solo celle unite.
1. PIVOT_TABLE carica Tabelle Pivot.
1. SETTINGS carica solo impostazioni di Libro & Foglio di lavoro.
1. SHAPE carica solo forme.
1. STYLE carica formattazioni delle celle.
1. TABLE carica tabelle di Excel/Elenco Oggetti.

{{% alert color="primary" %}} 

Per ulteriori dettagli su questa funzionalità, si prega di consultare l'articolo dettagliato su [Filtro dei dati per il caricamento](/cells/it/java/filtrare-il-tipo-di-dati-durante-il-caricamento-del-file-modello/).

{{% /alert %}} 

Di seguito è riportato il semplice scenario d'uso.

**Java**

{{< highlight csharp >}}

 //Create an instance of LoadOptions & initialize it with type of template to be loaded

LoadOptions options = new LoadOptions(LoadFormat.XLSX);

//Set LoadDataFilterOptions to load only shapes

options.setLoadDataFilterOptions(LoadDataFilterOptions.SHAPE);

//Create an instance of Workbook from a existing spreadsheet using instance of LoadOptions

Workbook book = new Workbook(filePath, options);

{{< /highlight >}}
### **Convertire direttamente il grafico in PDF**
Le API di Aspose.Cells hanno già fornito la possibilità di renderizzare grafici in PDF utilizzando il metodo Chart.toPdf. Con questa release, l'API ha esposto un'altra versione sovraccaricata del suddetto metodo che potrebbe accettare un'istanza di OutputStream, permettendo agli utenti di salvare il PDF del grafico in un'istanza di ByteArrayOutputStream.

Di seguito è riportato il semplice scenario d'uso.

**Java**

{{< highlight csharp >}}

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
### **Aggiunta della proprietà WorkbookSettings.PaperSize**
Aspose.Cells for Java 8.8.1 ha esposto la proprietà WorkbookSettings.PaperSize per impostare la dimensione predefinita della carta per l'intero foglio elettronico. La proprietà WorkbookSettings.PaperSize accetta un valore dell'enumerazione PaperSizeType che contiene le dimensioni predefinite per la maggior parte dei tipi di carta da stampa più utilizzati.

**Java**

{{< highlight csharp >}}

 //Create an instance of Workbook

//Optionally load an existing spreadsheet

Workbook book = new Workbook();

//Access WorkbookSettings from the Workbook

WorkbookSettings settings = book.getSettings();

//Set the default printing paper size for the Workbook

settings.setPaperSize(PaperSizeType.PAPER_A_4);

{{< /highlight >}}
### **Aggiunta della proprietà Shape.TextBody**
Questa release di Aspose.Cells for Java API ha esposto Shape.TextBody per manipolare gli aspetti del testo in una forma. Il seguente snippet utilizza la suddetta proprietà per impostare l'effetto ombra del testo in una TextBox.

{{% alert color="primary" %}} 

Per ulteriori dettagli su questa funzionalità, si prega di consultare l'articolo dettagliato su [Impostazione dell'effetto ombra per il testo](/cells/it/java/setting-shadow-of-text-effects-of-shape-or-textbox/).

{{% /alert %}} 

**Java**

{{< highlight csharp >}}

 //Create an instance of Workbook

Workbook book = new Workbook();

//Access first worksheet of the Workbook

Worksheet sheet = book.getWorksheets().get(0);

//Add a TextBox to the ShapeCollection

int index = sheet.getTextBoxes().add(2, 2, 100, 400);

TextBox textBox = sheet.getTextBoxes().get(index);

//Set the text of the TextBox

textBox.setText("This text has the following settings.\n\nText Effects > Shadow > Offset Bottom");

//Set shadow effect for text

for (int i = 0; i < textBox.getTextBody().getCount(); i++)

{

  textBox.getTextBody().get(i).getShapeFont().getFillFormat().getShadowEffect().setPresetType(PresetShadowType.OFFSET_BOTTOM);

}

{{< /highlight >}}
### **Aggiunto metodo Worksheet.calculateFormula(string formula, CalculationOptions opts)**
Aspose.Cells for Java 8.8.1 ha esposto un'altra sovraccarica per il metodo Worksheet.calculateFormula che fornisce la possibilità di calcolare una formula data direttamente con opzioni personalizzate.

{{% alert color="primary" %}} 

Per ulteriori dettagli su questa funzionalità, si prega di consultare l'articolo dettagliato su [Calcolo diretto di una funzione personalizzata](/cells/it/java/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/).

{{% /alert %}} 
### **Aggiunto metodo GridCell.createValidation**
Aspose.Cells.GridWeb ha fornito la possibilità di aggiungere direttamente la regola di convalida a una singola cella utilizzando il metodo GridCell.createValidation. Il suddetto metodo richiede 2 parametri. Il primo è di tipo GridValidationType che determina il tipo di convalida, mentre il secondo parametro (isRequied) è di tipo Boolean.

**Java**

{{< highlight csharp >}}

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
### **Aggiunto metodo GridCell.removeValidation**
Aspose.Cells.GridWeb ha anche fornito la possibilità di rimuovere la regola di convalida dei dati da una GridCell utilizzando il metodo GridCell.removeValidation.
## **API deprecate**
### **Proprietà Shape.TextFrame deprecata**
Si consiglia di utilizzare la proprietà Shape.TextBody.TextAlignment al suo posto.
