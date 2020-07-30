---
title : "Display and Hide Tabs of Workbook in xlsx4j" 
description : "" 
weight : 20684 
toc : false
type: docs
url: /java/plugins/xlsx4j/missingfeaturesinapscls/worksheets/display+and+hide+tabs+of+workbook+in+xlsx4j/
---

# Aspose.Cells for Java : Display and Hide Tabs of Workbook in xlsx4j


## Aspose.Cells - Display and Hide Tabs of Workbook

Aspose.Cells provides a class, Workbook, that represents a Microsoft Excel file. The `Workbook` class provides a wide range of properties and methods for managing an Excel file. To control the visibility of tabs in an Excel file, developers can use the Workbook class' setShowTabs method.

**Java**

{{< code lang="java" >}}
//Instantiating a Workbook object by excel file path
Workbook workbook = new Workbook(dataDir + "book1.xls");

//Hiding the tabs of the Excel file
workbook.getSettings().setShowTabs(false);

//Saving the modified Excel file in default (that is Excel 2003) format
workbook.save(dataDir + "AsposeHideTabs.xls");

// ===============================================================

//Displaying the tabs of the Excel file
workbook.getSettings().setShowTabs(true);

//Saving the modified Excel file in default (that is Excel 2003) format
workbook.save(dataDir + "AsposeDisplayTabs.xls");
{{< /code >}}

## Download Running Code

*   [CodePlex](http://asposecellsjavaxlsx4j.codeplex.com/releases/view/618923)
*   [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Xlsx4j-v1.0.0)

## Download Sample Code

*   [CodePlex](https://asposecellsjavaxlsx4j.codeplex.com/SourceControl/latest#src/main/java/com/aspose/cells/examples/asposefeatures/worksheets/displayandhidetabs/AsposeDisplayAndHideTabs.java)
*   [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose.Cells-for-Java_for_Xlsx4j/src/main/java/com/aspose/cells/examples/asposefeatures/worksheets/displayandhidetabs/AsposeDisplayAndHideTabs.java)

For more details, visit [Display or Hide Tabs](http://www.aspose.com/docs/display/cellsjava/Display+or+Hide+Tabs).

