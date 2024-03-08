---
title: 如何使用 Aspose.Cells 添加数据透视图
linktitle: 数据透视图
type: docs
weight: 100
url: /zh/net/how-to-add-pivot-chart/
description: 如何使用 Aspose.Cells 添加数据透视图。
keywords: PivotChart
---
## 什么是数据透视图

Excel 中的数据透视图是从数据透视表创建的数据的图形表示。它允许用户通过以图表形式汇总和显示信息来动态可视化和分析数据。数据透视图是交互式的，可以轻松修改以显示数据的不同视角，使其成为 Excel 中数据分析和演示的强大工具。

## 如何使用 Aspose.Cells 添加数据透视图

###  **添加数据透视表**

要使用 Aspose.Cells 创建数据透视表：

1. 使用 Cell 对象的 PutValue/setValue 方法将一些数据添加到工作表单元格。您还可以使用已填充数据的模板文件。该数据将用作数据透视表的数据源。
1. 通过调用 PivotTables 集合的 add 方法（封装在 Worksheet 对象中）将数据透视表添加到工作表中。
1. 通过传递索引从数据透视表集合中访问新的数据透视表对象。 # 使用封装在数据透视表对象中的任意数据透视表对象来管理表。

下面给出了代码示例。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CreatePivotTablesPivotCharts-CreatePivotTable-1.cs" >}}

###  **添加数据透视图**

要使用 Aspose.Cells 创建数据透视图：

1. 添加图表。
1. 设置图表的 PivotSource 以引用电子表格中的现有数据透视表。
1. 设置其他属性。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CreatePivotTablesPivotCharts-CreatePivotChart-1.cs" >}}

