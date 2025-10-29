---
title: 使用 C++ 和 Golang 格式化数据透视表
linktitle: 格式化数据透视表
type: docs
weight: 10
url: /zh/go-cpp/formatting-pivot-table/
description: 学习如何使用 Aspose.Cells for C++ 自定义数据透视表的外观。
---

## **数据透视表外观**

如何创建数据透视表介绍了如何创建简单的数据透视表。本文描述了如何通过设置各种属性来自定义数据透视表的外观:

- 数据透视表格式选项
- 数据透视字段格式选项
- 数据字段格式选项

### **设置数据透视表格式选项**

[**PivotTable**](https://reference.aspose.com/cells/go-cpp/pivottable/)类控制整体数据透视表，可以以多种方式进行格式设置。

#### **设置自动格式类型**

微软 Excel 提供多种预设的报表格式。Aspose.Cells 也支持这些格式。访问方式：

1. 将[**PivotTable.IsAutoFormat**](https://reference.aspose.com/cells/go-cpp/pivottable/isautoformat/)设置为**true**。
1. 从[**PivotTableAutoFormatType**](https://reference.aspose.com/cells/go-cpp/pivottableautoformattype/)枚举中分配一个格式选项。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FormattingPivotTable.go" >}}
#### **设置格式选项**

下面的代码示例演示如何格式化数据透视表以显示行和列的总计，以及如何设置报表的字段顺序。还演示了如何为空值设置自定义字符串。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FormattingPivotTable-1.go" >}}
#### **手动设置外观和感觉格式**

要手动调整数据透视表报告的显示方式，而不是使用预设的报表格式，可以使用 [**PivotTable.Format()**](https://reference.aspose.com/cells/go-cpp/pivottable/format_pivotarea_style/) 和 [**PivotTable.FormatAll()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/formatall/) 方法。创建一个样式对象以实现所需的格式，例如：

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FormattingPivotTable-2.go" >}}
### **设置数据透视字段格式选项**

[**PivotField**](https://reference.aspose.com/cells/go-cpp/pivotfield/)类表示数据透视表中的字段，并可以以多种方式进行格式设置。下面的代码示例演示了如何:

- 访问行字段。
- 设置合计。
- 设置自动排序。
- 设置自动显示。

#### **设置行/列/页字段格式**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FormattingPivotTable-3.go" >}}
### **设置数据字段格式**

以下代码示例显示如何设置数据字段的显示格式和数字格式。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FormattingPivotTable-4.go" >}}
### **清除数据透视字段**

[**PivotFieldCollection**](https://reference.aspose.com/cells/go-cpp/pivotfieldcollection/) 有一个名为 [**Clear()**](https://reference.aspose.com/cells/go-cpp/pivotfieldcollection/clear/) 的方法，允许您清除数据透视字段。当您想要清除区域中的所有数据透视字段时（例如页、列、行或数据），请使用它。
以下代码示例显示如何清除数据区域中的所有数据透视字段。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FormattingPivotTable-5.go" >}}
