---
title: 创建数据透视表
type: docs
weight: 10
url: /zh/java/create-pivot-table/
---

## **创建数据透视表**

### **使用 Aspose.Cells 创建透视表**

{{% alert color="primary" %}}

使用 Aspose.Cells，可以向电子表格添加透视表。Aspose.Cells具有多个专用类，专门用于创建和控制透视表。这些类用于创建和设置作为透视表构建块的 [**PivotTable**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTable) 对象的属性。

透视表对象包括：

- [**PivotField**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotField)：它代表透视表中的字段。
- [**PivotFieldCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotFieldCollection)：它代表透视表中所有 [**PivotField**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotField) 对象的集合。
- [**PivotTable**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTable)：它代表透视表。
- [**PivotTableCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTableCollection)：它代表工作表上所有透视表对象的集合。

{{% /alert %}}

### **创建简单的透视表**

要使用 Aspose.Cells 创建透视表，请按照以下步骤操作：

1. 通过 [**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/cell) 对象的 [**setValue**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Value) 方法将一些数据添加到工作表单元格中。这些数据将用作透视表的数据源。
1. 通过调用 [**PivotTableCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTableCollection) 类的 [**add**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottablecollection#add(com.aspose.cells.PivotTable,%20int,%20int,%20java.lang.String) 方法，在 [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) 对象中封装的方式向工作表添加透视表。
1. 通过传递 [**PivotTable**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTable) 索引，从 [**PivotTableCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTableCollection) 中访问 [**PivotTable**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTable) 对象。
1. 使用 [**PivotTable**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTable) 对象中封装的任何透视表对象（如上所述）来管理透视表。

{{% alert color="primary" %}}

将单元格范围分配为数据源时，范围必须从左上角设置到右下角。例如，"A1:C3" 是有效的；"C3:A1" 是无效的。

{{% /alert %}}

下面的示例代码展示如何按照上述基本步骤创建简单的透视表。执行代码时，工作表上将添加一个透视表：

**基于相应字段创建数据透视表**

![todo:image_alt_text](create-pivot-table_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-CreatePivotTable-CreatePivotTable.java" >}}
