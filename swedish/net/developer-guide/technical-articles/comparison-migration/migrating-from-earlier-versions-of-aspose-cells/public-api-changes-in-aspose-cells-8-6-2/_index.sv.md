---
title: Offentlig API Ändringar i Aspose.Cells 8.6.2
type: docs
weight: 210
url: /sv/net/public-api-changes-in-aspose-cells-8-6-2/
---
{{% alert color="primary" %}} 

Det här dokumentet beskriver ändringarna av Aspose.Cells API från version 8.6.1 till 8.6.2 som kan vara av intresse för modul-/applikationsutvecklare. Den innehåller inte bara nya och uppdaterade offentliga metoder, tillagda klasser, utan också en beskrivning av eventuella förändringar i beteendet bakom kulisserna i Aspose.Cells.

{{% /alert %}} 
## **Lade till API:er**
### **Stöd för återuppringning med smarta markörer**
 Den här versionen av Aspose.Cells for .NET API har avslöjat egenskapen WorkbookDesigner.CallBack och ISmartMarkerCallBack-gränssnittet som tillsammans tillåter[få meddelanden om cellreferens och/eller smartmarkör som bearbetas](/cells/sv/net/getting-notifications-while-merging-data-with-smart-markers/). Följande kodbit demonstrerar användningen av ISmartMarkerCallBack-gränssnittet för att definiera en ny klass som hanterar call back för WorkbookDesigner.Process-metoden.

**C#**

{{< highlight "csharp" >}}

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



Resten av processen inkluderar att ladda designerkalkylarket som innehåller de smarta markörerna med WorkbookDesigner och bearbeta det genom att ställa in datakällan. För att aktivera aviseringarna är det dock nödvändigt att ställa in egenskapen WorkbookDesigner.CallBack innan du anropar metoden WorkbookDesigner.Process som visas nedan.

**C#**

{{< highlight "csharp" >}}

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


### **Metoddiagram.ToPdf tillagd**
 Aspose.Cells for .NET 8.6.2 har exponerat metoden Chart.ToPdf som kan användas för att[rendera diagramformen direkt till PDF-format](/cells/sv/net/convert-an-excel-chart-to-image/). Nämnda metod accepterar för närvarande en parameter av typen sträng som filsökvägsplats för att lagra den resulterande filen på disken.

Följande är det enkla användningsscenariot.

**C#**

{{< highlight "csharp" >}}

 //Load spreadsheet containing charts

Workbook workbook = new Workbook(inputFilePath);

//Access first worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Access first chart inside the worksheet

Chart chart = worksheet.Charts[0];

//Save the chart in PDF format

chart.ToPdf(outputFilePath);

{{< /highlight >}}


### **Metod Workbook.RemoveUnusedStyles tillagd**
 Aspose.Cells for .NET 8.6.2 har exponerat metoden Workbook.RemoveUnusedStyles som kan användas för att[ta bort alla oanvända Style-objekt från poolen av stilar](/cells/sv/net/remove-unused-styles-inside-the-workbook/).

Följande är det enkla användningsscenariot.

**C#**

{{< highlight "csharp" >}}

 //Load spreadsheet

Workbook workbook = new Workbook(inputFilePath);

//Remove all unused styles from the template

workbook.RemoveUnusedStyles();

{{< /highlight >}}


### **Fastighet Cells.Stil tillagt**
Egenskapen Cells.Style kan användas för att komma åt stilen för arbetsbladet som representerar standardstilen.

Följande är det enkla användningsscenariot.

**C#**

{{< highlight "csharp" >}}

 //Load a spreadsheet

Workbook book = new Workbook(inputFilePath);

//Access the default style of worksheet

Style style = book.Worksheets[0].Cells.Style;

{{< /highlight >}}


### **Händelser tillagda för GridWeb**
Aspose.Cells.GridWeb for .NET 8.6.2 har avslöjat följande två nya händelser.

1. AjaxCallFinished: Avfyras när AJAX-uppdateringen av kontrollen är klar. (EnableAJAX ska ställas in på sant).
1. CellModifiedOnAjax: Avfyras när cellen modifieras i AJAX-anrop.
