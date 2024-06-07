---
title: 创建小计
type: docs
weight: 50
url: /zh/java/creating-subtotals/
---

{{% alert color="primary" %}}

您可以为电子表格中任何重复值自动创建小计。Aspose.Cells提供了API功能，帮助您以编程方式添加小计。

{{% /alert %}}

## **使用Microsoft Excel**

在Microsoft Excel中创建小计：

1.在工作簿的第一个工作表中创建一个简单的数据列表（如下图所示），并将文件保存为Book1.xls。
1.选择列表中的任何单元格。
1. 从“数据”菜单中选择“小计”。
   将显示小计对话框。定义要使用的功能和放置小计的位置。

   **选择添加小计的数据范围**

![todo:image_alt_text](creating-subtotals_1.png)

**小计对话框** 

![todo:image_alt_text](creating-subtotals_2.png)

## **使用Aspose.Cells API**

Aspose.Cells提供了一个表示Microsoft Excel文件的类[**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)。[**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)类包含一个[**WorksheetCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection)，允许访问Excel文件中的每个工作表。

工作表由[**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)类表示。该类提供了一个广泛的属性和方法集，用于管理工作表和其他对象。每个工作表由一个[**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)集合组成。要在工作表中创建小计，请使用[**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)类的subtotal方法。为方法的参数提供适当的值以获得所需的结果。

下面的示例演示了如何在模板文件（Book1.xls）的第一个工作表中使用Aspose.Cells API创建小计。

执行代码时，将创建带子汇总的工作表。

**应用小计** 

![todo:image_alt_text](creating-subtotals_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-CreatingSubtotals-CreatingSubtotals.java" >}}
