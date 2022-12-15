---
title: Öffentlich API Änderungen in Aspose.Cells 8.6.2
type: docs
weight: 210
url: /de/net/public-api-changes-in-aspose-cells-8-6-2/
---
{{% alert color="primary" %}} 

Dieses Dokument beschreibt die Änderungen an Aspose.Cells API von Version 8.6.1 zu 8.6.2, die für Modul-/Anwendungsentwickler von Interesse sein könnten. Es enthält nicht nur neue und aktualisierte öffentliche Methoden, hinzugefügte Klassen, sondern auch eine Beschreibung aller Änderungen im Verhalten hinter den Kulissen in Aspose.Cells.

{{% /alert %}} 
## **APIs hinzugefügt**
### **Unterstützung für Rückruf mit intelligenten Markierungen**
 Diese Version von Aspose.Cells for .NET API hat die WorkbookDesigner.CallBack-Eigenschaft und die ISmartMarkerCallBack-Schnittstelle bereitgestellt, die dies zusammen ermöglichen[Erhalten Sie die Benachrichtigungen über die verarbeitete Zellreferenz und/oder intelligente Markierung](/cells/de/net/getting-notifications-while-merging-data-with-smart-markers/). Der folgende Codeabschnitt veranschaulicht die Verwendung der ISmartMarkerCallBack-Schnittstelle zum Definieren einer neuen Klasse, die den Rückruf für die WorkbookDesigner.Process-Methode verarbeitet.

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



Der Rest des Prozesses umfasst das Laden der Designer-Tabelle mit den Smart Markers mit WorkbookDesigner und deren Verarbeitung durch Festlegen der Datenquelle. Um die Benachrichtigungen zu aktivieren, muss jedoch die WorkbookDesigner.CallBack-Eigenschaft festgelegt werden, bevor die WorkbookDesigner.Process-Methode wie unten gezeigt aufgerufen wird.

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


### **Methodendiagramm.ToPdf Hinzugefügt**
 Aspose.Cells for .NET 8.6.2 hat die Chart.ToPdf-Methode verfügbar gemacht, die verwendet werden kann[Rendern Sie die Diagrammform direkt in das PDF-Format](/cells/de/net/convert-an-excel-chart-to-image/). Das genannte Verfahren akzeptiert derzeit einen Parameter vom Typ Zeichenfolge als Dateipfad, um die resultierende Datei auf der Festplatte zu speichern.

Es folgt das einfache Nutzungsszenario.

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


### **Methode Workbook.RemoveUnusedStyles Hinzugefügt**
 Aspose.Cells for .NET 8.6.2 hat die Workbook.RemoveUnusedStyles-Methode bereitgestellt, die verwendet werden kann[Entfernen Sie alle nicht verwendeten Stilobjekte aus dem Stilpool](/cells/de/net/remove-unused-styles-inside-the-workbook/).

Es folgt das einfache Nutzungsszenario.

**C#**

{{< highlight "csharp" >}}

 //Load spreadsheet

Workbook workbook = new Workbook(inputFilePath);

//Remove all unused styles from the template

workbook.RemoveUnusedStyles();

{{< /highlight >}}


### **Eigenschaft Cells.Stil hinzugefügt**
Die Eigenschaft Cells.Style kann verwendet werden, um auf den Stil für das Arbeitsblatt zuzugreifen, das den Standardstil darstellt.

Es folgt das einfache Nutzungsszenario.

**C#**

{{< highlight "csharp" >}}

 //Load a spreadsheet

Workbook book = new Workbook(inputFilePath);

//Access the default style of worksheet

Style style = book.Worksheets[0].Cells.Style;

{{< /highlight >}}


### **Ereignisse für GridWeb hinzugefügt**
Aspose.Cells.GridWeb for .NET 8.6.2 hat die folgenden zwei neuen Ereignisse verfügbar gemacht.

1. AjaxCallFinished: Wird ausgelöst, wenn die AJAX-Aktualisierung des Steuerelements abgeschlossen ist. (EnableAJAX muss auf true gesetzt werden).
1. CellModifiedOnAjax: Wird ausgelöst, wenn die Zelle in einem AJAX-Aufruf geändert wird.
