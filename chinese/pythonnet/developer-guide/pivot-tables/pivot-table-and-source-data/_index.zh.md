---
title: 透视表和源数据
type: docs
weight: 30
url: /zh/python-net/pivot-table-and-source-data/
description: 本文展示了如何使用Aspose.Cells for Python via .NET更改数据透视表的源数据。
keywords: Aspose.Cells for Python Excel、Excel Python库、如何使用Aspose.Cells for Python Excel库更改数据透视表的源数据。
---

## **透视表的源数据**

有时您希望创建从不同数据源（如数据库）获取数据的透视表的Microsoft Excel报表，在设计时这些数据源是未知的。本文介绍了一种动态更改透视表数据源的方法。

### **更改透视表的数据源**

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

执行下面的示例代码会更改数据透视表的源数据。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTable-ChangeSourceData-1.py" >}}

