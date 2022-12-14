---
title: 在 Cells 中寻找价值
type: docs
weight: 20
url: /zh/net/find-value-in-cells/
---
## **Aspose.Cells - 在 Cells 中寻找价值**
在 Microsoft Excel 中，用户可以搜索包含特定数据的单元格。例如，点击**编辑**接着**寻找**打开搜索对话框。用户输入一个值并点击**好的**搜索它。 Excel 突出显示匹配字段。

**C#**

{{< highlight "cs" >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook("../../data/test.xlsx");

//Accessing the first worksheet in the Excel file

Worksheet worksheet = workbook.Worksheets[0];

//Finding the cell containing the specified formula

Cells cells = worksheet.Cells;

//Instantiate FindOptions

FindOptions findOptions = new FindOptions();

//Finding the cell containing a string value that starts with "Or"

findOptions.LookAtType = LookAtType.StartWith;

Cell cell = cells.Find("SH", null, findOptions);

//Printing the name of the cell found after searching worksheet

Console.WriteLine("Name of the cell containing String: " + cell.Name);

{{< /highlight >}}
## **下载运行代码**
下载**在 Cells 中寻找价值**形成以下任何一个社交编码网站：

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/AsposeCellsFeaturesMissinginNPOI_v1.0/Find.Value.In.Cells.Aspose.Cells.zip)

{{% alert color="primary" %}} 

欲了解更多详情，请访问[查找或搜索数据](/cells/zh/net/find-or-search-data/).

{{% /alert %}}
