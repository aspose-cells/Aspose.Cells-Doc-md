---
title: 合并文件
type: docs
weight: 20
url: /zh/net/merge-files/
---

## **介绍**

Aspose.Cells提供了不同的文件合并方式。对于带有数据、格式和公式的简单文件，可以使用[**Workbook.Combine()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/combine)方法合并多个工作簿，并可以使用[**Worksheet.Copy()**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/copy/index)方法将工作表复制到新工作簿中。这些方法简单易用，但是如果要合并大量文件，可能会消耗大量系统资源。为避免这种情况，请使用更高效的[**CellsHelper.MergeFiles**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/methods/mergefiles)静态方法来合并多个文件。

## **使用Aspose.Cells合并文件**

以下示例代码演示了如何使用[**CellsHelper.MergeFiles**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/methods/mergefiles)方法合并大文件。它使用两个简单但大型的文件，Book1.xls和Book2.xls。这些文件仅包含格式化数据和公式。

{{% alert color="primary" %}}

[**CellsHelper.MergeFiles**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/methods/mergefiles)方法仅支持合并数据、样式、格式和公式。像图表、图片、批注或其他对象之类的对象可能无法使用此方法进行合并。此外，用于存储过程中间数据的缓存文件。

{{% /alert %}}

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-CellsHelperClass-MergeFiles-1.cs" >}}
