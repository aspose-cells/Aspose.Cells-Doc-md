---
title: 创建数据透视表和数据透视图
type: docs
weight: 20
url: /zh/nodejs-cpp/create-pivot-tables-and-pivot-charts/
description: 如何使用Aspose.Cells for Node.js via C++添加数据透视表和数据透视图。
keywords: Aspose.Cells for Node.js via C++ Excel、Excel Node.js库，使用Aspose.Cells for Node.js via C++ Excel库添加数据透视表和数据透视图。
---

{{% alert color="primary" %}}

数据透视表是记录的互动摘要。例如，您可能有数百个工作表中列表中的发票条目。数据透视表可以按客户、产品或日期总计发票。使用Microsoft Excel，可以通过将按钮拖到新位置，快速重新排列数据透视表中的信息。

数据透视图图表是数据透视表中数据的交互式图形表示。数据透视图图表在Excel 2000中引入。使用数据透视图图表使数据更容易理解，因为数据透视表会自动创建小计和总计。

Aspose.Cells for Node.js via C++ 支持 [数据透视表](/cells/zh/nodejs-cpp/create-pivot-tables-and-pivot-charts/) 和 [数据透视图](/cells/zh/nodejs-cpp/create-pivot-tables-and-pivot-charts/)。

{{% /alert %}}

## **使用Aspose.Cells for Node.js via C++添加数据透视表和图表**

Aspose.Cells for Node.js via C++ 提供了一组用于创建数据透视表的特殊类。这些类用于创建和设置数据透视表对象，它们作为数据透视表对象的基本构建块：

- PivotField，数据透视表报告中的字段。
- PivotFields，数据透视表中所有 PivotField 对象的集合。
- 一个工作表上的数据透视表。
- 数据透视表是工作表上所有数据透视表对象的集合。

### **准备使用 Aspose.Cells for Node.js via C++**
1. 从 NPM 安装 Aspose.Cells for Node.js via C++，使用命令：$ npm install aspose.cells.node。
1. 你也可以按照逐步指引将“Aspose.Cells for Node.js via C++”安装到你的开发环境中。


### **如何使用 Aspose.Cells for Node.js via C++ 添加数据透视表**

使用 Aspose.Cells for Node.js via C++ 创建数据透视表的方法：

1. 使用Cell对象的put_value方法向工作表单元格添加一些数据。也可以使用填充了数据的模板文件。这些数据将被用作数据透视表的数据源。
1. 通过调用PivotTables集合的add方法（封装在Worksheet对象中）向工作表添加一个数据透视表。
1. 通过传入索引从PivotTables集合中访问新的 PivotTable 对象。# 使用 PivotTable 对象中封装的任何数据透视表对象来管理表。

下面是代码示例。

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "PivotTables-CreatePivotTablesPivotCharts-CreatePivotTable-1.js" >}}

### **如何使用 Aspose.Cells for Node.js via C++ 库添加数据透视图**

使用 Aspose.Cells for Node.js via C++ 创建数据透视图的方法：

1. 添加图表。
1. 将图表的数据源设置为引用电子表格中的现有数据透视表。
1. 设置其他属性。

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "PivotTables-CreatePivotTablesPivotCharts-CreatePivotChart-1.js" >}}

