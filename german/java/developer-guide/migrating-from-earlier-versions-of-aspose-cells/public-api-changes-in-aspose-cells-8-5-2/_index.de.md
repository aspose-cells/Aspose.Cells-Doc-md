---
title: Öffentliche API Änderungen in Aspose.Cells 8.5.2
type: docs
weight: 190
url: /de/java/public-api-changes-in-aspose-cells-8-5-2/
---

{{% alert color="primary" %}} 

Dieses Dokument beschreibt die Änderungen an der Aspose.Cells-API von Version 8.5.1 auf 8.5.2, die für Modul-/Anwendungs-Entwickler von Interesse sein könnten. Es enthält nicht nur neue und aktualisierte öffentliche Methoden, [hinzugefügte Klassen usw.](/cells/de/java/public-api-changes-in-aspose-cells-8-5-2/), sondern auch eine Beschreibung von Änderungen im Verhalten hinter den Kulissen in Aspose.Cells.

{{% /alert %}} 
## **Hinzugefügte APIs**
### **Arbeitsblatt in Grafikkontext rendern**
Diese Version von Aspose.Cells for Java-API hat eine weitere Überlastung der SheetRender.toImage-Methode freigelegt, die jetzt eine Instanz der Graphics2D-Klasse akzeptiert, um [das Arbeitsblatt im grafischen Kontext zu rendern](/cells/de/java/render-worksheet-to-graphic-context/). Die Signaturen der neu hinzugefügten Methode lauten wie folgt.

- SheetRender.toImage(int pageIndex, Graphics2D graphic)

Im Folgenden wird das einfache Anwendungsszenario beschrieben.

**Java**

{{< highlight csharp >}}

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
### **Hinzugefügter PivotTable.getCellByDisplayName-Methode**
Aspose.Cells for Java 8.5.2 hat die PivotTable.getCellByDisplayName-Methode freigelegt, die verwendet werden kann, um [das Zellenobjekt nach dem Namen des PivotField abzurufen](/cells/de/java/get-the-cell-object-by-displayname-of-pivotfield-of-pivottable/). Diese Methode könnte in Szenarien nützlich sein, in denen Sie den PivotField-Header hervorheben oder formatieren möchten.

Im Folgenden wird das einfache Anwendungsszenario beschrieben.

**Java**

{{< highlight csharp >}}

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
### **Hinzugefügte SaveOptions.MergeAreas-Eigenschaft**
Aspose.Cells for Java 8.5.2 hat die SaveOptions.MergeAreas-Eigenschaft freigelegt, die einen Wert vom Typ Boolean akzeptieren kann. Der Standardwert ist false, jedoch versucht, wenn er auf true gesetzt ist, die Aspose.Cells for Java-API, die einzelnen CellAreas vor dem Speichern der Datei zusammenzuführen.

{{% alert color="primary" %}} 

Wenn in einer Tabellenkalkulation zu viele einzelne Zellen mit angewendeter Validierung vorhanden sind, besteht die Gefahr, dass die resultierende Tabellenkalkulation beschädigt wird. Eine mögliche Lösung ist, die Zellen mit identischen Validierungsregeln zusammenzuführen, oder Sie können jetzt die SaveOptions.MergeAreas-Eigenschaft verwenden, um die API anzuweisen, die CellAreas automatisch vor dem Speichervorgang zusammenzuführen.

{{% /alert %}} 
### **Hinzugefügte Geometry.ShapeAdjustValues-Eigenschaft**
Mit der Veröffentlichung von v8.5.2 hat die Aspose.Cells-API die Geometry.getShapeAdjustValues-Methode freigelegt, die dazu verwendet werden kann, [auf die Anpassungspunkte verschiedener Formen zuzugreifen und Änderungen vorzunehmen](/cells/de/java/change-adjustment-values-of-the-shape/).

{{% alert color="primary" %}} 

Im Microsoft Excel-Interface werden die Anpassungspunkte als gelbe Diamantknoten angezeigt.

{{% /alert %}} 

Zum Beispiel 

1. Das abgerundete Rechteck hat eine Anpassung, um den Bogen zu ändern
1. Das Dreieck hat eine Anpassung, um die Position des Punkts zu ändern
1. Das Trapezoid hat eine Anpassung, um die Breite des oberen Teils zu ändern
1. Pfeile haben zwei Anpassungen, um die Form des Kopfes und des Endes zu ändern

Hier ist das einfachste Anwendungsszenario.

**Java**

{{< highlight csharp >}}

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
### **Aufzählungsfeldkonsolidierungsfunktion.DISTINCT_COUNT Hinzugefügt**
Aspose.Cells for Java 8.5.2 hat das Feld ConsolidationFunction.DISTINCT_COUNT freigelegt, das verwendet werden kann, um die konsolidierte Funktion Distinct Count auf das Datenfeld eines PivotTables anzuwenden.

{{% alert color="primary" %}} 

Die Konsolidierungsfunktion Distinct Count wird nur von Microsoft Excel 2013 unterstützt.

{{% /alert %}}
