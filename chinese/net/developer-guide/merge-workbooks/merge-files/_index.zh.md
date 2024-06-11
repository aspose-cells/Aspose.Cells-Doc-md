---
title: 合并文件
type: docs
weight: 20
url: /zh/net/merge-files/
---

## **介绍**

Aspose.Cells提供了不同的方式来合并文件。对于简单的包含数据、格式和公式的文件，可以使用[**Workbook.Combine()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/combine)方法来合并多个工作簿，使用[**Worksheet.Copy()**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/copy/index)方法将工作表复制到新工作簿。这些方法使用简单且有效，但如果要合并大量文件，可能需要大量系统资源。为了避免这种情况，使用更高效的方法[**CellsHelper.MergeFiles**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/methods/mergefiles)静态方法来合并多个文件。

## **使用Aspose.Cells合并文件**

以下示例代码演示了如何使用[**CellsHelper.MergeFiles**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/methods/mergefiles)方法合并大型文件。它使用两个简单但大型的文件，Book1.xls和Book2.xls。这些文件仅包含格式化的数据和公式。

{{% alert color="primary" %}}

[**CellsHelper.MergeFiles**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/methods/mergefiles)方法仅支持合并数据、样式、格式和公式。使用此方法可能无法合并图表、图片、批注或其他对象。此外，该方法使用一个缓存文件来存储临时数据以进行处理。

{{% /alert %}}

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-CellsHelperClass-MergeFiles-1.cs" >}}
