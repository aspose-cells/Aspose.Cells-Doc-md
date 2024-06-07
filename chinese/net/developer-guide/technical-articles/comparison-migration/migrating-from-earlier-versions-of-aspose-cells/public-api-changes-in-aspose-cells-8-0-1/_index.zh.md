---
title: Aspose.Cells 8.0.1 中的公共 API 更改
type: docs
weight: 20
url: /zh/net/public-api-changes-in-aspose-cells-8-0-1/
---

{{% alert color="primary" %}} 

本页面列出了在 Aspose.Cells 8.0.1 中引入的公共 API 更改。不仅包括新的和已过时的公共方法，还包括任何可能影响现有代码的幕后行为更改的描述。特别重要的是，介绍了可能被视为退化并修改了现有行为的任何行为，这里都有记录。

{{% /alert %}} 
## **向 Cells 类中添加了 MemorySetting 属性**
Cells 类已公开了 MemorySetting 属性，可用于优化单元格数据的内存使用，从而降低整体内存成本。以下示例显示如何以优化模式向工作表写入大量数据。

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

默认情况下，内存设置不会自动应用于 Workbook 对象自动创建的默认工作表。为了更改现有工作表的内存设置，请在执行任何数据操作之前手动应用内存设置。

{{% alert color="primary" %}} 

请查阅有关[在处理大数据集时优化内存的详细文章](/cells/zh/net/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/)

{{% /alert %}}
