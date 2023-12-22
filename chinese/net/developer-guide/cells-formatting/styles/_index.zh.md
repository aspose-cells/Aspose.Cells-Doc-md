---
title: 获取和设置单元格的样式
description: 了解如何在 Aspose.Cells for .NET 中执行数据格式化和样式设置，包括文本格式设置、数字格式设置、日期格式设置和其他样式选项。我们的指南将帮助您创建具有美观格式的专业电子表格。
keywords: Aspose.Cells for .NET, data formatting, styling, text formatting, number formatting, date formatting, styling options, spreadsheets, attractive formatting, professional-looking.
linktitle: 风格
type: docs
weight: 50
url: /zh/net/styling-and-data-formatting/
---
{{% alert color="primary" %}} 

Aspose.Cells for .NET 4.4.2 引入了两种格式化单元格的新方法：Cell.GetStyle 和 Cell.SetStyle。本文研究 Cell.GetStyle/SetStyle 方法，以帮助您判断哪种技术最适合您。

{{% /alert %}} 
##  **格式化Cells**
有两种设置单元格格式的方法，如下所示。
###  **使用 GetStyle()**
使用以下代码，在格式化每个单元格时为每个单元格启动一个 Style 对象。如果要格式化很多单元格，则会消耗大量内存，因为 Style 对象是一个大对象。在调用 Workbook.Save 方法之前，这些 Style 对象不会被释放。



**C#**

{{< highlight "csharp" >}}

cell.GetStyle().Font.IsBold = true;



{{< /highlight >}}
###  **使用 SetStyle()**
第一种方法简单直接，那么为什么我们要添加第二种方法呢？

我们添加了第二种方法来优化内存使用。使用 Cell.GetStyle 方法检索 Style 对象后，修改它并使用 Cell.SetStyle 方法将其设置回此单元格。此 Style 对象不会被保留，并且 .NET GC 在未引用它时会收集它。

调用 Cell.SetStyle 方法时，不会为每个单元格保存 Style 对象。相反，我们将此 Style 对象与内部 Style 对象池进行比较，看看它是否可以重用。对于每个 Workbook 对象，仅保留与现有样式对象不同的 Style 对象。这意味着每个 Excel 文件只有数百个 Style 对象，而不是数千个。对于每个单元格，仅保留样式对象池的索引。



**C#**

{{< highlight "csharp" >}}

Style style = cell.GetStyle();

style.Font.IsBold = true;

cell.SetStyle(style);
{{< /highlight >}}

##  **高级主题**
- [使用 CellsFactory 类创建 Style 对象](/cells/zh/net/create-style-object-using-cellsfactory-class/)
- [修改现有样式](/cells/zh/net/modify-an-existing-style/)
- [重用样式对象](/cells/zh/net/reusing-style-objects/)
- [使用内置样式](/cells/zh/net/using-built-in-styles/)


