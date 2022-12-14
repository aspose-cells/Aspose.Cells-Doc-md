---
title: Offentliga API-ändringar i Aspose.Cells 8.5.2
type: docs
weight: 180
url: /sv/net/public-api-changes-in-aspose-cells-8-5-2/
---
{{% alert color="primary" %}} 

 Det här dokumentet beskriver ändringarna av Aspose.Cells API från version 8.5.1 till 8.5.2 som kan vara av intresse för modul-/applikationsutvecklare. Det inkluderar inte bara nya och uppdaterade offentliga metoder,[lagt till klasser etc.](/cells/sv/net/public-api-changes-in-aspose-cells-8-5-2/), men också en beskrivning av eventuella förändringar i beteendet bakom kulisserna i Aspose.Cells.

{{% /alert %}} 
## **Lade till API:er**
### **Återge arbetsblad till grafisk kontext**
 Den här utgåvan av Aspose.Cells för .NET API har exponerat två nya överbelastningar av SheetRender.ToImage-metoden som nu gör det möjligt att acceptera en instans av klassen System.Drawing.Graphics till[rendera i grafiksammanhang](/cells/sv/net/render-worksheet-to-graphic-context/). Signaturerna för nyligen tillagda metoder är följande.

1. SheetRender.ToImage(int pageIndex, Graphics g, float x, float y)
1. SheetRender.ToImage(int pageIndex, Graphics g, float x, float y, float width, float höjd)

Följande är det enkla användningsscenariot.

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


### **Metod PivotTable.GetCellByDisplayName tillagd**
Aspose.Cells för .NET 8.5.2 har exponerat metoden PivotTable.GetCellByDisplayName som kan användas för att[hämta objektet Cell med namnet PivotField](/cells/sv/net/get-the-cell-object-by-displayname-of-pivotfield-of-pivottable/). Den här metoden kan vara användbar i scenarier där du vill markera eller formatera PivotField-huvudet.

Följande är det enkla användningsscenariot.

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


### **Property SaveOptions.MergeAreas tillagd**
Aspose.Cells för .NET 8.5.2 har avslöjat egenskapen SaveOptions.MergeAreas som kan acceptera booleskt typvärde. Standardvärdet är falskt, men om det är satt till true, försöker Aspose.Cells för .NET API att slå samman den enskilda CellArea innan filen sparas.

{{% alert color="primary" %}} 

Om ett kalkylark har för många enskilda celler med validering, finns det chanser att det resulterande kalkylarket kan skadas. En möjlig lösning är att slå samman cellerna med identiska valideringsregler eller så kan du nu använda egenskapen SaveOptions.MergeAreas för att styra API:et att automatiskt sammanfoga CellAreas innan du sparar.

{{% /alert %}} 
### **Egenskap Shape.Geometry.ShapeAdjustValues Added**
 Med lanseringen av v8.5.2 har Aspose.Cells API exponerat egenskapen Shape.Geometry.ShapeAdjustValues som kan användas för att[gör ändringar i justeringspunkterna för olika former](/cells/sv/net/change-adjustment-values-of-the-shape/).

{{% alert color="primary" %}} 

I Microsoft Excel-gränssnittet visas justeringspunkterna som gula diamantnoder.

{{% /alert %}} 

Till exempel,

1. Rundad rektangel har en justering för att ändra bågen
1. Triangeln har en justering för att ändra platsen för punkten
1. Trapets har en justering för att ändra toppens bredd
1. Pilarna har två justeringar för att ändra formen på huvudet och svansen

Här är det enklaste användningsscenariot.

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


### **Enumeration Field ConsolidationFunction.DistinctCount lagt till**
 Aspose.Cells för .NET 8.5.2 har exponerat fältet ConsolidationFunction.DistinctCount som kan användas för att[tillämpa konsolideringsfunktionen Distinct Count](/cells/sv/net/consolidation-function/) på datafältet i en pivottabell.

{{% alert color="primary" %}} 

Funktionen Distinct Count-konsolidering stöds endast av Microsoft Excel 2013.

{{% /alert %}} 
### **Bättre händelsehantering för GridDesktop**
Den här utgåvan av Aspose.Cells.GridDesktop har avslöjat 4 nya händelser. 2 av dessa händelser utlöses vid olika tillstånd för inläsning av kalkylbladsfiler i GridDesktop medan de andra två utlöses vid beräkning av formler.

Händelserna listas enligt följande.

1. GridDesktop.BeforeLoadFile
1. GridDesktop.FinishLoadFile
1. GridDesktop.BeforeCalculate
1. GridDesktop.FinishCalculate
