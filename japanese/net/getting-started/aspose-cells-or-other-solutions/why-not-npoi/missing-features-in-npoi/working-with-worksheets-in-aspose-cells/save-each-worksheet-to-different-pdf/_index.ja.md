---
title: 各ワークシートを異なる PDF に保存
type: docs
weight: 10
url: /ja/net/save-each-worksheet-to-different-pdf/
---
## **Aspose.Cells - 各ワークシートを別の PDF に保存**
Aspose.Cells は、XLS ファイル (画像、チャートなどを含む) の PDF ドキュメントへの変換をサポートしています。 Aspose.Cells for .NET は、スプレッドシートを Pdf ドキュメントに変換するために独立して機能し、変換に Aspose.Pdf for .NET を使用する必要がなくなりました。プロセス全体をメモリ内で実行できるため、変換では一時ファイルを作成/使用する必要はありません。

**C#**

{{< highlight "cs" >}}

//新しいワークブックをインスタンス化し、Excel を開く

//その場所からのファイル

Workbook workbook = new Workbook("../../data/test.xlsx");

//ブック内のワークシートの数を取得します

int sheetCount = workbook.Worksheets.Count;

//最初のワークシートを除くすべてのシートを非表示にします

for (int i = 1; i< workbook.Worksheets.Count; i++)

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
## **実行中のコードをダウンロード**
ダウンロード**各ワークシートを異なる PDF に保存**以下のソーシャル コーディング サイトのいずれかを形成します。

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/AsposeCellsFeaturesMissinginNPOI_v1.0/Save.Each.Worksheet.to.Different.PDF.Aspose.Cells.zip)

{{% alert color="primary" %}} 

詳細については、次を参照してください。[各ワークシートを異なる PDF ファイルに保存する](https://docs.aspose.com/cells/net/save-each-worksheet-to-a-different-pdf-file/).

{{% /alert %}}
