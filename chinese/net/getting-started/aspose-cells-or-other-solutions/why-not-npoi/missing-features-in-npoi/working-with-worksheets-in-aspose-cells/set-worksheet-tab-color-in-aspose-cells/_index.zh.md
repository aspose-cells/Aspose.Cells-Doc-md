---
title: 在 Aspose.Cells 中设置工作表标签颜色
type: docs
weight: 20
url: /zh/net/set-worksheet-tab-color-in-aspose-cells/
---

## **Aspose.Cells - 设置工作表标签颜色**
Aspose.Cells允许您更改单个工作表标签的颜色，使其与其他工作表区分开。例如，您可以将支出设置为红色，销售设置为绿色，资产设置为蓝色，等等。
### **使用Microsoft Excel设置工作表标签颜色**
1. 在当前工作表底部的标签工作表上右键单击。
1. 选择**标签颜色**。
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
从以下任何社交编码网站下载**设置工作表标签颜色**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/AsposeCellsFeaturesMissinginNPOI_v1.0/Set.Worksheet.Tab.Color.Aspose.Cells.zip)

{{% alert color="primary" %}} 

更多详情，请访问[设置工作表标签颜色](/cells/zh/net/set-worksheet-tab-color/)

{{% /alert %}}
