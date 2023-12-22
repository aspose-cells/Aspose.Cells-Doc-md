---
title: 创建数据透视表和数据透视图
type: docs
weight: 20
url: /zh/python-net/create-pivot-tables-and-pivot-charts/
description: 如何使用 Aspose.Cells for Python via .NET 添加数据透视表和数据透视图。
keywords: Add Pivot Tables and Pivot Charts.
---
{{% alert color="primary" %}}

数据透视表是记录的交互式摘要。例如，工作表的列表中可能有数百个发票条目。数据透视表可以按客户、产品或日期汇总发票。使用 Microsoft Excel，可以通过将按钮拖动到新位置来快速重新排列数据透视表中的信息。

数据透视图是数据透视表中数据的交互式图形表示。数据透视图是在 Excel 2000 中引入的。使用数据透视图可以更轻松地理解数据，因为数据透视表会自动创建小计和总计。

 Aspose.Cells for Python via .NET 支持[数据透视表](/cells/zh/python-net/create-pivot-tables-and-pivot-charts/)和[数据透视图](/cells/zh/python-net/create-pivot-tables-and-pivot-charts/).

{{% /alert %}}

##  **添加数据透视表和图表**

Aspose.Cells for Python via .NET 提供了一组用于创建数据透视表的特殊类。这些类用于创建和设置数据透视表对象，这些对象充当数据透视表对象的基本构建块：

- PivotField，数据透视表报表中的字段。
- PivotFields，数据透视表中所有 PivotField 对象的集合。
- 数据透视表，工作表上的数据透视表。
- 数据透视表，工作表上所有数据透视表对象的集合。

###  **准备使用 Aspose.Cells for Python via .NET**
1. 安装 Aspose.Cells for Python via .NET 从[皮皮](https://pypi.org/project/aspose-cells-python/)，使用命令为：$ pip install aspose-cells-python。
1. 您还可以按照有关如何将“Aspose.Cells for Python via .NET”安装到开发人员环境的分步说明进行操作。


###  **添加数据透视表**

要使用 Aspose.Cells for Python via .NET 创建数据透视表：

1. 使用 Cell 对象的 put_value 方法将一些数据添加到工作表单元格。您还可以使用已填充数据的模板文件。该数据将用作数据透视表的数据源。
1. 通过调用 PivotTables 集合的 add 方法（封装在 Worksheet 对象中）将数据透视表添加到工作表中。
1. 通过传递索引从数据透视表集合中访问新的数据透视表对象。 # 使用封装在数据透视表对象中的任意数据透视表对象来管理表。

下面给出了代码示例。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-CreatePivotTablesPivotCharts-CreatePivotTable-1.py" >}}

###  **添加数据透视图**

要使用 Aspose.Cells for Python via .NET 创建数据透视图：

1. 添加图表。
1. 设置图表的 PivotSource 以引用电子表格中的现有数据透视表。
1. 设置其他属性。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-CreatePivotTablesPivotCharts-CreatePivotChart-1.py" >}}

