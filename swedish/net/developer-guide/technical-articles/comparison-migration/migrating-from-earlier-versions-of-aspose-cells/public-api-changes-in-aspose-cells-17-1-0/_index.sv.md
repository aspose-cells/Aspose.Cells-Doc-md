---
title: Offentliga API ändringar i Aspose.Cells 17.1.0
type: docs
weight: 370
url: /sv/net/public-api-changes-in-aspose-cells-17-1-0/
---

{{% alert color="primary" %}} 

I detta dokument beskrivs ändringarna i Aspose.Cells API från version 16.12.0 till 17.1.0 som kan vara intressanta för modul/applikationsutvecklare. Det inkluderar inte bara nya och uppdaterade publika metoder, tilläggade och borttagna klasser, etc., utan också en beskrivning av eventuella förändringar i beteendet bakom kulisserna i Aspose.Cells.

{{% /alert %}} 
## **Tillagda API:er**
### **Support för Excel 2016-diagram**
Aspose.Cells API har lagt till stöd för några Excel 2016-diagram genom att förbättra ChartType-uppräkningen. Följande nya fält har lagts till med utgivningen av Aspose.Cells 17.1.0.

- ChartType.BoxWhisker: Serien placeras ut som en låda och ett whisker.
- ChartType.Funnel: Serien placeras ut som en tratt.
- ChartType.ParetoLine: Serien placeras ut som Pareto-linjer.
- ChartType.Sunburst: Serien placeras ut som en sunburst.
- ChartType.Treemap: Serien placeras ut som en treemap.
- ChartType.Waterfall: Serien placeras ut som en waterfall.
- ChartType.Histogram: Serien placeras ut som ett histogram.

{{% alert color="primary" %}} 

Kontrollera den detaljerade artikeln om [Läsning av Excel 2016-diagramtyper](/cells/sv/net/read-and-manipulate-excel-2016-charts/)

{{% /alert %}} 
### **Tillagd Setter for LoadFilter.LoadDataFilterOptions Property**
Aspose.Cells 17.1.0 har lagt till setter för LoadFilter.LoadDataFilterOptions-egendomen för att ersätta variabeln m_LoadDataFilterOptions. Användare kan ändra LoadDataFilterOptions-egendomen i sin egen implementation av LoadFilter-klassen för att ändra beteendet för att ladda mallfiler.

Här är ett enkelt användningsscenario.

{{% alert color="primary" %}} 

Kontrollera den detaljerade artikeln om [Anpassad mallfiltrering](/cells/sv/net/filter-objects-while-loading-workbook-or-worksheet/)

{{% /alert %}} 

**C#**

{{< highlight csharp >}}

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


### **Tillagd CellsHelper.SignificantDigits-egendom**
Aspose.Cells 17.1.0 har exponerat SignificantDigits-egendomen från CellsHelper-klassen vilket gör att man kan hämta eller ställa in antalet signifikanta siffror för numeriska värden i ett kalkylark. Standardvärdet för CellsHelper.SignificantDigits-egendomen är 17, och den är tillämplig endast om resultatet ska lagras i XLSX-filformatet.

Här är ett enkelt scenario för att demonstrera användningen av CellsHelper.SignificantDigits-egendomen.

{{% alert color="primary" %}} 

Kontrollera den detaljerade artikeln om [Angivande av antal signifikanta siffror som ska lagras i Excel-fil](/cells/sv/net/specifying-significant-digits-to-be-stored-in-excel-file/)

{{% /alert %}} 

**C#**

{{< highlight csharp >}}

 // Specify the number of significant digits

CellsHelper.SignificantDigits = 15;

{{< /highlight >}}


### **Tillagd GlowEffect.Color-egendom**
Aspose.Cells 17.1.0 har lagt till GlowEffect.Color-egendomen som kan användas för att hämta färgen på glödeffekten.

Följande utdrag använder GlowEffect.Color-egendomen.

{{% alert color="primary" %}} 

Kontrollera den detaljerade artikeln om [Läsning av formens glödfärg](/cells/sv/net/read-color-of-shape-s-glow-effect/)

{{% /alert %}} 

**C#**

{{< highlight csharp >}}

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


### **Tillagd PageSetup.PaperWidth & PaperHeight-egendom**
Aspose.Cells 17.1.0 har exponerat PaperWidth & PaperHeight-egendomen för PageSetup-klassen. PageSetup.PaperWidth & PageSetup.PaperHeight-egendomen är av typen double och representerar pappersbredden och höjden i tum med hänsyn till sidorienteringen.

{{% alert color="primary" %}} 

Kontrollera den detaljerade artikeln om [Hämtning av kalkylarks papperstorlek](/cells/sv/net/get-paper-width-and-height-of-page-setup-of-worksheet/)

{{% /alert %}} 
### **Tillagt WorkbookSettings.CheckCustomNumberFormat Egendom**
Aspose.Cells 17.1.0 har lagt till egenskapen CheckCustomNumberFormat till klassen WorkbookSettings. CheckCustomNumberFormat är användbar för att kontrollera om egendomen Style.Custom har ställts in korrekt eller inte. Om egenskapen Style.Custom har ställts in felaktigt, det vill säga om värdet inte överensstämmer med ett giltigt mönster, kommer Aspose.Cells API:erna att kasta CellsException med lämpligt meddelande.

{{% alert color="primary" %}} 

Kontrollera den detaljerade artikeln om [Verifiering av anpassat format](/cells/sv/net/check-custom-number-format-when-setting-style-custom-property/)

{{% /alert %}} 

**C#**

{{< highlight csharp >}}

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


### **Tillagt DisplayUnitType.Percentage Fält**
Aspose.Cells 17.1.0 har även exponerat fältet Percentage till enumen DisplayUnitType. Fältet DisplayUnitType.Percentage indikerar att värdena på diagrammet ska delas med 0.01.
## **Borttagen API:er**
### **Instans Variabel m_LoadDataFilterOptions Borttagen**
Denna version har tagit bort instansvariabeln m_LoadDataFilterOptions. Det rekommenderas att istället använda egenskapen LoadFilter.LoadDataFilterOptions.
