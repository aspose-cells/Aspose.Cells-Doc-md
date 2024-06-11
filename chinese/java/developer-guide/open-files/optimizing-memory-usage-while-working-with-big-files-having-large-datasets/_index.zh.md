---
title: 在处理拥有大型数据集的大文件时优化内存使用
type: docs
weight: 110
url: /zh/java/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/
---

{{% alert color="primary" %}}

在构建具有大型数据集的工作簿或读取大型Microsoft Excel文件时，进程所占用的总RAM是一个关注点。有一些措施可以应对这一挑战。Aspose.Cells提供了一些相关的选项和API调用来降低、减少和优化内存使用。此外，它可以帮助进程更高效地运行并提高速度。

使用[**MemorySetting.MEMORY_PREFERENCE**](https://reference.aspose.com/cells/java/com.aspose.cells/memorysetting#MEMORY_PREFERENCE)选项优化用于单元格数据的内存以减少整体内存成本。在构建大型数据集时，相较于使用默认设置[**MemorySetting.NORMAL**](https://reference.aspose.com/cells/java/com.aspose.cells/memorysetting#NORMAL)，它可以节省一定数量的内存。

{{% /alert %}}

## **优化内存**

### **读取大型Excel文件**

以下示例展示了如何以优化模式读取大型Microsoft Excel文件。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ReadLargeExcelFiles-ReadLargeExcelFiles.java" >}}

### **写入大型Excel文件**

以下示例显示如何在优化模式下将大型数据集写入工作表。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-WritingLargeExcelFiles-WritingLargeExcelFiles.java" >}}

## **注意**

默认选项{0}适用于所有版本。对于某些情况，例如构建包含大型单元格数据集的工作簿，{1}选项可以优化内存使用并降低应用程序的内存成本。然而，在一些特殊情况下，比如：</br>1. **随机和重复访问单元格**: 访问单元格集合的最有效顺序是逐行逐单元格，然后逐行。特别是，如果通过{0}、{1}和{2}获得的枚举器访问行/单元格，性能将通过{3}得到最大化。

1. **随机和重复访问单元格**：访问单元格集合最有效的顺序是一行一行地逐个访问单元格，尤其是如果通过[**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)、[**RowCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/RowCollection)和[**Row**](https://reference.aspose.com/cells/java/com.aspose.cells/Row)获得的枚举器来访问行/单元格，则使用[**MemorySetting.MEMORY_PREFERENCE**](https://reference.aspose.com/cells/java/com.aspose.cells/memorysetting#MEMORY_PREFERENCE)将最大化性能。
1. **插入和删除单元格和行**：请注意，如果有大量的单元格/行插入/删除操作，与[**MemorySetting.MEMORY_PREFERENCE**](https://reference.aspose.com/cells/java/com.aspose.cells/memorysetting#MEMORY_PREFERENCE)模式相比，性能下降将非常明显。
1. **操作不同的单元格类型**: 如果大多数单元格包含字符串值或公式，则内存成本与[**MemorySetting.NORMAL**](https://reference.aspose.com/cells/java/com.aspose.cells/memorysetting#NORMAL)模式相同，但如果存在大量空单元格，或单元格的值是数字、布尔值等，则[**MemorySetting.MEMORY_PREFERENCE**](https://reference.aspose.com/cells/java/com.aspose.cells/memorysetting#MEMORY_PREFERENCE)选项将提供更好的性能。
