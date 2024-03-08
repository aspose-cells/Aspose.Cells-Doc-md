---
title: 如何使用 Aspose.Cells 添加数据透视图
linktitle: 数据透视图
type: docs
weight: 100
url: /zh/java/how-to-add-pivot-chart/
description: 如何使用 Aspose.Cells 添加数据透视图。
keywords: PivotChart
---
## 什么是数据透视图

Excel 中的数据透视图是从数据透视表创建的数据的图形表示。它允许用户通过以图表形式汇总和显示信息来动态可视化和分析数据。数据透视图是交互式的，可以轻松修改以显示数据的不同视角，使其成为 Excel 中数据分析和演示的强大工具。

## 如何使用 Aspose.Cells 添加数据透视图
###  **创建数据透视表**

要使用 Aspose.Cells 创建数据透视表：

1. 使用 Cell 对象的 PutValue/setValue 方法将一些数据添加到工作表单元格。您还可以使用已填充数据的模板文件。该数据将用作数据透视表的数据源。
1. 通过调用 PivotTables 集合的 add 方法（封装在 Worksheet 对象中）将数据透视表添加到工作表中。
1. 通过传递索引从数据透视表集合中访问新的数据透视表对象。
1. 使用封装在数据透视表对象中的任何数据透视表对象来管理表。

下面给出了代码示例。执行代码会生成一个新文件：pivotTable_test.xls。

**输入数据** 

![待办事项：图像_替代_文本](create-pivot-tables-and-pivot-charts_1.png)

**输出数据透视表**

![待办事项：图像_替代_文本](create-pivot-tables-and-pivot-charts_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CreatePivotTable-CreatePivotTable.java" >}}

###  **基于数据透视表创建数据透视图**

要使用 Aspose.Cells 创建数据透视图：

1. 添加图表。
1. 设置图表的 PivotSource 以引用电子表格中的现有数据透视表。
1. 设置其他属性。

下面是组件用来完成任务的代码。执行代码会生成一个新文件：pivotChart_test.xls。

**数据透视图表**

![待办事项：图像_替代_文本](create-pivot-tables-and-pivot-charts_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CreatePivotChartbasedonPivotTable-CreatePivotChartbasedonPivotTable.java" >}}

{{% alert color="primary" %}}

本文介绍如何使用 Aspose.Cells 创建数据透视表和数据透视图。希望它能帮助您在自己的场景中使用这些功能。

Aspose.Cells得益于多年的研究、设计和精心调校。

欢迎您通过以下方式提出疑问、意见和建议：[Aspose.Cells 论坛](https://forum.aspose.com/c/cells/9)。我们保证及时回复。

{{% /alert %}}
