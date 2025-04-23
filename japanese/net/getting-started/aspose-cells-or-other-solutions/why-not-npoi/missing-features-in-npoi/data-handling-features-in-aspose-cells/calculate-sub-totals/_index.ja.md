---
title: 小計の計算
type: docs
weight: 10
url: /ja/net/calculate-sub-totals/
---

## **Aspose.Cells - 小計の計算**
スプレッドシート内の繰り返し値に自動的に小計を作成できます。Aspose.Cellsには、スプレッドシートに小計をプログラムで追加するのに役立つAPI機能が備わっています。

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
## **ランニングコードのダウンロード**
以下に記載されているソーシャルコーディングサイトのいずれかから**小計の計算**をダウンロードしてください:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/AsposeCellsFeaturesMissinginNPOI_v1.0/Calculate.Sub.Totals.Aspose.Cells.zip)

{{% alert color="primary" %}} 

詳細については、[サブトータルの作成](/cells/ja/net/creating-subtotals/)をご覧ください。

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}
