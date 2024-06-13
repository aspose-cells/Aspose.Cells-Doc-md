---
title: 格式化数据透视表
type: docs
weight: 60
url: /zh/java/formatting-pivot-table/
---

## **数据透视表外观**

《如何创建透视表》（/cells/zh/java/create-pivot-table/）展示了如何创建一个简单的透视表。这篇文章进一步讨论了如何通过设置属性自定义透视表的外观。

### **设置数据透视表格式选项**

[**PivotTable**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTable) 类允许您为透视表设置各种格式选项。

#### **设置自动格式和透视表样式类型**

接下来的代码示例说明了如何使用 [**AutoFormatType**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#AutoFormatType) 属性和 [**PivotTableStyleType**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#PivotTableStyleType) 属性设置自动格式类型和透视表样式类型。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-SetAutoFormatandPivotTableStyleTypes-SetAutoFormatandPivotTableStyleTypes.java" >}}

#### **设置格式选项**

接下来的代码示例说明了如何为透视表报告设置多项格式选项，包括为行和列添加总计。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-SettingFormatOptions-SettingFormatOptions.java" >}}

### **设置透视字段格式选项**

除了控制整个数据透视表的格式外，Aspose.Cells for Java 还允许对行字段、列字段和页面字段的格式进行精细控制。

#### **设置行、列和页面字段格式**

接下来的代码示例显示了如何访问行字段，访问特定行，设置小计，应用自动排序，并使用自动显示选项。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-SetRowColumnPageFieldsFormat-SetRowColumnPageFieldsFormat.java" >}}

### **设置数据字段格式**

下面的代码行演示了如何格式化数据字段。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-SettingDataFieldFormat-SettingDataFieldFormat.java" >}}

### **修改透视表的快速样式**

接下来的代码示例展示了如何修改应用于透视表的快速样式。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-ModifyPivotTableQuickStyle-ModifyPivotTableQuickStyle.java" >}}

### **清除数据透视字段**

[**PivotFieldCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotFieldCollection)有一个名为[**clear()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivotfieldcollection#clear--)的方法用于清除数据透视表字段。在清除页面、列、行或数据等区域的数据透视表字段时使用它。
下面的代码示例显示了如何清除数据区域中的所有透视字段。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-ClearPivotFields-ClearPivotFields.java" >}}

## **合并功能**

### **应用合并功能到数据字段的数据透视表**

Aspose.Cells可用于应用合并功能到数据透视表的数据字段（或值字段）。在Microsoft Excel中，您可以右键单击值字段，然后选择**值字段设置...**选项，然后选择**汇总方式**选项卡。从那里，您可以选择任何您喜欢的合并功能，如求和、计数、平均值、最大值、最小值、乘积、去重计数等。

Aspose.Cells提供[**ConsolidationFunction**](https://reference.aspose.com/cells/java/com.aspose.cells/ConsolidationFunction)枚举以支持以下合并功能。

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

以下代码将**平均值**合并功能应用于第一个数据字段（或值字段），并将**去重计数**合并功能应用于第二个数据字段（或值字段）。

{{% alert color="primary" %}}

Microsoft Excel 2013仅支持去重计数合并功能。

{{% /alert %}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-ConsolidationFunctions-ConsolidationFunctions.java" >}}
