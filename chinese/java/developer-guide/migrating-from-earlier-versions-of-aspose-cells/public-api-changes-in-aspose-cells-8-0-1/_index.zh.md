---
title: Aspose.Cells 8.0.1 中的公共 API 更改
type: docs
weight: 30
url: /zh/java/public-api-changes-in-aspose-cells-8-0-1/
---

{{% alert color="primary" %}} 

本页面列出了在 Aspose.Cells 8.0.1 中引入的公共 API 更改。不仅包括新的和已过时的公共方法，还包括任何可能影响现有代码的幕后行为更改的描述。特别重要的是，介绍了可能被视为退化并修改了现有行为的任何行为，这里都有记录。

{{% /alert %}} 
## **MemorySetting 属性已添加到 Cells 类中**
Cells 类已公开 setMemorySetting 和 getMemorySetting 方法，可用于优化单元格数据的内存使用，并因此减少整体内存成本。以下示例显示了如何以优化模式向工作表中写入大量数据。

**Java**

{{< highlight csharp >}}

 //Instantiate a new Workbook

Workbook book = new Workbook();

//Set the memory preferences

book.getSettings().setMemorySetting(MemorySetting.MEMORY_PREFERENCE);

//To change the memory setting of existing sheets, please change memory setting for them manually:

Cells cells = book.getWorksheets().get(0).getCells();

cells.setMemorySetting(MemorySetting.MEMORY_PREFERENCE);

//Input large dataset into the cells of the worksheet.

//Your code goes here

{{< /highlight >}}

{{% alert color="primary" %}} 

内存设置将不会自动适用于工作簿自动创建的默认工作表。为了更改现有工作表的内存设置，请在执行任何数据操作之前手动应用内存设置。 

{{% /alert %}} {{% alert color="primary" %}} 

请查看有关[处理大数据集时优化内存](/cells/zh/java/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/)的详细文章。

{{% /alert %}}
