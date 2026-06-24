---
title: Aspose.Cells for Java でスパークラインを画像と HTML に変換する
linktitle: Convert Sparkline to Image and HTML
description: Aspose.Cells のスパークラインをセル埋め込み用のスタンドアロン画像としてレンダリングする方法と、スパークラインを含むワークシートを HtmlSaveOptions を使用して HTML にエクスポートする方法を学びます。
keywords: Aspose.Cells, Java, sparkline, Sparkline.toImage, Cell.EmbeddedImage, HtmlSaveOptions, render sparkline, convert sparkline to image, export sparkline to HTML
type: docs
weight: 120
url: /ja/java/convert-sparkline-to-image-and-html/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
スパークラインはワークシートのセル内に配置されるミニチュアグラフです。Aspose.Cells では、各スパークラインをスタンドアロン画像として抽出（別のセルや外部レポートへの埋め込み用）し、スパークラインを含むワークシート全体を HTML にエクスポートしてブラウザで配布することも可能です。本記事で使用されている `Cell.EmbeddedImage` プロパティは、**Aspose.Cells 26.5 以降** で利用可能です。
{{% /alert %}}

## **はじめに**

スパークラインは、ワークシート内で直接トレンドを視覚化するコンパクトな方法です。Excel ユーザーはスパークラインをセル内にそのまま表示しますが、実際のシナリオでは、スパークラインをセルから取り出して使用することがよくあります。例えば、別のセルに静的な画像として埋め込んだり、自動メールに添付したり、Web に公開される HTML レポートの一部としてレンダリングしたりする場合です。

Aspose.Cells はこれらの両方の操作をサポートしています。`Sparkline.toImage` メソッドは個々のスパークラインをストリームにレンダリングし、生成されたバイト配列を `Cell.EmbeddedImage`（`setEmbeddedImage` 経由）に割り当てて、ワークブックの単一セル内に画像を保存できます。さらに、`HtmlSaveOptions` を使用すると、ワークシート全体（スパークラインを含む）を自己完結型の HTML ファイルに変換できます。本記事では両方のワークフローを順を追って説明します。

## **ワークフロー 1 — スパークラインを画像にレンダリングしてセルに埋め込む**

このワークフローでは、小範囲のソース値を含むワークシートを作成し、その範囲に 3 つの異なるスパークライングループ（ライン、列、積み上げ/勝敗）を追加し、各グループを PNG としてレンダリングして、それらの PNG バイト配列を隣接するセルに埋め込み画像として書き込みます。最終結果は、ライブスパークラインとそのレンダリングされた画像の両方を含む単一の `.xlsx` ファイルです。

### **ステップバイステップの説明**

1. 作業ディレクトリを定義し、ディスク上に存在することを確認します。
2. 新しい `Workbook` を作成し、最初の `Worksheet` の参照を取得します。
3. セル `A1` から `E1` に 5 つのサンプル数値（例えば、日次売上や温度測定値など）を入力します。
4. `worksheet.getSparklineGroups().add(...)` を呼び出して、ワークシートに 3 つの `SparklineGroup` オブジェクトを追加します：
   - `F1` に固定された `SparklineType.LINE` グループ、データ範囲は `A1:E1`。
   - `G1` に固定された `SparklineType.COLUMN` グループ、データ範囲は `A1:E1`。
   - `H1` に固定された `SparklineType.STACKED`（勝敗）グループ、データ範囲は `A1:E1`。
5. `ImageOrPrintOptions` インスタンスを作成し、`setImageType(ImageType.PNG)` を呼び出して、各スパークラインが透明な PNG としてレンダリングされるようにします。
6. 3 つのグループそれぞれに対して、`group.getSparklines().get(0).toImage(byteArrayOutputStream, imageOptions)` を使用して単一のスパークラインをレンダリングし、`ByteArrayOutputStream` を `byte[]` に変換して、`worksheet.getCells().get("F2").setEmbeddedImage(...)`、`worksheet.getCells().get("G2").setEmbeddedImage(...)`、および `worksheet.getCells().get("H2").setEmbeddedImage(...)` 経由で配列をそれぞれ割り当てます。
7. `workbook.save("output_with_sparklines.xlsx")` を呼び出して、ワークブックをディスクに保存します。

