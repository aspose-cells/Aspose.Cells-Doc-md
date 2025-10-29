---
title: 为单元格获取和设置样式
description: 了解如何在 Aspose.Cells for JavaScript 通过 C++ 中进行数据格式化和样式设置，包括文本格式化、数字格式化、日期格式化以及其他样式选项。我们的指南将帮助你创建专业且吸引人的电子表格。
keywords: Aspose.Cells for JavaScript 通过 C++，数据格式化，样式设置，文本格式化，数字格式化，日期格式化，样式选项，电子表格，吸引人的格式，专业外观。
linktitle: 样式
type: docs
weight: 50
url: /zh/javascript-cpp/styling-and-data-formatting/
---

{{% alert color="primary" %}} 

Aspose.Cells for JavaScript 通过 C++ 引入了两个新的单元格格式化方法：Cell.style 和 Cell.setStyle。本文将探讨这两种方法，帮助你判断哪种更适合你。

{{% /alert %}} 
## **格式化单元格**
有两种格式化单元格的方式，如下所示。
### **使用样式**
使用以下代码，为每个单元格格式化时会初始化一个Style对象。如果要格式化很多单元格，将会消耗大量内存，因为Style对象较大。这些Style对象在调用Workbook.save方法之前不会被释放。

**JavaScript**

{{< highlight javascript >}}
cell.style.font.isBold = true;
{{< /highlight >}}
### **使用样式**
第一种方法简单直接，为什么我们还添加了第二种方法？

我们添加了第二种方法以优化内存使用。在使用 Cell.style 属性获取 Style 对象后，可以修改它并通过 Cell.style 赋回到该单元格。这个 Style 对象不会被保存，当不再引用时，JavaScript 的垃圾收集器会将其回收。

在为单元格赋值 Cell.style 属性时，Style 对象不会为每个单元格单独保存。相反，我们会将此 Style 对象与内部的 Style 对象池进行比较，判断是否可以重用。只有与现有的 Style 不同的对象才会被保留在每个工作簿中。这意味着每个 Excel 文件中只有几百个 Style 对象，而不是数千个。每个单元格仅保留一个 Style 对象池的索引。

**JavaScript**

{{< highlight javascript >}}
let style = cell.style;

style.font.isBold = true;

cell.style = style;
{{< /highlight >}}

## **高级主题**
- [使用CellsFactory类创建Style对象](/cells/zh/javascript-cpp/create-style-object-using-cellsfactory-class/)
- [修改现有样式](/cells/zh/javascript-cpp/modify-an-existing-style/)
- [重用样式对象](/cells/zh/javascript-cpp/reusing-style-objects/)
- [使用内置样式](/cells/zh/javascript-cpp/using-built-in-styles/)
