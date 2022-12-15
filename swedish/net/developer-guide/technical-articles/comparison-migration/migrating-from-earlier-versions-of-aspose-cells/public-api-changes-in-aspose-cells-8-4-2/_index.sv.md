---
title: Offentlig API Ändringar i Aspose.Cells 8.4.2
type: docs
weight: 150
url: /sv/net/public-api-changes-in-aspose-cells-8-4-2/
---
{{% alert color="primary" %}} 

 Det här dokumentet beskriver ändringarna av Aspose.Cells API från version 8.4.1 till 8.4.2 som kan vara av intresse för modul-/applikationsutvecklare. Det inkluderar inte bara nya och uppdaterade offentliga metoder,[lagt till klasser etc.](/cells/sv/net/public-api-changes-in-aspose-cells-8-4-2/), men också en beskrivning av eventuella förändringar i beteendet bakom kulisserna i Aspose.Cells.

{{% /alert %}} 
## **Lade till API:er**
### **Förbättrad mekanism för att skapa diagram**
Klassen Aspose.Cells.Charts.Chart har exponerat metoden SetChartDataRange för att underlätta arbetet med att skapa diagram. Metoden SetChartDataRange accepterar två parametrar, där den första parametern är av typen sträng som anger från vilket cellområde dataserien ska plottas. Den andra parametern är av typen Boolean som anger plotorienteringen, det vill säga; om du vill plotta diagramdataserien från ett intervall av cellvärden efter rad eller kolumner.

Följande kodavsnitt visar hur man skapar ett kolumndiagram med några rader kod förutsatt att diagrammets plotseriedata finns på samma kalkylblad från cell A1 till D4.

**C#**

{{< highlight "csharp" >}}

 //Add a new chart of type Column to chart collection

int idx = worksheet.Charts.Add(ChartType.Column, 6, 5, 20, 13);

//Retrieve the newly added chart instance

Chart chart = worksheet.Charts[idx];

//Specify the chart's data series from cell A1 to D4

chart.SetChartDataRange("A1:D4", true);

{{< /highlight >}}


### **Metod VbaModuleCollection.Add tillagd**
Aspose.Cells for .NET 8.4.2 har avslöjat metoden VbaModuleCollection.Add för att lägga till en ny VBA-modul till instansen av Workbook. Metoden VbaModuleCollection.Add accepterar en parameter av typ av arbetsblad för att lägga till en kalkylbladsspecifik modul.

Följande kodavsnitt visar hur man använder metoden VbaModuleCollection.Add.

**C#**

{{< highlight "csharp" >}}

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


### **Överbelastad metod Cells.CopyColumns har lagts till**
Aspose.Cells for .NET 8.4.2 har avslöjat en överbelastad version av metoden Cells.CopyColumns för att upprepa källkolumnerna till destinationen. Den nyligen exponerade metoden accepterar 5 parametrar totalt, där de första 4 parametrarna är desamma som för den vanliga Cells.CopyColumns-metoden. Den sista parametern av typen int anger dock antalet destinationskolumner som källkolumnerna måste upprepas på.

Följande kodavsnitt visar hur man använder den nyligen exponerade metoden Cells.CopyColumns.

**C#**

{{< highlight "csharp" >}}

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


### **Uppräkningsfält PasteType.Default & PasteType.DefaultExceptBorders har lagts till**
Med lanseringen av v8.4.2 har Aspose.Cells API lagt till 2 nya uppräkningsfält för PasteType som beskrivs nedan.

- PasteType.Default: Fungerar liknande Excels "Alla"-funktion för att klistra in cellintervall.
- PasteType.DefaultExceptBorders: Fungerar liknande Excels "Alla utom gränser"-funktionalitet för att klistra in cellintervall.

Följande exempelkod visar användningen av fältet PasteType.Default.

**C#**

{{< highlight "csharp" >}}

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

Från och med lanseringen av Aspose.Cells for .NET 8.4.2, uppförde uppräkningen PasteType.All sig annorlunda jämfört med Excels "Alla"-funktion för att klistra in cellintervall. Nu kopierar PasteType.All också kolumnbredderna till destinationsintervallet i motsats till Excels "Alla"-funktionalitet. För att efterlikna Excels "Alla" beteende, använd PasteType.Default.

{{% /alert %}}
