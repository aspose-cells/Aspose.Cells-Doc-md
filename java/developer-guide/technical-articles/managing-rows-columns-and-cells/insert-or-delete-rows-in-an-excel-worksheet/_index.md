---
title: Insert or Delete Rows in an Excel Worksheet
type: docs
weight: 20
url: /java/insert-or-delete-rows-in-an-excel-worksheet/
---

{{% alert color="primary" %}}

When creating a new worksheet, or working with an existing worksheet, you might need to add extra rows or columns to accommodate data. At other times, you might need to delete rows or columns from specified positions in the worksheet.

{{% /alert %}}

Aspose.Cells offers two methods for inserting and deleting rows: [**Cells.insertRows**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#insertRow(int)) and [**Cells.deleteRows**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#deleteRows(int,%20int)). These methods are optimized for performance and do the job very quickly.

To insert or remove a number of rows, we recommend that you always use the [**Cells.insertRows**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#insertRow(int)) and [**Cells.deleteRows**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#deleteRows(int,%20int)) methods instead of using the [**Cells.insertRow**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#insertRow(int)) or [**Cells.deleteRow**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#deleteRow(int)) methods in a loop.

Aspose.Cells works in the same way as Microsoft Excel does. When rows or columns are added, the worksheet content is shifted down and to the right. When rows or columns are removed, the worksheet content is shifted up or to the left. Any references in other worksheets and cells are updated when rows are added or removed.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-InsertDeleteRows-InsertDeleteRows.java" >}}
