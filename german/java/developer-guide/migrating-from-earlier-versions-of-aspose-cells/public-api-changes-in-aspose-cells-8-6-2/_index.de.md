---
title: Öffentlich API Änderungen in Aspose.Cells 8.6.2
type: docs
weight: 220
url: /de/java/public-api-changes-in-aspose-cells-8-6-2/
---
{{% alert color="primary" %}} 

Dieses Dokument beschreibt die Änderungen an Aspose.Cells API von Version 8.6.1 zu 8.6.2, die für Modul-/Anwendungsentwickler von Interesse sein könnten. Es enthält nicht nur neue und aktualisierte öffentliche Methoden, hinzugefügte Klassen, sondern auch eine Beschreibung aller Änderungen im Verhalten hinter den Kulissen in Aspose.Cells.

{{% /alert %}} 
## **APIs hinzugefügt**
### **Unterstützung für Rückruf mit intelligenten Markierungen**
Diese Version von Aspose.Cells for Java API hat das WorkbookDesigner.CallBack-Feld und die ISmartMarkerCallBack-Schnittstelle bereitgestellt, die dies zusammen ermöglichen[Erhalten Sie die Benachrichtigungen über die verarbeitete Zellreferenz und/oder intelligente Markierung](/cells/de/java/getting-notifications-while-merging-data-with-smart-markers/) . Der folgende Codeabschnitt demonstriert die Verwendung der ISmartMarkerCallBack-Schnittstelle zum Definieren einer neuen Klasse, die den Rückruf für die WorkbookDesigner.process-Methode verarbeitet.

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

Der Rest des Prozesses umfasst das Laden des Designer-Arbeitsblatts mit den Smart Markern mit WorkbookDesigner oder das Erstellen eines neuen Arbeitsblatts und das Verarbeiten durch Festlegen der Datenquelle. Um die Benachrichtigungen zu aktivieren, muss jedoch die WorkbookDesigner.CallBack-Eigenschaft festgelegt werden, bevor die WorkbookDesigner.process-Methode wie unten gezeigt aufgerufen wird.

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
### **Method Chart.toPdf hinzugefügt**
Aspose.Cells for Java 8.6.2 hat die Chart.toPdf-Methode verfügbar gemacht, die verwendet werden kann, um die Diagrammform direkt in das PDF-Format zu rendern. Die genannte Methode akzeptiert derzeit einen Parameter vom Typ String als Dateipfad, um die resultierende Datei auf der Festplatte zu speichern.

Es folgt das einfache Nutzungsszenario.

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
### **Methode Workbook.removeUnusedStyles hinzugefügt**
 Aspose.Cells for Java 8.6.2 hat die Workbook.removeUnusedStyles-Methode bereitgestellt, die verwendet werden kann[Entfernen Sie alle nicht verwendeten Stilobjekte aus dem Stilpool](/cells/de/java/remove-unused-styles-inside-the-workbook/). 

Es folgt das einfache Nutzungsszenario.

**Java**

{{< highlight "csharp" >}}

 //Load spreadsheet

Workbook workbook = new Workbook(inputFilePath);

//Remove all unused styles from the template

workbook.removeUnusedStyles();

{{< /highlight >}}
### **Eigenschaft Cells.Stil hinzugefügt**
Die Eigenschaft Cells.Style kann verwendet werden, um auf den Stil für das Arbeitsblatt zuzugreifen, das den Standardstil darstellt.

Es folgt das einfache Nutzungsszenario.

**Java**

{{< highlight "csharp" >}}

 //Load a spreadsheet

Workbook book = new Workbook(inputFilePath);

//Access the default style of worksheet

Style style = book.getWorksheets().get(0).getCells().getStyle();

{{< /highlight >}}
### **Ereignisse für GridWeb hinzugefügt**
Aspose.Cells.GridWeb for Java 8.6.2 hat die folgenden zwei neuen Ereignisse verfügbar gemacht.

1. AjaxCallFinished: Wird ausgelöst, wenn die AJAX-Aktualisierung des Steuerelements abgeschlossen ist. (EnableAJAX sollte auf true gesetzt sein).
1. CellModifiedOnAjax: Wird ausgelöst, wenn die Zelle in einem AJAX-Aufruf geändert wird.
