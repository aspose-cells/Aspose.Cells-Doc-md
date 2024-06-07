---
title: 获取和设置单元格样式
description: 了解如何在Aspose.Cells for .NET中执行数据格式化和样式设置，包括文本格式化、数字格式化、日期格式化和其他样式选项。 我们的指南将帮助您创建外观专业的电子表格，并具有吸引人的格式。
keywords: 在Aspose.Cells for .NET中，数据格式化，样式设置，文本格式化，数字格式化，日期格式化，样式选项，电子表格，吸引人的格式，外观专业。
linktitle: Styles
type: docs
weight: 50
url: /zh/net/styling-and-data-formatting/
---

{{% alert color="primary" %}} 

Aspose.Cells for .NET 4.4.2引入了两种新的格式化单元格的方法: Cell.GetStyle 和 Cell.SetStyle。 本文探讨了Cell.GetStyle/SetStyle方法，帮助您判断哪种技术最适合您。

{{% /alert %}} 
## **格式化单元格**
有两种格式化单元格的方法，如下所示。
### **使用GetStyle()**
使用下面的代码片段，当格式化单元格时为每个单元格初始化一个Style对象。 如果正在格式化大量单元格，则会消耗大量内存，因为Style对象是一个庞大的对象。 直到调用Workbook.Save方法时，这些Style对象都不会被释放。



**C#**

{{< highlight csharp >}}

cell.GetStyle().Font.IsBold = true;



{{< /highlight >}}
### **使用SetStyle()**
第一种方法简单明了，那么为什么我们还添加了第二种方法呢？

我们添加第二种方法是为了优化内存使用。 使用Cell.GetStyle方法检索Style对象、修改它并使用Cell.SetStyle方法将其设置回此单元格。 当不再引用时，此Style对象不会保留，并且.NET GC将对其进行回收。

调用Cell.SetStyle方法时，并未为每个单元格保存Style对象。 相反，我们将此Style对象与内部Style对象池进行比较，以查看是否可以重用。 仅将与现有对象不同的Style对象保存为每个Workbook对象。 这意味着每个Excel文件只有几百个Style对象，而不是数千个。 对于每个单元格，仅保留到Style对象池的索引。



**C#**

{{< highlight csharp >}}

Style style = cell.GetStyle();

style.Font.IsBold = true;

cell.SetStyle(style);
{{< /highlight >}}

## **高级主题**
- [使用 CellsFactory 类创建 Style 对象](/cells/zh/net/create-style-object-using-cellsfactory-class/)
- [修改现有样式](/cells/zh/net/modify-an-existing-style/)
- [重用样式对象](/cells/zh/net/reusing-style-objects/)
- [使用内置样式](/cells/zh/net/using-built-in-styles/)


