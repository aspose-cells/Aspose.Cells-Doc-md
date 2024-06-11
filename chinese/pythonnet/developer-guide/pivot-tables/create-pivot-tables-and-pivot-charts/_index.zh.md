---
title: 创建数据透视表和数据透视图
type: docs
weight: 20
url: /zh/python-net/create-pivot-tables-and-pivot-charts/
description: 如何使用Aspose.Cells for Python via .NET添加数据透视表和数据透视图。
keywords: 使用Aspose.Cells for Python Excel库，添加数据透视表和数据透视图。
---

{{% alert color="primary" %}}

数据透视表是记录的互动摘要。例如，您可能有数百个工作表中列表中的发票条目。数据透视表可以按客户、产品或日期总计发票。使用Microsoft Excel，可以通过将按钮拖到新位置，快速重新排列数据透视表中的信息。

数据透视图图表是数据透视表中数据的交互式图形表示。数据透视图图表在Excel 2000中引入。使用数据透视图图表使数据更容易理解，因为数据透视表会自动创建小计和总计。

Aspose.Cells for Python via .NET支持[pivot tables](/cells/zh/python-net/create-pivot-tables-and-pivot-charts/) 和[pivot charts](/cells/zh/python-net/create-pivot-tables-and-pivot-charts/)。

{{% /alert %}}

## **使用Aspose.Cells for Python Excel库添加数据透视表和数据透视图**

Aspose.Cells for Python via .NET提供了一组特殊的类，用于创建数据透视表。这些类用于创建和设置PivotTable对象，作为PivotTable对象的基本构建块：

- PivotField，数据透视表报告中的字段。
- PivotFields，数据透视表中所有 PivotField 对象的集合。
- 一个工作表上的数据透视表。
- 数据透视表是工作表上所有数据透视表对象的集合。

### **准备使用Aspose.Cells for Python via .NET**
从 [pypi](https://pypi.org/project/aspose-cells-python/) 安装 Aspose.Cells for Python via .NET，请使用如下命令：$ pip install aspose-cells-python。
1. 您还可以按照逐步说明，将“Aspose.Cells for Python via .NET”安装到您的开发环境中。


### **使用Aspose.Cells for Python Excel库添加数据透视表的方法**

使用Aspose.Cells for Python via .NET创建数据透视表：

1. 使用Cell对象的put_value方法向工作表单元格添加一些数据。也可以使用填充了数据的模板文件。这些数据将被用作数据透视表的数据源。
1. 通过调用PivotTables集合的add方法（封装在Worksheet对象中）向工作表添加一个数据透视表。
1. 通过传入索引从PivotTables集合中访问新的 PivotTable 对象。# 使用 PivotTable 对象中封装的任何数据透视表对象来管理表。

下面是代码示例。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-CreatePivotTablesPivotCharts-CreatePivotTable-1.py" >}}

### **使用Aspose.Cells for Python Excel库添加数据透视图的方法**

使用Aspose.Cells for Python via .NET创建数据透视图：

1. 添加图表。
1. 将图表的数据源设置为引用电子表格中的现有数据透视表。
1. 设置其他属性。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-CreatePivotTablesPivotCharts-CreatePivotChart-1.py" >}}

