---
title : "Locking WordArt Watermark in Aspose.Cells" 
description : "" 
weight : 20881 
toc : false
type: docs
url: /net/plugins/openxml/missingfeaturesinopenxml/mngchartsandshapes/locking+wordart+watermark+in+aspose.cells/
---

# Aspose.Cells for .NET : Locking WordArt Watermark in Aspose.Cells


Aspose.Cells APIs allow to add WordArt watermarks on the worksheet in a way that the WordArt becomes an object that you can be moved and positioned on the worksheet. It is also possible to lock the WordArt object for any interaction such as editing, movement & selection. This article explains the usage of `Shape.SetLockedProperty` method to lock a few aspects of the watermark.

  

Aspose.Cells APIs allow to lock certain aspects of the watermark so that the user interaction could be limited or completely blocked. The following code snippet demonstrates the usage of Aspose.Cells for .NET API to lock selection, movement, editing and re-sizing of the watermark by creating a spreadsheet from scratch.

**C#**

string FilePath = @"..\\..\\..\\Sample Files\\";string FileName = FilePath + "Locking WordArt Watermark.xlsx";//Instantiate a new WorkbookWorkbook workbook = new Workbook();//Get the first default sheetWorksheet sheet = workbook.Worksheets\[0\];//Add WatermarkAspose.Cells.Drawing.Shape wordart = sheet.Shapes.AddTextEffect(MsoPresetTextEffect.TextEffect1,"CONFIDENTIAL", "Arial Black", 50, false, true, 18, 8, 1, 1, 130, 800);//Lock Shape Aspectswordart.IsLocked = true;wordart.SetLockedProperty(ShapeLockType.Selection, true);wordart.SetLockedProperty(ShapeLockType.ShapeType, true);wordart.SetLockedProperty(ShapeLockType.Move, true);wordart.SetLockedProperty(ShapeLockType.Resize, true);wordart.SetLockedProperty(ShapeLockType.Text, true);//Get the fill format of the word artMsoFillFormat wordArtFormat = wordart.FillFormat;//Set the colorwordArtFormat.ForeColor = Color.Red;//Set the transparencywordArtFormat.Transparency = 0.9;//Make the line invisibleMsoLineFormat lineFormat = wordart.LineFormat;lineFormat.IsVisible = false;//Save the fileworkbook.Save(FileName);

### Download Sample Code

*   [Codeplex](https://asposeopenxml.codeplex.com/SourceControl/latest#Aspose.Cells Features missing in OpenXML/Locking WordArt Watermark/)
*   [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20OpenXML%20Spreadsheets/OpenXML%20Missing%20Features/Locking%20WordArt%20Watermark)
*   [Code.MSDN](https://code.msdn.microsoft.com/AsposeCells-Features-8fba7c3c/view/SourceCode#content)

### Download Running Example

*   [Codeplex](https://asposecellsopenxml.codeplex.com/releases/view/619160)
*   [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
*   [Code.MSDN](https://code.msdn.microsoft.com/AsposeCells-Features-8fba7c3c)

