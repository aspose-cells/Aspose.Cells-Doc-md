---
title: 为单元格获取和设置样式
description: 发现如何在 Aspose.Cells for .NET 中执行数据格式设置和样式设置，包括文本格式设置，数字格式设置，日期格式设置以及其他样式选项。我们的指南将帮助您创建具有吸引人格式设置的专业电子表格。
keywords: Aspose.Cells for .NET，数据格式设置，样式设置，文本格式设置，数字格式设置，日期格式设置，样式选项，电子表格，吸引人格式设置，专业外观。
linktitle: 样式
type: docs
weight: 50
url: /zh/net/styling-and-data-formatting/
---

{{% alert color="primary" %}} 

Aspose.Cells for .NET 4.4.2 版本引入了两种格式化单元格的新方法：Cell.GetStyle 和 Cell.SetStyle。本文探讨了 Cell.GetStyle/SetStyle 方法，帮助您判断哪种技术最适合您。

{{% /alert %}} 
## **格式化单元格**
有两种格式化单元格的方式，如下所示。
### **使用 GetStyle()**
通过下面的代码片段，在格式化单元格时为每个单元格初始化一个 Style 对象。如果要格式化很多单元格，会消耗大量内存，因为 Style 对象是一个大对象。这些 Style 对象直到调用 Workbook.Save 方法时才会被释放。



**C#**

{{< highlight csharp >}}

cell.GetStyle().Font.IsBold = true;



{{< /highlight >}}
### **使用 SetStyle()**
第一种方法简单直接，为什么我们还添加了第二种方法？

我们添加了第二种方法以优化内存使用。使用 Cell.GetStyle 方法检索 Style 对象后，修改它并使用 Cell.SetStyle 方法将其设置回该单元格。当不再引用该 Style 对象时，它将不会被保留，.NET GC 会对其进行回收。

调用 Cell.SetStyle 方法时，不会为每个单元格保存 Style 对象。相反，我们将该 Style 对象与内部的 Style 对象池进行比较，查看是否可以重用。每个 Workbook 对象仅保留与现有对象有所不同的 Style 对象。这意味着每个 Excel 文件仅保留了数百个 Style 对象，而不是数千个。对于每个单元格，仅会保留对 Style 对象池的索引。



**C#**

{{< highlight csharp >}}

Style style = cell.GetStyle();

style.Font.IsBold = true;

cell.SetStyle(style);
{{< /highlight >}}

## **高级主题**
- [使用CellsFactory类创建Style对象](/cells/zh/net/create-style-object-using-cellsfactory-class/)
- [修改现有样式](/cells/zh/net/modify-an-existing-style/)
- [重用样式对象](/cells/zh/net/reusing-style-objects/)
- [使用内置样式](/cells/zh/net/using-built-in-styles/)


{{< app/cells/assistant language="csharp" >}}
