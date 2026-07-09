---
title: Aspose.Cells for .NET でスパークラインを画像と HTML に変換する
linktitle: Convert Sparkline to Image and HTML
description: Aspose.Cells のスパークラインをスタンドアロン画像としてレンダリングしてセルに埋め込む方法と、スパークラインを含むワークシートを HtmlSaveOptions を使用して HTML にエクスポートする方法を学びます。
keywords: Aspose.Cells, .NET, スパークライン, Sparkline.ToImage, Cell.EmbeddedImage, HtmlSaveOptions, スパークラインをレンダリング, スパークラインを画像に変換, スパークラインを HTML にエクスポート
type: docs
weight: 120
url: /ja/net/convert-sparkline-to-image-and-html/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
スパークラインはワークシートのセル内に配置される小型のグラフです。Aspose.Cells では、各スパークラインをスタンドアロン画像として抽出して(別のセルや外部レポートに埋め込むため)、さらにスパークラインを含むワークシート全体を HTML にエクスポートしてブラウザベースの配布を行うこともできます。この記事で使用されている `Cell.EmbeddedImage` プロパティは **Aspose.Cells 26.5 以降** で利用可能です。
{{% /alert %}}

## **はじめに**

スパークラインは、ワークシート内で直接トレンドを可視化するコンパクトな手段です。Excel ユーザーはセル内で確認できますが、実際のシナリオではスパークラインをセルから取り出して使用する必要がある場合が多くあります。たとえば、別のセルに静的な画像として埋め込んだり、自動メールに添付したり、Web に公開された HTML レポートの一部としてレンダリングしたりする場合です。

Aspose.Cells はこれら両方の操作をサポートしています。`Sparkline.ToImage` メソッドは個々のスパークラインをストリームにレンダリングし、結果のバイトを `Cell.EmbeddedImage` に割り当てることによって、ワークブックの単一セル内に画像を保存できます。別途、`HtmlSaveOptions` を使用すると、ワークブック全体(スパークラインを含む)を自己完結型の HTML ファイルに変換できます。本記事では両方のワークフローを順を追って説明します。

## **ワークフロー 1 — スパークラインを画像にレンダリングしてセルに埋め込む**

このワークフローでは、少量のソース値を含むワークシートを作成し、その範囲に 3 種類の異なるスパークライングループ(Line、Column、Stacked/Win-Loss)を関連付け、各グループを PNG としてレンダリングし、それらの PNG バイトを隣接するセルに埋め込み画像として書き込みます。最終結果は、ライブスパークラインとそのレンダリングされた画像版の両方を含む単一の `.xlsx` ファイルです。

### **ステップバイステップの手順**

1. 作業ディレクトリを定義し、ディスク上に存在することを確認します。
2. 新しい `Workbook` を作成し、最初の `Worksheet` への参照を取得します。
3. セル `A1` から `E1` に 5 つのサンプル数値(たとえば、日次の売上や気温測定値など)を入力します。
4. `worksheet.SparklineGroups.Add(...)` を呼び出して、ワークシートに 3 つの `SparklineGroup` オブジェクトを追加します。
   - `F1` に固定された、データ範囲 `A1:E1` を持つ `SparklineType.Line` グループ。
   - `G1` に固定された、データ範囲 `A1:E1` を持つ `SparklineType.Column` グループ。
   - `H1` に固定された、データ範囲 `A1:E1` を持つ `SparklineType.Stacked`(勝敗)グループ。
5. `ImageOrPrintOptions` インスタンスを作成し、その `ImageType` を `ImageType.Png` に設定して、各スパークラインが透明な PNG としてレンダリングされるようにします。
6. 3 つのグループのそれぞれについて、`group.Sparklines[0].ToImage(memoryStream, imageOptions)` を使用して単一のスパークラインをレンダリングし、`MemoryStream` を `byte[]` に変換して、配列を `worksheet.Cells["F2"].EmbeddedImage`、`worksheet.Cells["G2"].EmbeddedImage`、および `worksheet.Cells["H2"].EmbeddedImage` にそれぞれ割り当てます。
7. ワークブックを `output_with_sparklines.xlsx` として保存します。

