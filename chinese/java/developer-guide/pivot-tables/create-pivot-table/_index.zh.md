---
title: 创建数据透视表
type: docs
weight: 10
url: /zh/java/create-pivot-table/
---

## **创建数据透视表**

### **使用Aspose.Cells创建数据透视表**

{{% alert color="primary" %}}

使用Aspose.Cells，可以向电子表格中添加数据透视表。 Aspose.Cells具有许多专门用于创建和控制数据透视表的特殊类。 这些类用于创建和设置[**PivotTable**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTable)对象的属性，用作数据透视表的构建模块。

数据透视表对象为:

- [**PivotField**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotField)：它表示数据透视表中的一个字段。
- [**PivotFieldCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotFieldCollection)：它表示数据透视表中所有 [**PivotField**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotField) 对象的集合。
- [**PivotTable**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTable)：它表示数据透视表。
- [**PivotTableCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTableCollection)：它表示工作表上所有数据透视表对象的集合。

{{% /alert %}}

### **创建简单的数据透视表**

使用Aspose.Cells创建数据透视表，请按照以下步骤进行:

1. 使用 [**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/cell) 对象的 [**setValue**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Value) 方法向工作表单元格添加一些数据。这些数据将作为数据透视表的数据源。
1. 通过调用 [**PivotTableCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTableCollection) 类的 [**add**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottablecollection#add-com.aspose.cells.PivotTable-int-int-java.lang.String-) 方法在工作表中添加数据透视表，封装在 [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) 对象中。
1. 通过传递 [**PivotTable**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTable) 索引从 [**PivotTableCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTableCollection) 中访问 [**PivotTable**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTable) 对象。
1. 使用 [**PivotTable**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTable) 对象封装的任何数据透视表对象（如上所述）来管理数据透视表。

{{% alert color="primary" %}}

在将单元格范围指定为数据源时，范围必须从左上到右下进行设置。例如，“A1:C3” 是有效的；“C3:A1” 是无效的。

{{% /alert %}}

下面的代码示例显示了如何根据上述基本步骤创建一个简单的数据透视表。执行代码时，会在工作表中添加一个数据透视表:

**基于相应字段创建数据透视表**

![todo:image_alt_text](create-pivot-table_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-CreatePivotTable-CreatePivotTable.java" >}}
{{< app/cells/assistant language="java" >}}
