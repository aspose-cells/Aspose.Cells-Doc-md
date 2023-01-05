---
title: 格式化数据透视表
type: docs
weight: 10
url: /zh/net/formatting-pivot-table/
---
## **数据透视表外观**

如何创建数据透视表解释了如何创建一个简单的数据透视表。本文介绍如何通过设置各种属性来自定义数据透视表的外观：

- 数据透视表格式选项
- 数据透视字段格式选项
- 数据字段格式选项

### **设置数据透视表格式选项**

这[**数据透视表**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable)类控制整个数据透视表，可以通过多种方式进行格式化。

#### **设置自动套用格式类型**

Microsoft Excel 提供了许多不同的预设报告格式。 Aspose.Cells 也支持这些格式化选项。要访问它们：

1. 放[**数据透视表.IsAutoFormat**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/properties/isautoformat)到**真的**.
1. 从[**数据透视表自动格式类型**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottableautoformattype)枚举。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTable-SettingAutoFormat-1.cs" >}}

#### **设置格式选项**

下面的代码示例显示了如何设置数据透视表的格式以显示行和列的总计，以及如何设置报表的字段顺序。它还展示了如何为空值设置客户字符串。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTable-SettingFormatOptions-1.cs" >}}

#### **手动格式化外观**

要手动格式化数据透视表报告的外观，而不是使用预设的报告格式，请使用[**数据透视表格式()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/methods/format)和[**数据透视表.FormatAll()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/methods/formatall)方法。为您想要的格式创建一个样式对象，例如：

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTable-FormattingLook-1.cs" >}}

### **设置数据透视字段格式选项**

这[**数据透视表**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotfield)类表示数据透视表中的一个字段，可以通过多种方式进行格式化。下面的代码示例显示了如何：

- 访问行字段。
- 设置小计。
- 设置自动排序。
- 设置自动显示。

#### **设置行/列/页字段格式**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTable-SettingPageFieldFormat-1.cs" >}}

### **设置数据字段格式**

下面的代码示例显示了如何设置数据字段的显示格式和数字格式。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTable-SettingDataFieldFormat-1.cs" >}}

### **清除数据透视字段**

这[**数据透视字段集合**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotfieldcollection)有一个名为的方法[**清除（）**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotfieldcollection/methods/clear)这允许您清除数据透视字段。当您要清除区域中的所有数据透视字段时使用它，例如页、列、行或数据。
下面的代码示例显示了如何清除数据区域中的所有数据透视字段。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTable-ClearPivotFields-1.cs" >}}
