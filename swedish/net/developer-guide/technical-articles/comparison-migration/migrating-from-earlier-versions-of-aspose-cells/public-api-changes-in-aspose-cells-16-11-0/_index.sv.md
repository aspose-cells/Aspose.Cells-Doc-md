---
title: Offentlig API Ändringar i Aspose.Cells 16.11.0
type: docs
weight: 350
url: /sv/net/public-api-changes-in-aspose-cells-16-11-0/
---
{{% alert color="primary" %}} 

Det här dokumentet beskriver ändringarna av Aspose.Cells API från version 16.10.0 till 16.11.0 som kan vara av intresse för modul-/applikationsutvecklare. Den innehåller inte bara nya och uppdaterade offentliga metoder, tillagda och borttagna klasser etc., utan också en beskrivning av eventuella förändringar i beteendet bakom kulisserna i Aspose.Cells.

{{% /alert %}} 
## **Lade till API:er**
### **Stöd för globaliseringsinställningar**
Aspose.Cells 16.11.0 har exponerat GlobalizationSettings-klassen tillsammans med WorkbookSettings.GlobalizationSettings-egenskapen för att tvinga Aspose.Cells API:erna att använda anpassade etiketter för delsummor. Klassen GlobalizationSettings har följande metoder som kan åsidosättas i den anpassade implementeringen för att ge önskade namn till etiketterna**Total** & **Totalsumma**.

- GlobalizationSettings.GetTotalName: Hämtar det totala namnet på funktionen.
- GlobalizationSettings.GetGrandTotalName: Får det totala namnet på funktionen.

Här är en enkel anpassad klass som utökar GlobalizationSettings-klassen och åsidosätter dess ovannämnda metoder för att returnera anpassade etiketter för konsolideringsfunktionen Average.

**C#**

{{< highlight "csharp" >}}

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



Följande utdrag läser in ett befintligt kalkylblad och lägger till delsumman av typen Average på data som redan finns i kalkylbladet. Klassen CustomSettings och dess GetTotalName & GetGrandTotalName-metoder kommer att anropas när Deltotal läggs till i kalkylbladet.

**C#**

{{< highlight "csharp" >}}

 // Loads an existing spreadsheet containing some data

Workbook book = new Workbook(dir + "sample.xlsx");

// Assigns the GlobalizationSettings property of the WorkbookSettings class

// to the class created in first step

book.Settings.GlobalizationSettings = new Cells.CustomSettings();

// Accesses the 1st worksheet from the collection which contains data

// Data resides in the cell range A2:B9

Worksheet sheet = book.Worksheets[0];

// Adds SubTotal of type Average to the worksheet

sheet.Cells.Subtotal(CellArea.CreateCellArea("A2", "B9"), 0, ConsolidationFunction.Average, new int[]{ 0,1 });

// Calculates Formulas

book.CalculateFormula();

// Auto fits all columns

sheet.AutoFitColumns();

// Saves the workbook on disc

book.Save(dir + "output.xlsx");

{{< /highlight >}}



Klassen GlobalizationSettings erbjuder också metoden GetOtherName som är användbar för att få namnet på "Other"-etiketter för cirkeldiagram. Här är ett enkelt användningsscenario för metoden GlobalizationSettings.GetOtherName.

**C#**

{{< highlight "csharp" >}}

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



Följande utdrag laddar ett befintligt kalkylblad som innehåller ett cirkeldiagram och renderar diagrammet till bild samtidigt som klassen CustomSettings som skapats ovan används.

**C#**

{{< highlight "csharp" >}}

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


### **Lade till CellsFactory Class**
Aspose.Cells 16.11.0 har exponerat klassen CellsFactory som för närvarande har en metod, det vill säga; Skapa stil. Metoden CellsFactory.CreateStyle kan användas för att skapa en instans av klassen Style utan att lägga till den i poolen av arbetsboksstilar.

Här är ett enkelt användningsscenario för CellsFactory.CreateStyle-metoden.

**C#**

{{< highlight "csharp" >}}

 // Initializes the CellsFactory class

CellsFactory factory = new CellsFactory();

// Creates an instance of Style

Style style = factory.CreateStyle();

{{< /highlight >}}


### **Lade till Workbook.AbsolutePath-egenskap**
Aspose.Cells 16.11.0 har exponerat egenskapen Workbook.AbsolutePath gör det möjligt att hämta eller ställa in den absoluta sökvägen för arbetsboken som lagras i filen workbook.xml. Den här egenskapen är användbar endast vid uppdatering av externa länkar.
### **Lade till GridHyperlinkCollection.GetHyperlink Method**
Aspose.Cells.GridWeb 16.11.0 har exponerat GetHyperlink-metoden för GridHyperlinkCollection-klassen som gör det möjligt att hämta instansen av GridHyperlink genom att antingen skicka en instans GridCell eller ett par heltal som motsvarar radkolumnindexen.

{{% alert color="primary" %}} 

Om ingen hyperlänk har hittats i den angivna cellen skulle GetHyperlink-metoden returnera null.

{{% /alert %}} 

Här är ett enkelt användningsscenario för GetHyperlink-metoden.

**C#**

{{< highlight "csharp" >}}

 // Gets the active worksheet from the collection

GridWorksheet sheet = GridWeb1.WorkSheets[GridWeb1.ActiveSheetIndex];

// Accesses the GridHyperlinkCollection

GridHyperlinkCollection links = sheet.Hyperlinks;

// Gets hyperlink from cell A1

GridHyperlink link = links.GetHyperlink(sheet.Cells["A1"]);

// Gets hyperlink from cell D1

link = links.GetHyperlink(0, 3);

{{< /highlight >}}
## **Föråldrade API:er**
### **Föråldrad stilkonstruktör**
Använd cellsFactory.CreateStyle-metoden som ett alternativ.
## **Borttagna API:er**
### **Raderad Cell.GetConditionalStyle Method**
Använd metoden Cell.GetConditionalFormattingResult istället.
### **Raderad Cells.MaxDataRowInColumn(int kolumn) Metod**
Använd metoden Cells.GetLastDataRow(int) som ett alternativ.
### **Borttagen PageSetup.Draft-egenskap**
Det rekommenderas att använda egenskapen PageSetup.PrintDraft istället.
### **Raderad AutoFilter.FilterColumnCollection-egenskap**
Överväg att använda egenskapen AutoFilter.FilterColumns för att uppnå samma mål.
### **Raderade TickLabels.Rotation Property**
Använd egenskapen TickLabels.RotationAngle istället.
