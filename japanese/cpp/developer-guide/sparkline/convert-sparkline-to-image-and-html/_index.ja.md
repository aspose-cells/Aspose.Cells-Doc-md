---
title: Aspose.Cells for C++ でスパークラインを画像および HTML に変換する
linktitle: Aspose.Cells for C++ でスパークラインを画像および HTML に変換する
description: Aspose.Cells のスパークラインをセル埋め込み用の独立した画像としてレンダリングする方法、HtmlSaveOptions を使用してスパークラインを含むワークシートを HTML にエクスポートする方法を学習します。
keywords: Aspose.Cells, C++, スパークライン, Sparkline.ToImage, Cell.EmbeddedImage, HtmlSaveOptions, スパークラインのレンダリング, スパークラインを画像に変換, スパークラインを HTML にエクスポート
type: docs
weight: 120
url: /ja/cpp/convert-sparkline-to-image-and-html/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
スパークラインは、ワークシートのセル内に配置される小型のグラフです。Aspose.Cells では、各 Sparkline を独立した画像として抽出(別のセルや外部レポートへの埋め込み用)したり、スパークラインを含むワークシート全体をブラウザベースの配信向けに HTML にエクスポートしたりすることができます。本記事で使用している `Cell.EmbeddedImage` プロパティは、**Aspose.Cells 26.5 以降**で利用可能です。
{{% /alert %}}

## **Introduction**
スパークラインは、ワークシート内で直接トレンドを可視化するためのコンパクトな手段です。Excel ユーザーはスプレッドシート上でスパークラインを確認しますが、多くの実シナリオではスパークラインをセルから取り出して扱う必要があります。たとえば、別のセルに静的画像として埋め込む、自動メールに添付する、Web に公開される HTML レポートの一部としてレンダリングするといった用途が考えられます。
Aspose.Cells はこれら両方の操作をサポートしています。`Sparkline.ToImage` メソッドは個々の Sparkline を `Vector<uint8_t>` バイト配列にレンダリングし、そのバイトを `Cell.EmbeddedImage` に代入することで、画像をワークブックの単一セル内に保存できます。さらに、`HtmlSaveOptions` を使用すると、ワークブック全体(スパークラインを含むすべて)を自己完結型の HTML ファイルに変換できます。本記事では両方のワークフローを end-to-end で解説します。

## **Workflow 1 — Render Sparklines to Images and Embed Them into Cells**
このワークフローでは、少範囲のソース値を含むワークシートを作成し、3 種類の異なるスパークライン グループ(Line、Column、Stacked/Win-Loss)をその範囲に割り当て、各グループを PNG としてレンダリングして、その PNG バイトを隣接するセルに画像として書き込みます。最終結果は、生きたスパークラインとそのレンダリング画像の両方を含む単一の `.xlsx` ファイルです。

### **Step-by-Step Instructions**
1. 作業ディレクトリを定義し、ディスク上に存在することを確認します。
2. 新しい `Workbook` を作成し、最初の `Worksheet` への参照を取得します。
3. セル `A1` から `E1` に 5 つのサンプル数値(例:日次売上や気温測定値など)を入力します。
4. `worksheet.SparklineGroups.Add(...)` を呼び出して、ワークシートに 3 つの `SparklineGroup` オブジェクトを追加します。
   - `F1` にアンカーされ、データ範囲 `A1:E1` を持つ `SparklineType.Line` グループ。
   - `G1` にアンカーされ、データ範囲 `A1:E1` を持つ `SparklineType.Column` グループ。
   - `H1` にアンカーされ、データ範囲 `A1:E1` を持つ `SparklineType.Stacked`(Win/Loss)グループ。
