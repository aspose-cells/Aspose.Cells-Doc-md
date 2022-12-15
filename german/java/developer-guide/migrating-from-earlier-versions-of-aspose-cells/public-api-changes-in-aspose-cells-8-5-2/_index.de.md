---
title: Öffentlich API Änderungen in Aspose.Cells 8.5.2
type: docs
weight: 190
url: /de/java/public-api-changes-in-aspose-cells-8-5-2/
---
{{% alert color="primary" %}} 

 Dieses Dokument beschreibt die Änderungen an Aspose.Cells API von Version 8.5.1 zu 8.5.2, die für Modul-/Anwendungsentwickler von Interesse sein könnten. Es enthält nicht nur neue und aktualisierte öffentliche Methoden,[zusätzliche Klassen usw.](/cells/de/java/public-api-changes-in-aspose-cells-8-5-2/), sondern auch eine Beschreibung etwaiger Verhaltensänderungen hinter den Kulissen in Aspose.Cells.

{{% /alert %}} 
## **APIs hinzugefügt**
### **Rendern Sie das Arbeitsblatt in den grafischen Kontext**
Diese Version von Aspose.Cells for Java API hat eine weitere Überladung der SheetRender.toImage-Methode verfügbar gemacht, die es jetzt ermöglicht, eine Instanz der Graphics2D-Klasse zu akzeptieren[Rendern Sie das Arbeitsblatt im Grafikkontext](/cells/de/java/render-worksheet-to-graphic-context/). Die Signaturen der neu hinzugefügten Methode sind wie folgt.

- SheetRender.toImage(int pageIndex, Graphics2D-Grafik)

Es folgt das einfache Nutzungsszenario.

**Java**

{{< highlight "csharp" >}}

 //Create workbook object from source file

Workbook workbook = new Workbook("source.xlsx");

//Access first worksheet

Worksheet worksheet = workbook.getWorksheets().get(0);

//Create empty image and fill it with blue color

int width = 800;

int height = 800;

BufferedImage image = new BufferedImage(width, height, BufferedImage.TYPE_INT_ARGB);

Graphics2D g = image.createGraphics();

g.setColor(java.awt.Color.blue);

g.fillRect(0, 0, width, height);

//Set one page per sheet to true in image or print options

ImageOrPrintOptions opts = new ImageOrPrintOptions();

opts.setOnePagePerSheet(true);

//Render worksheet to graphics context

SheetRender sr = new SheetRender(worksheet, opts);

sr.toImage(0, g);

//Save the graphics context image in Png format

File outputfile = new File("test.png");

ImageIO.write(image, "png", outputfile);

{{< /highlight >}}
### **Methode PivotTable.getCellByDisplayName hinzugefügt**
 Aspose.Cells for Java 8.5.2 hat die PivotTable.getCellByDisplayName-Methode verfügbar gemacht, die verwendet werden kann[Rufen Sie das Objekt Cell nach dem Namen des PivotField ab](/cells/de/java/get-the-cell-object-by-displayname-of-pivotfield-of-pivottable/). Diese Methode kann in Szenarien nützlich sein, in denen Sie den PivotField-Header hervorheben oder formatieren möchten.

Es folgt das einfache Nutzungsszenario.

**Java**

{{< highlight "csharp" >}}

 //Create workbook object from source excel file

Workbook workbook = new Workbook("source.xlsx");

//Access first worksheet

Worksheet worksheet = workbook.getWorksheets().get(0);

//Access first pivot table inside the worksheet

PivotTable pivotTable = worksheet.getPivotTables().get(0);

//Access cell by display name of 2nd data field of the pivot table

String displayName = pivotTable.getDataFields().get(1).getDisplayName();

Cell cell = pivotTable.getCellByDisplayName(displayName);

//Access cell style and set its fill color and font color

Style style = cell.getStyle();

style.setForegroundColor(Color.getLightBlue());

style.getFont().setColor(Color.getBlack());

//Set the style of the cell

pivotTable.format(cell.getRow(), cell.getColumn(), style);

//Save workbook

workbook.save("output.xlsx");

{{< /highlight >}}
### **Eigenschaft SaveOptions.MergeAreas hinzugefügt**
Aspose.Cells for Java 8.5.2 hat die Eigenschaft SaveOptions.MergeAreas verfügbar gemacht, die Werte vom Typ Boolean akzeptieren kann. Der Standardwert ist "false". Wenn er jedoch auf "true" gesetzt ist, versucht Aspose.Cells for Java API, die einzelne CellArea zusammenzuführen, bevor die Datei gespeichert wird.

{{% alert color="primary" %}} 

Wenn eine Tabelle zu viele einzelne Zellen mit angewendeter Validierung enthält, besteht die Möglichkeit, dass die resultierende Tabelle beschädigt wird. Eine mögliche Lösung besteht darin, die Zellen mit identischen Validierungsregeln zusammenzuführen, oder Sie können jetzt die Eigenschaft SaveOptions.MergeAreas verwenden, um API anzuweisen, die CellAreas vor dem Speichervorgang automatisch zusammenzuführen.

{{% /alert %}} 
### **Eigenschaft Geometry.ShapeAdjustValues hinzugefügt**
 Mit der Veröffentlichung von v8.5.2 hat Aspose.Cells API die Geometry.getShapeAdjustValues-Methode verfügbar gemacht, die verwendet werden kann[auf die Anpassungspunkte verschiedener Formen zugreifen und Änderungen daran vornehmen](/cells/de/java/change-adjustment-values-of-the-shape/).

{{% alert color="primary" %}} 

In der Microsoft Excel-Oberfläche werden die Anpassungspunkte als gelbe Rautenknoten angezeigt.

{{% /alert %}} 

 Zum Beispiel,

1. Abgerundetes Rechteck hat eine Anpassung, um den Bogen zu ändern
1. Dreieck hat eine Anpassung, um die Position des Punktes zu ändern
1. Trapez hat eine Anpassung, um die Breite der Oberseite zu ändern
1. Pfeile haben zwei Anpassungen, um die Form des Kopfes und des Schwanzes zu ändern

Hier ist das einfachste Anwendungsszenario.

**Java**

{{< highlight "csharp" >}}

 //Create workbook object from source excel file

Workbook workbook = new Workbook("source.xlsx");

//Access first worksheet

Worksheet worksheet = workbook.getWorksheets().get(0);

//Access first three shapes of the worksheet

Shape shape1 = worksheet.getShapes().get(0);

Shape shape2 = worksheet.getShapes().get(1);

Shape shape3 = worksheet.getShapes().get(2);

//Change the adjustment values of the shapes

shape1.getGeometry().getShapeAdjustValues().get(0).setValue(0.5d);

shape2.getGeometry().getShapeAdjustValues().get(0).setValue(0.8d);

shape3.getGeometry().getShapeAdjustValues().get(0).setValue(0.5d);

//Save the workbook

workbook.save("output.xlsx");

{{< /highlight >}}
### **Aufzählungsfeld ConsolidationFunction.DISTINCT_COUNT Hinzugefügt**
Aspose.Cells for Java 8.5.2 hat das Feld ConsolidationFunction.DISTINCT_COUNT bereitgestellt, das verwendet werden kann, um die konsolidierte Funktion Distinct Count auf DataField einer PivotTable anzuwenden.

{{% alert color="primary" %}} 

Die Distinct Count-Konsolidierungsfunktion wird nur von Microsoft Excel 2013 unterstützt.

{{% /alert %}}
