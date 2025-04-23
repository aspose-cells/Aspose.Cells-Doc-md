---
title: Aspose.Cellsを使用した合計計算
type: docs
weight: 20
url: /ja/java/calculate-sub-totals-using-aspose-cells/
---

## **Aspose.Cells - 小計の計算**
スプレッドシート内の繰り返し値に自動的に小計を作成できます。Aspose.Cellsには、スプレッドシートに小計をプログラムで追加するのに役立つAPI機能が備わっています。

**Java**

{{< highlight java >}}

 //Instantiate a new workbook

Workbook workbook = new Workbook("book1.xls");

//Get the Cells collection in the first worksheet

Cells cells = workbook.getWorksheets().get(0).getCells();

//Create a cellarea i.e.., B3:C19

CellArea ca = new CellArea();

ca.StartRow = 2;

ca.StartColumn =1;

ca.EndRow = 18;

ca.EndColumn = 2;

//Apply subtotal, the consolidation function is Sum and it will applied to

//Second column (C) in the list

cells.subtotal(ca, 0, ConsolidationFunction.SUM, new int[] { 1 });

//Save the excel file

workbook.save("AsposeTotal.xls");

{{< /highlight >}}
## **ランニングコードのダウンロード**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **サンプルコードをダウンロード**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/asposefeatures/formula/AsposeCreateSubTotals.java)

{{% alert color="primary" %}} 

詳細については、[小計の作成](/cells/ja/java/creating-subtotals) をご覧ください。

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
