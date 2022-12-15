---
title: 数据透视表和源数据
type: docs
weight: 110
url: /zh/java/pivot-table-and-source-data/
---
## **数据透视表的源数据**
有时您想要创建 Microsoft Excel 报告，其中包含从设计时未知的不同数据源（例如数据库）获取数据的数据透视表。本文提供了一种动态更改数据透视表数据源的方法。
## **更改数据透视表的源数据**
1. 创建一个新的设计器模板。
1. 如下图所示创建一个新的设计器模板文件。
 1.然后定义一个命名范围，**数据源**，它指的是这个单元格范围。

      **创建设计器模板并定义命名范围、DataSource** 

![待办事项：图像_替代_文本](pivot-table-and-source-data_1.png)

1. 基于这个命名范围创建数据透视表。
 1. 在 Microsoft Excel 中，选择**数据**， 然后**数据透视表**和**数据透视图报表**.
1. 根据第一步创建的命名范围创建数据透视表。

      **基于命名范围 DataSource 创建数据透视表** 

![待办事项：图像_替代_文本](pivot-table-and-source-data_2.png)

1. 将相应的字段拖动到数据透视表的行和列，然后创建结果数据透视表，如下面的屏幕截图所示。

   **根据相应字段创建数据透视表** 

![待办事项：图像_替代_文本](pivot-table-and-source-data_3.png)

1. 右键单击数据透视表并选择**表格选项**.
1. 检查**打开时刷新**在**数据选项**设置。

      **设置数据透视表选项** 

![待办事项：图像_替代_文本](pivot-table-and-source-data_4.png)



现在，您可以将此文件保存为设计器模板文件。

1. 填充新数据和更改数据透视表的源数据。
1. 创建设计器模板后，使用以下代码更改数据透视表的源数据。

执行下面的示例代码会更改数据透视表的源数据，数据透视表将如下所示。

**动态变化的数据透视表** 

![待办事项：图像_替代_文本](pivot-table-and-source-data_5.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-ChangeSourceData-ChangeSourceData.java" >}}
