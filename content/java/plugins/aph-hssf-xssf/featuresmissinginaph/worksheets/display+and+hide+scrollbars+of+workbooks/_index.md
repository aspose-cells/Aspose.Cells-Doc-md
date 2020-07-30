---
title : "Display and Hide Scrollbars of Workbooks" 
description : "" 
weight : 20639 
toc : false
type: docs
url: /java/plugins/aph-hssf-xssf/featuresmissinginaph/worksheets/display+and+hide+scrollbars+of+workbooks/
---

# Aspose.Cells for Java : Display and Hide Scrollbars of Workbooks


## Aspose.Cells - Display and Hide Scrollbars of Workbooks

Aspose.Cells provides a class, **Workbook** that represents an Excel file. **Workbook** class provides a wide range of properties and methods to manage an Excel file. But, to control the visibility of the scroll bars in the Excel file, developers may use **setVScrollBarVisible** & **setHScrollBarVisible** methods of the **Workbook** class.

**Java**

{{< code lang="java" >}}
//Instantiating a Excel object by excel file path
Workbook workbook = new Workbook(dataDir + "book1.xls");

//Hiding the vertical scroll bar of the Excel file
workbook.getSettings().setVScrollBarVisible(false);

//Hiding the horizontal scroll bar of the Excel file
workbook.getSettings().setHScrollBarVisible(false);

//Saving the modified Excel file in default (that is Excel 2003) format
workbook.save(dataDir + "AsposeSrollbarsHide.xls");

// ===============================================================

//Displaying the vertical scroll bar of the Excel file
workbook.getSettings().setVScrollBarVisible(true);

//Displaying the horizontal scroll bar of the Excel file
workbook.getSettings().setHScrollBarVisible(true);

//Saving the modified Excel file in default (that is Excel 2003) format
workbook.save(dataDir + "AsposeDisplaySrollbars.xls");

{{< /code >}}

## Download Running Code

*   [CodePlex](https://asposecellsjavaapachepoi.codeplex.com/releases/view/618615)
*   [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)

## Download Sample Code

*   [CodePlex](https://asposecellsjavaapachepoi.codeplex.com/SourceControl/latest#src/main/java/com/aspose/cells/examples/asposefeatures/worksheets/AsposeDisplayAndHideScrollbars.java)
*   [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/src/main/java/com/aspose/cells/examples/asposefeatures/worksheets/AsposeDisplayAndHideScrollbars.java)

For more details, visit [Display or Hide Scroll Bars](http://www.aspose.com/docs/display/cellsjava/Display+or+Hide+Scroll+Bars).

