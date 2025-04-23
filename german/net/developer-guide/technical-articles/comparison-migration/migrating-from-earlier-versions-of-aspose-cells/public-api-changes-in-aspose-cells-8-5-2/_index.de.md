---
title: Öffentliche API Änderungen in Aspose.Cells 8.5.2
type: docs
weight: 180
url: /de/net/public-api-changes-in-aspose-cells-8-5-2/
---

{{% alert color="primary" %}} 

Dieses Dokument beschreibt die Änderungen an der Aspose.Cells-API von Version 8.5.1 auf 8.5.2, die für Modul-/Anwendungs-Entwickler von Interesse sein könnten. Es enthält nicht nur neue und aktualisierte öffentliche Methoden, [hinzugefügte Klassen usw.](/cells/de/net/public-api-changes-in-aspose-cells-8-5-2/), sondern auch eine Beschreibung von Änderungen im Verhalten hinter den Kulissen in Aspose.Cells.

{{% /alert %}} 
## **Hinzugefügte APIs**
### **Arbeitsblatt in Grafikkontext rendern**
Mit dieser Version von Aspose.Cells for .NET API wurden zwei neue Überladungen der SheetRender.ToImage-Methode freigegeben, die jetzt eine Instanz der System.Drawing.Graphics-Klasse akzeptieren, um [im Grafikkontext zu rendern](/cells/de/net/render-worksheet-to-graphic-context/). Die Signaturen der neu hinzugefügten Methoden lauten wie folgt.

1. SheetRender.ToImage(int pageIndex, Graphics g, float x, float y)
1. SheetRender.ToImage(int pageIndex, Graphics g, float x, float y, float width, float height)

Im Folgenden wird das einfache Anwendungsszenario beschrieben.

**C#**

{{< highlight csharp >}}

 //Create workbook object from source file

Workbook workbook = new Workbook(filePath);

//Access first worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Create empty Bitmap

Bitmap bmp = new Bitmap(800, 800);

//Create Graphics Context

Graphics g = Graphics.FromImage(bmp);

g.Clear(Color.Blue);

//Set one page per sheet to true in image or print options

ImageOrPrintOptions opts = new ImageOrPrintOptions();

opts.OnePagePerSheet = true;

//Render worksheet to graphics context

SheetRender sr = new SheetRender(worksheet, opts);

sr.ToImage(0, g, 0, 0);

//Save the graphics context image in Png format

bmp.Save("test.png", ImageFormat.Png);

{{< /highlight >}}


### **Hinzugefügte PivotTable.GetCellByDisplayName-Methode**
Aspose.Cells for .NET 8.5.2 hat die PivotTable.GetCellByDisplayName-Methode freigegeben, die verwendet werden kann, um [das Zellenobjekt nach dem Namen des PivotField abzurufen](/cells/de/net/get-the-cell-object-by-displayname-of-pivotfield-of-pivottable/). Diese Methode könnte in Szenarien nützlich sein, in denen Sie das PivotField-Header hervorheben oder formatieren möchten.

Im Folgenden wird das einfache Anwendungsszenario beschrieben.

**C#**

{{< highlight csharp >}}

 //Create workbook object from source excel file

Workbook workbook = new Workbook(filePath);

//Access first worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Access first pivot table inside the worksheet

PivotTable pivotTable = worksheet.PivotTables[0];

//Access cell by display name of 2nd data field of the pivot table

Cell cell = pivotTable.GetCellByDisplayName(pivotTable.DataFields[1].DisplayName);

//Access cell style and set its fill color and font color

Style style = cell.GetStyle();

style.ForegroundColor = Color.LightBlue;

style.Font.Color = Color.Black;

//Set the style of the cell

pivotTable.Format(cell.Row, cell.Column, style);

//Save workbook

workbook.Save("output.xlsx");

{{< /highlight >}}


