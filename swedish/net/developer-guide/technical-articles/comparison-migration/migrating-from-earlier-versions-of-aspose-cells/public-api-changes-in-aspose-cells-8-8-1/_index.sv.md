---
title: Offentliga API ändringar i Aspose.Cells 8.8.1
type: docs
weight: 270
url: /sv/net/public-api-changes-in-aspose-cells-8-8-1/
---

{{% alert color="primary" %}} 

Detta dokument beskriver förändringarna i Aspose.Cells API från version 8.8.0 till 8.8.1 som kan vara av intresse för modul/applikationsutvecklare. Det inkluderar inte bara nya och uppdaterade offentliga metoder, tillagda och borttagna klasser etc., utan även en beskrivning av eventuella förändringar i beteendet bakom kulisserna i Aspose.Cells.

{{% /alert %}} 
## **Tillagda API:er**
### **Filtrera data för inläsning**
Aspose.Cells for .NET 8.8.1 har exponerat LoadDataFilterOptions uppräkningen tillsammans med LoadOptions.LoadDataFilterOptions egenskapen som kan användas för att specificera datatypen som ska laddas när arbetsboken byggs från en mallfil. Filtrering av inläst data kan förbättra prestandan för speciella ändamål, särskilt vid användning av LightCells APIer.

LoadDataFilterOptions-enumen tillhandahåller följande val.

1. Allt för att ladda allt från kalkylarket.
1. Inget för att inte ladda något från kalkylarket.
1. CellBlank laddar celler vars värden är blanka.
1. CellBool laddar celler vars värden är Booleska.
1. CellData laddar cellers data inklusive värden, formler och formatering.
1. CellError laddar celler vars värden är fel.
1. CellNumeric laddar celler vars värden är numeriska (inklusive datum och tid).
1. CellString laddar celler vars värden är text/sträng.
1. CellValue laddar endast cellvärden (alla typer).
1. Diagram laddar endast diagram.
1. Villkorlig formatering laddar endast villkorliga formateringsregler.
1. Datavalidering laddar endast datavalideringsregler.
1. Dokumentegenskaper laddar endast dokumentegenskaper.
1. Formel laddar formler inklusive definierade namn.
1. Sammanslagna områden laddar endast sammanslagna celler.
1. PivotTabell laddar pivot tabeller.
1. Inställningar laddar endast Arbetsbok och Arbetsbladsinställningar.
1. Form laddar endast cellformatering.
1. Stil laddar Excel-tabeller/Listobjekt.
För mer detaljer om denna funktion, vänligen granska den detaljerade artikeln om [Filtrera data för inläsning](/cells/sv/net/filtering-the-kind-of-data-while-loading-the-workbook-from-template-file/).

{{% alert color="primary" %}} 

För mer detaljerad information om den här funktionen, vänligen granska den detaljerade artikeln om [Filtrera data vid inläsning](/cells/sv/net/filtering-the-kind-of-data-while-loading-the-workbook-from-template-file/).

{{% /alert %}} 

Följande är det enkla användningscenariot.

**C#**

{{< highlight csharp >}}

 //Create an instance of LoadOptions & initialize it with type of template to be loaded

var options = new LoadOptions(LoadFormat.Xlsx);

//Set LoadDataFilterOptions to load only shapes

options.LoadDataFilterOptions = LoadDataFilterOptions.Shape;

//Create an instance of Workbook from a existing spreadsheet using instance of LoadOptions

var book = new Workbook(filePath, options);

{{< /highlight >}}


### **Konvertera direkt diagram till PDF**
Aspose.Cells APIer har redan tillhandahållit möjligheten att rendera diagram till PDF samtidigt som man använder Chart.ToPdf metoden. Med denna version har APIen exponerat en överlagrad version av nämnda metod som kan acceptera en instans av Stream, vilket gör det möjligt för användarna att spara diagrammets PDF i en instans av MemoryStream.

Följande är det enkla användningscenariot.

**C#**

{{< highlight csharp >}}

 //Create an instance of Workbook and load an existing spreadsheet with a chart

var workbook = new Workbook(filePath);

//Access first worksheet containing a chart

var worksheet = workbook.Worksheets[0];

