##Public API Changes in Aspose.Cells 8.5.2
This document describes the changes to the Aspose.Cells API from version 8.5.1 to 8.5.2 that may be of interest to module/application developers. It includes not only new and updated public methods, [added classes etc.](https://docs.aspose.com/cells/net/public-api-changes-in-aspose-cells-8-5-2/), but also a description of any changes in the behavior behind the scenes in Aspose.Cells.
## **Added APIs**
### **Render Worksheet to Graphic Context**
This release of Aspose.Cells for .NET API has exposed two new overloads of SheetRender.ToImage method that now allows to accept an instance of System.Drawing.Graphics class to [render in Graphics context](https://docs.aspose.com/cells/net/render-worksheet-to-graphic-context/). The signatures of newly added methods are as follow.
1. SheetRender.ToImage(int pageIndex, Graphics g, float x, float y)
1. SheetRender.ToImage(int pageIndex, Graphics g, float x, float y, float width, float height)
Following is the simple usage scenario.
**C#**
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
### **Added PivotTable.GetCellByDisplayName Method**
Aspose.Cells for .NET 8.5.2 has exposed the PivotTable.GetCellByDisplayName method that can be used to [retrieve the Cell object by the name of the PivotField](https://docs.aspose.com/cells/net/get-the-cell-object-by-displayname-of-pivotfield-of-pivottable/). This method could be useful in scenarios where you wish to highlight or format the PivotField header.
Following is the simple usage scenario.
**C#**
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
### **Added SaveOptions.MergeAreas Property**
Aspose.Cells for .NET 8.5.2 has exposed the SaveOptions.MergeAreas property that can accept Boolean type value. The default value is false however, if set to true, the Aspose.Cells for .NET API tries to merge the individual CellArea before saving the file.
If a spreadsheet has too many individual cells with validation applied, there are chances that the resultant spreadsheet may get corrupted. One possible solution is to merge the cells with identical validation rules or you can now use the SaveOptions.MergeAreas property to direct the API to auto merge the CellAreas before save operation.
### **Added Shape.Geometry.ShapeAdjustValues Property**
With the release of v8.5.2, the Aspose.Cells API has exposed the Shape.Geometry.ShapeAdjustValues property that can be used to [make changes to the adjustment points of different shapes](https://docs.aspose.com/cells/net/change-adjustment-values-of-the-shape/).
In the Microsoft Excel interface, the adjustment points display as yellow diamond nodes.
For instance,
1. Rounded Rectangle has an adjustment to change the arc
1. Triangle has an adjustment to change the location of the point
1. Trapezoid has an adjustment to change the width of the top
1. Arrows have two adjustments to change the shape of the head and tail
Here is the simplest usage scenario.
**C#**
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
### **Enumeration Field ConsolidationFunction.DistinctCount Added**
Aspose.Cells for .NET 8.5.2 has exposed the ConsolidationFunction.DistinctCount field that can be used to [apply the Distinct Count consolidation function](https://docs.aspose.com/cells/net/consolidation-function/) on DataField of a PivotTable.
Distinct Count consolidation function is supported by Microsoft Excel 2013 only.
### **Better Event Handling for GridDesktop**
This release of Aspose.Cells.GridDesktop has exposed 4 new events. 2 of these events trigger on different states of loading spreadsheet files in GridDesktop whereas the other 2 trigger upon calculation of formulas.
The events are listed as follow.
1. GridDesktop.BeforeLoadFile
1. GridDesktop.FinishLoadFile
1. GridDesktop.BeforeCalculate
1. GridDesktop.FinishCalculate
