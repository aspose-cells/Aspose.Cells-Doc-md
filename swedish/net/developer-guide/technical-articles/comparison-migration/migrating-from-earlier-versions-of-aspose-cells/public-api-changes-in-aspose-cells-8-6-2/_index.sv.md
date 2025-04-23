---
title: Offentliga API ändringar i Aspose.Cells 8.6.2
type: docs
weight: 210
url: /sv/net/public-api-changes-in-aspose-cells-8-6-2/
---

{{% alert color="primary" %}} 

Detta dokument beskriver ändringarna i Aspose.Cells API från version 8.6.1 till 8.6.2 som kan vara av intresse för modul-/applikationsutvecklare. Det inkluderar inte bara nya och uppdaterade publika metoder, tillagda klasser, utan också en beskrivning av eventuella förändringar i beteendet bakom kulisserna i Aspose.Cells.

{{% /alert %}} 
## **Tillagda API:er**
### **Stöd för återanrop med Smart Markers**
Denna release av Aspose.Cells for .NET API har exponerat WorkbookDesigner.CallBack-egenskapen och ISmartMarkerCallBack-gränssnittet som tillsammans möjliggör att [få meddelanden om cellreferensen och/eller smart markern som behandlas](/cells/sv/net/getting-notifications-while-merging-data-with-smart-markers/). Följande kodexempel demonstrerar användningen av ISmartMarkerCallBack-gränssnittet för att definiera en ny klass som hanterar återuppringning för WorkbookDesigner.Process-metoden.

**C#**

{{< highlight csharp >}}

 class SmartMarkerCallBack : ISmartMarkerCallBack

{

    Workbook workbook;

    internal SmartMarkerCallBack(Workbook workbook)

    {

        this.workbook = workbook;

    }

    public void Process(int sheetIndex, int rowIndex, int colIndex, string tableName, string columnName)

    {

        Console.WriteLine("Processing Cell : " + workbook.Worksheets[sheetIndex].Name + "!" + CellsHelper.CellIndexToName(rowIndex, colIndex));

        Console.WriteLine("Processing Marker : " + tableName + "." + columnName);

    }

}

{{< /highlight >}}



Resten av processen inkluderar att ladda kalkylbladet med Smart Markers med WorkbookDesigner och behandla det genom att ställa in datakällan. Men för att aktivera meddelandena är det nödvändigt att ställa in WorkbookDesigner.CallBack-egenskapen innan du anropar WorkbookDesigner.Process-metoden, enligt nedanvisad demonstration.

**C#**

{{< highlight csharp >}}

 //Loading the designer spreadsheet in an instance of Workbook

Workbook workbook = new Workbook(inputFilePath);

//Loading the instance of Workbook in an instance of WorkbookDesigner

WorkbookDesigner designer = new WorkbookDesigner(workbook);

//Set the WorkbookDesigner.CallBack property to an instance of newly created class

designer.CallBack = new SmartMarkerCallBack(workbook);

//Set the data source 

designer.SetDataSource(table);

//Process the Smart Markers in the designer spreadsheet

designer.Process(false);

{{< /highlight >}}


### **Tillagd Chart.ToPdf-metod**
Aspose.Cells for .NET 8.6.2 har exponerat Chart.ToPdf-metoden som kan användas för [att direktrendera Diagram-formen till PDF-format](/cells/sv/net/convert-an-excel-chart-to-image/). Den angivna metoden accepterar för närvarande en parameter av typen sträng som filväg för att lagra den resulterande filen på disken.

Följande är det enkla användningscenariot.

**C#**

{{< highlight csharp >}}

 //Load spreadsheet containing charts

Workbook workbook = new Workbook(inputFilePath);

//Access first worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Access first chart inside the worksheet

Chart chart = worksheet.Charts[0];

//Save the chart in PDF format

chart.ToPdf(outputFilePath);

{{< /highlight >}}


### **Tillagd Workbook.RemoveUnusedStyles-metod**
Aspose.Cells for .NET 8.6.2 har exponerat Workbook.RemoveUnusedStyles-metoden som kan användas för [att ta bort alla oanvända stilobjekt från stilsamlingen](/cells/sv/net/remove-unused-styles-inside-the-workbook/).

Följande är det enkla användningscenariot.

**C#**

{{< highlight csharp >}}

 //Load spreadsheet

Workbook workbook = new Workbook(inputFilePath);

//Remove all unused styles from the template

workbook.RemoveUnusedStyles();

{{< /highlight >}}


### **Lade till Cells.Style-egenskapen**
Cells.Style-egenskapen kan användas för att komma åt stilen för Worksheet som representerar standardstilen.

Följande är det enkla användningscenariot.

**C#**

{{< highlight csharp >}}

 //Load a spreadsheet

Workbook book = new Workbook(inputFilePath);

//Access the default style of worksheet

Style style = book.Worksheets[0].Cells.Style;

{{< /highlight >}}


### **Händelser tillagda för GridWeb**
Aspose.Cells.GridWeb för .NET 8.6.2 har exponerat följande två nya händelser.

1. AjaxCallFinished: Utsänds när AJAX-uppdateringen av kontrollen är färdig. (EnableAJAX ska vara satt till true).
1. CellModifiedOnAjax: Anropas när cellen ändras i AJAX-anrop.
{{< app/cells/assistant language="csharp" >}}
