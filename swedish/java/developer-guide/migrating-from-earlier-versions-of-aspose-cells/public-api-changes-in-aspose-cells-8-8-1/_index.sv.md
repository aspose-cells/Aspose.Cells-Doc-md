---
title: Offentliga API ändringar i Aspose.Cells 8.8.1
type: docs
weight: 280
url: /sv/java/public-api-changes-in-aspose-cells-8-8-1/
---

{{% alert color="primary" %}} 

Detta dokument beskriver förändringarna i Aspose.Cells API från version 8.8.0 till 8.8.1 som kan vara av intresse för modul/applikationsutvecklare. Det inkluderar inte bara nya och uppdaterade offentliga metoder, tillagda och borttagna klasser etc., utan även en beskrivning av eventuella förändringar i beteendet bakom kulisserna i Aspose.Cells.

{{% /alert %}} 
## **Tillagda API:er**
### **Filtrera data för inläsning**
Aspose.Cells for Java 8.8.1 har exponerat LoadDataFilterOptions-enumen tillsammans med LoadOptions.LoadDataFilterOptions-egenskapen som kan användas för att specificera datatypen som ska laddas vid skapandet av arbetsboken från en mallfil. Filtrering av inläst data kan förbättra prestandan för speciella ändamål, särskilt när du använder LightCells API.

LoadDataFilterOptions-enumen tillhandahåller följande val.

1. ALL för att ladda allt från kalkylarket.
1. NONE för att inte ladda något från kalkylarket.
1. CELL_BLANK laddar celler vars värden är blanka.
1. CELL_BOOL laddar celler vars värden är Booleska.
1. CELL_DATA laddar celler med data inklusive värden, formler och formatering.
1. CELL_ERROR laddar celler vars värden är fel.
1. CELL_NUMERIC laddar celler vars värden är numeriska (inklusive datum och tid).
1. CELL_STRING laddar celler vars värden är text/sträng.
1. CELL_VALUE laddar endast cellvärden (alla typer).
1. CHART laddar endast diagram.
1. CONDITIONAL_FORMATTING laddar endast villkorlig formatering.
1. DATA_VALIDATION laddar endast datavalideringsregler.
1. DOCUMENT_PROPERTIES laddar endast dokumentegenskaper.
1. FORMULA laddar formler inklusive definierade namn.
1. MERGED_AREA laddar endast sammanfogade celler.
1. PIVOT_TABLE laddar pivottabeller.
1. SETTINGS laddar endast arbetsbok- och kalkylbladsinställningar.
1. SHAPE laddar endast former.
1. STYLE laddar cellformatering.
1. TABLE laddar Excel-tabeller/Listobjekt.

{{% alert color="primary" %}} 

För mer detaljerad information om denna funktion, vänligen granska den detaljerade artikeln om [Filtrera data för inläsning](/cells/sv/java/filtering-the-kind-of-data-while-loading-the-workbook-from-template-file/).

{{% /alert %}} 

Följande är det enkla användningscenariot.

**Java**

{{< highlight csharp >}}

 //Create an instance of LoadOptions & initialize it with type of template to be loaded

LoadOptions options = new LoadOptions(LoadFormat.XLSX);

//Set LoadDataFilterOptions to load only shapes

options.setLoadDataFilterOptions(LoadDataFilterOptions.SHAPE);

//Create an instance of Workbook from a existing spreadsheet using instance of LoadOptions

Workbook book = new Workbook(filePath, options);

{{< /highlight >}}
### **Konvertera direkt diagram till PDF**
Aspose.Cells API har redan gett möjlighet att rendera diagram till PDF medan du använder Chart.toPdf-metoden. Med denna version har API:et exponerat en ytterligare överlagrad version av nämnda metod som kan acceptera en instans av OutputStream, vilket tillåter användare att spara diagrammets PDF i en instans av ByteArrayOutputStream.

Följande är det enkla användningscenariot.

**Java**

{{< highlight csharp >}}

 //Create an instance of Workbook and load an existing spreadsheet with a chart

Workbook workbook = new Workbook(filePath);

//Access first worksheet containing a chart

Worksheet worksheet = workbook.getWorksheets().get(0);

//Access first chart from the worksheet

Chart chart = worksheet.getCharts().get(0);

