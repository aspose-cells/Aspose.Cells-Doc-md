---
title: Ändringar i offentlig API i Aspose.Cells 8.5.2
type: docs
weight: 180
url: /sv/net/public-api-changes-in-aspose-cells-8-5-2/
---

{{% alert color="primary" %}} 

Dokumentet beskriver ändringarna i Aspose.Cells API från version 8.5.1 till 8.5.2, som kan vara av intresse för modul-/applikationsutvecklare. Det inkluderar inte bara nya och uppdaterade offentliga metoder, [tillagda klasser etc.](/cells/sv/net/public-api-changes-in-aspose-cells-8-5-2/), utan beskriver också eventuella förändringar i beteendet bakom kulisserna i Aspose.Cells.

{{% /alert %}} 
## **Tillagda API:er**
### **Rendera kalkylblad till grafiskt sammanhang**
Denna version av Aspose.Cells for .NET API har exponerat två nya överbelastningar av SheetRender.ToImage-metoden som nu tillåter att acceptera en instans av klassen System.Drawing.Graphics för [rendering i grafikkontext](/cells/sv/net/render-worksheet-to-graphic-context/). Signaturerna för de nytt tillagda metoderna är följande.

1. SheetRender.ToImage(int pageIndex, Graphics g, float x, float y)
1. SheetRender.ToImage(int pageIndex, Graphics g, float x, float y, float width, float height)

Följande är det enkla användningscenariot.

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


### **Tillagd PivotTable.GetCellByDisplayName-metod**
Aspose.Cells for .NET 8.5.2 har exponerat metoden PivotTable.GetCellByDisplayName som kan användas för att [hämta Cell-objektet efter namnet på PivotField](/cells/sv/net/get-the-cell-object-by-displayname-of-pivotfield-of-pivottable/). Denna metod kan vara användbar i scenarier där du vill markera eller formatera PivotField-rubriken.

Följande är det enkla användningscenariot.

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


### **Lade till SaveOptions.MergeAreas-egenskapen**
Aspose.Cells for .NET 8.5.2 har exponerat SaveOptions.MergeAreas-egenskapen som kan acceptera Boolean-värde. Standardvärdet är falskt, men om det är inställt på true, försöker Aspose.Cells for .NET API att sammanfoga individuella CellArea före sparandet av filen.

{{% alert color="primary" %}} 

Om ett kalkylblad har för många individuella celler med tillämpad validering finns det chanser att det resulterande kalkylbladet kan bli korrupt. En möjlig lösning är att sammanfoga cellerna med identiska valideringsregler eller så kan du nu använda SaveOptions.MergeAreas-egenskapen för att instruera API att automatiskt sammanfoga CellAreas före sparningen.

{{% /alert %}} 
### **Lade till Shape.Geometry.ShapeAdjustValues-egenskapen**
Med utgivningen av v8.5.2 har Aspose.Cells API exponerat Shape.Geometry.ShapeAdjustValues-egenskapen som kan användas för [att göra ändringar i justeringspunkterna för olika former](/cells/sv/net/change-adjustment-values-of-the-shape/).

{{% alert color="primary" %}} 

I Microsoft Excel-gränssnittet visas justeringspunkterna som gula diamantnoder.

{{% /alert %}} 

Till exempel,

1. Avrundad rektangel har en justering för att ändra bågen
1. Triangel har en justering för att ändra platsen för punkten
1. Trapets har en justering för att ändra bredden på toppen
1. Pilar har två justeringar för att ändra formen på huvudet och svansen

Här är det enklaste användningsscenario.

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


### **Tillägg av värde ConsilidationFunction.DistinctCount**
Aspose.Cells for .NET 8.5.2 har exponerat ConsilidationFunction.DistinctCount-fältet som kan användas för att [tillämpa sammanställningsfunktionen Distinct Count](/cells/sv/net/consolidation-function/) på DataField i en PivotTable.

{{% alert color="primary" %}} 

Unik räkning konsolideringsfunktion stöds endast av Microsoft Excel 2013.

{{% /alert %}} 
### **Bättre hantering av händelser för GridDesktop**
Denna version av Aspose.Cells.GridDesktop har exponerat 4 nya händelser. 2 av dessa händelser triggas vid olika stadier av inläsning av kalkylbladsfiler i GridDesktop, medan de andra 2 triggas vid beräkning av formler.

Händelserna är listade enligt följande.

1. GridDesktop.BeforeLoadFile
1. GridDesktop.FinishLoadFile
1. GridDesktop.BeforeCalculate
1. GridDesktop.FinishCalculate
