---
title: Aspose.Cells for Node.js via C++ でスパークラインを画像および HTML に変換する
linktitle: Convert Sparkline to Image and HTML
description: Aspose.Cells のスパークラインをスタンドアロン画像にレンダリングしてセルに埋め込む方法や、スパークラインを含むワークシートを HtmlSaveOptions を使用して HTML にエクスポートする方法を学習します。
keywords: Aspose.Cells, Node.js via C++, sparkline, Sparkline.toImage, cell.embeddedImage, HtmlSaveOptions, render sparkline, convert sparkline to image, export sparkline to HTML
type: docs
weight: 120
url: /ja/nodejs-cpp/convert-sparkline-to-image-and-html/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
スパークラインとは、ワークシートのセル内に配置された小型のグラフです。Aspose.Cells では、各スパークラインをスタンドアロン画像として抽出して（別のセルや外部レポートに埋め込み可能）、スパークラインを含むワークシート全体を HTML にエクスポートしてブラウザベースで配布することもできます。本記事で使用されている `cell.embeddedImage` プロパティは、**Aspose.Cells 26.5 以降** で利用可能です。
{{% /alert %}}

## **はじめに**

スパークラインは、ワークシート内で直接トレンドを視覚化するためのコンパクトな手法です。Excel ユーザーはセル内でスパークラインを確認しますが、実際のシナリオでは、スパークラインをセル外で利用する必要が生じる場合があります。たとえば、別のセルに静止画像として埋め込んだり、自動メールに添付したり、Web に公開される HTML レポートの一部としてレンダリングしたりする場合です。

Aspose.Cells はこれら両方の操作をサポートしています。`Sparkline.toImage` メソッドは個々のスパークラインをストリームにレンダリングし、その結果得られるバイトを `cell.embeddedImage` に割り当てることで、ワークブックの単一セル内に画像を保存できます。別途、`HtmlSaveOptions` を使用すると、ワークブック全体（スパークラインを含む）を自己完結型の HTML ファイルに変換できます。本記事では、両方のワークフローについて順を追って説明します。

## **ワークフロー 1 — スパークラインを画像にレンダリングしてセルに埋め込む**

このワークフローでは、少数のソース値を含むワークシートを作成し、その範囲に 3 つの異なるスパークライングループ（Line、Column、および Stacked/Win-Loss）を関連付け、各グループを PNG としてレンダリングして、それらの PNG バイトを隣接するセルに埋め込み画像として書き込みます。最終的な結果は、ライブスパークラインとレンダリングされた画像の両方を含む単一の `.xlsx` ファイルとなります。

### **手順ごとの説明**

1. 作業ディレクトリを定義し、ディスク上に存在することを確認します。
2. 新しい `Workbook` を作成し、最初の `Worksheet` への参照を取得します。
3. セル `A1` から `E1` に 5 つのサンプル数値（例：日次売上や気温測定値など）を入力します。
4. `worksheet.sparklineGroups.add(...)` を呼び出して、ワークシートに 3 つの `SparklineGroup` オブジェクトを追加します：
   - `F1` に固定され、データ範囲 `A1:E1` を持つ `SparklineType.Line` グループ。
   - `G1` に固定され、データ範囲 `A1:E1` を持つ `SparklineType.Column` グループ。
   - `H1` に固定され、データ範囲 `A1:E1` を持つ `SparklineType.Stacked`（win/loss）グループ。
5. `ImageOrPrintOptions` インスタンスを作成し、その `ImageType` を `ImageType.Png` に設定して、各スパークラインが透明な PNG としてレンダリングされるようにします。
6. 3 つのグループそれぞれに対して、`group.sparklines[0].toImage(memoryStream, imageOrPrintOptions)` を使用して単一のスパークラインをレンダリングし、ストリームを `Buffer`（または `Uint8Array`）に変換し、そのバイトを `worksheet.cells["F2"].embeddedImage`、`worksheet.cells["G2"].embeddedImage`、および `worksheet.cells["H2"].embeddedImage` にそれぞれ割り当てます。
7. ワークブックを `output_with_sparklines.xlsx` として保存します。

