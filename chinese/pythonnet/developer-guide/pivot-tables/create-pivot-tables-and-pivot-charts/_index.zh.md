---
title: 创建数据透视表和数据透视图
type: docs
weight: 20
url: /zh/python-net/create-pivot-tables-and-pivot-charts/
description: 如何使用 Aspose.Cells for Python 通过 .NET 添加数据透视表和数据透视图
keywords: Aspose.Cells for Python Excel，Excel Python 库，使用 Aspose.Cells for Python Excel 库添加数据透视表和数据透视图。
---

{{% alert color="primary" %}}

数据透视表是记录的交互式摘要。例如，您可能在工作表的列表中有数百个发票条目。数据透视表可以按客户、产品或日期对发票进行汇总。使用 Microsoft Excel，可以通过将按钮拖动到新位置来快速重新排列数据透视表中的信息。

数据透视图是数据透视表中数据的交互式图形表示。数据透视图是在 Excel 2000 中引入的。使用数据透视图可以更容易地理解数据，因为数据透视表会自动创建小计和合计。

Aspose.Cells for Python 通过 .NET 支持 [数据透视表](/cells/zh/python-net/create-pivot-tables-and-pivot-charts/) 和 [数据透视图](/cells/zh/python-net/create-pivot-tables-and-pivot-charts/)。

{{% /alert %}}

## **使用 Aspose.Cells for Python Excel 库添加数据透视表和数据透视图**

Aspose.Cells for Python 通过 .NET 提供了一组特殊的类，用于创建数据透视表。这些类用于创建和设置 PivotTable 对象，作为 PivotTable 对象的基本构建块：

- PivotField，数据透视表报告中的字段。
- PivotFields，数据透视表中所有PivotField对象的集合。
- PivotTable，工作表上的数据透视表报告。
- PivotTables，工作表上所有PivotTable对象的集合。

### **准备使用 Aspose.Cells for Python 通过 .NET**
1. 从 [pypi](https://pypi.org/project/aspose-cells-python/) 安装 Aspose.Cells for Python 通过 .NET，使用以下命令: $ pip install aspose-cells-python。
1. 您还可以按步骤执行有关如何将“Aspose.Cells for Python通过.NET”安装到您的开发环境中的说明。


### **使用Aspose.Cells for Python Excel库添加数据透视表**

使用Aspose.Cells for Python通过.NET创建数据透视表：

1. 使用Cell对象的put_value方法向工作表单元格添加一些数据。您还可以使用已填充数据的模板文件。数据将用作数据透视表的数据源。
1. 通过调用PivotTables集合的add方法（封装在Worksheet对象中）向工作表添加一个数据透视表。
1. 通过传递其索引从PivotTables集合中访问新的PivotTable对象。# 使用数据透视表对象封装的任何数据透视表对象来管理数据表。

以下是代码示例。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-CreatePivotTablesPivotCharts-CreatePivotTable-1.py" >}}

### **使用Aspose.Cells for Python Excel库添加数据透视图**

使用Aspose.Cells for Python通过.NET创建数据透视图：

1. 添加一个图表。
1. 将图表的PivotSource设置为引用电子表格中现有的数据透视表。
1. 设置其他属性。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-CreatePivotTablesPivotCharts-CreatePivotChart-1.py" >}}

