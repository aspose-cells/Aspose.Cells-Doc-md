---
title: Aspose.Cells for Node.js via Java でスパークラインを画像および HTML に変換する
linktitle: Convert Sparkline to Image and HTML
description: Aspose.Cells のスパークラインをセル埋め込み用のスタンドアロン画像にレンダリングする方法と、HtmlSaveOptions を使用してスパークラインを含むワークシートを HTML にエクスポートする方法を学びます。
keywords: Aspose.Cells, Node.js via Java, スパークライン, Sparkline.toImage, Cell.EmbeddedImage, HtmlSaveOptions, スパークラインをレンダリング, スパークラインを画像に変換, スパークラインを HTML にエクスポート
type: docs
weight: 120
url: /ja/nodejs-java/convert-sparkline-to-image-and-html/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
スパークラインはワークシートのセル内に配置された小型のグラフです。Aspose.Cells では、各スパークラインをスタンドアロン画像として抽出して（別のセルや外部レポートに埋め込むために）、あるいはスパークラインを含むワークシート全体を HTML にエクスポートして、ブラウザベースで配信することも可能です。本記事で使用されている `Cell.EmbeddedImage` プロパティは、**Aspose.Cells 26.5 以降**で利用できます。
{{% /alert %}}

## **はじめに**

スパークラインは、ワークシート内で直接トレンドを視覚化するためのコンパクトな手段です。Excel ユーザーはセル内でそれらを確認しますが、実世界の多くのシナリオでは、スパークラインをセル外に取り出す必要があります。たとえば、別のセルに静的な画像として埋め込んだり、自動メールに添付したり、Web に公開された HTML レポートの一部としてレンダリングしたりする場合です。

Aspose.Cells はこれら両方の操作をサポートしています。`Sparkline.toImage` メソッドは個々のスパークラインをストリームにレンダリングし、その結果得られるバイト列を `Cell.EmbeddedImage` に割り当てることができます。これにより、画像がワークブックの単一セル内に保存されます。一方、`HtmlSaveOptions` を使用すると、ワークブック全体（スパークラインを含むすべて）を自己完結型の HTML ファイルに変換できます。本記事では、両方のワークフローを順を追って説明します。

## **ワークフロー 1 — スパークラインを画像にレンダリングしてセルに埋め込む**

このワークフローでは、ソース値の小範囲を含むワークシートを作成し、その範囲に 3 つの異なるスパークライングループ（Line、Column、Stacked/Win-Loss）を関連付け、各グループを PNG としてレンダリングして、それらの PNG バイトを隣接するセルに埋め込み画像として書き込みます。最終結果は、ライブのスパークラインとそのレンダリングされたピクチャの両方を含む単一の `.xlsx` ファイルです。

### **ステップごとの手順**

1. 作業ディレクトリを定義し、ディスク上に存在することを確認します。
2. 新しい `Workbook` を作成し、最初の `Worksheet` への参照を取得します。
3. セル `A1` から `E1` に 5 つのサンプル数値（たとえば、日次売上や気温の測定値など）を入力します。
4. `worksheet.sparklineGroups.add(...)` を呼び出して、ワークシートに 3 つの `SparklineGroup` オブジェクトを追加します：
   - `F1` にアンカーされ、データ範囲が `A1:E1` の `SparklineType.Line` グループ。
   - `G1` にアンカーされ、データ範囲が `A1:E1` の `SparklineType.Column` グループ。
   - `H1` にアンカーされ、データ範囲が `A1:E1` の `SparklineType.Stacked`（win/loss）グループ。
5. `ImageOrPrintOptions` インスタンスを作成し、その `ImageType` を `ImageType.Png` に設定して、各スパークラインが透明な PNG としてレンダリングされるようにします。
6. 3 つのグループそれぞれについて、`group.sparklines[0].toImage(outputStream, imageOptions)` を使用して単一のスパークラインをレンダリングし、`ByteArrayOutputStream` を `byte[]` に変換して、その配列を `worksheet.cells.get("F2").setEmbeddedImage(...)`、`worksheet.cells.get("G2").setEmbeddedImage(...)`、および `worksheet.cells.get("H2").setEmbeddedImage(...)` にそれぞれ割り当てます。
7. ワークブックを `output_with_sparklines.xlsx` として保存します。

