---
title: Ändringar i offentlig API i Aspose.Cells 8.5.2
type: docs
weight: 190
url: /sv/java/public-api-changes-in-aspose-cells-8-5-2/
---

{{% alert color="primary" %}} 

Detta dokument beskriver ändringarna i Aspose.Cells API från version 8.5.1 till 8.5.2 som kan vara av intresse för modul/apputvecklare. Det inkluderar inte bara nya och uppdaterade offentliga metoder, [tillagda klasser etc.](/cells/sv/java/public-api-changes-in-aspose-cells-8-5-2/), men även en beskrivning av eventuella förändringar i beteendet bakom kulisserna i Aspose.Cells.

{{% /alert %}} 
## **Tillagda API:er**
### **Rendera kalkylblad till grafiskt sammanhang**
Detta släpp av Aspose.Cells for Java API har exponerat ytterligare en överbelastning av SheetRender.toImage-metoden som nu tillåter att acceptera en instans av Graphics2D-klassen för att [rendera arbetsbladet i grafiska sammanhang](/cells/sv/java/render-worksheet-to-graphic-context/). Signaturerna för den nyexponerade metoden är följande.

- SheetRender.toImage(int pageIndex, Graphics2D graphic)

Följande är det enkla användningscenariot.

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
### **Lade till PivotTable.getCellByDisplayName-metoden**
Aspose.Cells for Java 8.5.2 har exponerat PivotTable.getCellByDisplayName-metoden som kan användas för att [hämta Cell-objekt efter namnet på PivotField](/cells/sv/java/get-the-cell-object-by-displayname-of-pivotfield-of-pivottable/). Denna metod kan vara användbar i scenarier där du vill markera eller formatera PivotField-huvudet.

Följande är det enkla användningscenariot.

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
### **Lade till SaveOptions.MergeAreas-egenskapen**
Aspose.Cells for Java 8.5.2 har exponerat SaveOptions.MergeAreas-egenskapen som kan acceptera Boolean-värde. Standardvärdet är falskt, men om det är inställt på sant, försöker Aspose.Cells for Java API att sammanfoga de individuella CellArea före sparningen av filen.

{{% alert color="primary" %}} 

Om ett kalkylblad har för många individuella celler med tillämpad validering finns det chanser att det resulterande kalkylbladet kan bli korrupt. En möjlig lösning är att sammanfoga cellerna med identiska valideringsregler eller så kan du nu använda SaveOptions.MergeAreas-egenskapen för att instruera API att automatiskt sammanfoga CellAreas före sparningen.

{{% /alert %}} 
### **Lade till Geometry.ShapeAdjustValues-egenskapen**
Genom släppet av v8.5.2 har Aspose.Cells API exponerat Geometry.getShapeAdjustValues-metoden som kan användas för att [komma åt och göra ändringar i justeringspunkterna för olika former](/cells/sv/java/change-adjustment-values-of-the-shape/).

{{% alert color="primary" %}} 

I Microsoft Excel-gränssnittet visas justeringspunkterna som gula diamantnoder.

{{% /alert %}} 

Till exempel, 

1. Avrundad rektangel har en justering för att ändra bågen
1. Triangel har en justering för att ändra platsen för punkten
1. Trapets har en justering för att ändra bredden på toppen
1. Pilar har två justeringar för att ändra formen på huvudet och svansen

Här är det enklaste användningsscenario.

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
### **Enumeration Fält ConsolidationFunction.DISTINCT_COUNT Tillagt**
Aspose.Cells for Java 8.5.2 har exponerat fältet ConsolidationFunction.DISTINCT_COUNT som kan användas för att tillämpa den unika räknade konsolideringsfunktionen på DataField av en PivotTable.

{{% alert color="primary" %}} 

Unik räkning konsolideringsfunktion stöds endast av Microsoft Excel 2013.

{{% /alert %}}
