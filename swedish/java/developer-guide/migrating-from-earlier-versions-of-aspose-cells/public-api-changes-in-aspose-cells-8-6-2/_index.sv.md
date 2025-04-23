---
title: Offentliga API ändringar i Aspose.Cells 8.6.2
type: docs
weight: 220
url: /sv/java/public-api-changes-in-aspose-cells-8-6-2/
---

{{% alert color="primary" %}} 

Detta dokument beskriver ändringarna i Aspose.Cells API från version 8.6.1 till 8.6.2 som kan vara av intresse för modul-/applikationsutvecklare. Det inkluderar inte bara nya och uppdaterade publika metoder, tillagda klasser, utan också en beskrivning av eventuella förändringar i beteendet bakom kulisserna i Aspose.Cells.

{{% /alert %}} 
## **Tillagda API:er**
### **Stöd för återanrop med Smart Markers**
Denna utgåva av Aspose.Cells for Java API har exponerat WorkbookDesigner.CallBack-fältet och ISmartMarkerCallBack-gränssnittet som tillsammans tillåter att [få aviseringar om cellreferensen och/eller smarta markörer som bearbetas](/cells/sv/java/getting-notifications-while-merging-data-with-smart-markers/). Följande kodstycke visar användningen av ISmartMarkerCallBack-gränssnittet för att definiera en ny klass som hanterar återanropet för WorkbookDesigner.process-metoden. 

**Java**

{{< highlight csharp >}}

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

Resten av processen innebär att ladda designark med Smart Markers med WorkbookDesigner eller skapa en från början och bearbeta den genom att ställa in datakällan. Dock måste WorkbookDesigner.CallBack-egenskapen ställas in innan WorkbookDesigner.process-metoden anropas för att aktivera aviseringarna, vilket visas nedan.

**Java**

{{< highlight csharp >}}

 //Instantiate a new Workbook designer

WorkbookDesigner report = new WorkbookDesigner();

//Get the first worksheet of the workbook

Worksheet sheet = report.getWorkbook().getWorksheets().get(0);

//Set the Variable Array marker to a cell

//You may also place this Smart Marker into a template file manually using Excel and then open this file via WorkbookDesigner 

sheet.getCells().get("A1").putValue("&=$VariableArray");

//Set the data source for the marker(s)

report.setDataSource("VariableArray", new String[] { "English", "Arabic", "Hindi", "Urdu", "French" });

//Set the CallBack property

report.setCallBack(new SmartMarkerCallBack(report.getWorkbook()));

//Process the markers

report.process(false);

{{< /highlight >}}
### **Lade till Chart.toPdf-metoden**
Aspose.Cells for Java 8.6.2 har exponerat Chart.toPdf-metoden som kan användas för att direkt rendera Chart-figurer till PDF-format. Denna metod accepterar för närvarande en parameter av typen String som filväg till platsen där den resulterande filen ska sparas på disken.

Följande är det enkla användningscenariot.

**Java**

{{< highlight csharp >}}

 //Load spreadsheet containing charts

Workbook workbook = new Workbook(inputFilePath);

//Access first worksheet

Worksheet worksheet = workbook.getWorksheets().get(0);

//Access first chart inside the worksheet

Chart chart = worksheet.getCharts().get(0);

//Save the chart in PDF format

chart.toPdf(outputFilePath);

{{< /highlight >}}
### **Lade till Workbook.removeUnusedStyles-metoden**
Aspose.Cells for Java 8.6.2 har exponerat Workbook.removeUnusedStyles-metoden som kan användas för att [ta bort alla oanvända Style-objekt från stilpoolen](/cells/sv/java/remove-unused-styles-inside-the-workbook/). 

Följande är det enkla användningscenariot.

**Java**

{{< highlight csharp >}}

 //Load spreadsheet

Workbook workbook = new Workbook(inputFilePath);

//Remove all unused styles from the template

workbook.removeUnusedStyles();

{{< /highlight >}}
### **Lade till Cells.Style-egenskapen**
Cells.Style-egenskapen kan användas för att komma åt stilen för Worksheet som representerar standardstilen.

Följande är det enkla användningscenariot.

**Java**

{{< highlight csharp >}}

 //Load a spreadsheet

Workbook book = new Workbook(inputFilePath);

//Access the default style of worksheet

Style style = book.getWorksheets().get(0).getCells().getStyle();

{{< /highlight >}}
### **Händelser tillagda för GridWeb**
Aspose.Cells.GridWeb för Java 8.6.2 har exponerat följande två nya händelser.

1. AjaxCallFinished: Anropas när AJAX-uppdateringen av kontrollen är klar. (EnableAJAX ska vara satt till true).
1. CellModifiedOnAjax: Anropas när cellen ändras i AJAX-anrop.
{{< app/cells/assistant language="java" >}}