```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);

// A1:E1のセルにサンプルデータを入力
worksheet.getCells().get("A1").putValue(5);
worksheet.getCells().get("B1").putValue(-3);
worksheet.getCells().get("C1").putValue(8);
worksheet.getCells().get("D1").putValue(-2);
worksheet.getCells().get("E1").putValue(6);

// F1（列5、行0）に配置されるラインスパークライングループを追加
let lineArea = new AsposeCells.CellArea();
lineArea.setStartColumn(5);
lineArea.setEndColumn(5);
lineArea.setStartRow(0);
lineArea.setEndRow(0);
let lineIdx = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.Line, "A1:E1", false, lineArea);

// G1（列6、行0）に配置されるカラムスパークライングループを追加
let columnArea = new AsposeCells.CellArea();
columnArea.setStartColumn(6);
columnArea.setEndColumn(6);
columnArea.setStartRow(0);
columnArea.setEndRow(0);
let columnIdx = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.Column, "A1:E1", false, columnArea);

// H1（列7、行0）に配置される勝敗（積み上げ）スパークライングループを追加
let stackedArea = new AsposeCells.CellArea();
stackedArea.setStartColumn(7);
stackedArea.setEndColumn(7);
stackedArea.setStartRow(0);
stackedArea.setEndRow(0);
let stackedIdx = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.Stacked, "A1:E1", false, stackedArea);

// PNG出力用の画像オプションを設定
let imageOptions = new AsposeCells.ImageOrPrintOptions();
imageOptions.setImageType(AsposeCells.ImageType.Png);

// ラインスパークラインを画像に変換し、セルF2に埋め込む
let lineSp = worksheet.getSparklineGroups().get(lineIdx).getSparklines().get(0);
let linePath = "line_sparkline.png";
lineSp.toImage(linePath, imageOptions);
worksheet.getCells().get("F2").setEmbeddedImage(fs.readFileSync(linePath));

// カラムスパークラインを画像に変換し、セルG2に埋め込む
let columnSp = worksheet.getSparklineGroups().get(columnIdx).getSparklines().get(0);
let columnPath = "column_sparkline.png";
columnSp.toImage(columnPath, imageOptions);
worksheet.getCells().get("G2").setEmbeddedImage(fs.readFileSync(columnPath));

// 勝敗スパークラインを画像に変換し、セルH2に埋め込む
let stackedSp = worksheet.getSparklineGroups().get(stackedIdx).getSparklines().get(0);
let stackedPath = "stacked_sparkline.png";
stackedSp.toImage(stackedPath, imageOptions);
worksheet.getCells().get("H2").setEmbeddedImage(fs.readFileSync(stackedPath));

// ワークブックをディスクに保存
workbook.save("output_with_sparklines.xlsx");
```

上記のコードにより、スパークラインの各視覚表現が 2 つの形式で複製されたワークブックが生成されます。1 つ目は 1 行目に固定されたライブのネイティブスパークラインで、2 つ目は 2 行目の隣接セルに直接埋め込まれた静止 PNG 画像です。画像がファイル自体に格納されているため、ワークブックは埋め込まれた画像参照を壊すことなく、メールで送信したりアーカイブしたりできる単一の自己完結型アーティファクトとして維持されます。各スパークライングループを PNG としてレンダリングし、ストリームを `Buffer` に変換して、その配列をターゲットセルの `embeddedImage` プロパティに割り当てます。この割り当てによって、画像がセルの格納コンテンツの一部となります。

{{% alert color="primary" %}}
各スパークライングループは単一のセルに固定されているため、`forEach` で列挙する代わりにインデクサ `group.sparklines[0]` を使用してアクセスできます。これにより、レンダリングコードが簡潔になり、「アンカーセルごとに 1 つのスパークライン」という典型的なパターンと一致します。`cell.embeddedImage` を使用して画像バイトを保存するには、Aspose.Cells 26.5 以降が必要です。
{{% /alert %}}

