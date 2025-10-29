---
title: 用Golang通过C++获取工作表中的最大范围
linktitle: 获取工作表中的最大范围
type: docs
weight: 360
url: /zh/go-cpp/get-max-range-in-a-worksheet/
description: 本文介绍了如何使用Aspose.Cells for C++库获取Excel文件的最大范围、最大数据范围和最大显示范围。
---

{{% alert color="primary" %}} 

在从工作表读取数据时，我们需要知道最大的区域。

在从工作表复制所有数据时，我们需要知道最大的区域。

在导出指定区域为HTML和PDF时，我们需要知道最大区域。

Aspose.Cells for C++提供了多种方法来查找工作表中的最大范围。 

{{% /alert %}} 

## **获取最大范围**
在Aspose.Cells中，如果初始化了[**Row**](https://reference.aspose.com/cells/go-cpp/row/)和[**Column**](https://reference.aspose.com/cells/cpp/aspose.cells/column/)对象，这些行和列将被计入最大区域，即使空行或空列没有数据。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-GetMaxRange.go" >}}
## **获取最大数据范围**
在大多数情况下，我们只需要获取包含所有数据的所有范围，即使范围外的空单元格被格式化。
以及有关形状、表格和数据透视表的设置将被忽略。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-GetMaxRange-1.go" >}}
## **获取最大显示范围**
当我们将工作表中的所有数据导出到 HTML、PDF 或图像时，需要获取一个包含所有可见对象的区域，包括数据、样式、图形、表格和数据透视表。
以下代码演示如何将最大显示范围渲染为HTML：

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-GetMaxRange-2.go" >}}
这是 [源 Excel 文件](Book1.xlsx)。
