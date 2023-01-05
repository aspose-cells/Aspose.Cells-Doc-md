---
title: 合并文件
type: docs
weight: 20
url: /zh/net/merge-files/
---
## **介绍**

Aspose.Cells 提供了不同的文件合并方式。对于包含数据、格式和公式的简单文件，[**工作簿.Combine()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/combine)方法可用于组合多个工作簿，并且[**工作表.Copy()**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/copy/index)方法可用于将工作表复制到新工作簿中。这些方法易于使用且有效，但是如果您有很多文件要合并，您可能会发现它们会占用大量系统资源。为避免这种情况，请使用[**CellsHelper.MergeFiles**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/methods/mergefiles)静态方法，一种合并多个文件的更有效方法。

## **使用 Aspose.Cells 合并文件**

以下示例代码说明了如何使用[**CellsHelper.MergeFiles**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/methods/mergefiles)方法。它需要两个简单但很大的文件，Book1.xls 和 Book2.xls。这些文件仅包含格式化数据和公式。

{{% alert color="primary" %}}

这[**CellsHelper.MergeFiles**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/methods/mergefiles)方法仅支持合并数据、样式、格式和公式。使用此方法可能无法合并图表、图片、评论或其他对象等对象。此外，缓存文件用于存储进程的临时数据。

{{% /alert %}}

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-CellsHelperClass-MergeFiles-1.cs" >}}
