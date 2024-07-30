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
数据透视表是数据的可视表示。数据透视图提供了一种总结、分析、探索和展示汇总数据的方法。以下是数据透视表的一些关键特性和方面：

1. 动态数据表示：数据透视图会自动更新以反映数据透视表中的更改。如果在数据透视表中添加或删除字段，数据透视图会相应地更新。

1. 交互式：数据透视图是交互式的，允许用户对数据进行筛选、排序和深入分析。这使得探索数据集的不同方面变得容易。

1. 灵活布局：用户可以通过拖放字段来更改数据透视图的布局，从而灵活可视化数据。

1. 各种图表类型：根据数据的性质和您希望获得的见解，可以使用各种图表类型来创建数据透视图，例如柱状图、折线图、饼图等。

1. 汇总：数据透视图总结大量数据并可显示总计、平均值、计数或其他汇总统计信息。

1. 筛选：它们提供筛选功能，允许您仅显示符合特定标准的数据。

<br>
数据透视图通常用于商业智能和数据分析，以对复杂数据集提供清晰简洁的可视汇总。它们是做出基于数据的决策的强大工具。

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
