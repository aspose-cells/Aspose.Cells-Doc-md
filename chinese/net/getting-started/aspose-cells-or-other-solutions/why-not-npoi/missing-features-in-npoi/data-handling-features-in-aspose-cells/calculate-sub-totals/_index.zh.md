---
title: 计算小计
type: docs
weight: 10
url: /zh/net/calculate-sub-totals/
---

## **Aspose.Cells - 计算小计**
您可以自动在电子表格中为任何重复值创建小计。 Aspose.Cells提供了API功能，帮助您以编程方式向电子表格添加小计。

**C#**

{{< highlight cs >}}

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

cells.Subtotal(ca, 0, ConsolidationFunction.Sum, new int[] { 1 });

//Save the excel file

workbook.Save("AsposeTotal.xls"); 

{{< /highlight >}}
## **下载运行代码**
从以下任何社交编码网站下载**计算小计**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/AsposeCellsFeaturesMissinginNPOI_v1.0/Calculate.Sub.Totals.Aspose.Cells.zip)

{{% alert color="primary" %}} 

有关详细信息，请访问[创建小计](/cells/zh/net/creating-subtotals/)

{{% /alert %}}
