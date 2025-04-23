---
title: Modifiche all API pubblica in Aspose.Cells 16.11.0
type: docs
weight: 350
url: /it/net/public-api-changes-in-aspose-cells-16-11-0/
---

{{% alert color="primary" %}} 

Questo documento descrive le modifiche all'API di Aspose.Cells dalla versione 16.10.0 alla 16.11.0 che potrebbero interessare agli sviluppatori di moduli/applicazioni. Include non solo nuovi metodi pubblici aggiornati, classi aggiunte e rimosse ecc., ma anche una descrizione di eventuali cambiamenti nel comportamento dietro le quinte in Aspose.Cells.

{{% /alert %}} 
## **API aggiunte**
### **Supporto per le impostazioni di globalizzazione**
Aspose.Cells 16.11.0 ha esposto la classe GlobalizationSettings insieme alla proprietà WorkbookSettings.GlobalizationSettings per imporre alle API di Aspose.Cells di utilizzare etichette personalizzate per i subtotali. La classe GlobalizationSettings ha i seguenti metodi che possono essere sovrascritti nell'implementazione personalizzata per dare nomi desiderati alle etichette **Totale** e **Totale generale**.

- GlobalizationSettings.GetTotalName: Restituisce il nome totale della funzione.
- GlobalizationSettings.GetGrandTotalName: Restituisce il nome totale generale della funzione.

Ecco una semplice classe personalizzata che estende la classe GlobalizationSettings e sovrascrive i suoi metodi sopra menzionati per restituire etichette personalizzate per la funzione di consolidamento Media.

**C#**

{{< highlight csharp >}}

 class CustomSettings : GlobalizationSettings

{

    public override string GetTotalName(ConsolidationFunction functionType)

    {

        switch (functionType)

        {

            case ConsolidationFunction.Average:

                return "AVG";

            default:

                return base.GetTotalName(functionType);

        }

    }

    public override string GetGrandTotalName(ConsolidationFunction functionType)

    {

        switch (functionType)

        {

            case ConsolidationFunction.Average:

                return "GRD AVG";

            default:

                return base.GetGrandTotalName(functionType);

        }

    }

}

{{< /highlight >}}



Il seguente snippet carica un foglio di calcolo esistente e aggiunge il Subtotale di tipo Media sui dati già disponibili nel foglio di lavoro. La classe CustomSettings e i suoi metodi GetTotalName e GetGrandTotalName verranno chiamati al momento dell'aggiunta del Subtotale al foglio di lavoro.

**C#**

{{< highlight csharp >}}

 // Loads an existing spreadsheet containing some data

Workbook book = new Workbook(dir + "sample.xlsx");

// Assigns the GlobalizationSettings property of the WorkbookSettings class

// to the class created in first step

book.Settings.GlobalizationSettings = new Cells.CustomSettings();

// Accesses the 1st worksheet from the collection which contains data

// Data resides in the cell range A2:B9

Worksheet sheet = book.Worksheets[0];

// Adds SubTotal of type Average to the worksheet

sheet.Cells.Subtotal(CellArea.CreateCellArea("A2", "B9"), 0, ConsolidationFunction.Average, new int[] { 0,1 });

// Calculates Formulas

book.CalculateFormula();

// Auto fits all columns

sheet.AutoFitColumns();

// Saves the workbook on disc

book.Save(dir + "output.xlsx");

{{< /highlight >}}



La classe GlobalizationSettings offre anche il metodo GetOtherName che è utile per ottenere il nome delle etichette "Altro" per i grafici a torta. Ecco un semplice scenario di utilizzo del metodo GlobalizationSettings.GetOtherName.

**C#**

{{< highlight csharp >}}

 class CustomSettings : GlobalizationSettings

{

    public override string GetOtherName()

    {

        int lcid = System.Globalization.CultureInfo.CurrentCulture.LCID;

        switch (lcid)

        {

            case 1033:

                return "Other";

            case 1036:

                return "Autre";

            case 1031:

                return "Andere";

            //Do other case

            default:

                return base.GetOtherName();

        }

    }

}

{{< /highlight >}}



