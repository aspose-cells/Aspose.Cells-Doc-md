---
title: Offentliga API-ändringar i Aspose.Cells 8.5.2
type: docs
weight: 190
url: /sv/java/public-api-changes-in-aspose-cells-8-5-2/
---
{{% alert color="primary" %}} 

 Det här dokumentet beskriver ändringarna av Aspose.Cells API från version 8.5.1 till 8.5.2 som kan vara av intresse för modul-/applikationsutvecklare. Det inkluderar inte bara nya och uppdaterade offentliga metoder,[lagt till klasser etc.](/cells/sv/java/public-api-changes-in-aspose-cells-8-5-2/), men också en beskrivning av eventuella förändringar i beteendet bakom kulisserna i Aspose.Cells.

{{% /alert %}} 
## **Lade till API:er**
### **Återge arbetsblad till grafisk kontext**
Den här utgåvan av Aspose.Cells för Java API har avslöjat ytterligare en överbelastning av SheetRender.toImage-metoden som nu gör det möjligt att acceptera en instans av Graphics2D-klassen till[rendera arbetsbladet i grafiksammanhang](/cells/sv/java/render-worksheet-to-graphic-context/). Signaturerna för den nyligen tillagda metoden är följande.

- SheetRender.toImage(int pageIndex, Graphics2D-grafik)

Följande är det enkla användningsscenariot.

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
### **Metod PivotTable.getCellByDisplayName tillagd**
 Aspose.Cells för Java 8.5.2 har exponerat metoden PivotTable.getCellByDisplayName som kan användas för att[hämta objektet Cell med namnet PivotField](/cells/sv/java/get-the-cell-object-by-displayname-of-pivotfield-of-pivottable/). Den här metoden kan vara användbar i scenarier där du vill markera eller formatera PivotField-huvudet.

Följande är det enkla användningsscenariot.

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
### **Property SaveOptions.MergeAreas tillagd**
Aspose.Cells för Java 8.5.2 har avslöjat egenskapen SaveOptions.MergeAreas som kan acceptera booleskt typvärde. Standardvärdet är falskt, men om det är satt till true, försöker API:et Aspose.Cells för Java att slå samman den enskilda CellArea innan filen sparas.

{{% alert color="primary" %}} 

Om ett kalkylark har för många enskilda celler med validering, finns det chanser att det resulterande kalkylarket kan skadas. En möjlig lösning är att slå samman cellerna med identiska valideringsregler eller så kan du nu använda egenskapen SaveOptions.MergeAreas för att styra API:et att automatiskt sammanfoga CellAreas innan du sparar.

{{% /alert %}} 
### **Property Geometry.ShapeAdjustValues Added**
 Med lanseringen av v8.5.2 har API:et Aspose.Cells avslöjat Geometry.getShapeAdjustValues-metoden som kan användas för att[komma åt och göra ändringar i justeringspunkterna för olika former](/cells/sv/java/change-adjustment-values-of-the-shape/).

{{% alert color="primary" %}} 

I Microsoft Excel-gränssnittet visas justeringspunkterna som gula diamantnoder.

{{% /alert %}} 

 Till exempel,

1. Rundad rektangel har en justering för att ändra bågen
1. Triangeln har en justering för att ändra platsen för punkten
1. Trapets har en justering för att ändra toppens bredd
1. Pilarna har två justeringar för att ändra formen på huvudet och svansen

Här är det enklaste användningsscenariot.

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
### **Uppräkningsfält ConsolidationFunction.DISTINCT_COUNT har lagts till**
Aspose.Cells för Java 8.5.2 har exponerat fältet ConsolidationFunction.DISTINCT_COUNT som kan användas för att tillämpa den konsoliderade funktionen Distinct Count på DataField i en pivottabell.

{{% alert color="primary" %}} 

Funktionen Distinct Count-konsolidering stöds endast av Microsoft Excel 2013.

{{% /alert %}}
