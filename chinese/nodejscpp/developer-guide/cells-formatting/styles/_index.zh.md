---
title: 为单元格获取和设置样式
description: 了解如何在Aspose.Cells for Node.js via C++中进行数据格式化和样式设置，包括文本格式化、数字格式化、日期格式化以及其他样式选项。我们的指南将帮助你创建专业且具有吸引力的电子表格。
keywords: Aspose.Cells for Node.js via C++，数据格式化，样式，文本格式化，数字格式化，日期格式化，样式选项，电子表格，吸引人的格式，专业外观。
linktitle: 样式
type: docs
weight: 50
url: /zh/nodejs-cpp/styling-and-data-formatting/
---

{{% alert color="primary" %}} 

Aspose.Cells for Node.js via C++引入了两种新的单元格格式化方法：Cell.getStyle和Cell.setStyle。本文将介绍这两种方法，帮助你判断哪种技术最适合你。

{{% /alert %}} 
## **格式化单元格**
有两种格式化单元格的方式，如下所示。
### **使用getStyle()**
使用以下代码，为每个单元格格式化时会初始化一个Style对象。如果要格式化很多单元格，将会消耗大量内存，因为Style对象较大。这些Style对象在调用Workbook.save方法之前不会被释放。

**JavaScript**

{{< highlight javascript >}}
cell.getStyle().getFont().setIsBold(true);
{{< /highlight >}}
### **使用setStyle()**
第一种方法简单直接，为什么我们还添加了第二种方法？

我们增加了第二种优化内存的方法。在使用Cell.getStyle方法检索Style对象后，修改它，并使用Cell.setStyle方法将其设置回单元格。这个Style对象不会被保留，当不再被引用时，JavaScript的垃圾收集器会自动回收它。

调用Cell.setStyle方法时，Style对象不会为每个单元格单独保存，而是与内部的Style对象池进行比较，判断是否可以重用。只有与已有不同的Style对象才会被保存到工作簿中。这意味着每个Excel文件只有几百个Style对象，而不是数千个。每个单元格只保存一个指向Style对象池的索引。

**JavaScript**

{{< highlight javascript >}}
let style = cell.getStyle();

style.getFont().setIsBold(true);

cell.setStyle(style);
{{< /highlight >}}

## **高级主题**
- [使用CellsFactory类创建Style对象](/cells/zh/nodejs-cpp/create-style-object-using-cellsfactory-class/)
- [修改现有样式](/cells/zh/nodejs-cpp/modify-an-existing-style/)
- [重用样式对象](/cells/zh/nodejs-cpp/reusing-style-objects/)
- [使用内置样式](/cells/zh/nodejs-cpp/using-built-in-styles/)

