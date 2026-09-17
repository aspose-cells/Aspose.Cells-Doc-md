---
title: Aspose.Cells for .NET でスパークラインを画像および HTML に変換する
linktitle: Aspose.Cells for .NET でスパークラインを画像および HTML に変換する
description: HtmlSaveOptions を使用して、セルへの埋め込み用に Aspose.Cells のスパークラインをスタンドアロン画像としてレンダリングし、スパークラインを含むワークシートを HTML にエクスポートする方法を学びます。
keywords: Aspose.Cells, .NET, スパークライン, Sparkline.ToImage, Cell.EmbeddedImage, HtmlSaveOptions, スパークラインのレンダリング, スパークラインを画像に変換, スパークラインを HTML にエクスポート
type: docs
weight: 120
url: /ja/net/convert-sparkline-to-image-and-html/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
スパークラインはワークシートのセル内に配置される小型のグラフです。Aspose.Cells を使用すると、各スパークラインをスタンドアロン画像として抽出したり（別のセルや外部レポートに埋め込むため）、スパークラインを含むワークシート全体をブラウザベースの配信向けに HTML にエクスポートしたりすることができます。本記事で使用する `Cell.EmbeddedImage` プロパティは、**Aspose.Cells 26.5 以降**で利用可能です。
{{% /alert %}}

## **Introduction**
スパークラインは、ワークシート内で直接トレンドを視覚化するコンパクトな手段です。Excel ユーザーはそれをその場で確認できますが、現実の多くのシナリオでは、スパークラインをセルから取り出す必要があります。たとえば、別のセルに静的な画像として埋め込んだり、自動化されたメールに添付したり、ウェブに公開される HTML レポートの一部としてレンダリングしたりする場合です。
Aspose.Cells はこれらの両方の操作をサポートしています。`Sparkline.ToImage` メソッドは個々のスパークラインをストリームにレンダリングし、結果のバイト列を `Cell.EmbeddedImage` に割り当てることができるため、その画像がワークブックの単一セル内に保存されます。別途、`HtmlSaveOptions` を使用すると、ワークブック全体（スパークラインを含むすべて）を自己完結型の HTML ファイルに変換できます。本記事では両方のワークフローを順を追って説明します。

## **Workflow 1 — Render Sparklines to Images and Embed Them into Cells**
このワークフローでは、少範囲のソース値を含むワークシートを作成し、3 つの異なるスパークライングループ（Line、Column、および Stacked/Win-Loss）をその範囲に付加し、各グループを PNG としてレンダリングして、その PNG バイト列を隣接するセルに埋め込み画像として書き込みます。最終結果は、ライブスパークラインとそのレンダリングされた画像版の両方を含む単一の `.xlsx` ファイルです。

### **Step-by-Step Instructions**
1. 新しい `Workbook` を作成し、最初の `Worksheet` への参照を取得します。
2. セル `A1` から `E1` に 5 つのサンプル数値（例：日次売上や気温測定値など）を入力します。
3. `worksheet.SparklineGroups.Add(...)` を呼び出して、ワークシートに 3 つの `SparklineGroup` オブジェクトを追加します：
   - `F1` にアンカーされ、データ範囲が `A1:E1` の `SparklineType.Line` グループ。
   - `G1` にアンカーされ、データ範囲が `A1:E1` の `SparklineType.Column` グループ。
   - `H1` にアンカーされ、データ範囲が `A1:E1` の `SparklineType.Stacked`（win/loss）グループ。
4. `ImageOrPrintOptions` インスタンスを作成し、その `ImageType` を `ImageType.Png` に設定して、各スパークラインを PNG 画像としてレンダリングします。
6. ワークブックを `output_with_sparklines.xlsx` として保存します。

```csharp
using System;
using System.IO;
using Aspose.Cells;
using Aspose.Cells.Charts;
using Aspose.Cells.Drawing;
using Aspose.Cells.Rendering;
// Create a new workbook and access the first worksheet
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];
// Populate sample data in cells A1:E1
worksheet.Cells["A1"].PutValue(5);
worksheet.Cells["B1"].PutValue(-3);
worksheet.Cells["C1"].PutValue(8);
worksheet.Cells["D1"].PutValue(-2);
worksheet.Cells["E1"].PutValue(6);
// Add a Line sparkline group anchored at F1 (column 5, row 0)
CellArea lineArea = new CellArea();
lineArea.StartColumn = 5;
lineArea.EndColumn = 5;
lineArea.StartRow = 0;
lineArea.EndRow = 0;
int lineIdx = worksheet.SparklineGroups.Add(SparklineType.Line, "A1:E1", false, lineArea);
// Add a Column sparkline group anchored at G1 (column 6, row 0)
CellArea columnArea = new CellArea();
columnArea.StartColumn = 6;
columnArea.EndColumn = 6;
columnArea.StartRow = 0;
columnArea.EndRow = 0;
int columnIdx = worksheet.SparklineGroups.Add(SparklineType.Column, "A1:E1", false, columnArea);
// Add a Win/Loss (Stacked) sparkline group anchored at H1 (column 7, row 0)
CellArea stackedArea = new CellArea();
stackedArea.StartColumn = 7;
stackedArea.EndColumn = 7;
stackedArea.StartRow = 0;
stackedArea.EndRow = 0;
int stackedIdx = worksheet.SparklineGroups.Add(SparklineType.Stacked, "A1:E1", false, stackedArea);
// Configure image options for PNG output
ImageOrPrintOptions imageOptions = new ImageOrPrintOptions();
imageOptions.ImageType = ImageType.Png;
// Convert the Line sparkline to image and embed it in cell F2
Sparkline lineSp = worksheet.SparklineGroups[lineIdx].Sparklines[0];
using (MemoryStream ms = new MemoryStream())
{
    lineSp.ToImage(ms, imageOptions);
    worksheet.Cells["F2"].EmbeddedImage = ms.ToArray();
}
// Convert the Column sparkline to image and embed it in cell G2
Sparkline columnSp = worksheet.SparklineGroups[columnIdx].Sparklines[0];
using (MemoryStream ms = new MemoryStream())
{
    columnSp.ToImage(ms, imageOptions);
    worksheet.Cells["G2"].EmbeddedImage = ms.ToArray();
}
// Convert the Win/Loss sparkline to image and embed it in cell H2
Sparkline stackedSp = worksheet.SparklineGroups[stackedIdx].Sparklines[0];
using (MemoryStream ms = new MemoryStream())
{
    stackedSp.ToImage(ms, imageOptions);
    worksheet.Cells["H2"].EmbeddedImage = ms.ToArray();
}
// Save the workbook to disk
workbook.Save("output_with_sparklines.xlsx");
```

