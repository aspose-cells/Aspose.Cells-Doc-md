---
title: 各ワークシートを異なる PDF に保存
type: docs
weight: 10
url: /ja/net/save-each-worksheet-to-different-pdf/
---

## **Aspose.Cells - 各ワークシートを異なる PDF に保存**
Aspose.Cells は、XLS ファイル（画像、グラフなどを含む）を PDF ドキュメントに変換することをサポートしています。Aspose.Cells for .NET は、単体でスプレッドシートを PDF ドキュメントに変換でき、変換にはもはや Aspose.Pdf for .NET を使用する必要はありません。変換には一時ファイルの作成/使用も必要ありません。なぜなら、全体のプロセスがメモリ内で行われるからです。

**C#**

{{< highlight cs >}}

 //Instantiate a new workbook and open the Excel

//File from its location

Workbook workbook = new Workbook("../../data/test.xlsx");

//Get the count of the worksheets in the workbook

int sheetCount = workbook.Worksheets.Count;

//Make all sheets invisible except first worksheet

for (int i = 1; i < workbook.Worksheets.Count; i++)

{

    workbook.Worksheets[i].IsVisible = false;

}

//Take Pdfs of each sheet

for (int j = 0; j < workbook.Worksheets.Count; j++)

{

    Worksheet ws = workbook.Worksheets[j];

    workbook.Save(ws.Name + ".pdf");

    if (j < workbook.Worksheets.Count - 1)

    {

        workbook.Worksheets[j + 1].IsVisible = true;

        workbook.Worksheets[j].IsVisible =false;

    }

}

{{< /highlight >}}
## **ランニングコードのダウンロード**
以下のソーシャルコーディングサイトから**各ワークシートを異なる PDF に保存**をダウンロードしてください。

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/AsposeCellsFeaturesMissinginNPOI_v1.0/Save.Each.Worksheet.to.Different.PDF.Aspose.Cells.zip)

{{% alert color="primary" %}} 

詳細については、[各ワークシートを別の PDF ファイルに保存](https://docs.aspose.com/cells/net/save-each-worksheet-to-a-different-pdf-file/)をご覧ください。

{{% /alert %}}
