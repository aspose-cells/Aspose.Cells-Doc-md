---
title: Aspose.Cells for Node.js via C++ でスパークラインを画像と HTML に変換
linktitle: Aspose.Cells for Node.js via C++ でスパークラインを画像と HTML に変換
description: Aspose.Cells のスパークラインをセル埋め込み用の独立した画像として描画し、HtmlSaveOptions を使用してスパークラインを含むワークシートを HTML にエクスポートする方法を学びます。
keywords: Aspose.Cells, Node.js via C++, スパークライン, Sparkline.toImage, cell.embeddedImage, HtmlSaveOptions, スパークラインの描画, スパークラインを画像に変換, スパークラインを HTML にエクスポート
type: docs
weight: 120
url: /ja/nodejs-cpp/convert-sparkline-to-image-and-html/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
スパークラインはワークシートのセル内に配置される小型のグラフです。Aspose.Cells では、各スパークラインを独立した画像として抽出（別のセルや外部レポートへの埋め込み用）したり、スパークラインを含むワークシート全体を HTML にエクスポートしてブラウザで配信したりすることができます。本記事で使用する `cell.embeddedImage` プロパティは、**Aspose.Cells 26.5 以降**でご利用いただけます。
{{% /alert %}}

## **Introduction**
スパークラインは、ワークシート内で直接トレンドを視覚化するためのコンパクトな手段です。Excel ユーザーはセル内でスパークラインを確認しますが、実際の多くのシナリオでは、スパークラインをセル外に取り出す必要があります。例えば、別のセルに静的な画像として埋め込む、自動メールに添付する、Web に公開される HTML レポートの一部として描画するといった用途が挙げられます。Aspose.Cells はこれらの両方の操作をサポートしています。`Sparkline.toImage` メソッドは個々のスパークラインをストリームに描画し、そのバイト列を `cell.embeddedImage` に割り当てることで、画像をワークブック内の単一のセルに格納できます。さらに、`HtmlSaveOptions` を使用すると、スパークラインを含むワークブック全体を、自己完結型の HTML ファイルに変換できます。本記事では、この 2 つのワークフローを順を追って説明します。

## **Workflow 1 — Render Sparklines to Images and Embed Them into Cells**
このワークフローでは、ソース値を含む小さな範囲を持つワークシートを作成し、その範囲に 3 つの異なるスパークライン グループ（折れ線、縦棒、積み上げ / Win-Loss）を関連付け、各グループを PNG として描画して、その PNG バイト列を隣接するセルに埋め込み画像として書き込みます。最終的な結果は、ライブのスパークラインと描画された画像の両方を含む単一の `.xlsx` ファイルです。

### **Step-by-Step Instructions**
1. 作業ディレクトリを定義し、ディスク上に存在することを確認します。
2. 新しい `Workbook` を作成し、最初の `Worksheet` への参照を取得します。
3. セル `A1` から `E1` までに 5 つのサンプル数値（例えば日次売上や気温測定値など）を入力します。
4. `worksheet.sparklineGroups.add(...)` を呼び出して、ワークシートに 3 つの `SparklineGroup` オブジェクトを追加します。
   - データ範囲 `A1:E1` を持ち、`F1` にアンカーされる `SparklineType.Line` グループ。
   - データ範囲 `A1:E1` を持ち、`G1` にアンカーされる `SparklineType.Column` グループ。
   - データ範囲 `A1:E1` を持ち、`H1` にアンカーされる `SparklineType.Stacked`（Win/Loss）グループ。
5. `ImageOrPrintOptions` インスタンスを作成し、各スパークラインが透明な PNG として描画されるように `ImageType` を `ImageType.Png` に設定します。
7. ワークブックを `output_with_sparklines.xlsx` として保存します。

```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
// Populate sample data in cells A1:E1
worksheet.getCells().get("A1").putValue(5);
worksheet.getCells().get("B1").putValue(-3);
worksheet.getCells().get("C1").putValue(8);
worksheet.getCells().get("D1").putValue(-2);
worksheet.getCells().get("E1").putValue(6);
// Add a Line sparkline group anchored at F1 (column 5, row 0)
let lineArea = new AsposeCells.CellArea();
lineArea.setStartColumn(5);
lineArea.setEndColumn(5);
lineArea.setStartRow(0);
lineArea.setEndRow(0);
let lineIdx = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.Line, "A1:E1", false, lineArea);
// Add a Column sparkline group anchored at G1 (column 6, row 0)
let columnArea = new AsposeCells.CellArea();
columnArea.setStartColumn(6);
columnArea.setEndColumn(6);
columnArea.setStartRow(0);
columnArea.setEndRow(0);
let columnIdx = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.Column, "A1:E1", false, columnArea);
// Add a Win/Loss (Stacked) sparkline group anchored at H1 (column 7, row 0)
let stackedArea = new AsposeCells.CellArea();
stackedArea.setStartColumn(7);
stackedArea.setEndColumn(7);
stackedArea.setStartRow(0);
stackedArea.setEndRow(0);
let stackedIdx = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.Stacked, "A1:E1", false, stackedArea);
// Configure image options for PNG output
let imageOptions = new AsposeCells.ImageOrPrintOptions();
imageOptions.setImageType(AsposeCells.ImageType.Png);
// Convert the Line sparkline to image and embed it in cell F2
let lineSp = worksheet.getSparklineGroups().get(lineIdx).getSparklines().get(0);
let linePath = "line_sparkline.png";
lineSp.toImage(linePath, imageOptions);
worksheet.getCells().get("F2").setEmbeddedImage(fs.readFileSync(linePath));
// Convert the Column sparkline to image and embed it in cell G2
let columnSp = worksheet.getSparklineGroups().get(columnIdx).getSparklines().get(0);
let columnPath = "column_sparkline.png";
columnSp.toImage(columnPath, imageOptions);
worksheet.getCells().get("G2").setEmbeddedImage(fs.readFileSync(columnPath));
// Convert the Win/Loss sparkline to image and embed it in cell H2
let stackedSp = worksheet.getSparklineGroups().get(stackedIdx).getSparklines().get(0);
let stackedPath = "stacked_sparkline.png";
stackedSp.toImage(stackedPath, imageOptions);
worksheet.getCells().get("H2").setEmbeddedImage(fs.readFileSync(stackedPath));
// Save the workbook to disk
workbook.save("output_with_sparklines.xlsx");
```

