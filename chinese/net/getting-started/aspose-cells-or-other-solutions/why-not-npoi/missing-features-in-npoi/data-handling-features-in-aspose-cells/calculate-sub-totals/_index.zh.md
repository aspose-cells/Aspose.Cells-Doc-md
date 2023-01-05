---
title: 计算小计
type: docs
weight: 10
url: /zh/net/calculate-sub-totals/
---
## **Aspose.Cells - 计算小计**
您可以为电子表格中的任何重复值自动创建小计。 Aspose.Cells 提供 API 功能，可帮助您以编程方式将小计添加到电子表格。

**C#**

{{< highlight "cs" >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook("../../data/test.xlsx");

//Get the Cells collection in the first worksheet

Cells cells = workbook.Worksheets[0].Cells;

//Create a cellarea i.e.., B3:C19

CellArea ca = new CellArea();

ca.StartRow = 2;

ca.StartColumn = 1;

ca.EndRow = 18;

ca.EndColumn = 2;

//Apply subtotal, the consolidation function is Sum and it will applied to

//Second column (C) in the list

cells.Subtotal(ca, 0, ConsolidationFunction.Sum, new int[]{ 1 });

//Save the excel file

workbook.Save("AsposeTotal.xls"); 

{{< /highlight >}}
## **下载运行代码**
下载**计算小计**形成以下任何一个社交编码网站：

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/AsposeCellsFeaturesMissinginNPOI_v1.0/Calculate.Sub.Totals.Aspose.Cells.zip)

{{% alert color="primary" %}} 

欲了解更多详情，请访问[创建小计](/cells/zh/net/creating-subtotals/).

{{% /alert %}}
