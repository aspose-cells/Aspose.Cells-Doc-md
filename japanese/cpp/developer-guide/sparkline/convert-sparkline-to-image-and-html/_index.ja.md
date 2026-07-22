---
title: Aspose.Cells for C++ でスパークラインを画像と HTML に変換する
linktitle: Convert Sparkline to Image and HTML
description: HtmlSaveOptions を使用して、Aspose.Cells のスパークラインをセル埋め込み用の独立した画像としてレンダリングする方法と、スパークラインを含むワークシートを HTML にエクスポートする方法を説明します。
keywords: Aspose.Cells, C++, スパークライン, Sparkline.ToImage, Cell.EmbeddedImage, HtmlSaveOptions, スパークラインをレンダリング, スパークラインを画像に変換, スパークラインを HTML にエクスポート
type: docs
weight: 120
url: /ja/cpp/convert-sparkline-to-image-and-html/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
スパークラインはワークシートのセル内に配置される小型のグラフです。Aspose.Cells では、各スパークラインを独立した画像として抽出して（別のセルや外部レポートに埋め込むため）、スパークラインを含むワークシート全体をブラウザで配布するために HTML へエクスポートすることもできます。この記事で使用されている `Cell.EmbeddedImage` プロパティは、**Aspose.Cells 26.5 以降** で利用可能です。
{{% /alert %}}

## **はじめに**

スパークラインは、ワークシート内で直接トレンドを視覚化するためのコンパクトな方法です。Excel ユーザーはセル内でスパークラインを確認しますが、実際の多くのシナリオでは、スパークラインをセルから取り出す必要があります。例えば、別のセルに静的な画像として埋め込んだり、自動メールに添付したり、Web に公開される HTML レポートの一部としてレンダリングしたりする場合です。

Aspose.Cells はこれらの両方の操作をサポートしています。`Sparkline.ToImage` メソッドは個々のスパークラインをストリームにレンダリングし、結果のバイト配列を `Cell.EmbeddedImage` に割り当てて、画像をワークブックの単一セル内に保存できます。別途、`HtmlSaveOptions` を使用すると、ワークシート全体（スパークラインを含む）を自己完結型の HTML ファイルに変換できます。この記事では、両方のワークフローを順を追って説明します。

## **ワークフロー 1 — スパークラインを画像にレンダリングしてセルに埋め込む**

このワークフローでは、サンプルの値を含む小さな範囲を持つワークシートを作成し、3 つの異なるスパークライン グループ（Line、Column、Stacked/Win-Loss）をその範囲に追加し、各グループを PNG としてレンダリングして、その PNG バイトを隣接するセルに埋め込み画像として書き込みます。最終結果は、ライブ スパークラインとレンダリングされた画像の両方を含む単一の `.xlsx` ファイルです。

### **手順**

1. 作業ディレクトリを定義し、ディスク上に存在することを確認します。
2. 新しい `Workbook` を作成し、最初の `Worksheet` への参照を取得します。
3. セル `A1` から `E1` までの 5 つのサンプル数値（例えば日次売上や気温測定値など）を入力します。
4. `worksheet.SparklineGroups.Add(...)` を呼び出して、ワークシートに 3 つの `SparklineGroup` オブジェクトを追加します：
   - `F1` にアンカーされ、データ範囲が `A1:E1` の `SparklineType.Line` グループ。
   - `G1` にアンカーされ、データ範囲が `A1:E1` の `SparklineType.Column` グループ。
   - `H1` にアンカーされ、データ範囲が `A1:E1` の `SparklineType.Stacked`（勝敗）グループ。
5. `ImageOrPrintOptions` インスタンスを作成し、その `ImageType` を `ImageType.Png` に設定して、各スパークラインが透明な PNG としてレンダリングされるようにします。
6. 3 つのグループそれぞれについて、`group.Sparklines[0].ToImage(memoryStream, imageOptions)` を使用して単一のスパークラインをレンダリングし、`MemoryStream` を `Vector<uint8_t>` に変換して、その配列を `worksheet.Cells["F2"].EmbeddedImage`、`worksheet.Cells["G2"].EmbeddedImage`、および `worksheet.Cells["H2"].EmbeddedImage` にそれぞれ割り当てます。
7. ワークブックを `output_with_sparklines.xlsx` として保存します。

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

