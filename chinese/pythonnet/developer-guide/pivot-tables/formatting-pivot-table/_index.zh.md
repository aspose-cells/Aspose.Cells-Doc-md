---
title: 格式化数据透视表
type: docs
weight: 10
url: /zh/python-net/formatting-pivot-table/
description: 如何使用Aspose.Cells for Python通过.NET格式化数据透视表
keywords: 格式化数据透视表。
---

## **数据透视表外观**

如何创建数据透视表介绍了如何创建一个简单的数据透视表。本文描述了通过设置各种属性来自定义数据透视表外观的方法:

- 数据透视表格式选项
- 数据透视表字段格式选项
- 数据字段格式选项

### **设置数据透视表格式选项的方法**

[**PivotTable**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/)类控制整体数据透视表，并可以以多种方式进行格式化。

#### **设置自动格式类型的方法**

Microsoft Excel提供了许多不同的预设报告格式。Aspose.Cells for Python通过.NET也支持这些格式选项。要访问它们：

1. 将 [**PivotTable.is_auto_format**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/is_auto_format/) 设置为 **true**。
1. 从 [**PivotTableAutoFormatType**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottableautoformattype/) 枚举中分配格式选项。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-SettingAutoFormat-1.py" >}}

#### **设置格式选项的方法**

以下代码示例展示了如何设置数据透视表以显示行和列的总计，以及如何设置报表的字段顺序。还展示了如何为空值设置客户字符串。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-SettingFormatOptions-1.py" >}}

#### **手动设置外观格式**

Manually根据您希望的格式创建样式对象，而不是使用预设的报告格式，使用[**PivotTable.format_all(style)**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/format_all/)和[**PivotTable.format(row, column, style)**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/format/)方法格式化数据透视表报告。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-FormattingLook-1.py" >}}

### **设置数据透视字段格式选项的方法**

[**PivotField**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivotfield/) 类表示数据透视表中的一个字段，可以以多种方式进行格式化。以下代码示例展示了如何：

- 访问行字段。
- 设置小计。
- 设置自动排序。
- 设置自动显示。

#### **设置行/列/页字段格式的方法**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-SettingPageFieldFormat-1.py" >}}

### **如何设置数据字段格式**

以下代码示例展示了如何为数据字段设置显示格式和数值格式。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-SettingDataFieldFormat-1.py" >}}

### **如何清除数据透视字段**

[**PivotFieldCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivotfieldcollection/) 类具有一个名为 [**clear()**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivotfieldcollection/clear/#) 的方法，允许您清除数据透视字段。当您想要清除所有数据透视字段时，请使用它，例如，页、列、行或数据。
以下代码示例展示了如何清除数据区域的所有数据透视字段。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-ClearPivotFields-1.py" >}}
