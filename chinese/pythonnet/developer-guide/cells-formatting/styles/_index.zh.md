---
title: 为单元格获取和设置样式
description: 了解在Aspose.Cells for Python via .NET中执行数据格式化与样式设计的方法，包括文本格式化、数字格式化、日期格式化和其他样式选择。我们的指南将帮助你创建具有吸引力样式的专业电子表格。
keywords: Aspose.Cells for Python via .NET，数据格式化，样式设计，文本格式化，数字格式化，日期格式化，样式选项，电子表格，吸引人的样式，专业外观。
linktitle: 样式
type: docs
weight: 50
url: /zh/python-net/styling-and-data-formatting/
---

{{% alert color="primary" %}} 

Aspose.Cells for Python via .NET引入了两种新的单元格格式化方法：Cell.GetStyle 和 Cell.SetStyle。本文将介绍这两种方法，帮助你判断哪种技巧更适合你。

{{% /alert %}} 

## **格式化单元格**
有两种格式化单元格的方式，如下所示。

### **使用 GetStyle()**
通过下面的代码片段，在格式化单元格时为每个单元格初始化一个 Style 对象。如果要格式化很多单元格，会消耗大量内存，因为 Style 对象是一个大对象。这些 Style 对象直到调用 Workbook.Save 方法时才会被释放。


**Python**

{{< highlight python >}}

cell.get_style().font.is_bold = True

{{< /highlight >}}

### **使用 SetStyle()**
第一种方法简单直接，为什么我们还添加了第二种方法？

我们添加了第二种方法以优化内存使用。使用 Cell.GetStyle 方法检索 Style 对象后，修改它并使用 Cell.SetStyle 方法将其设置回该单元格。当不再引用该 Style 对象时，它将不会被保留，.NET GC 会对其进行回收。

调用 Cell.SetStyle 方法时，不会为每个单元格保存 Style 对象。相反，我们将该 Style 对象与内部的 Style 对象池进行比较，查看是否可以重用。每个 Workbook 对象仅保留与现有对象有所不同的 Style 对象。这意味着每个 Excel 文件仅保留了数百个 Style 对象，而不是数千个。对于每个单元格，仅会保留对 Style 对象池的索引。



**Python**

{{< highlight python >}}

style = cell.get_style()
style.font.is_bold = True
cell.set_style(style)

{{< /highlight >}}

## **高级主题**
- [使用CellsFactory类创建Style对象](/cells/zh/python-net/create-style-object-using-cellsfactory-class/)
- [修改现有样式](/cells/zh/python-net/modify-an-existing-style/)
- [重用样式对象](/cells/zh/python-net/reusing-style-objects/)
- [使用内置样式](/cells/zh/python-net/using-built-in-styles/)


{{< app/cells/assistant language="python-net" >}}
