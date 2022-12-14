---
title: Öffentlich API Änderungen in Aspose.Cells 8.5.2
type: docs
weight: 180
url: /de/net/public-api-changes-in-aspose-cells-8-5-2/
---
{{% alert color="primary" %}} 

 Dieses Dokument beschreibt die Änderungen an Aspose.Cells API von Version 8.5.1 zu 8.5.2, die für Modul-/Anwendungsentwickler von Interesse sein könnten. Es enthält nicht nur neue und aktualisierte öffentliche Methoden,[zusätzliche Klassen usw.](/cells/de/net/public-api-changes-in-aspose-cells-8-5-2/), sondern auch eine Beschreibung etwaiger Verhaltensänderungen hinter den Kulissen in Aspose.Cells.

{{% /alert %}} 
## **APIs hinzugefügt**
### **Rendern Sie das Arbeitsblatt in den grafischen Kontext**
 Diese Version von Aspose.Cells for .NET API hat zwei neue Überladungen der SheetRender.ToImage-Methode verfügbar gemacht, die es jetzt ermöglichen, eine Instanz der System.Drawing.Graphics-Klasse zu akzeptieren[Rendern im Grafikkontext](/cells/de/net/render-worksheet-to-graphic-context/). Die Signaturen neu hinzugefügter Methoden lauten wie folgt.

1. SheetRender.ToImage(int pageIndex, Graphics g, float x, float y)
1. SheetRender.ToImage(int pageIndex, Graphics g, float x, float y, float width, float height)

Es folgt das einfache Nutzungsszenario.

**C#**

{{< highlight "csharp" >}}

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


### **Methode PivotTable.GetCellByDisplayName hinzugefügt**
 Aspose.Cells for .NET 8.5.2 hat die PivotTable.GetCellByDisplayName-Methode verfügbar gemacht, die verwendet werden kann[Rufen Sie das Objekt Cell nach dem Namen des PivotField ab](/cells/de/net/get-the-cell-object-by-displayname-of-pivotfield-of-pivottable/). Diese Methode kann in Szenarien nützlich sein, in denen Sie den PivotField-Header hervorheben oder formatieren möchten.

Es folgt das einfache Nutzungsszenario.

**C#**

{{< highlight "csharp" >}}

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


### **Eigenschaft SaveOptions.MergeAreas hinzugefügt**
Aspose.Cells for .NET 8.5.2 hat die Eigenschaft SaveOptions.MergeAreas verfügbar gemacht, die Werte vom Typ Boolean akzeptieren kann. Der Standardwert ist "false". Wenn er jedoch auf "true" gesetzt ist, versucht Aspose.Cells for .NET API, die einzelne CellArea zusammenzuführen, bevor die Datei gespeichert wird.

{{% alert color="primary" %}} 

Wenn eine Tabelle zu viele einzelne Zellen mit angewendeter Validierung enthält, besteht die Möglichkeit, dass die resultierende Tabelle beschädigt wird. Eine mögliche Lösung besteht darin, die Zellen mit identischen Validierungsregeln zusammenzuführen, oder Sie können jetzt die Eigenschaft SaveOptions.MergeAreas verwenden, um API anzuweisen, die CellAreas vor dem Speichervorgang automatisch zusammenzuführen.

{{% /alert %}} 
### **Eigenschaft Shape.Geometry.ShapeAdjustValues Hinzugefügt**
 Mit der Veröffentlichung von v8.5.2 hat Aspose.Cells API die Shape.Geometry.ShapeAdjustValues-Eigenschaft verfügbar gemacht, die verwendet werden kann[Nehmen Sie Änderungen an den Anpassungspunkten verschiedener Formen vor](/cells/de/net/change-adjustment-values-of-the-shape/).

{{% alert color="primary" %}} 

In der Excel-Oberfläche Microsoft werden die Anpassungspunkte als gelbe Rautenknoten angezeigt.

{{% /alert %}} 

Zum Beispiel,

1. Abgerundetes Rechteck hat eine Anpassung, um den Bogen zu ändern
1. Dreieck hat eine Anpassung, um die Position des Punktes zu ändern
1. Trapez hat eine Anpassung, um die Breite der Oberseite zu ändern
1. Pfeile haben zwei Anpassungen, um die Form des Kopfes und des Schwanzes zu ändern

Hier ist das einfachste Anwendungsszenario.

**C#**

{{< highlight "csharp" >}}

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


### **Aufzählungsfeld ConsolidationFunction.DistinctCount Hinzugefügt**
 Aspose.Cells for .NET 8.5.2 hat das ConsolidationFunction.DistinctCount-Feld bereitgestellt, das verwendet werden kann[Wenden Sie die Distinct Count-Konsolidierungsfunktion an](/cells/de/net/consolidation-function/) auf DataField einer PivotTable.

{{% alert color="primary" %}} 

Die Distinct Count-Konsolidierungsfunktion wird nur von Microsoft Excel 2013 unterstützt.

{{% /alert %}} 
### **Bessere Ereignisbehandlung für GridDesktop**
Diese Version von Aspose.Cells.GridDesktop hat 4 neue Ereignisse offengelegt. 2 dieser Ereignisse werden bei unterschiedlichen Zuständen beim Laden von Tabellenkalkulationsdateien in GridDesktop ausgelöst, während die anderen 2 bei der Berechnung von Formeln ausgelöst werden.

Die Ereignisse sind wie folgt aufgelistet.

1. GridDesktop.BeforeLoadFile
1. GridDesktop.FinishLoadFile
1. GridDesktop.BeforeCalculate
1. GridDesktop.FinishCalculate
