---
title: 合并文件
type: docs
weight: 10
url: /zh/java/merge-files/
---

## **介绍**

Aspose.Cells提供了不同的合并文件的方法。对于包含数据、格式和公式的简单文件，可以使用[**Workbook.combine()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#combine(com.aspose.cells.Workbook)) 方法来合并多个工作簿，还可以使用[**Worksheet.copy(**)](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#copy(com.aspose.cells.Worksheet)) 方法来将工作表复制到新的工作簿中。这些方法易于使用且有效，但如果要合并大量文件，可能会消耗大量系统资源。为了避免这种情况，使用CellsHelper.mergeFiles静态方法，这是一种更有效的合并多个文件的方式。

## **使用Aspose.Cells合并文件**

以下示例代码说明了如何使用CellsHelper.mergeFiles方法合并大文件。它包括两个简单但很大的文件，MyBook1.xls和MyBook2.xls。这些文件只包含格式化数据和公式。

{{% alert color="primary" %}}

CellsHelper.mergeFiles方法仅支持合并数据、样式、格式和公式。使用此方法可能无法合并图表、图片、注释或其他对象等对象。此外，使用缓存文件来存储临时数据以进行该过程。

{{% /alert %}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-CellsHelperClass-MergeFiles-MergeFiles.java" >}}
