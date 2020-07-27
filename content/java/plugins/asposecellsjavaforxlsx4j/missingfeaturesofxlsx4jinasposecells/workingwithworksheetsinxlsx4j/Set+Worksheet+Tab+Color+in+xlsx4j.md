+++
title = "Set Worksheet Tab Color in xlsx4j" 
description = "" 
weight = 20686 
+++

Aspose.Cells for Java : Set Worksheet Tab Color in xlsx4j  

# Aspose.Cells for Java : Set Worksheet Tab Color in xlsx4j


## Aspose.Cells - Set Worksheet Tab Color

Aspose.Cells allows you to change the color of individual worksheet tabs to make them prominent from the rest. For example, you can make Expenses red, Sales green, Assets blue, etc.

#### Setting Worksheet Tab Color with Microsoft Excel

1.  Right-click a tab in the tab-sheet at the bottom of the current worksheet.
2.  Select **Tab color**.
3.  Select a color from the palette.
4.  Click **OK**.

**Java**

{{< code lang="java" >}}
//Instantiate a new Workbook
Workbook workbook = new Workbook(dataDir + "workbook.xls");

//Get the first worksheet in the book
Worksheet worksheet = workbook.getWorksheets().get(0);

//Set the tab color
worksheet.setTabColor(Color.getRed());

//Save the Excel file
workbook.save(dataDir + "AsposeColoredTab_Out.xls");
{{< /code >}}

## Download Running Code

*   [CodePlex](http://asposecellsjavaxlsx4j.codeplex.com/releases/view/618923)
*   [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Xlsx4j-v1.0.0)

## Download Sample Code

*   [CodePlex](https://asposecellsjavaxlsx4j.codeplex.com/SourceControl/latest#src/main/java/com/aspose/cells/examples/asposefeatures/worksheets/settabcolor/AsposeSetWorksheetTabColor.java)
*   [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose.Cells-for-Java_for_Xlsx4j/src/main/java/com/aspose/cells/examples/asposefeatures/worksheets/settabcolor/AsposeSetWorksheetTabColor.java)

For more details, visit [Set Worksheet Tab Color](http://docs.aspose.com:8082/docs/display/cellsjava/Set+Worksheet+Tab+Color).

