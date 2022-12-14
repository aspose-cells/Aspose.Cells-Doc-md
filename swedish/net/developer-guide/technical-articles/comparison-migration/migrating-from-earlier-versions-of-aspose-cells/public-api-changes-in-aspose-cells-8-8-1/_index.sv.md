---
title: Offentliga API-ändringar i Aspose.Cells 8.8.1
type: docs
weight: 270
url: /sv/net/public-api-changes-in-aspose-cells-8-8-1/
---
{{% alert color="primary" %}} 

Det här dokumentet beskriver ändringarna av Aspose.Cells API från version 8.8.0 till 8.8.1 som kan vara av intresse för modul-/applikationsutvecklare. Den innehåller inte bara nya och uppdaterade offentliga metoder, tillagda och borttagna klasser etc., utan också en beskrivning av eventuella förändringar i beteendet bakom kulisserna i Aspose.Cells.

{{% /alert %}} 
## **Lade till API:er**
### **Filtrera data för laddning**
Aspose.Cells för .NET 8.8.1 har exponerat LoadDataFilterOptions-uppräkningen tillsammans med LoadOptions.LoadDataFilterOptions-egenskapen som kan användas för att ange vilken datatyp som ska laddas när arbetsboken byggs från en mallfil. Filtrering av laddade data kan förbättra prestandan för speciella ändamål, särskilt när du använder LightCells API:er.

Uppräkningen LoadDataFilterOptions ger följande val.

1. Allt för att ladda allt från kalkylarket.
1. Ingen för att ladda ingenting från kalkylarket.
1. CellBlank laddar cellerna vars värden är tomma.
1. CellBool laddar celler vars värden är booleska.
1. CellData laddar celldata inklusive värden, formler och formatering.
1. CellError laddar celler vars värden är fel.
1. CellNumeric laddar celler vars värden är numeriska (inklusive datum och tid).
1. CellString laddar celler vars värden är text/sträng.
1. CellValue laddar endast cellvärden (alla typer).
1. Diagram laddar bara diagram.
1. ConditionalFormatting läser bara in regler för villkorlig formatering.
1. DataValidation laddar endast datavalideringsregler.
1. DocumentProperties laddar endast dokumentegenskaper.
1. Formel laddar formler inklusive definierade namn.
1. MergedArea laddar bara sammanslagna celler.
1. Pivottabell laddar pivottabeller.
1. Inställningar läser bara in inställningar för arbetsbok och arbetsblad.
1. Shape laddar bara former.
1. Stil laddar cellformatering.
1. Tabell laddar Excel-tabeller/listobjekt.

{{% alert color="primary" %}} 

 För mer information om den här funktionen, läs den detaljerade artikeln om[Filtrera data för laddning](/cells/sv/net/filtering-the-kind-of-data-while-loading-the-workbook-from-template-file/).

{{% /alert %}} 

Följande är det enkla användningsscenariot.

**C#**

{{< highlight "csharp" >}}

 //Create an instance of LoadOptions & initialize it with type of template to be loaded

var options = new LoadOptions(LoadFormat.Xlsx);

//Set LoadDataFilterOptions to load only shapes

options.LoadDataFilterOptions = LoadDataFilterOptions.Shape;

//Create an instance of Workbook from a existing spreadsheet using instance of LoadOptions

var book = new Workbook(filePath, options);

{{< /highlight >}}


### **Konvertera diagram direkt till PDF**
Aspose.Cells API:er har redan gjort det möjligt att rendera diagram till PDF när man använder metoden Chart.ToPdf. Med den här utgåvan har API:et avslöjat en annan överbelastad version av nämnda metod som kan acceptera en instans av Stream, vilket gör att användarna kan spara diagrammets PDF i en instans av MemoryStream.

Följande är det enkla användningsscenariot.

**C#**

{{< highlight "csharp" >}}

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


### **Lade till WorkbookSettings.PaperSize-egenskap**
Aspose.Cells för .NET 8.8.1 har exponerat egenskapen WorkbookSettings.PaperSize för att ställa in standardstorleken för utskriftspapper för hela kalkylarket. Egenskapen WorkbookSettings.PaperSize accepterar ett värde från PaperSizeType-uppräkningen som innehåller de fördefinierade storlekarna för de mest använda utskriftspapperstyperna.

**C#**

{{< highlight "csharp" >}}

 //Create an instance of Workbook

//Optionally load an existing spreadsheet

var book = new Workbook();

//Access WorkbookSettings from the Workbook

var settings = book.Settings;

//Set the default printing paper size for the Workbook

settings.PaperSize = PaperSizeType.PaperA4;

{{< /highlight >}}


### **Lade till Shape.TextBody-egenskap**
Denna version av Aspose.Cells för .NET API har exponerat Shape.TextBody för att manipulera textens aspekter i en former. Följande utdrag använder nämnda egenskap för att ställa in skuggeffekten för texten i en textruta.

{{% alert color="primary" %}} 

 För mer information om den här funktionen, läs den detaljerade artikeln om[Ställa in skuggeffekt för text](/cells/sv/net/setting-shadow-of-text-effects-of-shape-or-textbox/).

{{% /alert %}} 

**C#**

{{< highlight "csharp" >}}

//Skapa en instans av Workbook

var book = new Workbook();

//Åtkomst till första kalkylbladet i arbetsboken

var sheet = book.Worksheets[0];

//Lägg till en textruta i ShapeCollection

var textBox = sheet.Shapes.AddTextBox(2, 0, 2, 0, 100, 400);

//Ställ in texten i textrutan

textBox.Text = "Denna text har följande inställningar.\n\nTexteffekter > Skugga > Offset Botten";

//Ställ in skuggeffekt för text

 för (int i = 0; i< textBox.TextBody.Count; i++)

{

    textBox.TextBody[i].ShapeFont.FillFormat.ShadowEffect.PresetType = PresetShadowType.OffsetBottom;

}

{{< /highlight >}}


### **Lade till Worksheet.CalculateFormula(strängformel, CalculationOptions opts) Metod**
Aspose.Cells för .NET 8.8.1 har avslöjat ytterligare en överbelastning för metoden CalculateFormula som ger möjlighet att beräkna en given formel direkt med anpassade alternativ.

{{% alert color="primary" %}} 

 För mer information om den här funktionen, läs den detaljerade artikeln om[Direkt beräkning av anpassad funktion](/cells/sv/net/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/).

{{% /alert %}} 
### **Lade till GridCell.CreateValidation Method**
Aspose.Cells.GridWeb har tillhandahållit möjligheten att direkt lägga till valideringsregeln till en enskild cell medan du använder metoden GridCell.CreateValidation. Den nämnda metoden kräver 2 parametrar. Den första är av typen GridValidationType som bestämmer valideringstypen, medan den andra parametern (isRequied) är av typen Boolean.



**C#**

{{< highlight "csharp" >}}

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


### **Lade till GridCell.RemoveValidation Method**
Aspose.Cells.GridWeb har också tillhandahållit möjligheten att ta bort datavalideringsregeln från en GridCell när du använder metoden GridCell.RemoveValidation.
## **Föråldrade API:er**
### **Föråldrad Shape.TextFrame-egenskap**
Det rekommenderas att använda egenskapen Shape.TextBody.TextAlignment istället.
