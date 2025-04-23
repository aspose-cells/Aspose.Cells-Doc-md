---
title: 从工作表中删除数据透视表
type: docs
weight: 50
url: /zh/java/delete-pivot-table-from-a-worksheet/
---

{{% alert color="primary" %}}

Aspose.Cells 提供了删除工作表中数据透视表的功能。您可以使用数据透视表对象或数据透视表位置来删除数据透视表。请使用 [**Worksheet.getPivotTables().remove()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottablecollection#remove-com.aspose.cells.PivotTable-) 方法使用数据透视表对象来删除数据透视表，用 [**Worksheet.getPivotTables().removeAt()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottablecollection#removeAt-int-) 方法使用数据透视表对象在数据透视表集合中的位置来删除数据透视表对象。

{{% /alert %}}

## **示例**

下面的示例代码从工作表中删除了两个数据透视表。首先，它使用 [**Worksheet.getPivotTables().remove()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottablecollection#remove-com.aspose.cells.PivotTable-) 方法删除数据透视表，然后使用 [**Worksheet.getPivotTables().removeAt()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottablecollection#removeAt-int-) 方法删除数据透视表对象。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-DeletePivotTableFromWorksheet-DeletePivotTableFromWorksheet.java" >}}
{{< app/cells/assistant language="java" >}}
