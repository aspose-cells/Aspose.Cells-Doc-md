---
title: 在 xlsx4j 中设置工作表选项卡颜色
type: docs
weight: 60
url: /zh/java/set-worksheet-tab-color-in-xlsx4j/
---
## **Aspose.Cells - 设置工作表标签颜色**
Aspose.Cells 允许您更改单个工作表选项卡的颜色，使它们在其余部分中突出显示。例如，您可以使费用为红色、销售为绿色、资产为蓝色等。
### **使用 Microsoft Excel 设置工作表选项卡颜色**
1. 右键单击当前工作表底部选项卡中的选项卡。
1. 选择**标签颜色**.
1. 从调色板中选择一种颜色。
1. 点击**好的**.

**Java**

{{< highlight "java" >}}

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

欲了解更多详情，请访问[设置工作表标签颜色](/java/set-worksheet-tab-color).

{{% /alert %}}
