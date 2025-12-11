---
title: Display and Hide Scrollbars of Workbooks in xlsx4j
type: docs
weight: 30
url: /java/display-and-hide-scrollbars-of-workbooks-in-xlsx4j/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Aspose.Cells - Display and Hide Scrollbars of Workbooks**
Aspose.Cells provides a class, [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook), that represents an Excel file. [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) class provides a wide range of properties and methods to manage an Excel file. But to control the visibility of the scroll bars in the Excel file, developers may use **setVScrollBarVisible** and **setHScrollBarVisible** methods of the [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) class.

**Java**

{{< highlight java >}}

 //Instantiating an Excel object by Excel file path

Workbook workbook = new Workbook(dataDir + "book1.xls");

//Hiding the vertical scroll bar of the Excel file

workbook.getSettings().setVScrollBarVisible(false);

//Hiding the horizontal scroll bar of the Excel file

workbook.getSettings().setHScrollBarVisible(false);

//Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(dataDir + "AsposeScrollbarsHide.xls");

// ===============================================================

//Displaying the vertical scroll bar of the Excel file

workbook.getSettings().setVScrollBarVisible(true);

//Displaying the horizontal scroll bar of the Excel file

workbook.getSettings().setHScrollBarVisible(true);

//Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(dataDir + "AsposeDisplayScrollbars.xls");


{{< /highlight >}}
## **Download Running Code**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Xlsx4j-v1.0.0)
## **Download Sample Code**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Xlsx4j/src/main/java/com/aspose/cells/examples/asposefeatures/worksheets/displayandhidescrollbars/AsposeDisplayAndHideScrollbars.java)
