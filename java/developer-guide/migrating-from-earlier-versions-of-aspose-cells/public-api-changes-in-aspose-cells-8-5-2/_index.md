---
title: Public API Changes in Aspose.Cells 8.5.2
type: docs
weight: 190
url: /java/public-api-changes-in-aspose-cells-8-5-2/
---

{{% alert color="primary" %}} 

This document describes the changes to the Aspose.Cells API from version 8.5.1 to 8.5.2 that may be of interest to module/application developers. It includes not only new and updated public methods, [added classes etc.](/cells/java/public-api-changes-in-aspose-cells-8-5-2-html/), but also a description of any changes in the behavior behind the scenes in Aspose.Cells.

{{% /alert %}} 
## **Added APIs**
### **Render Worksheet to Graphic Context**
This release of Aspose.Cells for Java API has exposed another overload of SheetRender.toImage method that now allows to accept an instance of Graphics2D class to [render the Worksheet in Graphics context](http://www.aspose.com/docs/display/cellsjava/Render+Worksheet+to+Graphic+Context). The signatures of newly added method is as follow.

- SheetRender.toImage(int pageIndex, Graphics2D graphic)

Following is the simple usage scenario.

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
### **Method PivotTable.getCellByDisplayName Added**
Aspose.Cells for Java 8.5.2 has exposed the PivotTable.getCellByDisplayName method that can be used to [retrieve the Cell object by the name of the PivotField](http://www.aspose.com/docs/display/cellsjava/Get+the+Cell+object+by+DisplayName+of+PivotField+of+PivotTable). This method could be useful in scenarios where you wish to highlight or format the PivotField header.

Following is the simple usage scenario.

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
### **Property SaveOptions.MergeAreas Added**
Aspose.Cells for Java 8.5.2 has exposed the SaveOptions.MergeAreas property that can accept Boolean type value. The default value is false however, if set to true, the Aspose.Cells for Java API tries to merge the individual CellArea before saving the file.

{{% alert color="primary" %}} 

If a spreadsheet has too many individual cells with validation applied, there are chances that the resultant spreadsheet may get corrupted. One possible solution is to merge the cells with identical validation rules or you can now use the SaveOptions.MergeAreas property to direct the API to auto merge the CellAreas before save operation.

{{% /alert %}} 
### **Property Geometry.ShapeAdjustValues Added**
With the release of v8.5.2, the Aspose.Cells API has exposed the Geometry.getShapeAdjustValues method that can be used to [access and make changes to the adjustment points of different shapes](http://www.aspose.com/docs/display/cellsjava/Change+Adjustment+Values+of+the+Shape).

{{% alert color="primary" %}} 

In Microsoft Excel interface, the adjustment points display as yellow diamond nodes.

{{% /alert %}} 

For instance, 

1. Rounded Rectangle has an adjustment to change the arc
1. Triangle has an adjustment to change the location of the point
1. Trapezoid has an adjustment to change the width of the top
1. Arrows have two adjustments to change the shape of the head and tail

Here is the simplest usage scenario.

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
### **Enumeration Field ConsolidationFunction.DISTINCT_COUNT Added**
Aspose.Cells for Java 8.5.2 has exposed the ConsolidationFunction.DISTINCT_COUNT field that can be used to apply the Distinct Count consolidated function on DataField of a PivotTable.

{{% alert color="primary" %}} 

Distinct Count consolidation function is supported by Microsoft Excel 2013 only.

{{% /alert %}}
