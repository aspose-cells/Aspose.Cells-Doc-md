---
title: Offentliga API ändringar i Aspose.Cells 16.11.0
type: docs
weight: 350
url: /sv/net/public-api-changes-in-aspose-cells-16-11-0/
---

{{% alert color="primary" %}} 

Detta dokument beskriver ändringarna i Aspose.Cells API från version 16.10.0 till 16.11.0 som kan vara av intresse för modul/applikationsutvecklare. Det inkluderar inte bara nya och uppdaterade offentliga metoder, tillagda och borttagna klasser osv., utan också en beskrivning av eventuella förändringar i beteendet bakom kulisserna i Aspose.Cells.

{{% /alert %}} 
## **Tillagda API:er**
### **Stöd för globaliseringsinställningar**
Aspose.Cells 16.11.0 har exponerat GlobalizationSettings-klassen tillsammans med WorkbookSettings.GlobalizationSettings-egenskapen för att tvinga Aspose.Cells API:er att använda anpassade etiketter för delsummer. GlobalizationSettings-klassen har följande metoder som kan åsidosättas i den anpassade implementationen för att ge önskade namn till etiketterna Total & Grand Total.

- GlobalizationSettings.GetTotalName: Hämtar totalnamnet för funktionen.
- GlobalizationSettings.GetGrandTotalName: Hämtar det stora totalnamnet för funktionen.

Här är en enkel anpassad klass som utökar GlobalizationSettings-klassen och åsidosätter dess ovanstående metoder för att returnera anpassade etiketter för konsolideringsfunktionen Medelvärde.

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



Följande utdrag laddar en befintlig kalkylblad och lägger till subtotal av typ Genomsnitt på data som redan finns i arbetsbladet. Klassen CustomSettings och dess metoder GetTotalName & GetGrandTotalName kommer att kallas vid tidpunkten för att lägga till subtotal i arbetsbladet.

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



Klassen GlobalizationSettings erbjuder också metoden GetOtherName som är användbar för att få namnet på "Andra" etiketter för cirkeldiagram. Här är ett enkelt användningsscenariot för metoden GlobalizationSettings.GetOtherName.

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



Följande utdrag laddar en befintlig kalkylblad som innehåller ett cirkeldiagram och renderar diagrammet till bild genom att använda klassen CustomSettings som skapats ovan.

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


### **Tillagd CellsFactory-klass**
Aspose.Cells 16.11.0 har exponerat klassen CellsFactory som för närvarande har en metod, det vill säga; CreateStyle. Metoden CellsFactory.CreateStyle kan användas för att skapa en instans av klassen Style utan att lägga till den i arbetsbokens stilpool.

Här är ett enkelt användningsscenariot för metoden CellsFactory.CreateStyle.

**C#**

{{< highlight csharp >}}

 // Initializes the CellsFactory class

CellsFactory factory = new CellsFactory();

// Creates an instance of Style

Style style = factory.CreateStyle();

{{< /highlight >}}


### **Tillagd Workbook.AbsolutePath-egenskap**
Aspose.Cells 16.11.0 har exponerat Workbook.AbsolutePath-egenskapen som tillåter att hämta eller ange den absoluta kalkylbladsbanan som är lagrad i workbook.xml-filen. Denna egenskap är användbar vid endast uppdatering av externa länkar.
### **Tillagd metoden GridHyperlinkCollection.GetHyperlink**
Aspose.Cells.GridWeb 16.11.0 har exponerat metoden GetHyperlink för klassen GridHyperlinkCollection som tillåter att hämta instansen av GridHyperlink genom antingen att skicka en instans av GridCell eller ett par heltal som motsvarar rad- och kolumnindex.

{{% alert color="primary" %}} 

Om ingen hyperlänk har hittats på den angivna cellen kommer metoden GetHyperlink att returnera null.

{{% /alert %}} 

Här är ett enkelt användningsscenariot för metoden GetHyperlink.

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
## **Obsoletterade API:er**
### **Obsoleterad Style-konstruktor**
Vänligen använd cellsFactory.CreateStyle-metoden som ett alternativ.
## **Raderade API:er**
### **Raderad Cell.GetConditionalStyle-metod**
Vänligen använd Cell.GetConditionalFormattingResult-metoden istället.
### **Raderad Cells.MaxDataRowInColumn(int column)-metod**
Vänligen använd Cells.GetLastDataRow(int)-metoden som ett alternativ.
### **Raderad PageSetup.Draft-egenskap**
Det rekommenderas att använda PageSetup.PrintDraft-egenskapen istället.
### **Raderad AutoFilter.FilterColumnCollection-egenskap**
Överväg att använda AutoFilter.FilterColumns-egenskapen för att uppnå samma mål.
### **Raderad TickLabels.Rotation-egenskap**
Använd istället TickLabels.RotationAngle-egenskapen.
{{< app/cells/assistant language="csharp" >}}
