---
title: Offentliga API ändringar i Aspose.Cells 8.4.2
type: docs
weight: 160
url: /sv/java/public-api-changes-in-aspose-cells-8-4-2/
---

{{% alert color="primary" %}} 

Detta dokument beskriver förändringarna i Aspose.Cells API från version 8.4.1 till 8.4.2 som kan vara av intresse för modul-/applikationsutvecklare. Det inkluderar inte bara nya och uppdaterade offentliga metoder, [tillagda klasser etc.](/cells/sv/java/public-api-changes-in-aspose-cells-8-4-2/), utan också en beskrivning av eventuella förändringar i beteendet bakom kulisserna i Aspose.Cells.

{{% /alert %}} 
## **Tillagda API:er**
### **Förbättrad diagramskapningsmekanism**
Klassen com.aspose.cells.charts.Chart har exponerat setChartDataRange-metoden för att underlätta uppgiften med diagramskapning. setChartDataRange-metoden accepterar två parametrar, där första parametern är av typen sträng som specificerar cellområdet från vilket dataserierna ska plottas. Den andra parametern är av typen Boolesk som specificerar plottorienteringen, det vill säga; om dataserierna ska plottas från en rad- eller kolumnvärdespalett.

Följande kodsnutt visar hur man skapar ett kolumnschema med några få rader kod under förutsättning att diagrammets plottseriedata finns på samma kalkylblad från cell A1 till D4.

**Java**

{{< highlight csharp >}}

 //Add a new chart of type Column to chart collection

int idx = worksheet.getCharts().add(ChartType.COLUMN, 6, 5, 20, 13);

//Retrieve the newly added chart instance

Chart chart = worksheet.getCharts().get(idx);

//Specify the chart's data series from cell A1 to D4

chart.setChartDataRange("A1:D4", true);

{{< /highlight >}}

### **Tillagd VbaModuleCollection.add-metod**
Aspose.Cells for Java 8.4.2 har exponerat VbaModuleCollection.add-metoden för att lägga till en ny VBA-modul till instansen av Workbook. VbaModuleCollection.add-metoden accepterar en parameter av typen Worksheet för att lägga till en arbetsboksspecifik modul.

Följande kodsnutt visar hur man använder VbaModuleCollection.add-metoden.

**Java**

{{< highlight csharp >}}

 //Create new workbook

Workbook workbook = new Workbook();

//Access first worksheet

Worksheet worksheet = workbook.getWorksheets().get(0);

//Add VBA module

int idx = workbook.getVbaProject().getModules().add(worksheet);

//Access the VBA Module, set its name and code

VbaModule module = workbook.getVbaProject().getModules().get(idx);

module.setName("TestModule");

module.setCodes("Sub ShowMessage()" + "\r\n" +

"    MsgBox \"Welcome to Aspose!\"" + "\r\n" +

"End Sub");

//Save the workbook

workbook.save(output, SaveFormat.XLSM);

{{< /highlight >}}

### **Överlagd metod Cells.copyColumns tillagd**
Aspose.Cells for Java 8.4.2 har exponerat en överlagd version av Cells.copyColumns-metoden för att upprepa kälkolumnerna till destinationskolumnerna. Den nyexponerade metoden accepterar totalt 5 parametrar, där de första 4 parametrarna är desamma som för den vanliga Cells.copyColumns-metoden. Det sista parametern av typen int specificerar antalet destinationskolumner till vilka kälkolumnerna ska upprepas.

Följande kodsnutt visar hur man använder den nyexponerade Cells.copyColumns-metoden.

**Java**

{{< highlight csharp >}}

 //Load an existing workbook

Workbook workbook = new Workbook(input);

//Access first worksheet

Worksheet worksheet = workbook.getWorksheets().get(0);

//Access cells of first worksheet

Cells cells = worksheet.getCells();

//Copy the first two columns (A & B) along with formatting

//to columns G, H & I.

//Please note, the columns G & H will be replaced by A & B respectively

//whereas, column I will be replaced by the column A

cells.copyColumns(cells, 0, 2, 6, 3);

//Save the workbook

workbook.save(output);

{{< /highlight >}}

### **Uppräkningsfälten PasteType.DEFAULT & PasteType.ALL_EXCEPT_BORDERS tillagda**
Med frisläppandet av v8.4.2 har Aspose.Cells API lagt till 2 nya uppräkningsfält för PasteType enligt detaljerna nedan.

- PasteType.DEFAULT: Fungerar liknande Excel's "All"-funktionalitet för att klistra in området av celler.
- PasteType.ALL_EXCEPT_BORDERS: Fungerar liknande Excel's "All except borders"-funktionalitet för att klistra in området av celler.

Följande exempelkod demonstrerar användningen av PasteType.DEFAULT-fältet.

**Java**

{{< highlight csharp >}}

 //Load an existing workbook

Workbook workbook = new Workbook(input);

//Access first worksheet

Worksheet worksheet = workbook.getWorksheets().get(0);

//Access cells of first worksheet

Cells cells = worksheet.getCells();

//Create source & destination ranges

Range source = cells.createRange("A1:B6");

Range destination = cells.createRange("D1:E6");

//Create an instance of PasteOptions and set its PasteType property

PasteOptions options = new PasteOptions();

options.setPasteType(PasteType.DEFAULT);

//Copy the source range onto the destination range with everything except column widths

destination.copy(source, options);

//Save the workbook

workbook.save(output);

{{< /highlight >}}

{{% alert color="primary" %}} 

Från och med frisläppandet av Aspose.Cells for Java 8.4.2 beter sig uppräkningfältet PasteType.ALL annorlunda jämfört med Excels  "All"-funktionalitet för att klistra in området av celler. Nu kopierar även PasteType.ALL kolumnbredderna till destinationsområdet till skillnad från Excels "All"-funktionalitet. För att efterlikna Excels "All"-beteende, använd PasteType.DEFAULT.

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
