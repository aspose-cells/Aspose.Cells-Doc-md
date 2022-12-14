---
title: Offentliga API-ändringar i Aspose.Cells 8.6.2
type: docs
weight: 220
url: /sv/java/public-api-changes-in-aspose-cells-8-6-2/
---
{{% alert color="primary" %}} 

Det här dokumentet beskriver ändringarna av Aspose.Cells API från version 8.6.1 till 8.6.2 som kan vara av intresse för modul-/applikationsutvecklare. Den innehåller inte bara nya och uppdaterade offentliga metoder, tillagda klasser, utan också en beskrivning av eventuella förändringar i beteendet bakom kulisserna i Aspose.Cells.

{{% /alert %}} 
## **Lade till API:er**
### **Stöd för återuppringning med smarta markörer**
Den här versionen av Aspose.Cells för Java API har exponerat WorkbookDesigner.CallBack-fältet och ISmartMarkerCallBack-gränssnittet som tillsammans gör det möjligt att[få meddelanden om cellreferens och/eller smartmarkör som bearbetas](/cells/sv/java/getting-notifications-while-merging-data-with-smart-markers/) . Följande kodbit demonstrerar användningen av ISmartMarkerCallBack-gränssnittet för att definiera en ny klass som hanterar call back for WorkbookDesigner.process-metoden.

**Java**

{{< highlight "csharp" >}}

 public class SmartMarkerCallBack implements ISmartMarkerCallBack 

{

	Workbook workbook;

	SmartMarkerCallBack(Workbook workbook)

	{

	    this.workbook = workbook;

	}



	@Override

	public void process(int sheetIndex, int rowIndex, int colIndex, String tableName, String columnName)

	{

	    System.out.println("Processing Cell : " + workbook.getWorksheets().get(sheetIndex).getName() + "!" + CellsHelper.cellIndexToName(rowIndex, colIndex));

	    System.out.println("Processing Marker : " + tableName + "." + columnName);

	}

}

{{< /highlight >}}

Resten av processen inkluderar att ladda designerkalkylarket som innehåller de smarta markörerna med WorkbookDesigner eller skapa ett från början och bearbeta det genom att ställa in datakällan. Men för att aktivera aviseringarna är det nödvändigt att ställa in egenskapen WorkbookDesigner.CallBack innan du anropar metoden WorkbookDesigner.process som visas nedan.

**Java**

{{< highlight "csharp" >}}

 //Instantiate a new Workbook designer

WorkbookDesigner report = new WorkbookDesigner();

//Get the first worksheet of the workbook

Worksheet sheet = report.getWorkbook().getWorksheets().get(0);

//Set the Variable Array marker to a cell

//You may also place this Smart Marker into a template file manually using Excel and then open this file via WorkbookDesigner 

sheet.getCells().get("A1").putValue("&=$VariableArray");

//Set the data source for the marker(s)

report.setDataSource("VariableArray", new String[]{ "English", "Arabic", "Hindi", "Urdu", "French" });

//Set the CallBack property

report.setCallBack(new SmartMarkerCallBack(report.getWorkbook()));

//Process the markers

report.process(false);

{{< /highlight >}}
### **Method Chart.toPdf tillagd**
Aspose.Cells för Java 8.6.2 har exponerat metoden Chart.toPdf som kan användas för att direkt rendera diagramformen till PDF-format. Nämnda metod accepterar för närvarande en parameter av typen String som filsökvägsplats för att lagra den resulterande filen på disken.

Följande är det enkla användningsscenariot.

**Java**

{{< highlight "csharp" >}}

 //Load spreadsheet containing charts

Workbook workbook = new Workbook(inputFilePath);

//Access first worksheet

Worksheet worksheet = workbook.getWorksheets().get(0);

//Access first chart inside the worksheet

Chart chart = worksheet.getCharts().get(0);

//Save the chart in PDF format

chart.toPdf(outputFilePath);

{{< /highlight >}}
### **Method Workbook.removeUnusedStyles tillagd**
 Aspose.Cells för Java 8.6.2 har avslöjat metoden Workbook.removeUnusedStyles som kan användas för att[ta bort alla oanvända Style-objekt från poolen av stilar](/cells/sv/java/remove-unused-styles-inside-the-workbook/). 

Följande är det enkla användningsscenariot.

**Java**

{{< highlight "csharp" >}}

 //Load spreadsheet

Workbook workbook = new Workbook(inputFilePath);

//Remove all unused styles from the template

workbook.removeUnusedStyles();

{{< /highlight >}}
### **Fastighet Cells.Stil tillagt**
Egenskapen Cells.Style kan användas för att komma åt stilen för arbetsbladet som representerar standardstilen.

Följande är det enkla användningsscenariot.

**Java**

{{< highlight "csharp" >}}

 //Load a spreadsheet

Workbook book = new Workbook(inputFilePath);

//Access the default style of worksheet

Style style = book.getWorksheets().get(0).getCells().getStyle();

{{< /highlight >}}
### **Händelser tillagda för GridWeb**
Aspose.Cells.GridWeb för Java 8.6.2 har avslöjat följande två nya händelser.

1. AjaxCallFinished: Avfyras när AJAX-uppdateringen av kontrollen är klar. (EnableAJAX ska vara satt till true).
1. CellModifiedOnAjax: Avfyras när cellen modifieras i AJAX-anrop.
