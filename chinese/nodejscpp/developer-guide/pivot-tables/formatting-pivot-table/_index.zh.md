---
title: 格式化数据透视表
type: docs
weight: 10
url: /zh/nodejs-cpp/formatting-pivot-table/
description: 如何用 Aspose.Cells for Node.js via C++ 格式化数据透视表
keywords: 格式化数据透视表。
---

## **数据透视表外观**

如何创建数据透视表介绍了如何创建简单的数据透视表。本文描述了如何通过设置各种属性来自定义数据透视表的外观:

- 数据透视表格式选项
- 数据透视字段格式选项
- 数据字段格式选项

### **如何设置数据透视表格式选项**

[**PivotTable**](https://reference.aspose.com/cells/nodejs-cpp/pivottable/)类控制整体数据透视表，可以以多种方式进行格式设置。

#### **如何设置自动格式类型**

微软Excel提供多种预设报告格式。Aspose.Cells for Node.js via C++ 同样支持这些格式。要访问它们：

1. 将[**PivotTable.setIsAutoFormat(value)**](https://reference.aspose.com/cells/nodejs-cpp/pivottable/#setIsAutoFormat-boolean-)设置为**true**。
1. 从[**PivotTableAutoFormatType**](https://reference.aspose.com/cells/nodejs-cpp/pivottableautoformattype/)枚举中分配一个格式选项。

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "PivotTables-SettingAutoFormat-1.js" >}}

#### **如何设置格式选项**

下面的代码示例演示了如何格式化数据透视表以显示行和列的总计，以及如何设置报告的字段顺序。它还显示了如何为空值设置自定义字符串。

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "PivotTables-SettingFormatOptions-1.js" >}}

#### **手动设置外观和感觉格式**

要手动设置数据透视表报告的外观和感觉，而不是使用预设的报告格式，请使用[**PivotTable.formatAll(style)**](https://reference.aspose.com/cells/nodejs-cpp/pivottable/#formatAll-style-)和[**PivotTable.format(row, column, style)**](https://reference.aspose.com/cells/nodejs-cpp/pivottable/#format-number-number-style-)方法。为所需的格式创建样式对象，例如：

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "PivotTables-FormattingLook-1.js" >}}

### **如何设置数据透视表字段格式选项**

[**PivotField**](https://reference.aspose.com/cells/nodejs-cpp/pivotfield/)类表示数据透视表中的字段，并可以以多种方式进行格式设置。下面的代码示例演示了如何:

- 访问行字段。
- 设置合计。
- 设置自动排序。
- 设置自动显示。

#### **如何设置行/列/页面字段格式**

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "PivotTables-SettingPageFieldFormat-1.js" >}}

### **如何设置数据字段格式**

以下代码示例显示如何设置数据字段的显示格式和数字格式。

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "PivotTables-SettingDataFieldFormat-1.js" >}}

### **如何清除数据透视字段**

[**PivotFieldCollection**](https://reference.aspose.com/cells/nodejs-cpp/pivotfieldcollection/) 有一个名为 [**clear()**](https://reference.aspose.com/cells/nodejs-cpp/pivotfieldcollection/#clear--) 的方法，允许您清除数据透视字段。当您想要清除区域中的所有数据透视字段时（例如页、列、行或数据），请使用它。
以下代码示例显示如何清除数据区域中的所有数据透视字段。

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "PivotTables-ClearPivotFields-1.js" >}}
