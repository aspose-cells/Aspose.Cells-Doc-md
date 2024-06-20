---
title: Aspose.Cellsでワークブックを印刷
type: docs
weight: 20
url: /ja/net/printing-workbooks-in-aspose-cells/
---

## **Aspose.Cells - ワークブックの印刷**
スプレッドシートの作成が完了したら、必要に応じてシートの印刷を行いたいと思うでしょう。印刷を行う際、MS Excelは特定の選択を指定しない限り、ワークシート全体を印刷するものと見なします。

ワークシートの印刷

**C#**

{{< highlight cs >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook("../../data/test.xlsx");

//Create an object for ImageOptions

ImageOrPrintOptions imgOptions = new ImageOrPrintOptions();

//Get the first worksheet

Worksheet sheet = workbook.Worksheets[0];

//Create a SheetRender object with respect to your desired sheet

SheetRender sr = new SheetRender(sheet, imgOptions);

//Print the worksheet

sr.ToPrinter("Samsung ML-1520 Series");

{{< /highlight >}}
## **ランニングコードのダウンロード**
以下のいずれかのソーシャルコーディングサイトから**ワークブックの印刷**をダウンロードしてください。

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/AsposeCellsFeaturesMissinginNPOI_v1.0/Printing.Workbooks.Aspose.Cells.zip)

{{% alert color="primary" %}} 

詳細については、[ワークブックの印刷](/cells/ja/net/printing-workbooks/)をご覧ください。

{{% /alert %}}
