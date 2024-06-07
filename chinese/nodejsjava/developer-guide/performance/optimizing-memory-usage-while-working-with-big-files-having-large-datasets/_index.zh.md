---
title: 在处理具有大型数据集的大文件时优化内存使用
type: docs
weight: 110
url: /zh/nodejs-java/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/
---

{{% alert color="primary" %}}

当构建具有大数据集的工作簿或读取大型 Microsoft Excel 文件时，进程将占用的总RAM量始终是一个令人担忧的问题。有一些措施可以适应这个挑战。Aspose.Cells提供了一些相关选项和API调用来降低、减少和优化内存使用。此外，它可以帮助进程更高效地工作并运行得更快。

使用[**MemorySetting.MEMORY_PREFERENCE**](https://reference.aspose.com/cells/java/com.aspose.cells/memorysetting#MEMORY_PREFERENCE)选项来优化单元格数据的内存使用，减少整体内存成本。在构建大数据集以供单元格使用时，与使用默认设置[**MemorySetting.NORMAL**](https://reference.aspose.com/cells/java/com.aspose.cells/memorysetting#NORMAL)相比，它可以节省一定量的内存。

{{% /alert %}}

## **优化内存**

以下示例显示如何在Aspose.Cells for Node.js via Java中使用大数据时优化内存使用。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-nodejs-optimize-memory-usage-while-working-with-large-data.java" >}}

## **注意**

在所有版本中都应用了默认选项[**MemorySetting.NORMAL**](https://reference.aspose.com/cells/java/com.aspose.cells/memorysetting#NORMAL)。在某些情况下，例如为单元格构建具有大数据集的工作簿，选项[**MemorySetting.MEMORY_PREFERENCE**](https://reference.aspose.com/cells/java/com.aspose.cells/memorysetting#MEMORY_PREFERENCE)可能会优化内存使用，并减少应用程序的内存成本。但是，该选项可能会在某些特殊情况下降低性能，例如...

1. **随机重复访问单元格**：访问单元格集合的最有效顺序是一行一行地逐个访问单元格，然后逐行访问。特别是，如果通过[**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)、[**RowCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/RowCollection)和[**Row**](https://reference.aspose.com/cells/java/com.aspose.cells/Row)获取的Enumerator访问行/单元格，性能将通过[**MemorySetting.MEMORY_PREFERENCE**](https://reference.aspose.com/cells/java/com.aspose.cells/memorysetting#MEMORY_PREFERENCE)最大化。
1. **插入和删除单元格和行**：请注意，如果有大量插入/删除单元格/行的操作，与[**MemorySetting.NORMAL**](https://reference.aspose.com/cells/java/com.aspose.cells/memorysetting#NORMAL)模式相比，对[**MemorySetting.MEMORY_PREFERENCE**](https://reference.aspose.com/cells/java/com.aspose.cells/memorysetting#MEMORY_PREFERENCE)模式的性能降低明显。
1. **操作不同的单元格类型**：如果大多数单元格包含字符串值或公式，那么内存成本与[**MemorySetting.NORMAL**](https://reference.aspose.com/cells/java/com.aspose.cells/memorysetting#NORMAL)模式相同，但是如果有大量空单元格，或者单元格值是数字、布尔值等，[**MemorySetting.MEMORY_PREFERENCE**](https://reference.aspose.com/cells/java/com.aspose.cells/memorysetting#MEMORY_PREFERENCE)选项将提供更好的性能。

