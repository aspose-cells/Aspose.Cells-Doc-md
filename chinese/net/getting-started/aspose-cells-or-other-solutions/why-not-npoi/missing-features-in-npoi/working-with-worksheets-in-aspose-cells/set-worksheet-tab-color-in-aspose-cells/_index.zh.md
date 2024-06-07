---
title: 在Aspose.Cells中设置工作表选项卡颜色
type: docs
weight: 20
url: /zh/net/set-worksheet-tab-color-in-aspose-cells/
---

## **Aspose.Cells - 设置工作表选项卡颜色**
Aspose.Cells允许您更改个别工作表标签的颜色，使其在其他工作表中突出显示。例如，您可以将Expenses设为红色，Sales设为绿色，Assets设为蓝色等。
### **使用Microsoft Excel设置工作表标签颜色**
1. 在当前工作表底部的选项卡表中右键单击一个选项卡。
1. 选择**选项卡颜色**。
1. 从调色板中选择一种颜色。
1. 单击**确定**。

**C#**

{{< highlight cs >}}

 //Instantiate a new Workbook

Workbook workbook = new Workbook("../../data/test.xlsx");

//Get the first worksheet in the book

Worksheet worksheet = workbook.Worksheets[0];

//Set the tab color

worksheet.TabColor = Color.Red;

//Save the Excel file

workbook.Save("AsposeColoredTab_Out.xls");

{{< /highlight >}}
## **下载运行代码**
从以下提到的任何社交编码网站下载**设置工作表标签颜色**：

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/AsposeCellsFeaturesMissinginNPOI_v1.0/Set.Worksheet.Tab.Color.Aspose.Cells.zip)

{{% alert color="primary" %}} 

有关更多详细信息，请访问[设置工作表标签颜色](/cells/zh/net/set-worksheet-tab-color/)。

{{% /alert %}}
