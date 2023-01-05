---
title: 在 Aspose.Cells 中设置工作表选项卡颜色
type: docs
weight: 20
url: /zh/net/set-worksheet-tab-color-in-aspose-cells/
---
## **Aspose.Cells - 设置工作表标签颜色**
Aspose.Cells 允许您更改单个工作表选项卡的颜色，使它们在其余部分中突出显示。例如，您可以使费用为红色、销售为绿色、资产为蓝色等。
### **使用 Microsoft Excel 设置工作表选项卡颜色**
1. 右键单击当前工作表底部选项卡中的选项卡。
1. 选择**标签颜色**.
1. 从调色板中选择一种颜色。
1. 点击**好的**.

**C#**

{{< highlight "cs" >}}

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
下载**设置工作表标签颜色**形成以下任何一个社交编码网站：

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/AsposeCellsFeaturesMissinginNPOI_v1.0/Set.Worksheet.Tab.Color.Aspose.Cells.zip)

{{% alert color="primary" %}} 

欲了解更多详情，请访问[设置工作表标签颜色](/cells/zh/net/set-worksheet-tab-color/).

{{% /alert %}}