上記のコードは、スパークラインの各視覚表現が 2 つの形式で複製されたワークブックを生成します。1 行目にアンカーされたライブのネイティブ スパークラインと、2 行目の隣接するセルに直接埋め込まれた静的な PNG 画像です。画像がファイル自体に保存されるため、ワークブックは埋め込み画像参照が壊れることなくメール送信やアーカイブ可能な単一の自己完結型アーティファクトのままでいられます。各スパークライン グループを PNG としてレンダリングし、`MemoryStream` を `Vector<uint8_t>` に変換して、配列を対象セルの `EmbeddedImage` プロパティに割り当てます — この割り当てによって画像がセルの保存内容の一部になります。

{{% alert color="primary" %}}
各スパークライン グループは単一セルにアンカーされるため、`foreach` で列挙する代わりにインデクサ `group.Sparklines[0]` を通じてアクセスできます。これにより、レンダリング コードが短くなり、「アンカー セルごとに 1 つのスパークライン」という典型的なパターンにも対応します。`Cell.EmbeddedImage` を使用して画像のバイトを保存するには、Aspose.Cells 26.5 以降が必要です。
{{% /alert %}}

## **ワークフロー 2 — スパークラインを含むワークシートを HTML にエクスポートする**

ワークブックにライブ スパークライン（およびオプションで埋め込み画像の対応物）が含まれるようになると、ワークシート全体を HTML として保存することで Web に公開できます。`HtmlSaveOptions` クラスは、このエクスポートを制御するために必要な設定を公開しています。このワークフローでは、ワークフロー 1 で作成された `output_with_sparklines.xlsx` ファイルを再利用し、クリーンな単一ページの HTML ドキュメントに変換します。

### **手順**

1. ワークフロー 1 で生成された `output_with_sparklines.xlsx` ファイルが、作業ディレクトリ内のディスク上で利用可能であることを確認します。
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

上記のコードは、ワークフロー 1 からのスパークラインを含むワークブックを取得して、ポータブルな HTML ファイルに変換します。スパークラインは、エクスポート モードに応じて、生成された HTML 内にインライン SVG または PNG レンダリングとして保持されるため、エンドユーザーは Excel がインストールされていなくても、最新のブラウザでトレンドを表示できます。`ExportActiveWorksheetOnly` を `true` に設定することで、非表示シートや補助データが誤って公開されることを回避できます — 現在ユーザーに表示されているワークシートのみがエクスポートされます。

{{% alert color="primary" %}}
`HtmlSaveOptions` クラスには、`ExportHiddenWorksheet`、`ExportImagesAsBase64`、`Encoding` など、出力を微調整するための追加プロパティがあります。デプロイ ターゲットに応じてこれらを適宜調整してください。
{{% /alert %}}

## **API の概要**

上記のワークフローは、一連の Aspose.Cells API が連携して動作することに依存しています。

- `SparklineGroup` およびコレクション アクセサ `worksheet.SparklineGroups` は、各スパークライン グループのタイプ（Line、Column、Stacked）、データ範囲、アンカー セルを宣言するために使用されます。この記事では各グループが単一セルにアンカーされているため、グループは `worksheet.SparklineGroups[i]` を通じてアクセスされます。
- `Sparkline` およびインデクサ `group.Sparklines[0]` は、グループ内の個々のスパークラインを返します。例では各グループに正確に 1 つのスパークラインが含まれているため、`foreach` ループは必要ありません。
- `Sparkline.ToImage(Stream, ImageOrPrintOptions)` は、スパークラインの画像を提供された `Stream` に書き込むレンダリング メソッドです。このメソッドは `void` を返します。呼び出し後にストリームからバイトを読み取ります。
- `Cell.EmbeddedImage` は、単一セル内に画像を保存する `Vector<uint8_t>` プロパティです。**Aspose.Cells 26.5 以降** で利用可能で、`ToImage` によってレンダリングされたスパークラインを同じワークブックに戻すための推奨される方法です。
- `HtmlSaveOptions.ExportActiveWorksheetOnly`（`bool` 型）は、HTML エクスポートをアクティブなワークシートに制限します。単一ページのレポートを生成する際に `HtmlSaveOptions` で最も一般的に使用されるプロパティの 1 つです。
- `ImageOrPrintOptions.ImageType` は `Aspose.Cells.Drawing` 名前空間にあり、`ToImage` でのレンダリングおよびワークシートの画像への印刷時に使用される画像形式（例えば `ImageType.Png`）を選択します。

## **関連記事**

- [Sparklines in Aspose.Cells for C++](/cells/ja/cpp/sparkline/)
- [Inserting an Image into a Cell](/cells/ja/cpp/inserting-an-image-into-a-cell/)
- [SmartMarker Single Cell Array Rendering | Aspose.Cells for C++](/cells/ja/cpp/SmartMarker-Single-Cell-Array-Rendering/)

{{< app/cells/assistant language="cpp" >}}