```csharp
using System;
using System.IO;
using Aspose.Cells;
using Aspose.Cells.Charts;
using Aspose.Cells.Drawing;
using Aspose.Cells.Rendering;

// 新しいワークブックを作成し、最初のワークシートにアクセスします
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];

// セル A1:E1 にサンプルデータを入力します
worksheet.Cells["A1"].PutValue(5);
worksheet.Cells["B1"].PutValue(-3);
worksheet.Cells["C1"].PutValue(8);
worksheet.Cells["D1"].PutValue(-2);
worksheet.Cells["E1"].PutValue(6);

// F1（列 5、行 0）にアンカーされた折れ線スパークライングループを追加します
CellArea lineArea = new CellArea();
lineArea.StartColumn = 5;
lineArea.EndColumn = 5;
lineArea.StartRow = 0;
lineArea.EndRow = 0;
int lineIdx = worksheet.SparklineGroups.Add(SparklineType.Line, "A1:E1", false, lineArea);

// G1（列 6、行 0）にアンカーされた縦棒スパークライングループを追加します
CellArea columnArea = new CellArea();
columnArea.StartColumn = 6;
columnArea.EndColumn = 6;
columnArea.StartRow = 0;
columnArea.EndRow = 0;
int columnIdx = worksheet.SparklineGroups.Add(SparklineType.Column, "A1:E1", false, columnArea);

// H1（列 7、行 0）にアンカーされた Win/Loss（積み上げ）スパークライングループを追加します
CellArea stackedArea = new CellArea();
stackedArea.StartColumn = 7;
stackedArea.EndColumn = 7;
stackedArea.StartRow = 0;
stackedArea.EndRow = 0;
int stackedIdx = worksheet.SparklineGroups.Add(SparklineType.Stacked, "A1:E1", false, stackedArea);

// PNG 出力用の画像オプションを設定します
ImageOrPrintOptions imageOptions = new ImageOrPrintOptions();
imageOptions.ImageType = ImageType.Png;

// 折れ線スパークラインを画像に変換し、セル F2 に埋め込みます
Sparkline lineSp = worksheet.SparklineGroups[lineIdx].Sparklines[0];
using (MemoryStream ms = new MemoryStream())
{
    lineSp.ToImage(ms, imageOptions);
    worksheet.Cells["F2"].EmbeddedImage = ms.ToArray();
}

// 縦棒スパークラインを画像に変換し、セル G2 に埋め込みます
Sparkline columnSp = worksheet.SparklineGroups[columnIdx].Sparklines[0];
using (MemoryStream ms = new MemoryStream())
{
    columnSp.ToImage(ms, imageOptions);
    worksheet.Cells["G2"].EmbeddedImage = ms.ToArray();
}

// Win/Loss スパークラインを画像に変換し、セル H2 に埋め込みます
Sparkline stackedSp = worksheet.SparklineGroups[stackedIdx].Sparklines[0];
using (MemoryStream ms = new MemoryStream())
{
    stackedSp.ToImage(ms, imageOptions);
    worksheet.Cells["H2"].EmbeddedImage = ms.ToArray();
}

// ワークブックをディスクに保存します
workbook.Save("output_with_sparklines.xlsx");
```

上記のコードは、スパークラインの各ビジュアル表現が 2 つの形式で複製されたワークブックを生成します。1 行目に固定されたライブのネイティブスパークラインと、2 行目の隣接セルに直接埋め込まれた静的な PNG 画像です。画像がファイル自体に保存されるため、ワークブックは埋め込み画像参照を壊すことなく電子メールで送信したりアーカイブしたりできる、単一の自己完結型アーティファクトのままです。各スパークライングループを PNG としてレンダリングし、`MemoryStream` を `byte[]` に変換して、配列を対象セルの `EmbeddedImage` プロパティに割り当てます。この割り当てによって、画像がセルの保存コンテンツの一部になります。

{{% alert color="primary" %}}
各スパークライングループは単一のセルに固定されているため、`foreach` で列挙する代わりにインデクサ `group.Sparklines[0]` を使用してアクセスできます。これによりレンダリングコードが簡潔になり、一般的な「アンカーセルごとに 1 つのスパークライン」というパターンと一致します。`Cell.EmbeddedImage` を介して画像バイトを保存するには、Aspose.Cells 26.5 以降が必要です。
{{% /alert %}}

## **ワークフロー 2 — スパークラインのワークシートを HTML にエクスポートする**

