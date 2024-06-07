---
title: 在处理具有大型数据集的大文件时优化内存使用
type: docs
weight: 180
url: /zh/net/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/
---

{{% alert color="primary" %}}

在构建具有大型数据集的工作簿或读取大型Microsoft Excel文件时，进程将占用的总内存量总是一个问题。有一些措施可以适应挑战。Aspose.Cells提供了一些相关选项和API调用以降低、减少和优化内存使用。此外，它可以帮助进程更高效、运行更快。

使用[**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/net/aspose.cells/memorysetting)选项来优化单元格数据的内存使用，降低总内存成本。在构建大型数据集的单元格时，相对于使用默认设置([**MemorySetting.Normal**](https://reference.aspose.com/cells/net/aspose.cells/memorysetting))，它可以节省一定量的内存。

{{% /alert %}}

## **优化内存**

### **读取大型Excel文件**

以下示例展示了如何以优化模式读取大型Microsoft Excel文件。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-OptimizingMemoryUsage-ReadingLargeExcelFiles-1.cs" >}}

### **写入大型Excel文件**

以下示例展示了如何以优化模式将大型数据集写入工作表。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-OptimizingMemoryUsage-WritingLargeExcelFiles-1.cs" >}}

## **注意**

默认选项[**MemorySetting.Normal**](https://reference.aspose.com/cells/net/aspose.cells/memorysetting)适用于所有版本。对于某些情况，例如构建具有大型单元格数据集的工作簿，选项[**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/net/aspose.cells/memorysetting)可能优化内存使用并降低应用程序的内存成本。然而，在一些特殊情况下，例如以下情况，此选项可能会降低性能。

1. **随机重复访问单元格**：访问单元格集合的最有效顺序是一行一行地逐个访问单元格，然后逐行访问。特别是，如果通过[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)、[**RowCollection**](https://reference.aspose.com/cells/net/aspose.cells/rowcollection)和[**Row**](https://reference.aspose.com/cells/net/aspose.cells/row)获取的Enumerator访问行/单元格，性能将通过[**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/net/aspose.cells/memorysetting)最大化。
1. **插入和删除单元格和行**：请注意，如果有大量插入/删除操作针对单元格/行，与*Normal*模式相比，对于*MemoryPreference*模式会明显降低性能。
1. **操作不同的单元格类型**：如果大多数单元格包含字符串值或公式，则内存成本与*Normal*模式相同，但如果有大量空单元格，或单元格值是数值、布尔值等，[**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/net/aspose.cells/memorysetting)选项将提供更好的性能。