```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);

// A1:E1のセルにサンプルデータを入力する
worksheet.getCells().get("A1").putValue(5);
worksheet.getCells().get("B1").putValue(-3);
worksheet.getCells().get("C1").putValue(8);
worksheet.getCells().get("D1").putValue(-2);
worksheet.getCells().get("E1").putValue(6);

// F1（列5、行0）にアンカーされた折れ線スパークライングループを追加する
let lineArea = new AsposeCells.CellArea();
lineArea.setStartColumn(5);
lineArea.setEndColumn(5);
lineArea.setStartRow(0);
lineArea.setEndRow(0);
let lineIdx = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.Line, "A1:E1", false, lineArea);

// G1（列6、行0）にアンカーされた縦棒スパークライングループを追加する
let columnArea = new AsposeCells.CellArea();
columnArea.setStartColumn(6);
columnArea.setEndColumn(6);
columnArea.setStartRow(0);
columnArea.setEndRow(0);
let columnIdx = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.Column, "A1:E1", false, columnArea);

// H1（列7、行0）にアンカーされたWin/Loss（積み上げ）スパークライングループを追加する
let stackedArea = new AsposeCells.CellArea();
stackedArea.setStartColumn(7);
stackedArea.setEndColumn(7);
stackedArea.setStartRow(0);
stackedArea.setEndRow(0);
let stackedIdx = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.Stacked, "A1:E1", false, stackedArea);

// PNG出力用の画像オプションを設定する
let imageOptions = new AsposeCells.ImageOrPrintOptions();
imageOptions.setImageType(AsposeCells.ImageType.Png);

// 折れ線スパークラインを画像に変換してセルF2に埋め込む
let lineSp = worksheet.getSparklineGroups().get(lineIdx).getSparklines().get(0);
let lineMs = new java.io.ByteArrayOutputStream();
lineSp.toImage(lineMs, imageOptions);
worksheet.getCells().get("F2").setEmbeddedImage(lineMs.toByteArray());

// 縦棒スパークラインを画像に変換してセルG2に埋め込む
let columnSp = worksheet.getSparklineGroups().get(columnIdx).getSparklines().get(0);
let columnMs = new java.io.ByteArrayOutputStream();
columnSp.toImage(columnMs, imageOptions);
worksheet.getCells().get("G2").setEmbeddedImage(columnMs.toByteArray());

// Win/Lossスパークラインを画像に変換してセルH2に埋め込む
let stackedSp = worksheet.getSparklineGroups().get(stackedIdx).getSparklines().get(0);
let stackedMs = new java.io.ByteArrayOutputStream();
stackedSp.toImage(stackedMs, imageOptions);
worksheet.getCells().get("H2").setEmbeddedImage(stackedMs.toByteArray());

// ワークブックをディスクに保存する
workbook.save("output_with_sparklines.xlsx");
```

上記のコードにより、スパークラインの各視覚表現が 2 つの形式で複製されたワークブックが生成されます。1 行目にアンカーされたライブのネイティブスパークラインと、2 行目の隣接するセルに直接埋め込まれた静的な PNG ピクチャです。ピクチャはファイル自体に格納されているため、ワークブックは埋め込み画像参照が壊れることなくメール送信やアーカイブが可能な単一の自己完結型の成果物のままです。各スパークライングループを PNG としてレンダリングし、`ByteArrayOutputStream` を `byte[]` に変換して、その配列を対象セルの `setEmbeddedImage` プロパティに割り当てます。この割り当てによって、ピクチャがセルの格納コンテンツの一部となります。

{{% alert color="primary" %}}
各スパークライングループは単一のセルにアンカーされるため、`forEach` で列挙する代わりにインデクサ `group.sparklines[0]` を通じてアクセスできます。これにより、レンダリングコードを短く保つことができ、一般的な「アンカーセルごとに 1 つのスパークライン」というパターンにも対応します。`Cell.EmbeddedImage` を使用してピクチャバイトを保存するには、Aspose.Cells 26.5 以降が必要です。
{{% /alert %}}

## **ワークフロー 2 — スパークラインのワークシートを HTML にエクスポートする**

ワークブックにライブのスパークライン（およびオプションで埋め込まれたピクチャ）が含まれるようになると、ワークシート全体を HTML として保存することで Web に公開できます。`HtmlSaveOptions` クラスには、このエクスポートを制御するために必要な機能が用意されています。このワークフローでは、ワークフロー 1 で生成された `output_with_sparklines.xlsx` ファイルを再利用して、クリーンな単一ページの HTML ドキュメントに変換します。