Il seguente snippet carica un foglio di calcolo esistente contenente un grafico a torta e rende il grafico in un'immagine utilizzando la classe CustomSettings creata in precedenza.

**C#**

{{< highlight csharp >}}

 // Loads an existing spreadsheet containing a pie chart

Workbook book = new Workbook(dir + "sample.xlsx");

// Assigns the GlobalizationSettings property of the WorkbookSettings class

// to the class created in first step

book.Settings.GlobalizationSettings = new Cells.CustomSettings();

// Accesses the 1st worksheet from the collection which contains pie chart

Worksheet sheet = book.Worksheets[0];

// Accesses the 1st chart from the collection

Chart chart = sheet.Charts[0];

// Refreshes the chart

chart.Calculate();

// Renders the chart to image

chart.ToImage(dir + "output.png", new ImageOrPrintOptions());

{{< /highlight >}}


### **Aggiunta classe CellsFactory**
Aspose.Cells 16.11.0 ha esposto la classe CellsFactory che attualmente ha un metodo, ossia CreateStyle. Il metodo CellsFactory.CreateStyle può essere utilizzato per creare un'istanza della classe Style senza aggiungerla al pool degli stili del documento di lavoro.

Ecco un semplice scenario di utilizzo del metodo CellsFactory.CreateStyle.

**C#**

{{< highlight csharp >}}

 // Initializes the CellsFactory class

CellsFactory factory = new CellsFactory();

// Creates an instance of Style

Style style = factory.CreateStyle();

{{< /highlight >}}


### **Aggiunta proprietà Workbook.AbsolutePath**
Aspose.Cells 16.11.0 ha esposto la proprietà Workbook.AbsolutePath che consente di ottenere o impostare il percorso assoluto del foglio di lavoro memorizzato nel file workbook.xml. Questa proprietà è utile durante l'aggiornamento solo dei collegamenti esterni.
### **Aggiunta del metodo GridHyperlinkCollection.GetHyperlink**
Aspose.Cells.GridWeb 16.11.0 ha esposto il metodo GetHyperlink alla classe GridHyperlinkCollection che consente di ottenere l'istanza di GridHyperlink passando un'istanza di GridCell o una coppia di interi corrispondenti agli indici di riga e colonna.

{{% alert color="primary" %}} 

Nel caso in cui non venga trovato alcun collegamento ipertestuale nella cella specificata, il metodo GetHyperlink restituirebbe null.

{{% /alert %}} 

Ecco un semplice scenario di utilizzo del metodo GetHyperlink.

**C#**

{{< highlight csharp >}}

 // Gets the active worksheet from the collection

GridWorksheet sheet = GridWeb1.WorkSheets[GridWeb1.ActiveSheetIndex];

// Accesses the GridHyperlinkCollection

GridHyperlinkCollection links = sheet.Hyperlinks;

// Gets hyperlink from cell A1

GridHyperlink link = links.GetHyperlink(sheet.Cells["A1"]);

// Gets hyperlink from cell D1

link = links.GetHyperlink(0, 3);

{{< /highlight >}}
## **API deprecate**
### **Costruttore di stili obsoleti**
Si prega di utilizzare il metodo cellsFactory.CreateStyle come alternativa.
## **API eliminate**
### **Metodo Cell.GetConditionalStyle eliminato**
Si prega di utilizzare il metodo Cell.GetConditionalFormattingResult al suo posto.
### **Metodo Cells.MaxDataRowInColumn(int column) eliminato**
Si prega di utilizzare il metodo Cells.GetLastDataRow(int) come alternativa.
### **Proprietà Draft di PageSetup eliminata**
Si consiglia di utilizzare la proprietà PageSetup.PrintDraft invece.
### **Proprietà della raccolta di colonne del filtro automatico eliminata**
Si prega di considerare l'uso della proprietà AutoFilter.FilterColumns per raggiungere lo stesso obiettivo.
### **Proprietà di rotazione di TickLabels eliminata**
Si prega di utilizzare la proprietà TickLabels.RotationAngle invece.
{{< app/cells/assistant language="csharp" >}}
