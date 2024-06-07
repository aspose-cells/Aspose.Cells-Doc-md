---
title: 在Aspose.Cells中设置工作表选项卡颜色
type: docs
weight: 90
url: /zh/java/set-worksheet-tab-color-in-aspose-cells/
---

## **Aspose.Cells - 设置工作表选项卡颜色**
Aspose.Cells允许您更改个别工作表标签的颜色，使其在其他工作表中突出显示。例如，您可以将Expenses设为红色，Sales设为绿色，Assets设为蓝色等。
#### **使用Microsoft Excel设置工作表标签颜色**
1. 在当前工作表底部的选项卡表中右键单击一个选项卡。
1. 选择**选项卡颜色**。
1. 从调色板中选择一种颜色。
1. 单击**确定**。

**Java**

{{< highlight java >}}

 //Instantiate a new Workbook

Workbook workbook = new Workbook(dataPath + "workbook.xls");

//Get the first worksheet in the book

Worksheet worksheet = workbook.getWorksheets().get(0);

//Set the tab color

worksheet.setTabColor(Color.getRed());

//Save the Excel file

workbook.save(dataPath + "AsposeColoredTab_Out.xls");

{{< /highlight >}}
## **下载运行代码**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **下载示例代码**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/asposefeatures/worksheets/SetWorksheetTabColor.java)

{{% alert color="primary" %}} 

有关详细信息，请访问[设置工作表选项卡颜色](/java/set-worksheet-tab-color)。

{{% /alert %}}
