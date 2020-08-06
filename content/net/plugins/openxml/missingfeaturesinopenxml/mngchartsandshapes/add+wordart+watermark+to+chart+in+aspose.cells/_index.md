---
title : "Add WordArt Watermark to Chart in Aspose.Cells" 
description : "" 
weight : 20878 
toc : false
type: docs
url: /net/plugins/openxml/missingfeaturesinopenxml/mngchartsandshapes/add+wordart+watermark+to+chart+in+aspose.cells/
---

# Aspose.Cells for .NET : Add WordArt Watermark to Chart in Aspose.Cells


You can use WordArt to add special text effects to spreadsheets. For example, stretch a title, decorate text, make text fit a preset shape, or apply the affected text to a chart’s plot area as a watermark. The WordArt becomes an object that you can move or position in your spreadsheets to add decoration.

The following example shows how to add a WordArt shape as a watermark for an existing chart’s plot area. The example uses a template Excel file that already contains the chart.

**The input file**  
![image](1612888729.png)

**The output file**

![image](700483713.png)

**C#**

string FilePath = @"..\\..\\..\\Sample Files\\";string FileName = FilePath + "Add WordArt Watermark to Chart.xlsx";//Open the existing excel file.Workbook workbook = new Workbook(FileName);//Get the chart in the first worksheet.Aspose.Cells.Charts.Chart chart = workbook.Worksheets\[0\].Charts\[0\];//Add a WordArt watermark (shape) to the chart's plot area.Aspose.Cells.Drawing.Shape wordart = chart.Shapes.AddTextEffectInChart(MsoPresetTextEffect.TextEffect2,"CONFIDENTIAL", "Arial Black", 66, false, false, 1200, 500, 2000, 3000);//Get the shape's fill format.Aspose.Cells.Drawing.MsoFillFormat wordArtFormat = wordart.FillFormat;//Set the transparency.wordArtFormat.Transparency = 0.9;//Get the line format and make it invisible.Aspose.Cells.Drawing.MsoLineFormat lineFormat = wordart.LineFormat;lineFormat.IsVisible = false;//Save the excel file.workbook.Save(FileName);

### Download Sample Code

*   [Codeplex](https://asposeopenxml.codeplex.com/SourceControl/latest#Aspose.Cells Features missing in OpenXML/Add WordArt Watermark to Chart/)
*   [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20OpenXML%20Spreadsheets/OpenXML%20Missing%20Features/Add%20WordArt%20Watermark%20to%20Chart)
*   [Code.MSDN](https://code.msdn.microsoft.com/AsposeCells-Features-8fba7c3c/view/SourceCode#content)

### Download Running Example

*   [Codeplex](https://asposecellsopenxml.codeplex.com/releases/view/619160)
*   [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
*   [Code.MSDN](https://code.msdn.microsoft.com/AsposeCells-Features-8fba7c3c)

