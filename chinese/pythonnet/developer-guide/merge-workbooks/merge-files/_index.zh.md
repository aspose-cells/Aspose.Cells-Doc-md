---
title: 合并文件
type: docs
weight: 20
url: /zh/python-net/merge-files/
---

## **介绍**

Aspose.Cells for Python via .NET 提供多种合并文件的方法。对于包含数据、格式和公式的简单文件，可以使用 [**Workbook.combine()**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/combine) 方法合并多个工作簿，而 [**Worksheet.copy()**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/copy) 方法可以将工作表复制到新工作簿中。这些方法使用简单且有效，但如果需要合并大量文件，可能会耗费大量系统资源。为避免此问题，可以使用 [**CellsHelper.merge_files**](https://reference.aspose.com/cells/python-net/aspose.cells/cellshelper/merge_files) 静态方法，这是一种更高效的合并多个文件的方式。

## **使用 Aspose.Cells for Python via .NET 合并文件**

以下示例代码演示了如何使用[**CellsHelper.merge_files**](https://reference.aspose.com/cells/python-net/aspose.cells/cellshelper/merge_files)方法合并大型文件。它使用两个简单但大型的文件，Book1.xls和Book2.xls。这些文件仅包含格式化的数据和公式。

{{% alert color="primary" %}}

[**CellsHelper.merge_files**](https://reference.aspose.com/cells/python-net/aspose.cells/cellshelper/merge_files)方法仅支持合并数据、样式、格式和公式。使用此方法可能无法合并图表、图片、批注或其他对象。此外，该方法使用一个缓存文件来存储临时数据以进行处理。

{{% /alert %}}

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Merge-Workbooks-CellsHelperClass-MergeFiles-1.py" >}}

