---
title: 如何使用Aspose.Cells添加数据透视图
linktitle: 数据透视图
type: docs
weight: 100
url: /zh/net/how-to-add-pivot-chart/
description: 如何使用Aspose.Cells添加数据透视图。
keywords: 数据透视图
---
## 什么是数据透视图

Excel中的数据透视图是从数据透视表创建的数据的图形表示。 它允许用户以图表形式汇总和显示信息，动态地可视化和分析数据。 数据透视图是交互式的，可以轻松修改以显示数据的不同视角，使其成为Excel中数据分析和呈现的强大工具。

## 如何使用Aspose.Cells添加数据透视图

### **添加数据透视表**

使用Aspose.Cells创建数据透视表:

1. 使用Cell对象的PutValue/setValue方法向工作表单元格添加一些数据。您还可以使用模板文件，该文件已经填充了数据。这些数据将用作数据透视表的数据源。
1. 通过调用PivotTables集合的add方法（封装在Worksheet对象中）向工作表添加一个数据透视表。
1. 通过传递其索引从PivotTables集合中访问新的PivotTable对象。# 使用数据透视表对象封装的任何数据透视表对象来管理数据表。

以下是代码示例。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CreatePivotTablesPivotCharts-CreatePivotTable-1.cs" >}}

### **添加数据透视图**

使用Aspose.Cells创建数据透视图:

1. 添加一个图表。
1. 将图表的PivotSource设置为引用电子表格中现有的数据透视表。
1. 设置其他属性。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CreatePivotTablesPivotCharts-CreatePivotChart-1.cs" >}}

