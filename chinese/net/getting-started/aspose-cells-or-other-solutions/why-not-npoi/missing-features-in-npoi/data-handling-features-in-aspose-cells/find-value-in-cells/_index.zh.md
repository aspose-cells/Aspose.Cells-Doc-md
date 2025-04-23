---
title: 在单元格中查找数值
type: docs
weight: 20
url: /zh/net/find-value-in-cells/
---

## **Aspose.Cells - 在单元格中查找数值**
在Microsoft Excel中，用户可以搜索包含特定数据的单元格。例如，点击**编辑**然后**查找**打开搜索对话框。用户输入一个值并点击**确定**来搜索它。Excel会高亮显示匹配字段。

**C#**

{{< highlight cs >}}

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
从以下任一社交编码站点下载**在单元格中查找数值**。

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/AsposeCellsFeaturesMissinginNPOI_v1.0/Find.Value.In.Cells.Aspose.Cells.zip)

{{% alert color="primary" %}} 

有关更多详细信息，请访问[查找或搜索数据](/cells/zh/net/find-or-search-data/)。

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}
