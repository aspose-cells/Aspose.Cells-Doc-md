---
title: Offentliga API-ändringar i Aspose.Cells 16.11.0
type: docs
weight: 360
url: /sv/java/public-api-changes-in-aspose-cells-16-11-0/
---
{{% alert color="primary" %}} 

Det här dokumentet beskriver ändringarna av Aspose.Cells API från version 16.10.0 till 16.11.0 som kan vara av intresse för modul-/applikationsutvecklare. Den innehåller inte bara nya och uppdaterade offentliga metoder, tillagda och borttagna klasser etc., utan också en beskrivning av eventuella förändringar i beteendet bakom kulisserna i Aspose.Cells.

{{% /alert %}} 
## **Lade till API:er**
### **Stöd för globaliseringsinställningar**
Aspose.Cells 16.11.0 har exponerat GlobalizationSettings-klassen tillsammans med WorkbookSettings.GlobalizationSettings-egenskapen för att tvinga Aspose.Cells API:erna att använda anpassade etiketter för delsummor. Klassen GlobalizationSettings har följande metoder som kan åsidosättas i den anpassade implementeringen för att ge önskade namn till etiketterna**Total** & **Totalsumma**.

- GlobalizationSettings.getTotalName: Hämtar det totala namnet på funktionen.
- GlobalizationSettings.getGrandTotalName: Får det totala namnet på funktionen.

Här är en enkel anpassad klass som utökar GlobalizationSettings-klassen och åsidosätter dess ovannämnda metoder för att returnera anpassade etiketter för konsolideringsfunktionen Average.

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

Följande utdrag läser in ett befintligt kalkylblad och lägger till delsumman av typen Average på data som redan finns i kalkylbladet. Klassen CustomSettings och dess getTotalName & getGrandTotalName-metoder kommer att anropas när Subtotal läggs till i kalkylbladet.

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

Klassen GlobalizationSettings erbjuder också metoden getOtherName som är användbar för att få namnet på "Other"-etiketter för cirkeldiagram. Här är ett enkelt användningsscenario för metoden GlobalizationSettings.getOtherName.

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

Följande utdrag laddar ett befintligt kalkylblad som innehåller ett cirkeldiagram och renderar diagrammet till bild samtidigt som klassen CustomSettings som skapats ovan används.

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
### **Lade till CellsFactory Class**
Aspose.Cells 16.11.0 har exponerat klassen CellsFactory som för närvarande har en metod, det vill säga; skapa stil. Metoden CellsFactory.createStyle kan användas för att skapa en instans av klassen Style utan att lägga till den i poolen av arbetsboksstilar.

Här är ett enkelt användningsscenario för metoden CellsFactory.createStyle.

**Java**

{{< highlight "csharp" >}}

 //Initializes the CellsFactory class

CellsFactory factory = new CellsFactory();

//Creates an instance of Style

Style style = factory.createStyle();

{{< /highlight >}}
### **Lade till Workbook.AbsolutePath-egenskap**
Aspose.Cells 16.11.0 har exponerat egenskapen Workbook.AbsolutePath gör det möjligt att hämta eller ställa in den absoluta sökvägen för arbetsboken som lagras i filen workbook.xml. Den här egenskapen är användbar endast vid uppdatering av externa länkar.
### **Lade till GridHyperlinkCollection.getHyperlink Method**
Aspose.Cells.GridWeb 16.11.0 har exponerat getHyperlink-metoden för GridHyperlinkCollection-klassen som gör det möjligt att hämta instansen av GridHyperlink genom att antingen skicka en instans GridCell eller ett par heltal som motsvarar radkolumnindexen.

{{% alert color="primary" %}} 

Om ingen hyperlänk har hittats i den angivna cellen skulle getHyperlink-metoden returnera null.

{{% /alert %}} 

Här är ett enkelt användningsscenario för getHyperlink-metoden.

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
## **Föråldrade API:er**
### **Föråldrad stilkonstruktör**
Använd cellsFactory.createStyle-metoden som ett alternativ.
## **Borttagna API:er**
### **Borttagen Cell.getConditionalStyle Method**
Använd metoden Cell.getConditionalFormattingResult istället.
### **Raderad Cells.getMaxDataRowInColumn(int kolumn) Metod**
Använd metoden Cells.getLastDataRow(int) som ett alternativ.
### **Borttagen PageSetup.Draft-egenskap**
Det rekommenderas att använda egenskapen PageSetup.PrintDraft istället.
### **Raderad AutoFilter.FilterColumnCollection-egenskap**
Överväg att använda egenskapen AutoFilter.FilterColumns för att uppnå samma mål.
### **Raderade TickLabels.Rotation Property**
Använd egenskapen TickLabels.RotationAngle istället.
