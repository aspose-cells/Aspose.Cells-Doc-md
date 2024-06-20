---
title: Modifiche all API pubblica in Aspose.Cells 16.11.0
type: docs
weight: 360
url: /it/java/public-api-changes-in-aspose-cells-16-11-0/
---

{{% alert color="primary" %}} 

Questo documento descrive le modifiche all'API di Aspose.Cells dalla versione 16.10.0 alla 16.11.0 che potrebbero interessare agli sviluppatori di moduli/applicazioni. Include non solo nuovi metodi pubblici aggiornati, classi aggiunte e rimosse ecc., ma anche una descrizione di eventuali cambiamenti nel comportamento dietro le quinte in Aspose.Cells.

{{% /alert %}} 
## **API aggiunte**
### **Supporto per le impostazioni di globalizzazione**
Aspose.Cells 16.11.0 ha esposto la classe GlobalizationSettings insieme alla proprietà WorkbookSettings.GlobalizationSettings per imporre alle API di Aspose.Cells di utilizzare etichette personalizzate per i subtotali. La classe GlobalizationSettings ha i seguenti metodi che possono essere sovrascritti nell'implementazione personalizzata per dare nomi desiderati alle etichette **Totale** e **Totale generale**.

- GlobalizationSettings.getTotalName: Restituisce il nome totale della funzione.
- GlobalizationSettings.getGrandTotalName: Ottiene il nome del totale generale della funzione.

Ecco una semplice classe personalizzata che estende la classe GlobalizationSettings e sovrascrive i suoi metodi sopra menzionati per restituire etichette personalizzate per la funzione di consolidamento Media.

**Java**

{{< highlight csharp >}}

 public class CustomSettings extends GlobalizationSettings

{    

    public String getTotalName(int functionType)

    {

    	 switch (functionType)

         {

             case ConsolidationFunction.AVERAGE:

                 return "AVG";

             default:

                return super.getTotalName(functionType);

         }

    }

    public String getGrandTotalName(int functionType)

    {

    	 switch (functionType)

         {

             case ConsolidationFunction.AVERAGE:

                 return "GRAND AVG";

             default:

            	 return super.getGrandTotalName(functionType);

         }



    }

}

{{< /highlight >}}

Il seguente snippet carica un foglio di calcolo esistente e aggiunge il Subtotale di tipo Media ai dati già disponibili nel foglio di lavoro. La classe CustomSettings e i suoi metodi getTotalName e getGrandTotalName verranno chiamati al momento dell'aggiunta del Subtotale al foglio di lavoro.

**Java**

{{< highlight csharp >}}

 //Loads an existing spreadsheet containing some data

Workbook book = new Workbook(dir + "sample.xlsx");

//Assigns the GlobalizationSettings property of the WorkbookSettings class

//to the class created in first step

book.getSettings().setGlobalizationSettings(new CustomSettings());

//Accesses the 1st worksheet from the collection which contains data

//Data resides in the cell range A2:B9

Worksheet sheet = book.getWorksheets().get(0);

//Adds SubTotal of type Average to the worksheet

sheet.getCells().subtotal(CellArea.createCellArea("A2", "B9"), 0, ConsolidationFunction.AVERAGE, new int[] { 0,1 });

//Calculates Formulas

book.calculateFormula();

//Auto fits all columns

sheet.autoFitColumns();

//Saves the workbook on disc

book.save(dir + "output.xlsx");

{{< /highlight >}}

La classe GlobalizationSettings offre anche il metodo getOtherName che è utile per ottenere il nome delle etichette "Altro" per i grafici a torta. Ecco un semplice scenario di utilizzo del metodo GlobalizationSettings.getOtherName.

**Java**

{{< highlight csharp >}}

 public class CustomSettings extends GlobalizationSettings

{ 

	public String getOtherName()

	{

		String language = Locale.getDefault().getLanguage();

		System.out.println(language);

		switch (language)

		{

			case "en":

				return "Other";

			case "fr":

				return "Autre";

			case "de":

				return "Andere";

			//Do other cases

			default:

				return super.getOtherName();

		}

	}

}

