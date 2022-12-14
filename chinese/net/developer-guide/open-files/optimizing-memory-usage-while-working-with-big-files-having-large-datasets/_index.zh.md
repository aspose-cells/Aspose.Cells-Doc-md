---
title: 在处理具有大型数据集的大文件时优化内存使用
type: docs
weight: 180
url: /zh/net/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/
---
{{% alert color="primary" %}}

在构建包含大型数据集的工作簿或读取大型 Microsoft Excel 文件时，进程占用的 RAM 总量始终是一个问题。可以采取一些措施来应对挑战。 Aspose.Cells 提供了一些相关选项和 API 调用以降低、减少和优化内存使用。此外，它还可以帮助流程更有效地工作并运行得更快。

使用[**内存设置.MemoryPreference**](https://reference.aspose.com/cells/net/aspose.cells/memorysetting)优化单元格数据的内存使用并降低整体内存成本的选项。在为单元格构建大型数据集时，与使用默认设置相比，它可以节省一定的内存（[**内存设置.正常**](https://reference.aspose.com/cells/net/aspose.cells/memorysetting)).

{{% /alert %}}

## **优化内存**

### **读取大型 Excel 文件**

以下示例显示如何在优化模式下读取大型 Microsoft Excel 文件。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-OptimizingMemoryUsage-ReadingLargeExcelFiles-1.cs" >}}

### **编写大型 Excel 文件**

以下示例显示如何以优化模式将大型数据集写入工作表。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-OptimizingMemoryUsage-WritingLargeExcelFiles-1.cs" >}}

## **警告**

默认选项，[**内存设置.正常**](https://reference.aspose.com/cells/net/aspose.cells/memorysetting)适用于所有版本。对于某些情况，例如构建包含大量单元格数据集的工作簿，[**内存设置.MemoryPreference**](https://reference.aspose.com/cells/net/aspose.cells/memorysetting)选项可以优化内存使用并降低应用程序的内存成本。但是，此选项可能会在某些特殊情况下降低性能，例如以下。

1. **随机重复访问Cells** ：访问单元格集合的最有效顺序是在一行中逐个单元格，然后逐行。特别是，如果您通过从中获取的枚举器访问行/单元格[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells), [**行集合**](https://reference.aspose.com/cells/net/aspose.cells/rowcollection)和[**排**](https://reference.aspose.com/cells/net/aspose.cells/row)，性能将最大化[**内存设置.MemoryPreference**](https://reference.aspose.com/cells/net/aspose.cells/memorysetting).
1. **插入和删除 Cells & 行** 请注意，如果对 Cells/Rows 有大量的插入/删除操作，性能下降将是显着的*内存偏好*模式相比*普通的*模式。
1. **操作不同的 Cell 类型**：如果大多数单元格包含字符串值或公式，则内存成本将与*普通的*模式，但如果有很多空单元格，或者单元格值为数字、布尔值等，则[**内存设置.MemoryPreference**](https://reference.aspose.com/cells/net/aspose.cells/memorysetting)选项将提供更好的性能。
