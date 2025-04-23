---
title: Offentliga API ändringar i Aspose.Cells 16.11.0
type: docs
weight: 360
url: /sv/java/public-api-changes-in-aspose-cells-16-11-0/
---

{{% alert color="primary" %}} 

Detta dokument beskriver ändringarna i Aspose.Cells API från version 16.10.0 till 16.11.0 som kan vara av intresse för modul/applikationsutvecklare. Det inkluderar inte bara nya och uppdaterade offentliga metoder, tillagda och borttagna klasser osv., utan också en beskrivning av eventuella förändringar i beteendet bakom kulisserna i Aspose.Cells.

{{% /alert %}} 
## **Tillagda API:er**
### **Stöd för globaliseringsinställningar**
Aspose.Cells 16.11.0 har exponerat GlobalizationSettings-klassen tillsammans med WorkbookSettings.GlobalizationSettings-egenskapen för att tvinga Aspose.Cells API:er att använda anpassade etiketter för delsummer. GlobalizationSettings-klassen har följande metoder som kan åsidosättas i den anpassade implementationen för att ge önskade namn till etiketterna Total & Grand Total.

- GlobalizationSettings.getTotalName: Hämtar det totala namnet på funktionen.
- GlobalizationSettings.getGrandTotalName: Hämtar det stora totala namnet på funktionen.

Här är en enkel anpassad klass som utökar GlobalizationSettings-klassen och åsidosätter dess ovanstående metoder för att returnera anpassade etiketter för konsolideringsfunktionen Medelvärde.

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

Följande kodsnutt laddar en befintlig kalkylblad och lägger till delsumma av typen genomsnitt på data som redan finns tillgänglig i arbetsbladet. Klassen CustomSettings och dess metoder getTotalName och getGrandTotalName kommer att anropas när delsumma läggs till arbetsbladet.

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

GlobalizationSettings-klassen erbjuder också metoden getOtherName som är användbar för att få namnet på "Övrigt"-etiketter för kagendiagram. Här är ett enkelt användningsscenario av GlobalizationSettings.getOtherName-metoden.

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

Följande utdrag laddar en befintlig kalkylblad som innehåller ett cirkeldiagram och renderar diagrammet till bild genom att använda klassen CustomSettings som skapats ovan.

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
### **Tillagd CellsFactory-klass**
Aspose.Cells 16.11.0 har exponerat CellsFactory-klassen som för närvarande har en metod, det vill säga createStyle. CellsFactory.createStyle-metoden kan användas för att skapa en instans av Style-klassen utan att lägga till den i arbetsbokens stilar.

Här är ett enkelt användningsscenario av CellsFactory.createStyle-metoden.

**Java**

{{< highlight csharp >}}

 //Initializes the CellsFactory class

CellsFactory factory = new CellsFactory();

//Creates an instance of Style

Style style = factory.createStyle();

{{< /highlight >}}
### **Tillagd Workbook.AbsolutePath-egenskap**
Aspose.Cells 16.11.0 har exponerat Workbook.AbsolutePath-egenskapen som tillåter att hämta eller ange den absoluta kalkylbladsbanan som är lagrad i workbook.xml-filen. Denna egenskap är användbar vid endast uppdatering av externa länkar.
### **Lades till GridHyperlinkCollection.getHyperlink-metod**
Aspose.Cells.GridWeb 16.11.0 har exponerat getHyperlink-metoden till GridHyperlinkCollection-klassen som tillåter att få instansen av GridHyperlink antingen genom att passera en instans av GridCell eller ett par heltal som motsvarar rad- och kolumnindex.

{{% alert color="primary" %}} 

Om ingen hyperlänk har hittats på den angivna cellen skulle getHyperlink-metoden returnera null.

{{% /alert %}} 

Här är ett enkelt användningsscenario av getHyperlink-metoden.

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
## **Obsoletterade API:er**
### **Obsoleterad Style-konstruktor**
Använd vänligen cellsFactory.createStyle-metoden som ett alternativ.
## **Raderade API:er**
### **Raderad Cell.getConditionalStyle-metod**
Använd vänligen Cell.getConditionalFormattingResult-metoden istället.
### **Raderad Cells.getMaxDataRowInColumn(int column)-metod**
Använd vänligen Cells.getLastDataRow(int)-metoden som ett alternativ.
### **Raderad PageSetup.Draft-egenskap**
Det rekommenderas att använda PageSetup.PrintDraft-egenskapen istället.
### **Raderad AutoFilter.FilterColumnCollection-egenskap**
Överväg att använda AutoFilter.FilterColumns-egenskapen för att uppnå samma mål.
### **Raderad TickLabels.Rotation-egenskap**
Använd istället TickLabels.RotationAngle-egenskapen.
{{< app/cells/assistant language="java" >}}
