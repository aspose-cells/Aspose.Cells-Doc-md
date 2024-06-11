---
title: Aspose.Cells 8.0.1中的公共API变更
type: docs
weight: 20
url: /zh/net/public-api-changes-in-aspose-cells-8-0-1/
---

{{% alert color="primary" %}} 

这些页面列出了Aspose.Cells 8.0.1中引入的公共API变更。它不仅包括新的和已过时的公共方法，还描述了在Aspose.Cells幕后的行为中可能会影响现有代码的任何变化。特别重要的是，这里记录了引入的任何可能被视为回归并修改现有行为的行为。

{{% /alert %}} 
## **在Cells类中添加了MemorySetting属性。**
Cells类已公开MemorySetting属性，可用于优化单元格数据的内存使用，并因此降低整体内存成本。以下示例显示了如何在优化模式下向工作表写入大数据。

**C#**

{{< highlight csharp >}}

 //Instantiate a new Workbook

Workbook book = new Workbook();

//Set the memory preferences

book.Settings.MemorySetting = MemorySetting.MemoryPreference;

//To change the memory setting of existing sheets, please change memory setting for them manually:

Cells cells = book.Worksheets[0].Cells;

cells.MemorySetting = MemorySetting.MemoryPreference;

//Input large dataset into the cells of the worksheet

//Your code goes here

{{< /highlight >}}

默认工作簿对象自动创建的工作表不会自动应用内存设置。为了更改现有工作表的内存设置，请在执行任何数据操作之前手动应用内存设置。

{{% alert color="primary" %}} 

请查看关于[在处理大数据集时优化内存使用](/cells/zh/net/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/)的详细文章

{{% /alert %}}
