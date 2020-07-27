+++
title = "Add Word Art Watermark to Worksheet using Aspose.Cells" 
description = "" 
weight = 20636 
+++

Aspose.Cells for Java : Add Word Art Watermark to Worksheet using Aspose.Cells  

# Aspose.Cells for Java : Add Word Art Watermark to Worksheet using Aspose.Cells


## Aspose.Cells - Add Word Art Watermark to Worksheet

Use WordArt to add special text effects to spreadsheets. For example, stretch a title across the top of the file, decorate text, and make text fit a preset shape, or apply text to an Excel sheet as A background watermark. The WordArt becomes an object that you can move or position in spreadsheets to add decoration.

**Java**

{{< code lang="java" >}}
Workbook workbook = new Workbook();
//Get the first default sheet
Worksheet sheet = workbook.getWorksheets().get(0);

//Add Watermark
Shape wordart = sheet.getShapes().addTextEffect(MsoPresetTextEffect.TEXT_EFFECT_1,
"CONFIDENTIAL", "Arial Black", 50, false, true
, 18, 8, 1, 1, 130, 800);

//Get the shape's fill format
FillFormat wordArtFormat = wordart.getFill();

//Set the transparency
wordArtFormat.setTransparency(0.9);

//Make the line invisible
wordart.setHasLine(false);

//Save the file
workbook.save(dataDir + "AsposeWatermark_Out.xls");
{{< /code >}}

## Download Running Code

*   [CodePlex](https://asposecellsjavaapachepoi.codeplex.com/releases/view/618615)
*   [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)

## Download Sample Code

*   [CodePlex](https://asposecellsjavaapachepoi.codeplex.com/SourceControl/latest#src/main/java/com/aspose/cells/examples/asposefeatures/worksheets/AddWatermarkToWorksheet.java)
*   [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/src/main/java/com/aspose/cells/examples/asposefeatures/worksheets/AddWatermarkToWorksheet.java)

For more details, visit [Add WordArt Watermark to Worksheet](http://docs.aspose.com:8082/docs/display/cellsjava/Add+WordArt+Watermark+to+Worksheet).

