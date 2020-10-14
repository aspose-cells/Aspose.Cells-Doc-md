---
title: Delete Pivot Table from a Worksheet
type: docs
weight: 50
url: /java/delete-pivot-table-from-a-worksheet/
---

{{% alert color="primary" %}}

Aspose.Cells provides a feature to delete or remove a Pivot Table from a Worksheet. You can delete the pivot table using the pivot table object or pivot table position. Please use the [**Worksheet.getPivotTables().remove()**](https://apireference.aspose.com/cells/java/com.aspose.cells/pivottablecollection#remove(com.aspose.cells.PivotTable)) method to delete the pivot table using the pivot table object and [**Worksheet.getPivotTables().removeAt()**](https://apireference.aspose.com/cells/java/com.aspose.cells/pivottablecollection#removeAt(int)) method to delete a pivot table object using its position inside the pivot table collection.

{{% /alert %}}

## **Example**

The following sample code deletes two pivot tables from the worksheet. First, it removes the pivot table using [**Worksheet.getPivotTables().remove()**](https://apireference.aspose.com/cells/java/com.aspose.cells/pivottablecollection#remove(com.aspose.cells.PivotTable)) method and then it removes the pivot table using [**Worksheet.getPivotTables().removeAt()**](https://apireference.aspose.com/cells/java/com.aspose.cells/pivottablecollection#removeAt(int)) method

{{< gist "aspose-com-gists" "a20e8fa273e7cfa37d032b8211fcf8bf" "Examples-src-main-java-com-aspose-cells-examples-articles-DeletePivotTableFromWorksheet-DeletePivotTableFromWorksheet.java" >}}
