---
title: 公共 API Aspose.Cells 8.0.1 的变化
type: docs
weight: 30
url: /zh/java/public-api-changes-in-aspose-cells-8-0-1/
---
{{% alert color="primary" %}} 

这些页面列出了 Aspose.Cells 8.0.1 中引入的公共 API 更改。它不仅包括新的和过时的公共方法，还包括对 Aspose.Cells 中可能影响现有代码的幕后行为的任何更改的描述。引入的任何可被视为回归并修改现有行为的行为都特别重要，并记录在此处。

{{% /alert %}} 
## **MemorySetting 属性添加到 Cells 类**
Cells 类公开了 setMemorySetting 和 getMemorySetting 方法，可用于优化单元格数据的内存使用，从而降低整体内存成本。以下示例显示如何在优化模式下将大数据写入工作表。

**Java**

{{< highlight "csharp" >}}

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

内存设置不适用于工作簿自动创建的默认工作表。为了更改现有工作表的内存设置，请在执行任何数据操作之前手动应用内存设置。

{{% /alert %}} {{% alert color="primary" %}} 

请查看详细文章[在处理大型数据集时优化内存](/cells/zh/java/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/)

{{% /alert %}}
