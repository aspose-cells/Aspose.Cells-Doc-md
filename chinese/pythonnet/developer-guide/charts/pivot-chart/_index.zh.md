---
title: 如何使用 Aspose.Cells for Python via .NET 添加数据透视图
linktitle: 数据透视图
type: docs
weight: 100
url: /zh/python-net/how-to-add-pivot-chart/
description: 如何使用 Aspose.Cells for Python via .NET 添加数据透视图。
keywords: 数据透视图
---
## 什么是数据透视图

透视图表是数据透视表的可视化表现形式。透视图表提供了汇总、分析、探索和展示汇总数据的方式。以下是透视图表的一些主要功能和特性：

1. 动态数据表示：数据透视图会自动更新以反映数据透视表的变化。如果在数据透视表中添加或删除字段，数据透视图也会相应更新。

1. 交互性强：数据透视图具有交互性，允许用户筛选、排序和深入分析数据。这使得探索数据的不同方面变得容易。

1. 灵活布局：用户可以通过拖放字段改变数据透视图的布局，为数据可视化提供灵活性。

1. 多种图表类型：可以根据数据的性质和需要获得的洞察，创建柱状图、折线图、饼图等多种类型的图表。

1. 汇总：数据透视图汇总大量数据，可以显示总计、平均值、计数或其他统计信息。

1. 筛选：提供筛选功能，仅显示符合特定条件的数据。

<br>
透视图表常用于商业智能和数据分析，帮助客户清晰、简洁地展示复杂数据，是做出数据驱动决策的强大工具。

## 如何使用 Aspose.Cells for Python Excel 库添加数据透视图

### **添加数据透视表**

使用Aspose.Cells for Python via .NET创建数据透视表：

1. 使用Cell对象的PutValue/setValue方法向工作表单元格添加一些数据。您还可以使用已填充数据的模板文件。这些数据将用作数据透视表的数据源。
1. 通过调用PivotTables集合的add方法（封装在Worksheet对象中）向工作表添加一个数据透视表。
1. 通过传入索引从PivotTables集合中访问新的 PivotTable 对象。# 使用 PivotTable 对象中封装的任何数据透视表对象来管理表。

下面是代码示例。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-CreatePivotTable-1.py" >}}

### **添加数据透视图**

使用Aspose.Cells for Python via .NET创建数据透视图：

1. 添加图表。
1. 将图表的数据源设置为引用电子表格中的现有数据透视表。
1. 设置其他属性。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-CreatePivotChart-1.py" >}}

