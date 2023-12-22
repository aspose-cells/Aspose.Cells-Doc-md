---
title: 数据透视表和源数据
type: docs
weight: 30
url: /zh/python-net/pivot-table-and-source-data/
description: 本文介绍如何使用 Aspose.Cells for Python via .NET 更改数据透视表的源数据。
keywords: Change Pivot Table's Source Data
---
##  **数据透视表的源数据**

有时，您希望使用数据透视表创建 Microsoft Excel 报表，这些数据透视表从设计时未知的不同数据源（例如数据库）获取数据。本文提供了一种动态更改数据透视表数据源的方法。

###  **更改数据透视表的源数据**

1. 创建新的设计器模板。
 1. 创建一个新的设计器模板文件，如下图所示。
 1. 然后定义一个命名范围*DataSource**，它引用该单元格范围。

      **创建设计器模板并定义命名范围、数据源** 

![待办事项：图像_替代_文本](pivot-table-and-source-data_1.png)
   
1. 基于此命名范围创建数据透视表。
1. 在Microsoft Excel中，选择**数据**，然后**数据透视表**和*数据透视图报告**。
 1. 根据第一步中创建的命名范围创建数据透视表。

      **基于命名范围、数据源创建数据透视表** 

![待办事项：图像_替代_文本](pivot-table-and-source-data_2.png)

   
1. 将相应字段拖动到数据透视表行和列，然后创建结果数据透视表，如下图所示。

   **根据相应字段创建数据透视表** 

![待办事项：图像_替代_文本](pivot-table-and-source-data_3.png)

   
1. 右键单击数据透视表并选择*表选项**。
 1. 检查**打开时刷新**在**数据选项**设置。

      **设置数据透视表选项** 

![待办事项：图像_替代_文本](pivot-table-and-source-data_4.png)


现在，您可以将此文件另存为设计器模板文件。

1. 填充新数据并更改数据透视表的源数据。
 1. 创建设计器模板后，使用以下代码更改数据透视表的源数据。

执行下面的示例代码会更改数据透视表的源数据。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTable-ChangeSourceData-1.py" >}}

