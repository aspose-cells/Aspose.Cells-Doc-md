---
title: 在 xlsx4j 中设置工作表选项卡颜色
type: docs
weight: 60
url: /zh/java/set-worksheet-tab-color-in-xlsx4j/
---

## **Aspose.Cells - 设置工作表标签颜色**
Aspose.Cells允许您更改单个工作表标签的颜色，使其与其他工作表区分开。例如，您可以将支出设置为红色，销售设置为绿色，资产设置为蓝色，等等。
### **使用Microsoft Excel设置工作表标签颜色**
1. 在当前工作表底部的标签工作表上右键单击。
1. 选择**标签颜色**。
1. 从调色板中选择一种颜色。
1. 单击**确定**。

**Java**

{{< highlight java >}}

 //Instantiate a new Workbook

Workbook workbook = new Workbook(dataDir + "workbook.xls");

//Get the first worksheet in the book

Worksheet worksheet = workbook.getWorksheets().get(0);

//Set the tab color

worksheet.setTabColor(Color.getRed());

//Save the Excel file

workbook.save(dataDir + "AsposeColoredTab_Out.xls");

{{< /highlight >}}
## **下载运行代码**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Xlsx4j-v1.0.0)
## **下载示例代码**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Xlsx4j/src/main/java/com/aspose/cells/examples/asposefeatures/worksheets/settabcolor/AsposeSetWorksheetTabColor.java)

{{% alert color="primary" %}} 

查看更多详情，请访问[设置工作表选项卡颜色](/java/set-worksheet-tab-color)。

{{% /alert %}}
