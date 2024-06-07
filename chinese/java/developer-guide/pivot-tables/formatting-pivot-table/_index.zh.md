---
title: 格式化数据透视表
type: docs
weight: 60
url: /zh/java/formatting-pivot-table/
---

## **数据透视表外观**

[如何创建数据透视表](/cells/zh/java/create-pivot-table/)展示了如何创建一个简单的数据透视表。本文进一步讨论了如何通过设置属性来自定义数据透视表的外观。

### **设置数据透视表格式选项**

[**PivotTable**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTable)类允许您为数据透视表设置各种格式选项。

#### **设置自动格式和数据透视表样式类型**

以下示例代码演示了如何使用[**AutoFormatType**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#AutoFormatType)和[**PivotTableStyleType**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#PivotTableStyleType)属性设置自动格式类型和数据透视表样式类型。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-SetAutoFormatandPivotTableStyleTypes-SetAutoFormatandPivotTableStyleTypes.java" >}}

#### **设置格式选项**

以下代码示例说明了如何为数据透视表报告设置多项格式选项，包括为行和列添加总计。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-SettingFormatOptions-SettingFormatOptions.java" >}}

### **设置数据透视表字段格式选项**

除了控制整体数据透视表的格式，Aspose.Cells for Java还允许对行字段、列字段和页字段的格式进行精细控制。

#### **设置行、列和页字段格式**

以下代码示例演示了如何访问行字段，访问特定行，设置小计，应用自动排序，并使用autoShow选项。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-SetRowColumnPageFieldsFormat-SetRowColumnPageFieldsFormat.java" >}}

### **设置数据字段格式**

以下代码行演示了如何格式化数据字段。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-SettingDataFieldFormat-SettingDataFieldFormat.java" >}}

### **修改数据透视表的快速样式**

以下的代码示例展示了如何修改应用于数据透视表的快速样式。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-ModifyPivotTableQuickStyle-ModifyPivotTableQuickStyle.java" >}}

### **清除数据透视字段**

[**PivotFieldCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotFieldCollection) 有一个名为 [**clear()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivotfieldcollection#clear() 的方法，可以清除数据透视表字段。可以使用该方法清除所有区域的数据透视表字段，例如页面、列、行或数据。
下面的代码示例展示了如何清除数据区域中的所有数据透视表字段。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-ClearPivotFields-ClearPivotFields.java" >}}

## **汇总函数**

### **将合并函数应用于数据透视表的数据字段**

Aspose.Cells可以应用ConsolidationFunction到数据透视表的数据字段（或值字段）。在Microsoft Excel中，您可以右键单击数值字段，然后选择**值字段设置...**选项，然后选择**汇总值方式**选项卡。从那里，您可以选择任何您喜欢的ConsolidationFunction，比如求和、计数、平均、最大、最小、乘积、不同计数等。

Aspose.Cells 提供 [**ConsolidationFunction**](https://reference.aspose.com/cells/java/com.aspose.cells/ConsolidationFunction) 枚举以支持以下合并函数。

- [**ConsolidationFunction.AVERAGE**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#AVERAGE)
- [**ConsolidationFunction.COUNT**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#COUNT)
- [**ConsolidationFunction.COUNT_NUMS**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#COUNT_NUMS)
- [**ConsolidationFunction.DISTINCT_COUNT**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#DISTINCT_COUNT)
- [**ConsolidationFunction.MAX**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#MAX)
- [**ConsolidationFunction.MIN**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#MIN)
- [**ConsolidationFunction.PRODUCT**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#PRODUCT)
- [**ConsolidationFunction.STD_DEV**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#STD_DEV)
- [**ConsolidationFunction.STD_DEVP**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#STD_DEVP)
- [**ConsolidationFunction.SUM**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#SUM)
- [**ConsolidationFunction.VAR**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#VAR)
- [**ConsolidationFunction.VARP**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#VARP)

以下代码应用**平均值**ConsolidationFunction到第一个数据字段（或值字段），并应用**不同计数**ConsolidationFunction到第二个数据字段（或值字段）。

{{% alert color="primary" %}}

**唯一计数**合并函数仅受 Microsoft Excel 2013 支持。

{{% /alert %}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-ConsolidationFunctions-ConsolidationFunctions.java" >}}
