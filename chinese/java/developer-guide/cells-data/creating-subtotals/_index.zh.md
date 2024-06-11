---
title: 创建分类汇总
type: docs
weight: 50
url: /zh/java/creating-subtotals/
---

{{% alert color="primary" %}}

您可以自动为电子表格中的任何重复值创建分类汇总。Aspose.Cells提供了API功能，可帮助您以编程方式向电子表格添加分类汇总。

{{% /alert %}}

## **使用Microsoft Excel**

在 Microsoft Excel 中创建分类汇总：

1. 在工作簿的第一个工作表中创建一个简单的数据列表（如下图所示），并将文件保存为 Book1.xls。
1. 选择列表中的任何单元格。
1. 从“数据”菜单中选择“分类汇总”选项。
   分类汇总对话框将显示出来。定义要使用的函数以及放置分类汇总的位置。

   选择要添加分类汇总的数据范围

![todo:image_alt_text](creating-subtotals_1.png)

分类汇总对话框 

![todo:image_alt_text](creating-subtotals_2.png)

## **使用 Aspose.Cells API**

Aspose.Cells 提供了一个代表 Microsoft Excel 文件的类，[**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)，该类包含一个 [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)，允许访问 Excel 文件中的每个工作表。

工作表由 [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) 类表示。此类提供了广泛的属性和方法用于管理工作表和其他对象。每个工作表都由一个 [**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) 集合组成。要在工作表中创建分类汇总，使用 [**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) 类的 subtotal 方法。为方法的参数提供适当的值，以获得所需的结果。

下面的示例显示了如何在模板文件（Book1.xls）的第一个工作表中使用 Aspose.Cells API 创建分类汇总。

执行代码后，将创建包含分类汇总的工作表。

应用分类汇总 

![todo:image_alt_text](creating-subtotals_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-CreatingSubtotals-CreatingSubtotals.java" >}}
