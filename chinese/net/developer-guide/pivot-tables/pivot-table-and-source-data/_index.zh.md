---
title: 数据透视表和源数据
type: docs
weight: 30
url: /zh/net/pivot-table-and-source-data/
---

## **数据透视表的源数据**

有时候您想要创建从不同数据源(如数据库)获取数据的数据透视表的Microsoft Excel报表，这些数据源在设计时是未知的。本文提供了一种动态更改数据透视表数据源的方法。

### **更改数据透视表的数据源**

1. 创建一个新的设计模板。
   1. 创建一个新的设计模板文件，如下面的屏幕截图所示。
   1. 然后定义一个名为**DataSource**的命名范围，该范围指向这些单元格。

      **创建一个设计模板并定义名为DataSource的命名范围** 

![todo:image_alt_text](pivot-table-and-source-data_1.png)

1. 基于这个命名范围创建一个数据透视表。
   1. 在Microsoft Excel中，选择**数据**，然后选择**数据透视表**和**数据透视图和图表报告**。
   1. 基于第一步创建的命名范围创建一个数据透视表。

      **基于名为DataSource的命名范围创建数据透视表** 

![todo:image_alt_text](pivot-table-and-source-data_2.png)


   1. 将相应字段拖动到数据透视表的行和列中，然后创建结果数据透视表，如下面的屏幕截图所示。

   **基于相应字段创建数据透视表** 

![todo:image_alt_text](pivot-table-and-source-data_3.png)


1. 右键单击数据透视表，然后选择**表选项**。
   1. 在**数据选项**设置中的**刷新时打开**中勾选。

      **设置数据透视表选项** 

![todo:image_alt_text](pivot-table-and-source-data_4.png)


现在，您可以将此文件保存为您的设计模板文件。

1. 填充新数据和更改数据透视表的源数据。
   1. 创建设计模板后，使用以下代码更改数据透视表的源数据。

执行下面的示例代码将更改数据透视表的源数据。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTable-ChangeSourceData-1.cs" >}}