{{< /highlight >}}

Il seguente snippet carica un foglio di calcolo esistente contenente un grafico a torta e rende il grafico in un'immagine utilizzando la classe CustomSettings creata in precedenza.

**Java**

{{< highlight csharp >}}

 //Loads an existing spreadsheet containing a pie chart

Workbook book = new Workbook(dir + "sample.xlsx");

//Assigns the GlobalizationSettings property of the WorkbookSettings class

//to the class created in first step

book.getSettings().setGlobalizationSettings(new CustomSettings());

//Accesses the 1st worksheet from the collection which contains pie chart

Worksheet sheet = book.getWorksheets().get(0);

//Accesses the 1st chart from the collection

Chart chart = sheet.getCharts().get(0);

//Refreshes the chart

chart.calculate();

//Renders the chart to image

chart.toImage(dir + "output.png", new ImageOrPrintOptions());

{{< /highlight >}}
### **Aggiunta classe CellsFactory**
Aspose.Cells 16.11.0 ha esposto la classe CellsFactory che attualmente ha un metodo, ovvero createStyle. Il metodo CellsFactory.createStyle può essere utilizzato per creare un'istanza della classe Style senza aggiungerla al pool degli stili del foglio di lavoro.

Ecco un semplice scenario di utilizzo del metodo CellsFactory.createStyle.

**Java**

{{< highlight csharp >}}

 //Initializes the CellsFactory class

CellsFactory factory = new CellsFactory();

//Creates an instance of Style

Style style = factory.createStyle();

{{< /highlight >}}
### **Aggiunta proprietà Workbook.AbsolutePath**
Aspose.Cells 16.11.0 ha esposto la proprietà Workbook.AbsolutePath che consente di ottenere o impostare il percorso assoluto del foglio di lavoro memorizzato nel file workbook.xml. Questa proprietà è utile durante l'aggiornamento solo dei collegamenti esterni.
### **Aggiunto metodo GridHyperlinkCollection.getHyperlink**
Aspose.Cells.GridWeb 16.11.0 ha esposto il metodo getHyperlink per la classe GridHyperlinkCollection che consente di ottenere l'istanza di GridHyperlink passando un'istanza di GridCell o una coppia di interi corrispondenti agli indici di riga e colonna.

{{% alert color="primary" %}} 

Nel caso in cui non sia stata trovata alcuna ipercollegamento sulla cella specificata, il metodo getHyperlink restituirebbe null.

{{% /alert %}} 

Ecco un semplice scenario di utilizzo del metodo getHyperlink.

**Java**

{{< highlight csharp >}}

 //Gets the active worksheet from the collection

GridWorksheet sheet = gridWeb1.getWorkSheets().get(gridWeb1.getActiveSheetIndex());

//Accesses the GridHyperlinkCollection

GridHyperlinkCollection links = sheet.getHyperlinks();

//Gets hyperlink from cell A1

GridHyperlink link = links.getHyperlink(sheet.getCells().get("A1"));

//Gets hyperlink from cell D1

link = links.getHyperlink(0, 3);

{{< /highlight >}}
## **API deprecate**
### **Costruttore di stili obsoleti**
Si prega di utilizzare il metodo cellsFactory.createStyle come alternativa.
## **API eliminate**
### **Metodo Cell.getConditionalStyle eliminato**
Si prega di utilizzare il metodo Cell.getConditionalFormattingResult al suo posto.
### **Metodo Deleted Cells.getMaxDataRowInColumn(int column)**
Si prega di utilizzare il metodo Cells.getLastDataRow(int) come alternativa.
### **Proprietà Draft di PageSetup eliminata**
Si consiglia di utilizzare la proprietà PageSetup.PrintDraft invece.
### **Proprietà della raccolta di colonne del filtro automatico eliminata**
Si prega di considerare l'uso della proprietà AutoFilter.FilterColumns per raggiungere lo stesso obiettivo.
### **Proprietà di rotazione di TickLabels eliminata**
Si prega di utilizzare la proprietà TickLabels.RotationAngle invece.
