---
title: 合并文件
type: docs
weight: 10
url: /zh/java/merge-files/
---
## **介绍**

Aspose.Cells 提供了不同的文件合并方式。对于包含数据、格式和公式的简单文件，[**工作簿.combine()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#combine(com.aspose.cells.Workbook) 方法可用于组合多个工作簿，并且[**工作表.copy(**)](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#copy(com.aspose.cells.Worksheet)) 方法可用于将工作表复制到新工作簿中。这些方法易于使用且有效，但是如果您有很多文件要合并，您可能会发现它们会占用大量系统资源。为避免这种情况，请使用 CellsHelper.mergeFiles 静态方法，这是一种更有效的合并多个文件的方法。

## **使用 Aspose.Cells 合并文件**

以下示例代码说明了如何使用 CellsHelper.mergeFiles 方法合并大型文件。它需要两个简单但很大的文件，MyBook1.xls 和 MyBook2.xls。这些文件仅包含格式化数据和公式。

{{% alert color="primary" %}}

CellsHelper.mergeFiles 方法仅支持合并数据、样式、格式和公式。使用此方法可能无法合并图表、图片、评论或其他对象等对象。此外，缓存文件用于存储进程的临时数据。

{{% /alert %}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-CellsHelperClass-MergeFiles-MergeFiles.java" >}}
