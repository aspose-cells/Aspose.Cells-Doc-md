---
title: Aspose.Cells 8.0.1中的公共API变更
type: docs
weight: 30
url: /zh/java/public-api-changes-in-aspose-cells-8-0-1/
---

{{% alert color="primary" %}} 

这些页面列出了Aspose.Cells 8.0.1中引入的公共API变更。它不仅包括新的和已过时的公共方法，还描述了在Aspose.Cells幕后的行为中可能会影响现有代码的任何变化。特别重要的是，这里记录了引入的任何可能被视为回归并修改现有行为的行为。

{{% /alert %}} 
## **向Cells类添加了MemorySetting属性**
Cells类已经公开了setMemorySetting和getMemorySetting方法，用于优化单元格数据的内存使用，并因此减少总体内存开销。下面的示例展示了如何以优化模式将大量数据写入工作表。

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

内存设置不会自动适用于Workbook自动创建的默认工作表。为了更改现有工作表的内存设置，请在执行任何数据操作之前手动应用内存设置。 

{{% /alert %}} {{% alert color="primary" %}} 

请查看详细的文章[在处理大型数据集时优化内存使用](/cells/zh/java/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/)

{{% /alert %}}
