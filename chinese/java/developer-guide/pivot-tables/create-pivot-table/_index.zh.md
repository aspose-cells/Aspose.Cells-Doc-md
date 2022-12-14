---
title: 创建数据透视表
type: docs
weight: 10
url: /zh/java/create-pivot-table/
---
## **创建数据透视表**

### **使用 Aspose.Cells 创建数据透视表**

{{% alert color="primary" %}}

使用 Aspose.Cells，可以将数据透视表添加到电子表格中。 Aspose.Cells 有许多专门用于创建和控制数据透视表的特殊类。这些类用于创建和设置[**数据透视表**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTable)对象，用作数据透视表的构建块。

数据透视表对象是：

- [**数据透视表**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotField)：它代表数据透视表中的一个字段。
- [**数据透视字段集合**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotFieldCollection)：它代表所有的集合[**数据透视表**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotField)数据透视表中的对象。
- [**数据透视表**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTable): 它代表一个数据透视表。
- [**数据透视表集合**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTableCollection)：它代表工作表上所有数据透视表对象的集合。

{{% /alert %}}

### **创建一个简单的数据透视表**

要使用 Aspose.Cells 创建数据透视表，请按照以下步骤操作：

1. 通过使用将一些数据添加到工作表单元格[**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/cell)对象的[**设定值**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Value)方法。此数据将用作数据透视表的数据源。
1. 通过调用将数据透视表添加到工作表[**添加**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottablecollection#add(com.aspose.cells.PivotTable,%20int,%20int,%20java.lang.String) 的方法[**数据透视表集合**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTableCollection)类，封装在[**工作表**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)目的。
1. 访问[**数据透视表**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTable)对象来自[**数据透视表集合**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTableCollection)通过传递[**数据透视表**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTable)指数。
1. 使用封装在[**数据透视表**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTable)对象来管理数据透视表。

{{% alert color="primary" %}}

将单元格范围指定为数据源时，范围必须设置为从左上角到右下角。例如，“A1:C3”有效； “C3:A1”无效。

{{% /alert %}}

下面的代码示例显示了如何按照上面列出的基本步骤创建一个简单的数据透视表。执行代码时，数据透视表会添加到工作表中：

**根据相应字段创建数据透视表**

![待办事项：图片_替代_文本](create-pivot-table_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-CreatePivotTable-CreatePivotTable.java" >}}