5. 各スパークラインを透過 PNG としてレンダリングするため、`ImageOrPrintOptions` インスタンスを作成し、その `ImageType` を `ImageType.Png` に設定します。
6. ワークブックを `output_with_sparklines.xlsx` として保存します。

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
int main() {
    Aspose::Cells::Startup();
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    worksheet.GetCells().Get(u"A1").PutValue(5);
    worksheet.GetCells().Get(u"B1").PutValue(-3);
    worksheet.GetCells().Get(u"C1").PutValue(8);
    worksheet.GetCells().Get(u"D1").PutValue(-2);
    worksheet.GetCells().Get(u"E1").PutValue(6);
    CellArea lineArea;
    lineArea.StartColumn = 5;
    lineArea.EndColumn = 5;
    lineArea.StartRow = 0;
    lineArea.EndRow = 0;
    int lineIdx = worksheet.GetSparklineGroups().Add(SparklineType::Line, U16String("A1:E1"), false, lineArea);
    CellArea columnArea;
    columnArea.StartColumn = 6;
    columnArea.EndColumn = 6;
    columnArea.StartRow = 0;
    columnArea.EndRow = 0;
    int columnIdx = worksheet.GetSparklineGroups().Add(SparklineType::Column, U16String("A1:E1"), false, columnArea);
    CellArea stackedArea;
    stackedArea.StartColumn = 7;
    stackedArea.EndColumn = 7;
    stackedArea.StartRow = 0;
    stackedArea.EndRow = 0;
    int stackedIdx = worksheet.GetSparklineGroups().Add(SparklineType::Stacked, U16String("A1:E1"), false, stackedArea);
    ImageOrPrintOptions imageOptions;
    imageOptions.SetImageType(ImageType::Png);
    Sparkline lineSp = worksheet.GetSparklineGroups().Get(lineIdx).GetSparklines().Get(0);
    Vector<uint8_t> lineImg = lineSp.ToImage(imageOptions);
    worksheet.GetCells().Get(u"F2").SetEmbeddedImage(lineImg);
    Sparkline columnSp = worksheet.GetSparklineGroups().Get(columnIdx).GetSparklines().Get(0);
    Vector<uint8_t> columnImg = columnSp.ToImage(imageOptions);
    worksheet.GetCells().Get(u"G2").SetEmbeddedImage(columnImg);
    Sparkline stackedSp = worksheet.GetSparklineGroups().Get(stackedIdx).GetSparklines().Get(0);
    Vector<uint8_t> stackedImg = stackedSp.ToImage(imageOptions);
    worksheet.GetCells().Get(u"H2").SetEmbeddedImage(stackedImg);
    workbook.Save(u"output_with_sparklines.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

上記のコードは、スパークラインの各視覚表現が 2 つの形式で複製されたワークブックを生成します。1 行目にアンカーされたライブのネイティブ スパークラインと、2 行目の隣接セルに直接埋め込まれた静的 PNG 画像です。画像はファイル自体に保存されているため、ワークブックは単一の自己完結型アーティファクトであり、埋め込まれた画像参照が壊れることなくメール送信やアーカイブが可能です。各スパークライン グループを PNG としてレンダリングします。`Sparkline.ToImage(ImageOrPrintOptions)` は画像バイトを `Vector<uint8_t>` として直接返し、その配列を対象セルの `EmbeddedImage` プロパティに代入します。この代入によって画像がセルの保存内容の一部となります。

{{% alert color="primary" %}}
各スパークライン グループは単一セルにアンカーされているため、`foreach` で列挙する代わりにインデクサ `group.Sparklines[0]` を通じてアクセスできます。これによりレンダリング コードを短く保つことができ、「anchor セルごとに 1 つのスパークライン」という一般的なパターンにも対応します。`Cell.EmbeddedImage` による画像バイトの保存には Aspose.Cells 26.5 以降が必要です。

## **Workflow 2 — Export the Sparkline Worksheet to HTML**
ワークブックに生きたスパークライン(および必要に応じて埋め込まれた画像)が含まれる場合、ワークシート全体を HTML として保存することで Web に公開できます。`HtmlSaveOptions` クラスにはこのエクスポートを制御するための設定が用意されています。このワークフローでは、ワークフロー 1 で生成された `output_with_sparklines.xlsx` ファイルを再利用し、整った単一ページの HTML ドキュメントに変換します。

### **Step-by-Step Instructions**
1. ワークフロー 1 で生成された `output_with_sparklines.xlsx` ファイルが作業ディレクトリ内のディスク上に存在することを確認します。
2. そのファイルを新しい `Workbook` インスタンスに読み込みます。
3. `HtmlSaveOptions` をインスタンス化し、その `ExportActiveWorksheetOnly` プロパティを `true` に設定して、生成される HTML ファイルにワークブック全体ではなくアクティブなワークシートのみが含まれるようにします。
4. `workbook.Save("sparklines.html", htmlOptions)` を呼び出して、HTML 出力をディスクに書き込みます。

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
int main() {
    Aspose::Cells::Startup();
    Workbook workbook(u"output_with_sparklines.xlsx");
    HtmlSaveOptions htmlOptions;
    htmlOptions.SetExportActiveWorksheetOnly(true);
    workbook.Save(u"sparklines.html", htmlOptions);
    Aspose::Cells::Cleanup();
    return 0;
}
```

上記のコードは、ワークフロー 1 のスパークラインを含むワークブックをポータブルな HTML ファイルに変換します。スパークラインは、エクスポート モードに応じて生成された HTML 内にインライン SVG または PNG レンダリングとして保持されるため、エンド ユーザーは Excel をインストールしていなくても任意のモダンブラウザでトレンドを閲覧できます。`ExportActiveWorksheetOnly` を `true` に設定することで、非表示シートや補助データが誤って公開されることを防ぎ、現在ユーザーに表示されているワークシートのみがエクスポートされます。
{{% /alert %}}

{{% alert color="primary" %}}
`HtmlSaveOptions` クラスには、出力を細かく調整するための追加プロパティ(例:`ExportHiddenWorksheet`、`ExportImagesAsBase64`、`Encoding`)が用意されています。デプロイ先のターゲットに応じて適宜調整してください。

## **API Summary**
上記のワークフローは、少数の Aspose.Cells API の連携に依存しています。
- `SparklineGroup` とコレクションヘアクセサ `worksheet.SparklineGroups` は、各スパークライン グループの種別(Line、Column、Stacked)、データ範囲、anchor セルを宣言するために使用されます。本記事では各グループが単一セルにアンカーされているため、グループには `worksheet.SparklineGroups[i]` を通じてアクセスします。
- `Sparkline` とインデクサ `group.Sparklines[0]` は、グループ内の個々の Sparkline を返します。例のすべてのグループには厳密に 1 つのスパークラインしか含まれていないため、`foreach` ループは必要ありません。
- `Sparkline.ToImage(ImageOrPrintOptions)` は、Sparkline の画像を `Vector<uint8_t>` バイト配列として直接返すレンダリング メソッドです。
- `HtmlSaveOptions.ExportActiveWorksheetOnly`(`bool`)は、HTML エクスポートをアクティブなワークシートのみに制限します。単一ページ レポートを生成する際に、`HtmlSaveOptions` 上で最もよく使用されるプロパティの 1 つです。
- `ImageOrPrintOptions.ImageType` は `Aspose.Cells.Drawing` 名前空間に属し、`ToImage` でのレンダリングやワークシートの画像への印刷時に使用される画像形式(例:`ImageType.Png`)を選択します。

## **Related Articles**
- [セルに画像を挿入する](/cells/ja/cpp/inserting-an-image-into-a-cell/)
{{% /alert %}}

{{< app/cells/assistant language="cpp" >}}