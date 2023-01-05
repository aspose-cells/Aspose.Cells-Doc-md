---
title: 小計の計算
type: docs
weight: 10
url: /ja/net/calculate-sub-totals/
---
## **Aspose.Cells - 小計の計算**
スプレッドシートで繰り返される値の小計を自動的に作成できます。 Aspose.Cells は、小計をプログラムでスプレッドシートに追加するのに役立つ API 機能を提供します。

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
## **実行中のコードをダウンロード**
ダウンロード**小計の計算**以下のソーシャル コーディング サイトのいずれかを形成します。

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/AsposeCellsFeaturesMissinginNPOI_v1.0/Calculate.Sub.Totals.Aspose.Cells.zip)

{{% alert color="primary" %}} 

詳細については、次を参照してください。[小計の作成](/cells/ja/net/creating-subtotals/).

{{% /alert %}}
