---
title: 如何使用Aspose.Cells添加数据透视图
linktitle: 数据透视图
type: docs
weight: 100
url: /zh/java/how-to-add-pivot-chart/
description: 如何使用Aspose.Cells添加一个数据透视图。
keywords: 数据透视图
---
## 什么是数据透视图

Excel中的数据透视图是从数据透视表中创建的数据的图形表示。它允许用户通过以图表形式汇总和显示信息来动态可视化和分析数据。数据透视图是交互式的，可以轻松修改以显示数据的不同视角，因此是Excel中数据分析和演示的强大工具。

## 如何使用Aspose.Cells添加数据透视图
### **创建数据透视表**

使用Aspose.Cells创建数据透视表：

1. 使用Cell对象的PutValue/setValue方法向工作表单元格添加一些数据。您还可以使用已填充数据的模板文件。这些数据将用作数据透视表的数据源。
1. 通过调用PivotTables集合的add方法（封装在Worksheet对象中）向工作表添加一个数据透视表。
1. 通过传递其索引从PivotTables集合中访问新的PivotTable对象。
1. 使用PivotTable对象中封装的任何数据透视表对象来管理表。

下面给出了一段代码示例。执行该代码将生成一个新文件：pivotTable_test.xls。

**输入数据** 

![todo:image_alt_text](create-pivot-tables-and-pivot-charts_1.png)

**输出的数据透视表**

![todo:image_alt_text](create-pivot-tables-and-pivot-charts_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CreatePivotTable-CreatePivotTable.java" >}}

### **基于数据透视表创建数据透视图**

使用Aspose.Cells创建一个数据透视图:

1. 添加图表。
1. 将图表的数据源设置为引用电子表格中的现有数据透视表。
1. 设置其他属性。

以下是组件用于完成任务的代码。执行代码会生成一个新文件：pivotChart_test.xls。

**数据透视图表工作表**

![todo:image_alt_text](create-pivot-tables-and-pivot-charts_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CreatePivotChartbasedonPivotTable-CreatePivotChartbasedonPivotTable.java" >}}

{{% alert color="primary" %}}

本文介绍了如何使用Aspose.Cells创建数据透视表和数据透视图表。希望能帮助您在自己的场景中使用这些功能。

Aspose.Cells 从多年的研究、设计和精心调整中受益。

我们欢迎您在[Aspose.Cells 论坛](https://forum.aspose.com/c/cells/9)上提出问题、评论和建议。我们保证会及时回复。

{{% /alert %}}
