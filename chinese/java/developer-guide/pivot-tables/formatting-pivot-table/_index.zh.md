---
title: 格式化数据透视表
type: docs
weight: 60
url: /zh/java/formatting-pivot-table/
---
## **数据透视表外观**

[如何创建数据透视表](/cells/zh/java/create-pivot-table/)展示了如何创建一个简单的数据透视表。本文进一步讨论了如何通过设置属性来自定义数据透视表的外观。

### **设置数据透视表格式选项**

这[**数据透视表**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTable)类允许您为数据透视表设置各种格式设置选项。

#### **设置自动套用格式和数据透视表样式类型**

下面的代码示例说明了如何使用设置自动格式类型和数据透视表样式类型[**自动格式类型**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#AutoFormatType)和[**数据透视表样式类型**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#PivotTableStyleType)特性。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-SetAutoFormatandPivotTableStyleTypes-SetAutoFormatandPivotTableStyleTypes.java" >}}

#### **设置格式选项**

下面的代码示例说明了如何为数据透视表报表设置多个格式设置选项，包括为行和列添加总计。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-SettingFormatOptions-SettingFormatOptions.java" >}}

### **设置数据透视字段格式选项**

除了控制整个数据透视表的格式外，Aspose.Cells for Java 还允许对行字段、列字段和页字段的格式进行微调控制。

#### **设置行、列和页面字段格式**

下面的代码示例显示了如何访问行字段、访问特定行、设置小计、应用自动排序以及使用 autoShow 选项。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-SetRowColumnPageFieldsFormat-SetRowColumnPageFieldsFormat.java" >}}

### **设置数据字段格式**

以下代码行说明了如何格式化数据字段。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-SettingDataFieldFormat-SettingDataFieldFormat.java" >}}

### **修改数据透视表的快速样式**

下面的代码示例显示了如何修改应用于数据透视表的快速样式。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-ModifyPivotTableQuickStyle-ModifyPivotTableQuickStyle.java" >}}

### **清除数据透视字段**

[**数据透视字段集合**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotFieldCollection)有一个名为的方法[**清除（）**](https://reference.aspose.com/cells/java/com.aspose.cells/pivotfieldcollection#clear()清除数据透视字段。使用它来清除所有区域中的数据透视字段，例如页面、列、行或数据。
下面的代码示例显示了如何清除数据区域中的所有数据透视字段。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-ClearPivotFields-ClearPivotFields.java" >}}

## **整合功能**

### **将 ConsolidationFunction 应用于数据透视表的数据字段**

 Aspose.Cells 可用于将 ConsolidationFunction 应用于数据透视表的数据字段（或值字段）。在Microsoft Excel中，您可以右键单击值字段然后选择**值字段设置...**选项，然后选择选项卡**值汇总依据**.从那里，您可以选择您选择的任何 ConsolidationFunction，例如 Sum、Count、Average、Max、Min、Product、Distinct Count 等。

Aspose.Cells提供[**整合功能**](https://reference.aspose.com/cells/java/com.aspose.cells/ConsolidationFunction)支持以下合并功能的枚举。

- [**合并函数.AVERAGE**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#AVERAGE)
- [**合并函数.COUNT**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#COUNT)
- [**合并函数.COUNT_NUMS**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#COUNT_NUMS)
- [**合并函数.DISTINCT_COUNT**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#DISTINCT_COUNT)
- [**合并函数.MAX**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#MAX)
- [**合并函数.MIN**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#MIN)
- [**合并函数.PRODUCT**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#PRODUCT)
- [**合并函数.STD_DEV**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#STD_DEV)
- [**合并函数.STD_DEVP**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#STD_DEVP)
- [**合并函数.SUM**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#SUM)
- [**合并函数.VAR**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#VAR)
- [**合并函数**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#VARP)

以下代码适用**平均的**合并功能到第一个数据字段（或值字段）和**非重复计数**合并功能到第二个数据字段（或值字段）。

{{% alert color="primary" %}}

Microsoft 仅 Excel 2013 支持 DistinctCount 合并函数。

{{% /alert %}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-ConsolidationFunctions-ConsolidationFunctions.java" >}}