## **ワークフロー 2 — スパークラインのワークシートを HTML にエクスポートする**

ワークブックにライブスパークライン（および必要に応じて埋め込み画像）が含まれたら、ワークシート全体を HTML として保存することで Web に公開できます。`HtmlSaveOptions` クラスにはこのエクスポートを制御するために必要な機能が備わっています。このワークフローでは、ワークフロー 1 で生成された `output_with_sparklines.xlsx` ファイルを再利用し、それをクリーンな単一ページの HTML ドキュメントに変換します。

### **手順ごとの説明**

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

上記のコードは、ワークフロー 1 のスパークラインを含むワークブックを取得し、ポータブルな HTML ファイルに変換します。スパークラインは、エクスポートモードに応じて、生成された HTML 内のインライン SVG または PNG レンダリングとして保持されるため、エンドユーザーは Excel がインストールされていなくても、最新のブラウザでトレンドを表示できます。`exportActiveWorksheetOnly` を `true` に設定することで、非表示シートや補助データを誤って公開することを防ぎ、現在ユーザーに表示されているワークシートのみがエクスポートされます。

{{% alert color="primary" %}}
`HtmlSaveOptions` クラスには、出力を微調整するための追加プロパティ（`exportHiddenWorksheet`、`exportImagesAsBase64`、`encoding` など）が用意されています。デプロイメントターゲットに応じてこれらを適宜調整してください。
{{% /alert %}}

## **API の概要**

上記のワークフローは、一連の Aspose.Cells API が連携して機能することに依存しています。

- `SparklineGroup` およびコレクションアクセッサ `worksheet.sparklineGroups` は、各スパークライングループのタイプ（Line、Column、Stacked）、データ範囲、およびアンカーセルを宣言するために使用されます。本記事では、各グループが単一のセルに固定されているため、グループには `worksheet.sparklineGroups[i]` を通じてアクセスします。
- `Sparkline` およびインデクサ `group.sparklines[0]` は、グループ内の個々のスパークラインを返します。例では各グループにスパークラインが 1 つだけ含まれているため、`forEach` ループは必要ありません。
- `Sparkline.toImage(Stream, ImageOrPrintOptions)` は、指定された `Stream` にスパークラインの画像を書き込むレンダリングメソッドです。このメソッドは `void` を返します。呼び出し後にストリームからバイトを読み取ります。
- `cell.embeddedImage` は、単一のセル内に画像を保存する `Buffer`（または `Uint8Array`）プロパティです。これは **Aspose.Cells 26.5 以降** で利用可能であり、`toImage` でレンダリングされたスパークラインを同じワークブックにラウンドトリップさせるための推奨される方法です。
- `htmlSaveOptions.exportActiveWorksheetOnly`（`bool` 型）は、HTML エクスポートをアクティブなワークシートに限定します。単一ページレポートを生成する際に、`HtmlSaveOptions` で最も一般的に使用されるプロパティの 1 つです。
- `imageOrPrintOptions.imageType` は `Aspose.Cells.Drawing` 名前空間に属し、`toImage` でのレンダリング時およびワークシートを画像に印刷する際に使用される画像形式（例：`ImageType.Png`）を選択します。

## **関連記事**

- [Aspose.Cells for Node.js via C++ のスパークライン](/cells/ja/nodejs-cpp/sparkline/)
- [セルへの画像の挿入](/cells/ja/nodejs-cpp/inserting-an-image-into-a-cell/)
- [SmartMarker 単一セル配列レンダリング | Aspose.Cells Node.js via C++](/cells/ja/nodejs-cpp/SmartMarker-Single-Cell-Array-Rendering/)

{{< app/cells/assistant language="javascript" >}}