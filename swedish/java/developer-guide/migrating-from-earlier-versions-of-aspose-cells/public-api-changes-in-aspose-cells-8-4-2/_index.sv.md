---
title: Offentlig API Ändringar i Aspose.Cells 8.4.2
type: docs
weight: 160
url: /sv/java/public-api-changes-in-aspose-cells-8-4-2/
---
{{% alert color="primary" %}} 

 Det här dokumentet beskriver ändringarna av Aspose.Cells API från version 8.4.1 till 8.4.2 som kan vara av intresse för modul-/applikationsutvecklare. Det inkluderar inte bara nya och uppdaterade offentliga metoder,[lagt till klasser etc.](/cells/sv/java/public-api-changes-in-aspose-cells-8-4-2/), men också en beskrivning av eventuella förändringar i beteendet bakom kulisserna i Aspose.Cells.

{{% /alert %}} 
## **Lade till API:er**
### **Förbättrad mekanism för att skapa diagram**
Klassen com.aspose.cells.charts.Chart har avslöjat metoden setChartDataRange för att underlätta arbetet med att skapa diagram. Metoden setChartDataRange accepterar två parametrar, där den första parametern är av typen sträng som anger det cellområde från vilket dataserien ska plottas. Den andra parametern är av typen Boolean som anger plotorienteringen, det vill säga; om du vill plotta diagramdataserien från ett intervall av cellvärden efter rad eller kolumner.

Följande kodavsnitt visar hur man skapar ett kolumndiagram med några rader kod förutsatt att diagrammets plotseriedata finns på samma kalkylblad från cell A1 till D4.

**Java**

{{< highlight "csharp" >}}

 //Add a new chart of type Column to chart collection

int idx = worksheet.getCharts().add(ChartType.COLUMN, 6, 5, 20, 13);

//Retrieve the newly added chart instance

Chart chart = worksheet.getCharts().get(idx);

//Specify the chart's data series from cell A1 to D4

chart.setChartDataRange("A1:D4", true);

{{< /highlight >}}

### **Metod VbaModuleCollection.add Tillagd**
Aspose.Cells for Java 8.4.2 har avslöjat metoden VbaModuleCollection.add för att lägga till en ny VBA-modul till instansen av Workbook. Metoden VbaModuleCollection.add accepterar en parameter av typ av kalkylblad för att lägga till en kalkylbladsspecifik modul.

Följande kodavsnitt visar hur man använder metoden VbaModuleCollection.add.

**Java**

{{< highlight "csharp" >}}

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

### **Överbelastad metod Cells.copyColumns tillagd**
Aspose.Cells for Java 8.4.2 har avslöjat en överbelastad version av metoden Cells.copyColumns för att upprepa källkolumnerna till destinationen. Den nyligen exponerade metoden accepterar 5 parametrar totalt, där de första 4 parametrarna är desamma som för den vanliga metoden Cells.copyColumns. Den sista parametern av typen int anger dock antalet destinationskolumner som källkolumnerna måste upprepas på.

Följande kodavsnitt visar hur man använder den nyligen exponerade metoden Cells.copyColumns.

**Java**

{{< highlight "csharp" >}}

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

### **Uppräkningsfält PasteType.DEFAULT & PasteType.ALL_EXCEPT_BORDERS har lagts till**
Med lanseringen av v8.4.2 har Aspose.Cells API lagt till 2 nya uppräkningsfält för PasteType som beskrivs nedan.

- PasteType.DEFAULT: Fungerar på samma sätt som Excels "Alla"-funktion för att klistra in cellintervall.
- PasteType.ALL_BORTSETT FRÅN_BORDERS: Fungerar liknande Excels "Alla utom ramar"-funktionalitet för att klistra in cellintervall.

Följande exempelkod visar användningen av fältet PasteType.DEFAULT.

**Java**

{{< highlight "csharp" >}}

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

Från och med släppet av Aspose.Cells for Java 8.4.2, beter sig den registrerade uppräkningen PasteType.ALL annorlunda jämfört med Excels "Alla"-funktion för att klistra in cellintervall. Nu kopierar PasteType.ALL också kolumnbredderna till destinationsintervallet i motsats till Excels "Alla"-funktionalitet. För att efterlikna Excels "Alla" beteende, använd PasteType.DEFAULT.

{{% /alert %}}
