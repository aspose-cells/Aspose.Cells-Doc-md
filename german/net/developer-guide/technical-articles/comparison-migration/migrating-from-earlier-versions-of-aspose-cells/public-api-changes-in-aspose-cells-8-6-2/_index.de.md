---
title: Öffentliche API Änderungen in Aspose.Cells 8.6.2
type: docs
weight: 210
url: /de/net/public-api-changes-in-aspose-cells-8-6-2/
---

{{% alert color="primary" %}} 

Dieses Dokument beschreibt die Änderungen an der Aspose.Cells-API von Version 8.6.1 auf 8.6.2, die für Modul-/Anwendungsentwickler interessant sein können. Es enthält nicht nur neue und aktualisierte öffentliche Methoden, hinzugefügte Klassen, sondern auch eine Beschreibung etwaiger Änderungen im Verhalten hinter den Kulissen in Aspose.Cells.

{{% /alert %}} 
## **Hinzugefügte APIs**
### **Unterstützung für Rückruf mit Smart Markers**
Diese Version der Aspose.Cells for .NET-API hat das WorkbookDesigner.CallBack-Eigenschaft und das ISmartMarkerCallBack-Interface freigelegt, die es zusammen ermöglichen,[Benachrichtigungen über die Zellreferenz und/oder den gerade verarbeiteten Smart Marker zu erhalten](/cells/de/netz/erhalten-von-benachrichtigungen-beim-zusammenführen-von-daten-mit-smart-markern/). Der folgende Codeausschnitt zeigt die Verwendung des ISmartMarkerCallBack-Interfaces zur Definition einer neuen Klasse, die den Rückruf für die WorkbookDesigner.Process-Methode behandelt.

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



Der Rest des Prozesses umfasst das Laden der Designer-Arbeitsmappe mit Smart Markers mit WorkbookDesigner und die Verarbeitung durch Festlegung der Datenquelle. Um jedoch die Benachrichtigungen zu aktivieren, ist es erforderlich, das WorkbookDesigner.CallBack-Eigenschaft zu setzen, bevor die WorkbookDesigner.Process-Methode aufgerufen wird, wie im Folgenden dargestellt.

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


### **Hinzugefügte Chart.ToPdf-Methode**
Aspose.Cells for .NET 8.6.2 hat die Chart.ToPdf-Methode freigelegt, die verwendet werden kann, um [die Chart-Form direkt in das PDF-Format zu rendern](/cells/de/netz/umwandeln-eines-excel-diagramms-in-ein-bild/). Die genannte Methode akzeptiert derzeit einen Parameter des Typs string als Dateipfad zum Speichern der resultierenden Datei auf der Festplatte.

Im Folgenden wird das einfache Anwendungsszenario beschrieben.

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


### **Hinzugefügte Workbook.RemoveUnusedStyles-Methode**
Aspose.Cells for .NET 8.6.2 hat die Workbook.RemoveUnusedStyles-Methode freigelegt, die verwendet werden kann, um [alle unbenutzten Style-Objekte aus dem Pool von Styles zu entfernen](/cells/de/netz/unbenutzte-styles-in-der-arbeitsmappe-entfernen/).

Im Folgenden wird das einfache Anwendungsszenario beschrieben.

**C#**

{{< highlight csharp >}}

 //Load spreadsheet

Workbook workbook = new Workbook(inputFilePath);

//Remove all unused styles from the template

workbook.RemoveUnusedStyles();

{{< /highlight >}}


### **Hinzugefügte Cells.Style-Eigenschaft**
Die Cells.Style-Eigenschaft kann verwendet werden, um auf den Stil für das Arbeitsblatt zuzugreifen, der den Standardstil darstellt.

Im Folgenden wird das einfache Anwendungsszenario beschrieben.

**C#**

{{< highlight csharp >}}

 //Load a spreadsheet

Workbook book = new Workbook(inputFilePath);

//Access the default style of worksheet

Style style = book.Worksheets[0].Cells.Style;

{{< /highlight >}}


### **Hinzugefügte Ereignisse für GridWeb**
Aspose.Cells.GridWeb für .NET 8.6.2 hat die folgenden zwei neuen Ereignisse freigelegt.

1. AjaxCallFinished: Wird ausgelöst, wenn das AJAX-Update des Steuerelements abgeschlossen ist. (EnableAJAX muss auf true gesetzt sein).
1. CellModifiedOnAjax: Wird ausgelöst, wenn die Zelle im AJAX-Aufruf geändert wird.
{{< app/cells/assistant language="csharp" >}}