//Access first chart from the worksheet

var chart = worksheet.Charts[0];

//Save the chart to PDF as Stream

using (MemoryStream stream = new MemoryStream())

{

    chart.ToPdf(stream);

}

{{< /highlight >}}


### **Lagt till WorkbookSettings.PaperSize-egenskapen**
Aspose.Cells for .NET 8.8.1 har exponerat WorkbookSettings.PaperSize egenskapen för att ställa in standard utskriftspappersstorlek för hela kalkylarket. WorkbookSettings.PaperSize egenskapen accepterar ett värde från PaperSizeType-omfattningen som innehåller fördefinierade storlekar för de mest använda utskriftspappren.

**C#**

{{< highlight csharp >}}

 //Create an instance of Workbook

//Optionally load an existing spreadsheet

var book = new Workbook();

//Access WorkbookSettings from the Workbook

var settings = book.Settings;

//Set the default printing paper size for the Workbook

settings.PaperSize = PaperSizeType.PaperA4;

{{< /highlight >}}


### **Lade till Shape.TextBody egenskapen**
Denna version av Aspose.Cells for .NET API har exponerat Shape.TextBody för att manipulera aspekterna av texten i former. Följande kodsnutt använder den nämnda egenskapen för att ställa in skugg effekten av texten i en textruta.

{{% alert color="primary" %}} 

För mer information om denna funktion, vänligen se den detaljerade artikeln om [Inställning av Skugg Effekt för Text](/cells/sv/net/setting-shadow-of-text-effects-of-shape-or-textbox/).

{{% /alert %}} 

**C#**

{{< highlight csharp >}}

 //Create an instance of Workbook

var book = new Workbook();

//Access first worksheet of the Workbook

var sheet = book.Worksheets[0];

//Add a TextBox to the ShapeCollection

var textBox = sheet.Shapes.AddTextBox(2, 0, 2, 0, 100, 400);

//Set the text of the TextBox

textBox.Text = "This text has the following settings.\n\nText Effects > Shadow > Offset Bottom";

//Set shadow effect for text

for (int i = 0; i < textBox.TextBody.Count; i++)

{

    textBox.TextBody[i].ShapeFont.FillFormat.ShadowEffect.PresetType = PresetShadowType.OffsetBottom;

}

{{< /highlight >}}


### **Tillagt Worksheet.CalculateFormula(string formula, CalculationOptions opts) Metod**
Aspose.Cells for .NET 8.8.1 har exponerat en annan överbelastning för CalculateFormula metoden som ger möjlighet att beräkna en given formel direkt med anpassade alternativ.

{{% alert color="primary" %}} 

För mer information om denna funktion, vänligen se den detaljerade artikeln om [Direkt Beräkning av Anpassad Funktion](/cells/sv/net/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/).

{{% /alert %}} 
### **Tillagt GridCell.CreateValidation Metod**
Aspose.Cells.GridWeb har gett förmågan att direkt lägga till valideringsregeln till en enskild cell genom att använda GridCell.CreateValidation metoden. Nämnda metod kräver 2 parametrar. Första är av typen GridValidationType som bestämmer valideringstypen, medan den andra parametern (isRequied) är av typen Boolean.



**C#**

{{< highlight csharp >}}

 //Access first worksheet

GridWorksheet sheet = GridWeb1.WorkSheets[0];

//Access cell B3

GridCell cell = sheet.Cells["B3"];

//Add validation inside the GridCell

//Any value which is not between 20 and 40 will cause error in a GridCell

GridValidation val = cell.CreateValidation(GridValidationType.WholeNumber, true);

val.Formula1 = "=20";

val.Formula2 = "=40";

val.Operator = GridOperatorType.Between;

val.ShowError = true;

val.ShowInput = true;

{{< /highlight >}}


### **Tillagt GridCell.RemoveValidation Metod**
Aspose.Cells.GridWeb har även gett förmågan att ta bort datavalideringsregeln från en GridCell genom att använda GridCell.RemoveValidation metoden.
## **Obsoletterade API:er**
### **Föråldrat Shape.TextFrame Egenskap**
Det rekommenderas att använda Shape.TextBody.TextAlignment egenskapen istället.
