---
title: Pubblico API Modifiche Aspose.Cells 16.11.0
type: docs
weight: 360
url: /it/java/public-api-changes-in-aspose-cells-16-11-0/
---
{{% alert color="primary" %}} 

Questo documento descrive le modifiche allo Aspose.Cells API dalla versione 16.10.0 alla 16.11.0 che potrebbero interessare gli sviluppatori di moduli/applicazioni. Include non solo metodi pubblici nuovi e aggiornati, classi aggiunte e rimosse ecc., ma anche una descrizione di eventuali cambiamenti nel comportamento dietro le quinte in Aspose.Cells.

{{% /alert %}} 
## **API aggiunte**
### **Supporto per le impostazioni di globalizzazione**
Aspose.Cells 16.11.0 ha esposto la classe GlobalizationSettings insieme alla proprietà WorkbookSettings.GlobalizationSettings per imporre alle API Aspose.Cells l'utilizzo di etichette personalizzate per i subtotali. La classe GlobalizationSettings ha i seguenti metodi che possono essere sovrascritti nell'implementazione personalizzata per dare i nomi desiderati alle etichette**Totale** & **Somma totale**.

- GlobalizationSettings.getTotalName: ottiene il nome totale della funzione.
- GlobalizationSettings.getGrandTotalName: ottiene il nome del totale complessivo della funzione.

Ecco una semplice classe personalizzata che estende la classe GlobalizationSettings e ne esegue l'override dei metodi sopra menzionati per restituire etichette personalizzate per la funzione di consolidamento Average.

**Java**

{{< highlight "csharp" >}}

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

Lo snippet seguente carica un foglio di calcolo esistente e aggiunge il subtotale di tipo Media sui dati già disponibili nel foglio di lavoro. La classe CustomSettings ei relativi metodi getTotalName e getGrandTotalName verranno chiamati al momento dell'aggiunta di Subtotal al foglio di lavoro.

**Java**

{{< highlight "csharp" >}}

 //Loads an existing spreadsheet containing some data

Workbook book = new Workbook(dir + "sample.xlsx");

//Assigns the GlobalizationSettings property of the WorkbookSettings class

//to the class created in first step

book.getSettings().setGlobalizationSettings(new CustomSettings());

//Accesses the 1st worksheet from the collection which contains data

//Data resides in the cell range A2:B9

Worksheet sheet = book.getWorksheets().get(0);

//Adds SubTotal of type Average to the worksheet

sheet.getCells().subtotal(CellArea.createCellArea("A2", "B9"), 0, ConsolidationFunction.AVERAGE, new int[]{ 0,1 });

//Calculates Formulas

book.calculateFormula();

//Auto fits all columns

sheet.autoFitColumns();

//Saves the workbook on disc

book.save(dir + "output.xlsx");

{{< /highlight >}}

La classe GlobalizationSettings offre anche il metodo getOtherName utile per ottenere il nome delle etichette "Altro" per i grafici a torta. Ecco un semplice scenario di utilizzo del metodo GlobalizationSettings.getOtherName.

**Java**

{{< highlight "csharp" >}}

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

Il frammento di codice seguente carica un foglio di calcolo esistente contenente un grafico a torta ed esegue il rendering del grafico in immagine mentre utilizza la classe CustomSettings creata in precedenza.

**Java**

{{< highlight "csharp" >}}

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
### **Classe CellsFactory aggiunta**
Aspose.Cells 16.11.0 ha esposto la classe CellsFactory che attualmente ha un metodo, ovvero; createStyle. Il metodo CellsFactory.createStyle può essere utilizzato per creare un'istanza della classe Style senza aggiungerla al pool di stili della cartella di lavoro.

Ecco un semplice scenario di utilizzo del metodo CellsFactory.createStyle.

**Java**

{{< highlight "csharp" >}}

 //Initializes the CellsFactory class

CellsFactory factory = new CellsFactory();

//Creates an instance of Style

Style style = factory.createStyle();

{{< /highlight >}}
### **Aggiunta proprietà Workbook.AbsolutePath**
Aspose.Cells 16.11.0 ha esposto la proprietà Workbook.AbsolutePath che consente di ottenere o impostare il percorso assoluto della cartella di lavoro memorizzato nel file workbook.xml. Questa proprietà è utile solo durante l'aggiornamento dei collegamenti esterni.
### **Aggiunto il metodo GridHyperlinkCollection.getHyperlink**
Aspose.Cells.GridWeb 16.11.0 ha esposto il metodo getHyperlink alla classe GridHyperlinkCollection che consente di ottenere l'istanza di GridHyperlink passando un'istanza GridCell o una coppia di interi corrispondenti agli indici di colonna di riga.

{{% alert color="primary" %}} 

Nel caso in cui non sia stato trovato alcun collegamento ipertestuale nella cella specificata, il metodo getHyperlink restituirà null.

{{% /alert %}} 

Ecco un semplice scenario di utilizzo del metodo getHyperlink.

**Java**

{{< highlight "csharp" >}}

 //Gets the active worksheet from the collection

GridWorksheet sheet = gridWeb1.getWorkSheets().get(gridWeb1.getActiveSheetIndex());

//Accesses the GridHyperlinkCollection

GridHyperlinkCollection links = sheet.getHyperlinks();

//Gets hyperlink from cell A1

GridHyperlink link = links.getHyperlink(sheet.getCells().get("A1"));

//Gets hyperlink from cell D1

link = links.getHyperlink(0, 3);

{{< /highlight >}}
## **API obsolete**
### **Costruttore di stili obsoleto**
Si prega di utilizzare il metodo cellsFactory.createStyle come alternativa.
## **API eliminate**
### **Metodo Cell.getConditionalStyle eliminato**
Utilizzare invece il metodo Cell.getConditionalFormattingResult.
### **Metodo Cells.getMaxDataRowInColumn(int colonna) eliminato**
Utilizzare il metodo Cells.getLastDataRow(int) come alternativa.
### **Proprietà PageSetup.Draft eliminata**
Si consiglia invece di utilizzare la proprietà PageSetup.PrintDraft.
### **Proprietà AutoFilter.FilterColumnCollection eliminata**
Si prega di prendere in considerazione l'utilizzo della proprietà AutoFilter.FilterColumns per raggiungere lo stesso obiettivo.
### **Proprietà TickLabels.Rotation eliminata**
Utilizzare invece la proprietà TickLabels.RotationAngle.
