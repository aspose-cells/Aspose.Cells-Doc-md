---
title: 创建数据透视表
linktitle: 创建数据透视表
description: 使用 Aspose.Cells for Java 创建数据透视表并设置其格式。
keywords: 创建数据透视表, 插入数据透视表, 设置数据透视表格式.
type: docs
weight: 160
url: /zh/java/create-pivot-table/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **什么是数据透视表？**
数据透视表是一种交互式汇总报告：无需任何公式，即可将大量逐行记录的原始数据汇总为紧凑的矩阵。您可以决定哪些列用作行标签、哪些列用作列标签，以及哪些列作为值进行聚合——数据透视表将自动完成分组和计算：
- **汇总**——按产品、区域或季度汇总销售总额，无需冗长的公式链。
- **比较**——将类别置于行中、期间置于列中，可将扁平列表转换为交叉报表，使趋势一目了然。
- **下钻**——双击任意汇总值，即可查看其对应的源行。
- **刷新**——源数据发生变化时，只需刷新一次即可重新计算整个报告。
常见应用场景包括销售仪表板、费用构成分析和库存分析——无论是“这些数字如何按类别和时间细分？”一类问题，均可通过数据透视表进行分析。Aspose.Cells for Java 支持以编程方式创建同类数据透视表，因此应用程序生成的工作簿不仅可以包含原始数据，还能提供现成的报告。

### **使用 Aspose.Cells 创建数据透视表**

{{% alert color="primary" %}}
使用 Aspose.Cells，可以将数据透视表添加到电子表格中。Aspose.Cells 提供了多个专门用于创建和控制数据透视表的类。这些类用于创建 [**PivotTable**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTable) 对象并设置其属性；该对象是构建数据透视表的基本组成部分。
数据透视表相关对象包括：
- [**PivotField**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotField)：表示数据透视表中的字段。
- [**PivotFieldCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotFieldCollection)：表示数据透视表中所有 [**PivotField**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotField) 对象的集合。
- [**PivotTable**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTable)：表示数据透视表。
- [**PivotTableCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTableCollection)：表示工作表上所有数据透视表对象的集合。
{{% /alert %}}

### **创建简单的数据透视表**
创建数据透视表需要执行以下步骤：将源数据写入工作表单元格、在目标位置添加数据透视表，并将数据透视字段放入行区域、列区域和数据区域。
1. 使用 [**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/cell) 对象的 [**setValue**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#setValue-java.lang.Object-) 方法（大多数示例使用 `putValue`）将数据添加到工作表单元格中。该数据将用作数据透视表的数据源。
2. 调用 [**PivotTableCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTableCollection) 类的 [**add**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottablecollection#add-com.aspose.cells.PivotTable-int-int-) 方法，向工作表添加数据透视表：`add(sourceData, row, column)`。`sourceData` 为源区域（例如 "A1:C8"）；`row` 和 `column` 为数据透视表左上角目标单元格的从 0 开始的坐标（单元格 E3 表示第 2 行、第 4 列）。该方法直接返回新的 [**PivotTable**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTable) 对象。
3. 使用 [**PivotTable**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTable) 对象的 `addFieldToArea` 方法添加数据透视字段：字段名称可添加到行区域（`PivotFieldType.ROW`）、列区域（`PivotFieldType.COLUMN`）或数据区域（`PivotFieldType.DATA`）。
4. 保存工作簿——数据透视表将写入保存后的文件中。
以下代码示例按照上述步骤创建一个简单的数据透视表。运行后，将根据源数据在工作表中添加数据透视表：
![todo:image_alt_text](create-pivot-table_1.png)

```java
import com.aspose.cells.*;

// 创建一个新的工作簿并获取第一个工作表
Workbook workbook = new Workbook();
Worksheet sheet = workbook.getWorksheets().get(0);
Cells cells = sheet.getCells();

// 写入源数据：按运动项目和季度划分的销售额
cells.get("A1").putValue("Sport");
cells.get("B1").putValue("Quarter");
cells.get("C1").putValue("Sales");
cells.get("A2").putValue("Golf");
cells.get("B2").putValue("Qtr3");
cells.get("C2").putValue(1500);
cells.get("A3").putValue("Golf");
cells.get("B3").putValue("Qtr4");
cells.get("C3").putValue(2000);
cells.get("A4").putValue("Tennis");
cells.get("B4").putValue("Qtr3");
cells.get("C4").putValue(600);
cells.get("A5").putValue("Tennis");
cells.get("B5").putValue("Qtr4");
cells.get("C5").putValue(1500);
cells.get("A6").putValue("Tennis");
cells.get("B6").putValue("Qtr3");
cells.get("C6").putValue(4070);
cells.get("A7").putValue("Tennis");
cells.get("B7").putValue("Qtr4");
cells.get("C7").putValue(5000);
cells.get("A8").putValue("Golf");
cells.get("B8").putValue("Qtr3");
cells.get("C8").putValue(6430);

// 在目标单元格 E3 处添加数据透视表，数据源为 A1:C8
PivotTable pivotTable = sheet.getPivotTables().add("A1:C8", 2, 4);

// 分配数据透视表字段：将 Sport 放入行区域，将 Quarter 放入列区域，将 Sales 放入数据区域
pivotTable.addFieldToArea(PivotFieldType.ROW, "Sport");
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Quarter");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Sales");

// 保存工作簿
workbook.save("pivotTable_test_out.xlsx");
```

{{% alert color="primary" %}}
将一组单元格指定为数据源时，必须按从左上角到右下角的顺序设置该区域。例如，"A1:C3" 有效，"C3:A1" 无效。
{{% /alert %}}

{{< app/cells/assistant language="java" >}}