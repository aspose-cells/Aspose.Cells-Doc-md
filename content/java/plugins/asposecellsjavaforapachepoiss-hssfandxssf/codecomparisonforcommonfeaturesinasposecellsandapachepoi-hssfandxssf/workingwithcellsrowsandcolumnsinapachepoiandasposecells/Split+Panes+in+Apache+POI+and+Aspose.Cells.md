+++
title = "Split Panes in Apache POI and Aspose.Cells" 
description = "" 
weight = 20612 
+++

Aspose.Cells for Java : Split Panes in Apache POI and Aspose.Cells  

# Aspose.Cells for Java : Split Panes in Apache POI and Aspose.Cells


## Aspose.Cells - Split Panes

Aspose.Cells provides a class, Workbook that represents a Microsoft Excel file. The Workbook class provides a wide range of properties and methods for managing Excel files. To implement split views, use the Worksheet class' split method. To remove split panes, use the removeSplit method.

**Java**

{{< code lang="java" >}}
//Instantiate a new workbook / Open a template file
Workbook book = new Workbook(dataDir + "workbook.xls");

//Set the active cell
book.getWorksheets().get(0).setActiveCell("A20");

//Split the worksheet window
book.getWorksheets().get(0).split();
{{< /code >}}

## Apache POI SS - HSSF & XSSF - Split Panes

Split Panes functionality can be achieved by createSplitPane method while using Apache POI SS (HSSF & XSSF) API

**Java**

{{< code lang="java" >}}
Workbook wb = new XSSFWorkbook();
Sheet sheet = wb.createSheet("new sheet");

// Create a split with the lower left side being the active quadrant
sheet.createSplitPane(2000, 2000, 0, 0, Sheet.PANE_LOWER_LEFT);
{{< /code >}}

## Download Running Code

*   [CodePlex](https://asposecellsjavaapachepoi.codeplex.com/releases/view/618615)
*   [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)

## Download Sample Code

*   [CodePlex](https://asposecellsjavaapachepoi.codeplex.com/SourceControl/latest#src/main/java/com/aspose/cells/examples/featurescomparison/cellsrowscolumns/splitpanes/)
*   [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/src/main/java/com/aspose/cells/examples/featurescomparison/cellsrowscolumns/splitpanes)

For more details, visit [Split Panes](http://docs.aspose.com:8082/docs/display/cellsjava/Split+Panes).