上記のコードにより、スパークラインの視覚的表現が 2 つの形式で存在するワークブックが生成されます。1 行目に配置されたライブでネイティブなスパークラインと、2 行目の隣接セルに直接埋め込まれた静的な PNG 画像です。画像がファイル自体に格納されているため、ワークブックは埋め込み画像参照が壊れることなくメール送信やアーカイブが可能な単一の自己完結型アーティファクトのままです。

{{% alert color="primary" %}}
各スパークライングループは単一のセルにアンカーされているため、`foreach` で列挙する代わりにインデクサ `group.Sparklines[0]` を通じてアクセスできます。これによりレンダリングコードが簡潔になり、「アンカーセルごとに 1 つのスパークライン」という一般的なパターンと一致します。`Cell.EmbeddedImage` による画像のバイト列保存には Aspose.Cells 26.5 以降が必要です。

## **Workflow 2 — Export the Sparkline Worksheet to HTML**
ワークブックにライブスパークライン（およびオプションで埋め込み画像版）が含まれたら、ワークシート全体を HTML として保存することでウェブに公開できます。`HtmlSaveOptions` クラスはこのエクスポートを制御するためのノブを公開しています。このワークフローでは、ワークフロー 1 で生成された `output_with_sparklines.xlsx` ファイルを再利用して、きれいな単一ページの HTML ドキュメントに変換します。

### **Step-by-Step Instructions**
1. ワークフロー 1 で生成された `output_with_sparklines.xlsx` ファイルが作業ディレクトリ内のディスクに存在することを確認します。
2. そのファイルを新しい `Workbook` インスタンスに読み込みます。
3. `HtmlSaveOptions` をインスタンス化し、その `ExportActiveWorksheetOnly` プロパティを `true` に設定して、結果の HTML ファイルにワークブック全体ではなくアクティブなワークシートのみが含まれるようにします。
4. `workbook.Save("sparklines.html", htmlOptions)` を呼び出して HTML 出力をディスクに書き込みます。

```csharp
using System;
using System.IO;
using Aspose.Cells;
Workbook workbook = new Workbook("output_with_sparklines.xlsx");
HtmlSaveOptions htmlOptions = new HtmlSaveOptions();
htmlOptions.ExportActiveWorksheetOnly = true;
workbook.Save("sparklines.html", htmlOptions);
```

上記のコードは、ワークフロー 1 からのスパークラインを含むワークブックを、ポータブルな HTML ファイルに変換します。スパークライングループは生成された HTML テーブル内にインライン画像としてレンダリングされるため、エンドユーザーは Excel をインストールすることなく任意のモダンブラウザでトレンドを表示できます。`ExportActiveWorksheetOnly` を `true` に設定することで、非表示シートや補助データが誤って公開されることを避け、現在ユーザーに表示されているワークシートのみがエクスポートされます。
{{% /alert %}}

{{% alert color="primary" %}}
`HtmlSaveOptions` クラスには、`ExportHiddenWorksheet`、`ExportImagesAsBase64`、`Encoding` など、出力を微調整するための追加プロパティが用意されています。デプロイメントターゲットに応じてこれらを適宜調整してください。

## **API Summary**
上記のワークフローは、Aspose.Cells の少数の API の組み合わせに依存しています。
- `SparklineGroup` およびコレクションアクセサ `worksheet.SparklineGroups` は、各スパークライングループのタイプ（Line、Column、Stacked）、データ範囲、およびアンカーセルを宣言するために使用されます。本記事では各グループが単一のセルにアンカーされているため、グループは `worksheet.SparklineGroups[i]` を通じてアクセスされます。
- `Sparkline` およびインデクサ `group.Sparklines[0]` は、グループ内の個々のスパークラインを返します。例では各グループが正確に 1 つのスパークラインしか含まないため、`foreach` ループは不要です。
- `Sparkline.ToImage(Stream, ImageOrPrintOptions)` は、スパークラインの画像を提供された `Stream` に書き込むレンダリングメソッドです。このメソッドは `void` を返します。呼び出し後にストリームからバイト列を読み取ります。
- `HtmlSaveOptions.ExportActiveWorksheetOnly`（`bool` 型）は、HTML エクスポートをアクティブなワークシートのみに制限します。単一ページレポートを生成する際に最も一般的に使用される `HtmlSaveOptions` のプロパティの 1 つです。
- `ImageOrPrintOptions.ImageType` は `Aspose.Cells.Drawing` 名前空間に属し、`ToImage` でのレンダリング時およびワークシートを画像に印刷する際に使用される画像形式（たとえば `ImageType.Png`）を選択します。

## **Related Articles**
{{% /alert %}}

{{< app/cells/assistant language="csharp" >}}