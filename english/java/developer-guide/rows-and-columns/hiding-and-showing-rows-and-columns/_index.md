---
title: Hiding and Showing Rows and Columns
type: docs
weight: 50
url: /java/hiding-and-showing-rows-and-columns/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Introduction**
Sometimes it may be required by users to hide certain rows or columns of the worksheet and then display them later. Microsoft Excel provides this feature, and so does Aspose.Cells.

## **Controlling the Visibility of Rows & Columns**
Aspose.Cells provides a class, [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook), that represents a Microsoft Excel file. The [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) class contains a [WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) that allows access to each worksheet in the Excel file. A worksheet is represented by the [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) class. The [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) class provides a [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) collection that represents all cells in the worksheet. The [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) collection provides several methods for managing rows or columns in a worksheet. Some of these are discussed below.

### **Hiding Rows or Columns**
Developers can hide a row or column by calling the [HideRow](https://reference.aspose.com/cells/java/com.aspose.cells/cells#hideRow-int-) and [HideColumn](https://reference.aspose.com/cells/java/com.aspose.cells/cells#hideColumn-int-) methods of the [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) collection respectively. Both methods take the row/column index as a parameter to hide the specific row or column.

{{% alert color="primary" %}} 

Note: It is also possible to hide a row or column by setting the row height or column width to **0**, respectively.

{{% /alert %}} 

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_columns-HidingRowsandColumns-HidingRowsandColumns.java" >}}
### **Showing Rows and Columns**
Developers can unhide any hidden row or column by calling the [UnhideRow](https://reference.aspose.com/cells/java/com.aspose.cells/cells#unhideRow-int-double-) and [UnhideColumn](https://reference.aspose.com/cells/java/com.aspose.cells/cells#unhideColumn-int-double-) methods of the [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) collection respectively. Both methods take two parameters:

- **Row or column index** – the index of a row or column that is used to show the specific row or column.
- **Row height or column width** – the row height or column width assigned to the row or column after it’s shown.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_columns-UnhidingRowsandColumns-UnhidingRowsandColumns.java" >}}

{{% alert color="primary" %}} 

While making a hidden column/row visible, if you need to restore it to a previously assigned width or height, or its original width or height, please unhide the column or row with a negative width or height. For example, `worksheet.getCells().unhideColumn(5, -1)`.

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
