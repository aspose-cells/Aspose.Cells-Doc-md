---
title: Öffentliche API Änderungen in Aspose.Cells 8.6.2
type: docs
weight: 220
url: /de/java/public-api-changes-in-aspose-cells-8-6-2/
---

{{% alert color="primary" %}} 

Dieses Dokument beschreibt die Änderungen an der Aspose.Cells-API von Version 8.6.1 auf 8.6.2, die für Modul-/Anwendungsentwickler interessant sein können. Es enthält nicht nur neue und aktualisierte öffentliche Methoden, hinzugefügte Klassen, sondern auch eine Beschreibung etwaiger Änderungen im Verhalten hinter den Kulissen in Aspose.Cells.

{{% /alert %}} 
## **Hinzugefügte APIs**
### **Unterstützung für Rückruf mit Smart Markers**
Diese Version der Aspose.Cells for Java-API hat das WorkbookDesigner.CallBack-Feld und das ISmartMarkerCallBack-Interface freigelegt, das es zusammen ermöglicht, [Benachrichtigungen über die verarbeitete Zellreferenz und/oder den verarbeiteten Smart Marker zu erhalten](/cells/de/java/getting-notifications-while-merging-data-with-smart-markers/). Der folgende Codeausschnitt demonstriert die Verwendung des ISmartMarkerCallBack-Interfaces zum Definieren einer neuen Klasse, die den Rückruf für die WorkbookDesigner.process-Methode behandelt. 

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

Der restliche Prozess umfasst das Laden der Designer-Arbeitsmappe mit Smart Markers mit WorkbookDesigner oder das Erstellen einer solchen von Grund auf und deren Verarbeitung durch Festlegen der Datenquelle. Um jedoch die Benachrichtigungen zu aktivieren, ist es notwendig, die WorkbookDesigner.CallBack-Eigenschaft vor dem Aufruf der WorkbookDesigner.process-Methode wie unten demonstriert zu setzen.

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
### **Hinzugefügte Chart.toPdf-Methode**
Aspose.Cells for Java 8.6.2 hat die Chart.toPdf-Methode freigelegt, die verwendet werden kann, um die Chart-Form direkt in das PDF-Format zu rendern. Die genannte Methode akzeptiert derzeit einen Parameter vom Typ String als Dateipfad, um die resultierende Datei auf dem Datenträger zu speichern.

Im Folgenden wird das einfache Anwendungsszenario beschrieben.

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
### **Hinzugefügte Workbook.removeUnusedStyles-Methode**
Aspose.Cells for Java 8.6.2 hat die Workbook.removeUnusedStyles-Methode freigelegt, die verwendet werden kann, um [alle ungenutzten Style-Objekte aus dem Pool der Styles zu entfernen](/cells/de/java/remove-unused-styles-inside-the-workbook/). 

Im Folgenden wird das einfache Anwendungsszenario beschrieben.

**Java**

{{< highlight csharp >}}

 //Load spreadsheet

Workbook workbook = new Workbook(inputFilePath);

//Remove all unused styles from the template

workbook.removeUnusedStyles();

{{< /highlight >}}
### **Hinzugefügte Cells.Style-Eigenschaft**
Die Cells.Style-Eigenschaft kann verwendet werden, um auf den Stil für das Arbeitsblatt zuzugreifen, der den Standardstil darstellt.

Im Folgenden wird das einfache Anwendungsszenario beschrieben.

**Java**

{{< highlight csharp >}}

 //Load a spreadsheet

Workbook book = new Workbook(inputFilePath);

//Access the default style of worksheet

Style style = book.getWorksheets().get(0).getCells().getStyle();

{{< /highlight >}}
### **Hinzugefügte Ereignisse für GridWeb**
Aspose.Cells.GridWeb für Java 8.6.2 hat die folgenden beiden neuen Ereignisse freigegeben.

1. AjaxCallFinished: Wird ausgelöst, wenn das AJAX-Update der Steuerung abgeschlossen ist. (EnableAJAX sollte auf true gesetzt sein).
1. CellModifiedOnAjax: Wird ausgelöst, wenn die Zelle im AJAX-Aufruf geändert wird.