ワークブックにライブスパークライン(およびオプションで埋め込まれた画像版)が含まれたら、ワークシート全体を HTML として保存することで Web に公開できます。`HtmlSaveOptions` クラスには、このエクスポートを制御するために必要な設定項目が用意されています。このワークフローでは、ワークフロー 1 で生成された `output_with_sparklines.xlsx` ファイルを再利用して、クリーンな単一ページの HTML ドキュメントに変換します。

### **ステップバイステップの手順**

1. ワークフロー 1 で生成された `output_with_sparklines.xlsx` ファイルが、作業ディレクトリ内のディスク上で使用可能であることを確認します。
2. そのファイルを新しい `Workbook` インスタンスにロードします。
3. `HtmlSaveOptions` をインスタンス化し、その `ExportActiveWorksheetOnly` プロパティを `true` に設定して、結果の HTML ファイルにワークブック全体ではなくアクティブなワークシートのみが含まれるようにします。
4. `workbook.Save("sparklines.html", htmlOptions)` を呼び出して、HTML 出力をディスクに書き込みます。

```csharp
using System;
using System.IO;
using Aspose.Cells;

Workbook workbook = new Workbook("output_with_sparklines.xlsx");
HtmlSaveOptions htmlOptions = new HtmlSaveOptions();
htmlOptions.ExportActiveWorksheetOnly = true;
workbook.Save("sparklines.html", htmlOptions);
```

上記のコードは、ワークフロー 1 のスパークラインを含むワークブックを、ポータブルな HTML ファイルに変換します。スパークラインは、エクスポートモードに応じて生成された HTML 内にインライン SVG または PNG レンダリングとして保持されるため、エンドユーザーは Excel がインストールされていない任意のモダンブラウザでトレンドを表示できます。`ExportActiveWorksheetOnly` を `true` に設定することで、非表示シートや補助データを誤って公開することを回避でき、現在ユーザーに表示されているワークシートのみがエクスポートされます。

{{% alert color="primary" %}}
`HtmlSaveOptions` クラスには、`ExportHiddenWorksheet`、`ExportImagesAsBase64`、`Encoding` など、出力を微調整するための追加プロパティがあります。デプロイメントターゲットに応じてこれらを適宜調整してください。
{{% /alert %}}

## **API の概要**

上記のワークフローは、少数の Aspose.Cells API の連携に依存しています。

- `SparklineGroup` およびコレクションアクセッサ `worksheet.SparklineGroups` は、各スパークライングループのタイプ(Line、Column、Stacked)、データ範囲、およびアンカーセルを宣言するために使用されます。本記事では各グループが単一のセルに固定されているため、グループは `worksheet.SparklineGroups[i]` を通じてアクセスされます。
- `Sparkline` およびインデクサ `group.Sparklines[0]` は、グループ内の個々のスパークラインを返します。例のすべてのグループには厳密に 1 つのスパークラインしか含まれていないため、`foreach` ループは必要ありません。
- `Sparkline.ToImage(Stream, ImageOrPrintOptions)` は、スパークラインの画像を提供された `Stream` に書き込むレンダリングメソッドです。このメソッドは `void` を返します。呼び出し後にストリームからバイトを読み取ります。
- `Cell.EmbeddedImage` は、単一セル内に画像を保存する `byte[]` プロパティです。これは **Aspose.Cells 26.5 以降** で利用可能であり、`ToImage` でレンダリングされたスパークラインを同じワークブックにラウンドトリップするための推奨される方法です。
- `HtmlSaveOptions.ExportActiveWorksheetOnly`(`bool` 型)は、HTML エクスポートをアクティブなワークシートのみに制限します。単一ページレポートを生成する際に、`HtmlSaveOptions` で最も一般的に使用されるプロパティの 1 つです。
- `ImageOrPrintOptions.ImageType` は `Aspose.Cells.Drawing` 名前空間にあり、`ToImage` でのレンダリングおよびワークシートの画像への印刷時に使用される画像形式(たとえば `ImageType.Png`)を選択します。

## **関連記事**

- [Aspose.Cells for .NET のスパークライン](/cells/ja/net/sparkline/)
- [セルへの画像の挿入](/cells/ja/net/inserting-an-image-into-a-cell/)
- [SmartMarker 単一セル配列レンダリング | Aspose.Cells .NET](/cells/ja/net/SmartMarker-Single-Cell-Array-Rendering/)

{{< app/cells/assistant language="csharp" >}}