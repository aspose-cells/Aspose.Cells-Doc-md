---
title: Offentlig API Ändringar i Aspose.Cells 8.8.1
type: docs
weight: 280
url: /sv/java/public-api-changes-in-aspose-cells-8-8-1/
---
{{% alert color="primary" %}} 

Det här dokumentet beskriver ändringarna av Aspose.Cells API från version 8.8.0 till 8.8.1 som kan vara av intresse för modul-/applikationsutvecklare. Den innehåller inte bara nya och uppdaterade offentliga metoder, tillagda och borttagna klasser etc., utan också en beskrivning av eventuella förändringar i beteendet bakom kulisserna i Aspose.Cells.

{{% /alert %}} 
## **Lade till API:er**
### **Filtrera data för laddning**
Aspose.Cells for Java 8.8.1 har exponerat LoadDataFilterOptions-uppräkningen tillsammans med LoadOptions.LoadDataFilterOptions-egenskapen som kan användas för att specificera datatypen som ska laddas när arbetsboken byggs från en mallfil. Filtrering av laddade data kan förbättra prestandan för speciella ändamål, särskilt när du använder LightCells API:er.

Uppräkningen LoadDataFilterOptions ger följande val.

1. ALLA för att ladda allt från kalkylarket.
1. INGEN för att ladda ingenting från kalkylarket.
1. CELL_BLANK laddar cellerna vars värden är tomma.
1. CELL_BOOL laddar celler vars värden är booleska.
1. CELL_DATA laddar celldata inklusive värden, formler och formatering.
1. CELL_ERROR laddar celler vars värden är fel.
1. CELL_NUMERIC laddar celler vars värden är numeriska (inklusive datum och tid).
1. CELL_STRING laddar celler vars värden är text/sträng.
1. CELL_VALUE laddar endast cellvärden (alla typer).
1. CHART laddar bara sjökort.
1. CONDITIONAL_FORMATTING läser bara in regler för villkorlig formatering.
1. DATA_VALIDATION laddar endast datavalideringsregler.
1. DOCUMENT_PROPERTIES laddar endast dokumentegenskaper.
1. FORMULA laddar formler inklusive definierade namn.
1. MERGED_AREA laddar endast sammanslagna celler.
1. PIVOT_TABLE laddar pivottabeller.
1. INSTÄLLNINGAR laddar endast inställningar för arbetsbok och arbetsblad.
1. SHAPE laddar endast former.
1. STYLE laddar cellformatering.
1. TABLE laddar Excel-tabeller/listobjekt.

{{% alert color="primary" %}} 

 För mer information om den här funktionen, läs den detaljerade artikeln om[Filtrera data för laddning](/cells/sv/java/filtering-the-kind-of-data-while-loading-the-workbook-from-template-file/).

{{% /alert %}} 

Följande är det enkla användningsscenariot.

**Java**

{{< highlight "csharp" >}}

 //Create an instance of LoadOptions & initialize it with type of template to be loaded

LoadOptions options = new LoadOptions(LoadFormat.XLSX);

//Set LoadDataFilterOptions to load only shapes

options.setLoadDataFilterOptions(LoadDataFilterOptions.SHAPE);

//Create an instance of Workbook from a existing spreadsheet using instance of LoadOptions

Workbook book = new Workbook(filePath, options);

{{< /highlight >}}
### **Konvertera diagram direkt till PDF**
Aspose.Cells API:er har redan gjort det möjligt att rendera diagram till PDF när man använder metoden Chart.toPdf. Med den här utgåvan har API avslöjat en annan överbelastad version av nämnda metod som kan acceptera en instans av OutputStream, vilket gör att användarna kan spara diagrammets PDF i en instans av ByteArrayOutputStream.

Följande är det enkla användningsscenariot.

**Java**

{{< highlight "csharp" >}}

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
### **Lade till WorkbookSettings.PaperSize-egenskap**
Aspose.Cells for Java 8.8.1 har exponerat egenskapen WorkbookSettings.PaperSize för att ställa in standardstorleken för utskriftspapper för hela kalkylarket. Egenskapen WorkbookSettings.PaperSize accepterar ett värde från PaperSizeType-uppräkningen som innehåller de fördefinierade storlekarna för de mest använda utskriftspapperstyperna.

**Java**

{{< highlight "csharp" >}}

 //Create an instance of Workbook

//Optionally load an existing spreadsheet

Workbook book = new Workbook();

//Access WorkbookSettings from the Workbook

WorkbookSettings settings = book.getSettings();

//Set the default printing paper size for the Workbook

settings.setPaperSize(PaperSizeType.PAPER_A_4);

{{< /highlight >}}
### **Lade till Shape.TextBody-egenskap**
Den här versionen av Aspose.Cells for Java API har exponerat Shape.TextBody för att manipulera textens aspekter i en former. Följande utdrag använder nämnda egenskap för att ställa in skuggeffekten för texten i en textruta.

{{% alert color="primary" %}} 

 För mer information om den här funktionen, läs den detaljerade artikeln om[Ställa in skuggeffekt för text](/cells/sv/java/setting-shadow-of-text-effects-of-shape-or-textbox/).

{{% /alert %}} 

**Java**

{{< highlight "csharp" >}}

 //Skapa en instans av Workbook

Arbetsbok bok = ny arbetsbok();

//Åtkomst till första kalkylbladet i arbetsboken

Arbetsblad = book.getWorksheets().get(0);

//Lägg till en textruta i ShapeCollection

int index = sheet.getTextBoxes().add(2, 2, 100, 400);

TextBox textBox = sheet.getTextBoxes().get(index);

//Ställ in texten i textrutan

textBox.setText("Denna text har följande inställningar.\n\nTexteffekter > Skugga > Offset Botten");

//Ställ in skuggeffekt för text

 för (int i = 0; i< textBox.getTextBody().getCount(); i++)

{

  textBox.getTextBody().get(i).getShapeFont().getFillFormat().getShadowEffect().setPresetType(PresetShadowType.OFFSET_BOTTOM);

}

{{< /highlight >}}
### **Lade till Worksheet.calculateFormula(strängformel, CalculationOptions opts) Metod**
Aspose.Cells for Java 8.8.1 har avslöjat ytterligare en överbelastning för metoden Worksheet.calculateFormula som ger möjlighet att beräkna en given formel direkt med anpassade alternativ.

{{% alert color="primary" %}} 

 För mer information om den här funktionen, läs den detaljerade artikeln om[Direkt beräkning av anpassad funktion](/cells/sv/java/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/).

{{% /alert %}} 
### **Lade till GridCell.createValidation Method**
Aspose.Cells.GridWeb har tillhandahållit möjligheten att direkt lägga till valideringsregeln till en enskild cell medan du använder metoden GridCell.createValidation. Den nämnda metoden kräver 2 parametrar. Den första är av typen GridValidationType som bestämmer valideringstypen, medan den andra parametern (isRequied) är av typen Boolean.

**Java**

{{< highlight "csharp" >}}

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
### **Lade till GridCell.removeValidation Method**
Aspose.Cells.GridWeb har också tillhandahållit möjligheten att ta bort datavalideringsregeln från en GridCell samtidigt som metoden GridCell.removeValidation används.
## **Föråldrade API:er**
### **Föråldrad Shape.TextFrame-egenskap**
Det rekommenderas att använda egenskapen Shape.TextBody.TextAlignment istället.
