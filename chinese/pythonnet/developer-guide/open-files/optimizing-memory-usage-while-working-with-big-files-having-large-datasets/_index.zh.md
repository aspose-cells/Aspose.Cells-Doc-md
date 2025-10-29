---
title: 在处理拥有大型数据集的大文件时优化内存使用
type: docs
weight: 180
url: /zh/python-net/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/
---

{{% alert color="primary" %}}

在构建大型数据集的工作簿或读取大型Microsoft Excel文件时，处理所需的总内存量始终是一个问题。可以采取一些措施应对挑战。Aspose.Cells for Python via .NET 提供了一些相关选项和API调用，以降低、减少和优化内存使用，还可以帮助流程更高效、更快运行。

使用[**MemorySetting.MEMORY_PREFERENCE**](https://reference.aspose.com/cells/python-net/aspose.cells/memorysetting)选项来优化单元格数据的内存使用并降低整体内存成本。在构建大型数据集时，相较于使用默认设置([**MemorySetting.NORMAL**](https://reference.aspose.com/cells/python-net/aspose.cells/memorysetting))，它可以节省一定量的内存。

{{% /alert %}}

## **优化内存**

### **读取大型Excel文件**

以下示例展示了如何以优化模式读取大型Microsoft Excel文件。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Open-files-OptimizingMemoryUsage-ReadingLargeExcelFiles-1.py" >}}

### **写入大型Excel文件**

以下示例展示了如何以优化模式将大型数据集写入工作表。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Open-files-OptimizingMemoryUsage-WritingLargeExcelFiles-1.py" >}}

## **注意**

默认选项[**MemorySetting.NORMAL**](https://reference.aspose.com/cells/python-net/aspose.cells/memorysetting)适用于所有版本。对于一些特殊情况，比如构建具有大型单元格数据集的工作簿，[**MemorySetting.MEMORY_PREFERENCE**](https://reference.aspose.com/cells/python-net/aspose.cells/memorysetting)选项可以优化内存使用并降低应用程序的内存成本。然而，该选项在某些特殊情况下可能会降低性能，例如下面所述。

1. **随机和重复访问单元格**：访问单元格集合最有效的顺序是一行一行地逐个访问单元格，尤其是如果通过[**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells)、[**RowCollection**](https://reference.aspose.com/cells/python-net/aspose.cells/rowcollection)和[**Row**](https://reference.aspose.com/cells/python-net/aspose.cells/row)获得的枚举器来访问行/单元格，则使用[**MemorySetting.MEMORY_PREFERENCE**](https://reference.aspose.com/cells/python-net/aspose.cells/memorysetting)将最大化性能。
1. **插入和删除单元格和行**：请注意，如果大量进行单元格/行的插入/删除操作，与*Normal*模式相比，*MemoryPreference*模式的性能将明显下降。
1. **操作不同的单元格类型**：如果大部分单元格包含字符串值或公式，那么内存成本将与*Normal*模式相同；但如果有大量的空单元格，或单元格值为数字、布尔值等，[**MemorySetting.MEMORY_PREFERENCE**](https://reference.aspose.com/cells/python-net/aspose.cells/memorysetting)选项将提供更好的性能。

{{< app/cells/assistant language="python-net" >}}