### **ステップごとの手順**

1. ワークフロー 1 で生成された `output_with_sparklines.xlsx` ファイルが、作業ディレクトリ内のディスク上で利用可能であることを確認します。
2. そのファイルを新しい `Workbook` インスタンスに読み込みます。
3. `HtmlSaveOptions` をインスタンス化し、その `ExportActiveWorksheetOnly` プロパティを `true` に設定します。これにより、結果として生成される HTML ファイルにはワークブック全体ではなく、アクティブなワークシートのみが含まれるようになります。
4. `workbook.save("sparklines.html", htmlOptions)` を呼び出して、HTML 出力をディスクに書き込みます。

```javascript
let workbook = new AsposeCells.Workbook("output_with_sparklines.xlsx");
let htmlOptions = new AsposeCells.HtmlSaveOptions();
htmlOptions.setExportActiveWorksheetOnly(true);
workbook.save("sparklines.html", htmlOptions);
```

上記のコードは、ワークフロー 1 からのスパークラインを含むワークブックを、ポータブルな HTML ファイルに変換します。スパークラインは、エクスポートモードに応じて生成された HTML 内でインライン SVG または PNG レンダリングとして保持されるため、エンドユーザーは Excel がインストールされていなくても、モダンなブラウザでトレンドを確認できます。`ExportActiveWorksheetOnly` を `true` に設定することで、非表示シートや補助データを誤って公開するのを防ぎ、現在ユーザーに表示されているワークシートのみがエクスポートされます。

{{% alert color="primary" %}}
`HtmlSaveOptions` クラスには、出力を微調整するための追加のプロパティ（`ExportHiddenWorksheet`、`ExportImagesAsBase64`、`Encoding` など）が用意されています。デプロイメントターゲットに応じてこれらを適宜調整してください。
{{% /alert %}}

## **API の概要**

上記のワークフローは、Aspose.Cells API の小さなセットが連携して動作することに依存しています。

- `SparklineGroup` およびコレクションアクセサ `worksheet.sparklineGroups` は、各スパークライングループのタイプ（Line、Column、Stacked）、データ範囲、アンカーセルを宣言するために使用されます。本記事では各グループが単一のセルにアンカーされているため、グループには `worksheet.sparklineGroups[i]` を通じてアクセスします。
- `Sparkline` およびインデクサ `group.sparklines[0]` は、グループ内の個々のスパークラインを返します。例のすべてのグループには正確に 1 つのスパークラインが含まれているため、`forEach` ループは必要ありません。
- `Sparkline.toImage(OutputStream, ImageOrPrintOptions)` は、提供された `OutputStream` にスパークラインのピクチャを書き込むレンダリングメソッドです。このメソッドは `void` を返します。呼び出し後にストリームからバイトを読み取ります。
- `Cell.EmbeddedImage` は `byte[]` プロパティであり、単一セル内にピクチャを格納します。これは **Aspose.Cells 26.5 以降**で利用可能であり、`toImage` でレンダリングされたスパークラインを同じワークブックにラウンドトリップさせるための推奨される方法です。
- `HtmlSaveOptions.ExportActiveWorksheetOnly`（`boolean`）は、HTML エクスポートをアクティブなワークシートのみに制限します。これは、単一ページレポートを生成する際に `HtmlSaveOptions` で最も一般的に使用されるプロパティの 1 つです。
- `ImageOrPrintOptions.ImageType` は `com.aspose.cells.drawing` 名前空間にあり、`toImage` を使用してレンダリングする際、およびワークシートを画像に印刷する際のピクチャ形式（たとえば `ImageType.Png`）を選択します。

## **関連記事**

- [Aspose.Cells for Aspose.Cells for Node.js via Java のスパークライン](/cells/ja/nodejs-java/sparkline/)
- [セルへの画像の挿入](/cells/ja/nodejs-java/inserting-an-image-into-a-cell/)
- [SmartMarker 単一セル配列レンダリング | Aspose.Cells for Aspose.Cells for Node.js via Java](/cells/ja/nodejs-java/SmartMarker-Single-Cell-Array-Rendering/)

{{< app/cells/assistant language="javascript" >}}