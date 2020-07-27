+++
title = "Set Worksheet Tab Color in Aspose.Cells" 
description = "" 
weight = 20644 
+++

Aspose.Cells for Java : Set Worksheet Tab Color in Aspose.Cells  

# Aspose.Cells for Java : Set Worksheet Tab Color in Aspose.Cells


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
Workbook workbook = new Workbook(dataPath + "workbook.xls");

//Get the first worksheet in the book
Worksheet worksheet = workbook.getWorksheets().get(0);

//Set the tab color
worksheet.setTabColor(Color.getRed());

//Save the Excel file
workbook.save(dataPath + "AsposeColoredTab_Out.xls");
{{< /code >}}

## Download Running Code

*   [CodePlex](https://asposecellsjavaapachepoi.codeplex.com/releases/view/618615)
*   [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)

## Download Sample Code

*   [CodePlex](https://asposecellsjavaapachepoi.codeplex.com/SourceControl/latest#src/main/java/com/aspose/cells/examples/asposefeatures/worksheets/SetWorksheetTabColor.java)
*   [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/src/main/java/com/aspose/cells/examples/asposefeatures/worksheets/SetWorksheetTabColor.java)

For more details, visit [Set Worksheet Tab Color](http://docs.aspose.com:8082/docs/display/cellsjava/Set+Worksheet+Tab+Color).