上記のコードでは、スパークラインの視覚表現が 2 つの形式で重複して作成されます。1 行目にアンカーされたライブのネイティブ スパークラインと、2 行目の隣接セルに直接埋め込まれた静的な PNG 画像です。画像がファイル自体に格納されているため、ワークブックは埋め込み画像参照を壊すことなく、単一の自己完結型の成果物としてメール送信やアーカイブが可能です。各スパークライン グループを PNG として描画し、ストリームを `Buffer` に変換して、その配列を対象セルの `embeddedImage` プロパティに割り当てます。この割り当てによって、イメージがセルの保存内容の一部となります。

{{% alert color="primary" %}}
各スパークライン グループは単一のセルにアンカーされるため、`forEach` で列挙する代わりにインデクサ `group.sparklines[0]` を使用してアクセスできます。これにより描画コードを短く保つことができ、一般的な「アンカー セルごとに 1 つのスパークライン」というパターンにも対応します。`cell.embeddedImage` 経由で画像のバイト列を格納するには、Aspose.Cells 26.5 以降が必要です。

## **Workflow 2 — Export the Sparkline Worksheet to HTML**
ワークブックにライブのスパークライン（および必要に応じて埋め込み画像）が含まれる状態になったら、ワークシート全体を HTML として保存することで Web に公開できます。`HtmlSaveOptions` クラスには、このエクスポートを制御するためのオプションが用意されています。このワークフローでは、ワークフロー 1 で生成された `output_with_sparklines.xlsx` ファイルを再利用して、クリーンな単一ページの HTML ドキュメントに変換します。

### **Step-by-Step Instructions**
1. ワークフロー 1 で生成された `output_with_sparklines.xlsx` ファイルが、作業ディレクトリ内のディスク上で利用可能であることを確認します。
2. そのファイルを新しい `Workbook` インスタンスに読み込みます。
3. `HtmlSaveOptions` をインスタンス化し、その `exportActiveWorksheetOnly` プロパティを `true` に設定して、生成される HTML ファイルにワークブック全体ではなくアクティブなワークシートのみが含まれるようにします。
4. `workbook.save("sparklines.html", htmlOptions)` を呼び出して、HTML 出力をディスクに書き込みます。

```javascript
let workbook = new AsposeCells.Workbook("output_with_sparklines.xlsx");
let htmlOptions = new AsposeCells.HtmlSaveOptions();
htmlOptions.setExportActiveWorksheetOnly(true);
workbook.save("sparklines.html", htmlOptions);
```

上記のコードは、ワークフロー 1 によるスパークラインを含むワークブックを、ポータブルな HTML ファイルに変換します。スパークラインは、エクスポート モードに応じて、生成された HTML 内のインライン SVG または PNG のレンダリングとして保持されるため、Excel をインストールしていないユーザーでも、最新のブラウザでトレンドを確認できます。`exportActiveWorksheetOnly` を `true` に設定することで、非表示シートや補助データが誤って公開されることを防ぎ、現在ユーザーに表示されているワークシートのみがエクスポートされます。
{{% /alert %}}

{{% alert color="primary" %}}
`HtmlSaveOptions` クラスには、出力を微調整するための追加プロパティが用意されています。例えば `exportHiddenWorksheet`、`exportImagesAsBase64`、`encoding` などがあります。デプロイ先の環境に応じてこれらを適宜調整してください。

## **API Summary**
上記のワークフローは、少数の Aspose.Cells API が連携して動作します。
- `SparklineGroup` およびコレクション アクセサ `worksheet.sparklineGroups` は、各スパークライン グループのタイプ（Line、Column、Stacked）、データ範囲、アンカー セルを宣言するために使用されます。本記事では各グループが単一のセルにアンカーされるため、`worksheet.sparklineGroups[i]` を通じてグループにアクセスします。
- `Sparkline` およびインデクサ `group.sparklines[0]` は、グループ内の個々のスパークラインを返します。例の各グループにはちょうど 1 つのスパークラインしか含まれていないため、`forEach` ループは不要です。
- `Sparkline.toImage(Stream, ImageOrPrintOptions)` は、スパークライン画像を提供された `Stream` に書き込む描画メソッドです。このメソッドは `void` を返します。呼び出し後にストリームからバイト列を読み取ります。
- `htmlSaveOptions.exportActiveWorksheetOnly`（`bool` 型）は、HTML エクスポートをアクティブなワークシートのみに制限します。これは、単一ページ レポートを生成する際に `HtmlSaveOptions` で最もよく使用されるプロパティの 1 つです。
- `imageOrPrintOptions.imageType` は `Aspose.Cells.Drawing` 名前空間に属し、`toImage` での描画時やワークシートの画像への印刷時に使用される画像形式（例えば `ImageType.Png`）を選択します。

## **Related Articles**
- [セルへの画像の挿入](/cells/ja/nodejs-cpp/inserting-an-image-into-a-cell/)
{{% /alert %}}

{{< app/cells/assistant language="javascript" >}}