---
title: 透视表和源数据
type: docs
weight: 110
url: /zh/java/pivot-table-and-source-data/
---

## **透视表的源数据**
有时，您希望创建能从不同数据源(如数据库)获取数据的Microsoft Excel报告中的数据透视表，但这些数据源在设计时是不确定的。本文提供了一种动态更改数据透视表数据源的方法。
## **更改透视表的数据源**
1. 创建一个新的设计模板。
   1. 创建一个新的设计模板文件，如下面的屏幕截图所示。
   1. 然后定义一个名为**DataSource**的命名范围，该范围引用这些单元格。 

      **创建设计模板并定义命名范围，数据源** 

![todo:image_alt_text](pivot-table-and-source-data_1.png)

1. 基于该命名范围创建数据透视表。
   1. 在Microsoft Excel中，选择**数据**，然后选择**数据透视表**和**数据透视图报表**。
   1. 根据第一步中创建的命名范围创建数据透视表。 

      **基于命名范围创建数据透视表，数据源** 

![todo:image_alt_text](pivot-table-and-source-data_2.png)

1. 将相应字段拖放到数据透视表的行和列中，然后按照下面的截图创建结果的数据透视表。 

   **基于相应字段创建数据透视表** 

![todo:image_alt_text](pivot-table-and-source-data_3.png)

1. 右键单击数据透视表，然后选择**表选项**。
   1. 在**数据选项**设置中选择**打开时刷新**。 

      **设置数据透视表选项** 

![todo:image_alt_text](pivot-table-and-source-data_4.png)



现在，您可以将此文件保存为您的设计模板文件。

1. 填充新数据并更改数据透视表的源数据。
   1. 一旦设计模板创建完成，使用以下代码修改数据透视表的源数据。

执行下面的示例代码将更改数据透视表的源数据，数据透视表将如下所示。

**动态更改的数据透视表** 

![todo:image_alt_text](pivot-table-and-source-data_5.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-ChangeSourceData-ChangeSourceData.java" >}}
{{< app/cells/assistant language="java" >}}
