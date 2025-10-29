---
title: 如何通过 C++ 使用 Golang 添加数据透视图
linktitle: 数据透视图
type: docs
weight: 100
url: /zh/go-cpp/how-to-add-pivot-chart/
description: 如何使用 Aspose.Cells 结合 Golang 和 C++ 添加数据透视图。
keywords: 数据透视图
---

## 什么是数据透视图

透视图表是数据透视表的可视化表现形式。透视图表提供了汇总、分析、探索和展示汇总数据的方式。以下是透视图表的一些主要功能和特性：

1. **动态数据表现**：透视图表会自动更新以反映数据透视表的变化。若添加或删除字段，图表相应变动。

1. **交互性**：透视图表支持交互操作，用户可以筛选、排序或深入探索数据。这使得分析更便捷。

1. **布局灵活**：用户可以通过拖放字段改变透视图表的布局，增强可定制性。

1. **多种图表类型**：透视图表支持柱状图、线图、饼图等多种类型，根据数据特性和分析需求定制。

1. **汇总统计**：透视图表可以汇总大量数据，并显示总计、平均值、计数或其他统计结果。

1. **筛选功能**：提供筛选功能，只显示符合条件的数据。

<br>
透视图表常用于商业智能和数据分析，帮助客户清晰、简洁地展示复杂数据，是做出数据驱动决策的强大工具。

## 如何使用Aspose.Cells添加数据透视图

### **添加数据透视表**

使用Aspose.Cells创建数据透视表：

1. 使用 `Cell` 对象的 `PutValue` 或 `SetValue` 方法向工作表单元格添加数据。您也可以使用已填充数据的模板文件。数据将用作枢轴表的数据源。
1. 通过调用`PivotTables`集合的`Add`方法（封装在`Worksheet`对象中）向工作表添加数据透视表。
1. 通过传递索引从`PivotTables`集合中访问新的`PivotTable`对象。使用任何封装在`PivotTable`对象中的数据透视表对象来管理表格。

下面是代码示例。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-PivotChart.go" >}}
### **添加数据透视图**

使用Aspose.Cells创建数据透视图：

1. 添加图表。
1. 设置图表的`PivotSource`，指向工作表中的现有数据透视表。
1. 设置其他属性。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-PivotChart-1.go" >}}
