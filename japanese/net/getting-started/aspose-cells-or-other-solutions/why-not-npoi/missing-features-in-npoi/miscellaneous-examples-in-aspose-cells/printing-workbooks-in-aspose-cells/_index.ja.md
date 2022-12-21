---
title: Aspose.Cells でワークブックを印刷する
type: docs
weight: 20
url: /ja/net/printing-workbooks-in-aspose-cells/
---
## **Aspose.Cells - ワークブックの印刷**
スプレッドシートの作成が完了したら、必要に応じてシートのハード コピーを印刷することをお勧めします。印刷するとき、MS Excel は、選択を指定しない限り、ワークシート領域全体を印刷すると想定します。

ワークシートの印刷

**C#**

{{< highlight "cs" >}}

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
## **実行中のコードをダウンロード**
ダウンロード**ワークブックの印刷**以下のソーシャル コーディング サイトのいずれかを形成します。

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/AsposeCellsFeaturesMissinginNPOI_v1.0/Printing.Workbooks.Aspose.Cells.zip)

{{% alert color="primary" %}} 

詳細については、次を参照してください。[ワークブックの印刷](/cells/ja/net/printing-workbooks/).

{{% /alert %}}