### **Hinzugefügte SaveOptions.MergeAreas-Eigenschaft**
Aspose.Cells for .NET 8.5.2 hat die SaveOptions.MergeAreas-Eigenschaft freigegeben, die einen Wert vom Typ Boolean akzeptieren kann. Der Standardwert ist false, jedoch versucht die Aspose.Cells for .NET-API, die einzelnen CellAreas vor dem Speichern der Datei zusammenzuführen, wenn sie auf true gesetzt ist.

{{% alert color="primary" %}} 

Wenn in einer Tabellenkalkulation zu viele einzelne Zellen mit angewendeter Validierung vorhanden sind, besteht die Gefahr, dass die resultierende Tabellenkalkulation beschädigt wird. Eine mögliche Lösung ist, die Zellen mit identischen Validierungsregeln zusammenzuführen, oder Sie können jetzt die SaveOptions.MergeAreas-Eigenschaft verwenden, um die API anzuweisen, die CellAreas automatisch vor dem Speichervorgang zusammenzuführen.

{{% /alert %}} 
### **Hinzugefügte Shape.Geometry.ShapeAdjustValues-Eigenschaft**
Mit der Veröffentlichung von v8.5.2 hat die Aspose.Cells-API die Shape.Geometry.ShapeAdjustValues-Eigenschaft freigegeben, die verwendet werden kann, um [Änderungen an den Anpassungspunkten verschiedener Formen vorzunehmen](/cells/de/net/change-adjustment-values-of-the-shape/).

{{% alert color="primary" %}} 

Im Microsoft Excel-Interface werden die Anpassungspunkte als gelbe Diamantknoten angezeigt.

{{% /alert %}} 

Zum Beispiel

1. Das abgerundete Rechteck hat eine Anpassung, um den Bogen zu ändern
1. Das Dreieck hat eine Anpassung, um die Position des Punkts zu ändern
1. Das Trapezoid hat eine Anpassung, um die Breite des oberen Teils zu ändern
1. Pfeile haben zwei Anpassungen, um die Form des Kopfes und des Endes zu ändern

Hier ist das einfachste Anwendungsszenario.

**C#**

{{< highlight csharp >}}

 //Create workbook object from source excel file

Workbook workbook = new Workbook(filePath);

//Access first worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Access first three shapes of the worksheet

Shape shape1 = worksheet.Shapes[0];

Shape shape2 = worksheet.Shapes[1];

Shape shape3 = worksheet.Shapes[2];

//Change the adjustment values of the shapes

shape1.Geometry.ShapeAdjustValues[0].Value = 0.5d;

shape2.Geometry.ShapeAdjustValues[0].Value = 0.8d;

shape3.Geometry.ShapeAdjustValues[0].Value = 0.5d;

//Save the workbook

workbook.Save("output.xls);

{{< /highlight >}}


### **Aufzählungsfeld ConsolidationFunction.DistinctCount hinzugefügt**
Aspose.Cells for .NET 8.5.2 hat das Feld ConsolidationFunction.DistinctCount freigegeben, das verwendet werden kann, um [die Distinct Count-Konsolidierungsfunktion](/cells/de/net/consolidation-function/) auf DataField eines PivotTable anzuwenden.

{{% alert color="primary" %}} 

Die Konsolidierungsfunktion Distinct Count wird nur von Microsoft Excel 2013 unterstützt.

{{% /alert %}} 
### **Besseres Event-Handling für GridDesktop**
Diese Version von Aspose.Cells.GridDesktop hat 4 neue Ereignisse freigegeben. 2 dieser Ereignisse werden bei verschiedenen Zuständen des Ladens von Tabellenkalkulationsdateien in GridDesktop ausgelöst, während die anderen 2 bei der Berechnung von Formeln ausgelöst werden.

Die Ereignisse werden wie folgt aufgelistet.

1. GridDesktop.BeforeLoadFile
1. GridDesktop.FinishLoadFile
1. GridDesktop.BeforeCalculate
1. GridDesktop.FinishCalculate
{{< app/cells/assistant language="csharp" >}}
