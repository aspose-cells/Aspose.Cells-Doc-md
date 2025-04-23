---
title: Offentliga API ändringar i Aspose.Cells 8.4.2
type: docs
weight: 150
url: /sv/net/public-api-changes-in-aspose-cells-8-4-2/
---

{{% alert color="primary" %}} 

Detta dokument beskriver ändringarna i Aspose.Cells API från version 8.4.1 till 8.4.2 som kan vara av intresse för modul-/applikationsutvecklare. Det inkluderar inte bara nya och uppdaterade offentliga metoder, [tillagda klasser etc.](/cells/sv/net/public-api-changes-in-aspose-cells-8-4-2/), utan även en beskrivning av eventuella förändringar i beteendet bakom kulisserna i Aspose.Cells.

{{% /alert %}} 
## **Tillagda API:er**
### **Förbättrad diagramskapningsmekanism**
Aspose.Cells.Charts.Chart-klassen har exponerat SetChartDataRange-metoden för att underlätta uppgiften med att skapa diagram. SetChartDataRange-metoden accepterar två parametrar, där första parametern är av typen sträng som specificerar cellområdet från vilket dataserierna ska plottas. Den andra parametern är av typen Boolean som specificerar plottorienteringen, det vill säga; om dataserierna ska plottas från ett cellvärdesområde efter rad eller kolumn.

Följande kodsnutt visar hur man skapar ett kolumnschema med några få rader kod under förutsättning att diagrammets plottseriedata finns på samma kalkylblad från cell A1 till D4.

**C#**

{{< highlight csharp >}}

 //Add a new chart of type Column to chart collection

int idx = worksheet.Charts.Add(ChartType.Column, 6, 5, 20, 13);

//Retrieve the newly added chart instance

Chart chart = worksheet.Charts[idx];

//Specify the chart's data series from cell A1 to D4

chart.SetChartDataRange("A1:D4", true);

{{< /highlight >}}


### **Tillagd VbaModuleCollection.Add-metod**
Aspose.Cells for .NET 8.4.2 har exponerat VbaModuleCollection.Add-metoden för att lägga till en ny VBA-modul till instansen av Workbook. VbaModuleCollection.Add-metoden accepterar en parameter av typen Worksheet för att lägga till en arbetsbladsspecifik modul.

Följande kodsnutt visar hur man använder VbaModuleCollection.Add-metoden.

**C#**

{{< highlight csharp >}}

 //Create new workbook

Workbook workbook = new Workbook();

//Access first worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Add VBA module for first worksheet

int idx = workbook.VbaProject.Modules.Add(worksheet);

//Access the VBA Module, set its name and code

Aspose.Cells.Vba.VbaModule module = workbook.VbaProject.Modules[idx];

module.Name = "TestModule";

module.Codes = "Sub ShowMessage()" + "\r\n" +

"    MsgBox \"Welcome to Aspose!\"" + "\r\n" +

"End Sub";

//Save the workbook

workbook.Save(output, SaveFormat.Xlsm);

{{< /highlight >}}


### **Överlagrad metod Cells.CopyColumns tillagd**
Aspose.Cells for .NET 8.4.2 har exponerat en överlagrad version av Cells.CopyColumns-metoden för att upprepa källkolumnerna på destinationen. Den nyexponerade metoden accepterar totalt 5 parametrar, där de första 4 parametrarna är desamma som Cells.CopyColumns-metoden. Men den sista parametern av typen int specifierar antalet destinationsspalter på vilka källspalterna ska upprepas.

Följande kodsnutt visar hur man använder den nyexponerade Cells.CopyColumns-metoden.

**C#**

{{< highlight csharp >}}

 //Load an existing workbook

Workbook workbook = new Workbook(input);

//Access first worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Access cells of first worksheet

Cells cells = worksheet.Cells;

//Copy the first two columns (A & B) along with formatting

//to columns G, H & I.

//Please note, the columns G & H will be replaced by A & B respectively

//whereas, column I will be replaced by the column A

cells.CopyColumns(cells, 0, 2, 6, 3);

//Save the workbook

workbook.Save(output);

{{< /highlight >}}


### **Enumerationsfälten PasteType.Default & PasteType.DefaultExceptBorders tillagda**
Med frisläppandet av v8.4.2 har Aspose.Cells API lagt till 2 nya uppräkningsfält för PasteType enligt detaljerna nedan.

- PasteType.Default: Fungerar liknande Excel's "All"-funktionalitet för att klistra in område med celler.
- PasteType.DefaultExceptBorders: Fungerar liknande Excel's "All except borders" funktion för att klistra in området med celler.

Följande kodexempel demonstrerar användningen av fältet PasteType.Default.

**C#**

{{< highlight csharp >}}

 //Load an existing workbook

Workbook workbook = new Workbook(input);

//Access first worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Access cells of first worksheet

Cells cells = worksheet.Cells;

//Create source & destination ranges

Range source = cells.CreateRange("A1:B6");

Range destination = cells.CreateRange("D1:E6");

//Copy the source range onto the destination range with everything except column widths

destination.Copy(source, new PasteOptions() { PasteType = PasteType.Default });

//Save the workbook

workbook.Save(output);

{{< /highlight >}}

{{% alert color="primary" %}} 

Från och med släppet av Aspose.Cells for .NET 8.4.2, beter sig uppräkningfältet PasteType.All annorlunda jämfört med Excels "All" funktionalitet vid att klistra in området med celler. Nu kopierar PasteType.All även kolumnbredderna till destinationsområdet istället för Excels "All" funktionalitet. För att härma Excels "All" beteende, vänligen använd PasteType.Default.

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}
