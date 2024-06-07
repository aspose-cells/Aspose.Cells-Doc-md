---
title: 格式化数据透视表
type: docs
weight: 10
url: /zh/net/formatting-pivot-table/
---

## **数据透视表外观**

如何创建数据透视表介绍了如何创建一个简单的数据透视表。本文描述了通过设置各种属性来自定义数据透视表外观的方法:

- 数据透视表格式选项
- 数据透视表字段格式选项
- 数据字段格式选项

### **设置数据透视表格式选项**

[**PivotTable**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable)类控制整体数据透视表，并可以以多种方式进行格式化。

#### **设置自动格式类型**

Microsoft Excel提供了许多不同的预设报表格式。Aspose.Cells也支持这些格式选项。要访问这些选项:

1. 将 [**PivotTable.IsAutoFormat**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/properties/isautoformat) 设置为 **true**。
1. 从 [**PivotTableAutoFormatType**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottableautoformattype) 枚举中分配格式选项。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTable-SettingAutoFormat-1.cs" >}}

#### **设置格式选项**

以下代码示例展示了如何设置数据透视表以显示行和列的总计，以及如何设置报表的字段顺序。还展示了如何为空值设置客户字符串。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTable-SettingFormatOptions-1.cs" >}}

#### **手动设置外观格式**

要手动设置数据透视表报告的外观格式，而不是使用预设的报告格式，请使用 [**PivotTable.Format()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/methods/format) 和 [**PivotTable.FormatAll()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/methods/formatall) 方法。为所需的格式创建一个样式对象，例如：

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTable-FormattingLook-1.cs" >}}

### **设置数据透视表字段格式选项**

[**PivotField**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotfield) 类表示数据透视表中的一个字段，可以以多种方式进行格式化。以下代码示例展示了如何：

- 访问行字段。
- 设置小计。
- 设置自动排序。
- 设置自动显示。

#### **设置行/列/字段格式**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTable-SettingPageFieldFormat-1.cs" >}}

### **设置数据字段格式**

以下代码示例展示了如何为数据字段设置显示格式和数值格式。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTable-SettingDataFieldFormat-1.cs" >}}

### **清除数据透视字段**

[**PivotFieldCollection**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotfieldcollection) 类具有一个名为 [**Clear()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotfieldcollection/methods/clear) 的方法，允许您清除数据透视字段。当您想要清除所有数据透视字段时，请使用它，例如，页、列、行或数据。
以下代码示例展示了如何清除数据区域的所有数据透视字段。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTable-ClearPivotFields-1.cs" >}}
