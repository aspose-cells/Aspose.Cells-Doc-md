---
title: 通过 C++ 在 Golang 中获取和设置单元格样式
linktitle: 样式
type: docs
weight: 50
url: /zh/go-cpp/styling-and-data-formatting/
description: 了解如何在 Aspose.Cells for C++ 中进行数据格式化和样式设置，包括文本格式、数字格式、日期格式及其他样式选项。我们的指南将帮助您创建专业外观的电子表格，具有吸引力的格式。
keywords: Aspose.Cells for C++，数据格式化，样式，文本格式，数字格式，日期格式，样式选项，电子表格，吸引人的格式，专业外观。
---

{{% alert color="primary" %}}

 Aspose.Cells for C++ 引入了两种新的单元格格式化方法：`Cell.GetStyle` 和 `Cell.SetStyle`。本文探讨了这两种方法，帮助你判断哪种技术更适合你。

{{% /alert %}}

## **格式化单元格**
有两种格式化单元格的方式，如下所示。

### **使用 GetStyle()**
 使用以下代码，为每个单元格格式化时会初始化一个 `Style` 对象。如果格式化大量单元格，会占用大量内存，因为 `Style` 对象是一个大型对象。这些 `Style` 对象在调用 `Workbook.Save` 方法前不会被释放。

**C++**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-Styles.go" >}}
### **使用 SetStyle()**
 第一种方法简单直观，为什么我们又添加了第二种方法？

 我们添加第二种方法是为了优化内存使用。在使用 `Cell.GetStyle` 方法检索 `Style` 对象后，修改它并用 `Cell.SetStyle` 方法将其设置回单元格。这个 `Style` 对象不会被保留，C++ 运行时会在不引用它时回收

 调用 `Cell.SetStyle` 方法时，`Style` 对象不会为每个单元格保存。它会将此对象与内部 `Style` 对象池进行比较，判断是否可以重用。只有与现有对象不同的 `Style` 才会为每个 `Workbook` 保留。这意味着每个Excel文件只有几百个 `Style` 对象，而不是成千上万。每个单元格只保留一个指向 `Style` 对象池的索引。

**C++**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-Styles-1.go" >}}
## ** 高级主题**
- [使用CellsFactory类创建Style对象](/cells/zh/cpp/create-style-object-using-cellsfactory-class/)
- [修改现有样式](/cells/zh/cpp/modify-an-existing-style/)
- [重用样式对象](/cells/zh/cpp/reusing-style-objects/)
- [使用内置样式](/cells/zh/cpp/using-built-in-styles/)
