---
title: 创建小计
type: docs
weight: 50
url: /zh/java/creating-subtotals/
---
{{% alert color="primary" %}}

您可以为电子表格中的任何重复值自动创建小计。 Aspose.Cells 提供 API 功能，可帮助您以编程方式将小计添加到电子表格。

{{% /alert %}}

## **使用 Microsoft Excel**

要在 Microsoft Excel 中创建小计：

1. 在工作簿的第一个工作表中创建一个简单的数据列表（如下图所示），并将文件保存为Book1.xls。
1. 选择列表中的任何单元格。
1. 来自**数据**菜单，选择**小计**.
显示小计对话框。定义要使用的函数以及放置小计的位置。

   **选择数据范围以添加小计**

![待办事项：图像_替代_文本](creating-subtotals_1.png)

**小计对话框** 

![待办事项：图像_替代_文本](creating-subtotals_2.png)

## **使用 Aspose.Cells API**

Aspose.Cells提供了一个类，[**工作簿**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)表示 Microsoft Excel 文件。这[**工作簿**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)类包含一个[**工作表集合**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection)允许访问 Excel 文件中的每个工作表。

工作表由[**工作表**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)班级。该类提供了广泛的属性和方法来管理工作表和其他对象。每个工作表由一个[**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)收藏。要在工作表中创建小计，请使用[**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)类的小计法。为方法的参数提供适当的值以获得您想要的结果。

下面的示例显示如何使用 Aspose.Cells API 在模板文件 (Book1.xls) 的第一个工作表中创建小计。

执行代码时，将创建一个包含小计的工作表。

**应用小计** 

![待办事项：图像_替代_文本](creating-subtotals_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-CreatingSubtotals-CreatingSubtotals.java" >}}
