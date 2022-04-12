---
title: Set Worksheet Tab Color in Aspose.Cells
type: docs
weight: 20
url: /net/set-worksheet-tab-color-in-aspose-cells/
---

## **Aspose.Cells - Set Worksheet Tab Color**
Aspose.Cells allows you to change the color of individual worksheet tabs to make them prominent from the rest. For example, you can make Expenses red, Sales green, Assets blue, etc.
### **Setting Worksheet Tab Color with Microsoft Excel**
1. Right-click a tab in the tab-sheet at the bottom of the current worksheet.
1. Select **Tab color**.
1. Select a color from the palette.
1. Click **OK**.

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
## **Download Running Code**
Download **Set Worksheet Tab Color** form any of the below mentioned social coding sites:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/AsposeCellsFeaturesMissinginNPOI_v1.0/Set.Worksheet.Tab.Color.Aspose.Cells.zip)

{{% alert color="primary" %}} 

For more details, visit [Set Worksheet Tab Color](/cells/net/set-worksheet-tab-color/).

{{% /alert %}}