//Save the chart to PDF as Stream

ByteArrayOutputStream outStream = new ByteArrayOutputStream();

chart.toPdf(outStream);

{{< /highlight >}}
### **Lagt till WorkbookSettings.PaperSize-egenskapen**
Aspose.Cells for Java 8.8.1 har exponerat WorkbookSettings.PaperSize-egenskapen för att ange standardpappersstorleken för hela kalkylarket. WorkbookSettings.PaperSize-egenskapen accepterar en värde från PaperSizeType enumen som innehåller fördefinierade storlekar för de mest använda pappersstorlekarna.

**Java**

{{< highlight csharp >}}

 //Create an instance of Workbook

//Optionally load an existing spreadsheet

Workbook book = new Workbook();

//Access WorkbookSettings from the Workbook

WorkbookSettings settings = book.getSettings();

//Set the default printing paper size for the Workbook

settings.setPaperSize(PaperSizeType.PAPER_A_4);

{{< /highlight >}}
### **Lade till Shape.TextBody egenskapen**
Denna version av Aspose.Cells for Java API har exponerat Shape.TextBody för att manipulera aspekterna av texten i en form. Följande kodsnutt använder den angivna egenskapen för att ställa in skugg effekten för texten i en TextBox.

{{% alert color="primary" %}} 

För mer information om den här funktionen, vänligen granska den detaljerade artikeln om [inställning av skugg effekt för text](/cells/sv/java/setting-shadow-of-text-effects-of-shape-or-textbox/).

{{% /alert %}} 

**Java**

{{< highlight csharp >}}

 //Create an instance of Workbook

Workbook book = new Workbook();

//Access first worksheet of the Workbook

Worksheet sheet = book.getWorksheets().get(0);

//Add a TextBox to the ShapeCollection

int index = sheet.getTextBoxes().add(2, 2, 100, 400);

TextBox textBox = sheet.getTextBoxes().get(index);

//Set the text of the TextBox

textBox.setText("This text has the following settings.\n\nText Effects > Shadow > Offset Bottom");

//Set shadow effect for text

for (int i = 0; i < textBox.getTextBody().getCount(); i++)

{

  textBox.getTextBody().get(i).getShapeFont().getFillFormat().getShadowEffect().setPresetType(PresetShadowType.OFFSET_BOTTOM);

}

{{< /highlight >}}
### **Lade till Worksheet.calculateFormula(string formula, CalculationOptions opts) Metoden**
Aspose.Cells for Java 8.8.1 har exponerat en annan överbelastning för Worksheet.calculateFormula-metoden som ger möjlighet att beräkna en given formel direkt med anpassade alternativ.

{{% alert color="primary" %}} 

För mer information om denna funktion, vänligen granska den detaljerade artikeln om [Direkt beräkning av anpassad funktion](/cells/sv/java/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/).

{{% /alert %}} 
### **Lade till GridCell.createValidation Metoden**
Aspose.Cells.GridWeb har gett möjlighet att direkt lägga till valideringsregeln till en enskild cell medan du använder GridCell.createValidation-metoden. Den angivna metoden kräver 2 parametrar. Den första är av typen GridValidationType som bestämmer valideringstypen, medan den andra parametern (isRequied) är av typen Boolean.

**Java**

{{< highlight csharp >}}

 //Access first worksheet

GridWorksheet sheet = gridweb.getWorkSheets().get(0);

//Access cell B3

GridCell cell = sheet.getCells().get("B3");

//Add validation inside the GridCell

//Any value which is not between 20 and 40 will cause error in a GridCell

GridValidation val = cell.createValidation(GridValidationType.WHOLE_NUMBER, true);

val.setFormula1("=20");

val.setFormula2("=40");

val.setOperator(OperatorType.BETWEEN);

val.setShowError(true);

val.setShowInput(true);

{{< /highlight >}}
### **Lade till GridCell.removeValidation Metoden**
Aspose.Cells.GridWeb har också gett möjlighet att ta bort data valideringsregeln från en GridCell medan du använder GridCell.removeValidation metoden.
## **Obsoletterade API:er**
### **Föråldrat Shape.TextFrame Egenskap**
Det rekommenderas att använda Shape.TextBody.TextAlignment egenskapen istället.
{{< app/cells/assistant language="java" >}}
