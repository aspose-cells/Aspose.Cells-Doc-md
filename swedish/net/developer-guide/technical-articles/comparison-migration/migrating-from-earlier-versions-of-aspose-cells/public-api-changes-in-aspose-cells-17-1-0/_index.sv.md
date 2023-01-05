---
title: Offentlig API Ändringar i Aspose.Cells 17.1.0
type: docs
weight: 370
url: /sv/net/public-api-changes-in-aspose-cells-17-1-0/
---
{{% alert color="primary" %}} 

Det här dokumentet beskriver ändringarna av Aspose.Cells API från version 16.12.0 till 17.1.0 som kan vara av intresse för modul-/applikationsutvecklare. Den innehåller inte bara nya och uppdaterade offentliga metoder, tillagda och borttagna klasser etc., utan också en beskrivning av eventuella förändringar i beteendet bakom kulisserna i Aspose.Cells.

{{% /alert %}} 
## **Lade till API:er**
### **Stöd för Excel 2016-diagram**
Aspose.Cells API:er har lagt till stöd för några Excel 2016-diagram genom att förbättra ChartType-uppräkningen. Följande nya fält har lagts till med utgivningen av Aspose.Cells 17.1.0.

- ChartType.BoxWhisker: Serien är upplagd som box och whisker.
- ChartType.Funnel: Serien är upplagd som en tratt.
- ChartType.ParetoLine: Serien är upplagd som pareto-linjer.
- ChartType.Sunburst: Serien är upplagd som en sunburst.
- ChartType.Treemap: Serien är upplagd som en trädkarta.
- ChartType.Waterfall: Serien är upplagd som ett vattenfall.
- ChartType.Histogram: Serien är upplagd som ett histogram.

{{% alert color="primary" %}} 

 Kolla den detaljerade artikeln om[Läser Excel 2016 diagramtyper](/cells/sv/net/read-and-manipulate-excel-2016-charts/)

{{% /alert %}} 
### **Lade till Setter för egenskapen LoadFilter.LoadDataFilterOptions**
Aspose.Cells 17.1.0 har lagt till setter för egenskapen LoadFilter.LoadDataFilterOptions för att ersätta instansvariabeln m_LoadDataFilterOptions. Användare kan ändra egenskapen LoadDataFilterOptions i sin egen implementering av klassen LoadFilter för att ändra beteendet för att ladda mallfiler.

Här är ett enkelt användningsscenario.

{{% alert color="primary" %}} 

 Kolla den detaljerade artikeln om[Anpassad mallfiltrering](/cells/sv/net/filter-objects-while-loading-workbook-or-worksheet/)

{{% /alert %}} 

**C#**

{{< highlight "csharp" >}}

 class CustomFilter : Aspose.Cells.LoadFilter

{

    public override void StartSheet(Worksheet sheet)

    {

        if (sheet.Name == "Sheet1")

        {

            // Load everything

            this.LoadDataFilterOptions = LoadDataFilterOptions.All;

        }

        else

        {

            // Load nothing

            this.LoadDataFilterOptions = LoadDataFilterOptions.None;

        }

    }

}

{{< /highlight >}}


### **Lade till CellsHelper.SignificantDigits Property**
Aspose.Cells 17.1.0 har exponerat egenskapen SignificantDigits från klassen CellsHelper som gör det möjligt att hämta eller ställa in antalet signifikanta siffror för numeriska värden i ett kalkylblad. Standardvärdet för egenskapen CellsHelper.SignificantDigits är 17 medan det endast är tillämpligt om resultatet måste lagras i filformatet XLSX.

Här är ett enkelt scenario för att demonstrera användningen av CellsHelper.SignificantDigits-egenskapen.

{{% alert color="primary" %}} 

 Kolla den detaljerade artikeln om[Ställa in antal signifikanta siffror](/cells/sv/net/specifying-significant-digits-to-be-stored-in-excel-file/)

{{% /alert %}} 

**C#**

{{< highlight "csharp" >}}

 // Specify the number of significant digits

CellsHelper.SignificantDigits = 15;

{{< /highlight >}}


### **Lade till egenskapen GlowEffect.Color**
Aspose.Cells 17.1.0 har lagt till egenskapen GlowEffect.Color som kan användas för att hämta färgen på glödeffekten.

Följande kodavsnitt använder egenskapen GlowEffect.Color.

{{% alert color="primary" %}} 

 Kolla den detaljerade artikeln om[Att läsa formens glödfärg](/cells/sv/net/read-color-of-shape-s-glow-effect/)

{{% /alert %}} 

**C#**

{{< highlight "csharp" >}}

 // Read the source excel file

var book = new Workbook(dir + "sample.xlsx");

// Access first worksheet

var sheet = book.Worksheets[0];

// Access the first shape

var shape = sheet.Shapes[0];

// Read the glow effect color

var glow = shape.Glow;

var color = glow.Color;

{{< /highlight >}}


### **Lade till PageSetup.PaperWidth & PaperHeight Properties**
Aspose.Cells 17.1.0 har exponerat egenskaperna PaperWidth & PaperHeight för klassen PageSetup. Egenskaperna PageSetup.PaperWidth & PageSetup.PaperHeight är av typen dubbel som representerar papperets bredd och höjd i enheten tum med hänsyn till sidorienteringen.

{{% alert color="primary" %}} 

 Kolla den detaljerade artikeln om[Hämtar arbetsbladets pappersstorlek](/cells/sv/net/get-paper-width-and-height-of-page-setup-of-worksheet/)

{{% /alert %}} 
### **Lade till WorkbookSettings.CheckCustomNumberFormat-egenskap**
Aspose.Cells 17.1.0 har lagt till egenskapen CheckCustomNumberFormat till klassen WorkbookSettings. CheckCustomNumberFormat är användbart för att kontrollera om Style.Custom-egenskapen har ställts in korrekt eller inte. Om egenskapen Style.Custom har ställts in felaktigt, det vill säga; värdet överensstämmer inte med ett giltigt mönster då Aspose.Cells API:erna skickar CellsException med lämpligt meddelande.

{{% alert color="primary" %}} 

 Kolla den detaljerade artikeln om[Verifierar anpassat format](/cells/sv/net/check-custom-number-format-when-setting-style-custom-property/)

{{% /alert %}} 

**C#**

{{< highlight "csharp" >}}

 // Create an instance of Workbook

var book = new Workbook();

// Set CheckCustomNumberFormat property to true

book.Settings.CheckCustomNumberFormat = true;

// Access first worksheet

var sheet = book.Worksheets[0];

// Access a cell

var cell = sheet.Cells["B5"];

// Insert a value to the cell

cell.PutValue(2347);

// Access cell's style

Style style = cell.GetStyle();



// Set Custom property to an invalid pattern

style.Custom = "ggg @ fff";

// Set the modified style to the cell

cell.SetStyle(style);

{{< /highlight >}}


### **Fältet DisplayUnitType.Percentage har lagts till**
Aspose.Cells 17.1.0 har också exponerat fältet Procent för DisplayUnitType-uppräkningen. Fältet DisplayUnitType.Percentage indikerar att värdena på diagrammet ska delas med 0,01.
## **Borttagna API:er**
### **Instansvariabel m_LoadDataFilterOptions borttagen**
Den här versionen har tagit bort instansvariabeln m_LoadDataFilterOptions. Det rekommenderas att använda egenskapen LoadFilter.LoadDataFilterOptions istället.