```java
import com.aspose.cells.*;
import java.io.*;

// 新しいワークブックを作成し、最初のワークシートにアクセスする
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);

// セル A1:E1 にサンプルデータを入力する
worksheet.getCells().get("A1").putValue(5);
worksheet.getCells().get("B1").putValue(-3);
worksheet.getCells().get("C1").putValue(8);
worksheet.getCells().get("D1").putValue(-2);
worksheet.getCells().get("E1").putValue(6);

// F1（列 5、行 0）にアンカーされた折れ線スパークライングループを追加する
CellArea lineArea = CellArea.createCellArea(5, 0, 5, 0);
int lineIdx = worksheet.getSparklineGroups().add(SparklineType.LINE, "A1:E1", false, lineArea);

// G1（列 6、行 0）にアンカーされた縦棒スパークライングループを追加する
CellArea columnArea = CellArea.createCellArea(6, 0, 6, 0);
int columnIdx = worksheet.getSparklineGroups().add(SparklineType.COLUMN, "A1:E1", false, columnArea);

// H1（列 7、行 0）にアンカーされた勝敗（積み上げ）スパークライングループを追加する
CellArea stackedArea = CellArea.createCellArea(7, 0, 7, 0);
int stackedIdx = worksheet.getSparklineGroups().add(SparklineType.STACKED, "A1:E1", false, stackedArea);

// PNG 出力用の画像オプションを設定する
ImageOrPrintOptions imageOptions = new ImageOrPrintOptions();
imageOptions.setImageType(ImageType.PNG);

// 折れ線スパークラインを画像に変換し、セル F2 に埋め込む
Sparkline lineSp = worksheet.getSparklineGroups().get(lineIdx).getSparklines().get(0);
ByteArrayOutputStream lineMs = new ByteArrayOutputStream();
lineSp.toImage(lineMs, imageOptions);
worksheet.getCells().get("F2").setEmbeddedImage(lineMs.toByteArray());

// 縦棒スパークラインを画像に変換し、セル G2 に埋め込む
Sparkline columnSp = worksheet.getSparklineGroups().get(columnIdx).getSparklines().get(0);
ByteArrayOutputStream columnMs = new ByteArrayOutputStream();
columnSp.toImage(columnMs, imageOptions);
worksheet.getCells().get("G2").setEmbeddedImage(columnMs.toByteArray());

// 勝敗スパークラインを画像に変換し、セル H2 に埋め込む
Sparkline stackedSp = worksheet.getSparklineGroups().get(stackedIdx).getSparklines().get(0);
ByteArrayOutputStream stackedMs = new ByteArrayOutputStream();
stackedSp.toImage(stackedMs, imageOptions);
worksheet.getCells().get("H2").setEmbeddedImage(stackedMs.toByteArray());

// ワークブックをディスクに保存する
workbook.save("output_with_sparklines.xlsx");
```

上記のコードでは、スパークラインの各視覚表現が 2 つの形式で複製されたワークブックが生成されます。1 行目に固定されたライブのネイティブスパークラインと、2 行目の隣接するセルに直接埋め込まれた静的な PNG 画像です。画像がファイル自体に格納されているため、ワークブックは埋め込み画像参照を壊すことなくメール送信やアーカイブ可能な単一の自己完結型アーティファクトのまま維持されます。各スパークライングループを PNG としてレンダリングし、`ByteArrayOutputStream` を `byte[]` に変換して、`setEmbeddedImage(byte[])` を通じて対象セルの `EmbeddedImage` プロパティに配列を割り当てます。この割り当てによって画像がセルの格納コンテンツの一部となります。

{{% alert color="primary" %}}
各スパークライングループは単一のセルに固定されているため、`for` ループで列挙する代わりにインデクサ `group.getSparklines().get(0)` を通じてアクセスできます。これにより、レンダリングコードを簡潔に保ち、一般的な「アンカーセルごとに 1 つのスパークライン」というパターンに対応します。`Cell.EmbeddedImage`（`setEmbeddedImage` を通じて設定）による画像のバイト配列の保存には、Aspose.Cells 26.5 以降が必要です。
{{% /alert %}}

## **ワークフロー 2 — スパークラインのワークシートを HTML にエクスポートする**

