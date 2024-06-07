---
title: 合并文件
type: docs
weight: 10
url: /zh/java/merge-files/
---

## **介绍**

Aspose.Cells提供不同的方式来合并文件。对于包含数据、格式和公式的简单文件，可以使用[**Workbook.combine()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#combine(com.aspose.cells.Workbook)方法来合并多个工作簿，并且可以使用[**Worksheet.copy(**)](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#copy(com.aspose.cells.Worksheet))方法将工作表复制到新工作簿中。这些方法易于使用且有效，但如果您有很多要合并的文件，可能会发现它们需要大量系统资源。为了避免这种情况，使用CellsHelper.mergeFiles静态方法，这是一种更高效的合并多个文件的方式。

## **使用Aspose.Cells合并文件**

以下示例代码说明了如何使用CellsHelper.mergeFiles方法合并大型文件。它合并了两个简单但大型的文件MyBook1.xls和MyBook2.xls。这些文件仅包含格式化数据和公式。

{{% alert color="primary" %}}

CellsHelper.mergeFiles方法仅支持合并数据、样式、格式和公式。图表、图片、批注或其他对象等对象可能无法使用此方法合并。此外，该方法使用缓存文件来存储过程的临时数据。

{{% /alert %}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-CellsHelperClass-MergeFiles-MergeFiles.java" >}}