ワークブックにライブスパークライン（およびオプションで埋め込み画像の対応物）が含まれている場合、ワークシート全体を HTML として保存することで Web に公開できます。`HtmlSaveOptions` クラスには、このエクスポートを制御するためのオプションが用意されています。このワークフローでは、ワークフロー 1 で生成された `output_with_sparklines.xlsx` ファイルを再利用し、簡潔な単一ページの HTML ドキュメントに変換します。

### **ステップバイステップの説明**

1. ワークフロー 1 で生成された `output_with_sparklines.xlsx` ファイルが作業ディレクトリ内のディスク上で利用可能であることを確認します。
2. そのファイルを新しい `Workbook` インスタンスに読み込みます。
3. `HtmlSaveOptions` をインスタンス化し、`setExportActiveWorksheetOnly(true)` を呼び出して、生成される HTML ファイルにワークブック全体ではなく、アクティブなワークシートのみが含まれるようにします。
4. `workbook.save("sparklines.html", htmlOptions)` を呼び出して、HTML 出力をディスクに書き込みます。

```java
import com.aspose.cells.*;

Workbook workbook = new Workbook("output_with_sparklines.xlsx");
HtmlSaveOptions htmlOptions = new HtmlSaveOptions();
htmlOptions.setExportActiveWorksheetOnly(true);
workbook.save("sparklines.html", htmlOptions);
```

上記のコードは、ワークフロー 1 からのスパークラインを含むワークブックを、ポータブルな HTML ファイルに変換します。スパークラインは、エクスポートモードに応じて、生成された HTML 内にインライン SVG または PNG レンダリングとして保持されるため、エンドユーザーは Excel をインストールすることなく、モダンブラウザでトレンドを表示できます。`setExportActiveWorksheetOnly(true)` を通じて `ExportActiveWorksheetOnly` を `true` に設定することで、誤って非表示シートや補助データが公開されることを防ぎ、ユーザーに現在表示されているワークシートのみがエクスポートされます。

{{% alert color="primary" %}}
`HtmlSaveOptions` クラスには、`ExportHiddenWorksheet`、`ExportImagesAsBase64`、`Encoding` など、出力を微調整するための追加のプロパティが用意されています。デプロイメントターゲットに応じてこれらを調整してください。
{{% /alert %}}

## **API 概要**

上記のワークフローは、一連の Aspose.Cells API が連携して動作することに依存しています。

- `SparklineGroup` とコレクションアクセサ `worksheet.getSparklineGroups()` は、各スパークライングループのタイプ（Line、Column、Stacked）、データ範囲、アンカーセルを宣言するために使用されます。本記事では各グループが単一のセルに固定されているため、グループは `worksheet.getSparklineGroups().get(i)` を通じてアクセスされます。
- `Sparkline` とインデクサ `group.getSparklines().get(0)` は、グループ内の個々のスパークラインを返します。例では各グループに正確に 1 つのスパークラインが含まれているため、`for` ループは必要ありません。
- `Sparkline.toImage(Stream, ImageOrPrintOptions)` は、提供された `Stream` にスパークラインの画像を描画するレンダリングメソッドです。このメソッドは `void` を返します。呼び出し後にストリームからバイトを読み取ります。
- `Cell.EmbeddedImage` は `byte[]` プロパティ（`cell.setEmbeddedImage(byte[])` 経由で割り当て）で、単一セル内に画像を保存します。これは **Aspose.Cells 26.5 以降** で利用可能で、`toImage` でレンダリングされたスパークラインを同じワークブックに戻すラウンドトリップの推奨方法です。
- `HtmlSaveOptions.setExportActiveWorksheetOnly(boolean)` は、HTML エクスポートをアクティブなワークシートに制限します。単一ページレポートを生成する際に `HtmlSaveOptions` で最も一般的に使用されるプロパティの 1 つです。
- `ImageOrPrintOptions.setImageType(ImageType)` は `com.aspose.cells.drawing` パッケージに含まれており、`toImage` でのレンダリングおよびワークシートの画像への印刷時に使用される画像形式（例えば `ImageType.PNG`）を選択します。

## **関連記事**

- [Aspose.Cells for Java のスパークライン](/cells/ja/java/sparkline/)
- [セルへの画像の挿入](/cells/ja/java/inserting-an-image-into-a-cell/)
- [SmartMarker 単一セル配列レンダリング | Aspose.Cells Java](/cells/ja/java/SmartMarker-Single-Cell-Array-Rendering/)

{{< app/cells/assistant language="java" >}}