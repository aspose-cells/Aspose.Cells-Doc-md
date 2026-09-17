---
title: Aspose.Cells for Java でスパークラインを画像と HTML に変換する
linktitle: Aspose.Cells for Java でスパークラインを画像と HTML に変換する
description: Aspose.Cells のスパークラインをセル埋め込み用のスタンドアロン画像にレンダリングする方法と、スパークラインを含むワークシートを HtmlSaveOptions を使用して HTML にエクスポートする方法を学びます。
keywords: Aspose.Cells, Java, スパークライン, Sparkline.toImage, Cell.EmbeddedImage, HtmlSaveOptions, スパークラインをレンダリング, スパークラインを画像に変換, スパークラインを HTML にエクスポート
type: docs
weight: 120
url: /ja/java/convert-sparkline-to-image-and-html/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
スパークラインはワークシートのセル内に配置されるミニチュアグラフです。Aspose.Cells では、各スパークラインをスタンドアロン画像として抽出（別のセルや外部レポートへの埋め込み用）したり、スパークラインを含むワークシート全体をブラウザでの配信用 HTML にエクスポートしたりすることができます。本記事で使用する `Cell.EmbeddedImage` プロパティは **Aspose.Cells 26.5 以降** で利用可能です。

## **はじめに**
スパークラインはワークシート内で直接トレンドを視覚化するコンパクトな方法です。Excel ユーザーはセル内でそれを閲覧しますが、多くの実際のシナリオではスパークラインをセルから取り出す必要があります。例えば、別のセルに静的な画像として埋め込む、自動化されたメールに添付する、Web に公開された HTML レポートの一部としてレンダリングするといったケースです。
Aspose.Cells はこれらの両方の操作をサポートしています。`Sparkline.toImage` メソッドは個々のスパークラインをストリームにレンダリングし、結果のバイト列を `setEmbeddedImage` を介して `Cell.EmbeddedImage` に割り当てることで、その画像をワークブックの単一セル内に保存できます。さらに、`HtmlSaveOptions` を使用すると、スパークラインを含むワークブック全体を自己完結型の HTML ファイルに変換できます。本記事では両方のワークフローを順を追って説明します。

## **ワークフロー 1 — スパークラインを画像にレンダリングしてセルに埋め込む**
このワークフローでは、ソース値の小さな範囲を含むワークシートを作成し、その範囲に 3 種類の異なるスパークライングループ（ライン、列、積み上げ / 勝ち負け）を関連付け、各グループを PNG としてレンダリングして、それらの PNG バイト列を隣接するセルに埋め込み画像として書き込みます。最終的な結果は、ライブスパークラインとそのレンダリングされた画像の両方を含む単一の `.xlsx` ファイルです。

### **ステップごとの手順**
1. 作業ディレクトリを定義し、ディスク上に存在することを確認します。
2. 新しい `Workbook` を作成し、最初の `Worksheet` への参照を取得します。
3. セル `A1` から `E1` に 5 つのサンプル数値（例えば、日次売上や気温測定値など）を入力します。
4. `worksheet.getSparklineGroups().add(...)` を呼び出して、ワークシートに 3 つの `SparklineGroup` オブジェクトを追加します：
   - データ範囲 `A1:E1` で `F1` にアンカーされた `SparklineType.LINE` グループ。
   - データ範囲 `A1:E1` で `G1` にアンカーされた `SparklineType.COLUMN` グループ。
   - データ範囲 `A1:E1` で `H1` にアンカーされた `SparklineType.STACKED`（勝ち負け）グループ。
5. `ImageOrPrintOptions` インスタンスをビルドし、`setImageType(ImageType.PNG)` を呼び出して、各スパークラインが透過 PNG としてレンダリングされるようにします。
6. `workbook.save("output_with_sparklines.xlsx")` を呼び出して、ワークブックをディスクに保存します。

```java
import com.aspose.cells.*;
import java.io.*;
// 新しいワークブックを作成し、最初のワークシートにアクセスします
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
// セルA1:E1にサンプルデータを入力します
worksheet.getCells().get("A1").putValue(5);
worksheet.getCells().get("B1").putValue(-3);
worksheet.getCells().get("C1").putValue(8);
worksheet.getCells().get("D1").putValue(-2);
worksheet.getCells().get("E1").putValue(6);
// F1（列5、行0）にアンカーされた折れ線スパークライングループを追加します
CellArea lineArea = CellArea.createCellArea(5, 0, 5, 0);
int lineIdx = worksheet.getSparklineGroups().add(SparklineType.LINE, "A1:E1", false, lineArea);
// G1（列6、行0）にアンカーされた縦棒スパークライングループを追加します
CellArea columnArea = CellArea.createCellArea(6, 0, 6, 0);
int columnIdx = worksheet.getSparklineGroups().add(SparklineType.COLUMN, "A1:E1", false, columnArea);
// H1（列7、行0）にアンカーされたWin/Loss（積み上げ）スパークライングループを追加します
CellArea stackedArea = CellArea.createCellArea(7, 0, 7, 0);
int stackedIdx = worksheet.getSparklineGroups().add(SparklineType.STACKED, "A1:E1", false, stackedArea);
// PNG出力用の画像オプションを設定します
ImageOrPrintOptions imageOptions = new ImageOrPrintOptions();
imageOptions.setImageType(ImageType.PNG);
// 折れ線スパークラインを画像に変換し、セルF2に埋め込みます
Sparkline lineSp = worksheet.getSparklineGroups().get(lineIdx).getSparklines().get(0);
ByteArrayOutputStream lineMs = new ByteArrayOutputStream();
lineSp.toImage(lineMs, imageOptions);
worksheet.getCells().get("F2").setEmbeddedImage(lineMs.toByteArray());
// 縦棒スパークラインを画像に変換し、セルG2に埋め込みます
Sparkline columnSp = worksheet.getSparklineGroups().get(columnIdx).getSparklines().get(0);
ByteArrayOutputStream columnMs = new ByteArrayOutputStream();
columnSp.toImage(columnMs, imageOptions);
worksheet.getCells().get("G2").setEmbeddedImage(columnMs.toByteArray());
// Win/Lossスパークラインを画像に変換し、セルH2に埋め込みます
Sparkline stackedSp = worksheet.getSparklineGroups().get(stackedIdx).getSparklines().get(0);
ByteArrayOutputStream stackedMs = new ByteArrayOutputStream();
stackedSp.toImage(stackedMs, imageOptions);
worksheet.getCells().get("H2").setEmbeddedImage(stackedMs.toByteArray());
// ワークブックをディスクに保存します
workbook.save("output_with_sparklines.xlsx");
```

上記のコードにより、スパークラインの各視覚表現が 2 つの形式で複製されたワークブックが生成されます。1 行目にアンカーされたライブのネイティブスパークラインと、2 行目の隣接するセルに直接埋め込まれた静的な PNG 画像です。画像はファイル自体に含まれているため、ワークブックは単一の自己完結型アーティファクトのままで、埋め込み画像の参照を壊すことなくメール送信やアーカイブが可能です。各スパークライングループを PNG としてレンダリングし、`ByteArrayOutputStream` を `byte[]` に変換して、その配列を `setEmbeddedImage(byte[])` を通じて対象セルの `EmbeddedImage` プロパティに割り当てます。この割り当てによって画像がセルの保存内容の一部になります。

{{% alert color="primary" %}}
各スパークライングループは単一セルにアンカーされているため、`for` ループで列挙する代わりにインデクサ `group.getSparklines().get(0)` を通じてアクセスできます。これによりレンダリングコードを簡潔に保ち、一般的な「アンカーセルごとに 1 つのスパークライン」パターンと一致します。`Cell.EmbeddedImage`（`setEmbeddedImage` を通じて設定）による画像のバイト列の保存には Aspose.Cells 26.5 以降が必要です。

## **ワークフロー 2 — スパークラインのワークシートを HTML にエクスポートする**
ワークブックにライブスパークライン（およびオプションで埋め込み画像の対応物）が含まれている場合、ワークシート全体を HTML として保存することで Web に公開できます。`HtmlSaveOptions` クラスは、このエクスポートを制御するために必要な設定を公開しています。このワークフローでは、ワークフロー 1 で生成された `output_with_sparklines.xlsx` ファイルを再利用し、それをクリーンな単一ページの HTML ドキュメントに変換します。

### **ステップごとの手順**
1. ワークフロー 1 で生成された `output_with_sparklines.xlsx` ファイルが作業ディレクトリ内のディスク上で利用可能であることを確認します。
2. そのファイルを新しい `Workbook` インスタンスに読み込みます。
3. `HtmlSaveOptions` をインスタンス化し、`setExportActiveWorksheetOnly(true)` を呼び出して、結果の HTML ファイルがワークブック全体ではなくアクティブなワークシートのみを含むようにします。
4. `workbook.save("sparklines.html", htmlOptions)` を呼び出して、HTML 出力をディスクに書き込みます。

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook("output_with_sparklines.xlsx");
HtmlSaveOptions htmlOptions = new HtmlSaveOptions();
htmlOptions.setExportActiveWorksheetOnly(true);
workbook.save("sparklines.html", htmlOptions);
```

上記のコードは、ワークフロー 1 のスパークラインを含むワークブックを取得し、ポータブルな HTML ファイルに変換します。スパークラインは、エクスポートモードに応じて、生成された HTML 内にインライン SVG または PNG のレンダリングとして保存されるため、エンドユーザーは Excel をインストールすることなく、どの最新ブラウザでもトレンドを閲覧できます。`setExportActiveWorksheetOnly(true)` を介して `ExportActiveWorksheetOnly` を `true` に設定することで、非表示シートや補助データを誤って公開することを避け、ユーザーに現在表示されているワークシートのみがエクスポートされます。

{{% alert color="primary" %}}
`HtmlSaveOptions` クラスには、出力を微調整するための追加プロパティがあります。例えば `ExportHiddenWorksheet`、`ExportImagesAsBase64`、`Encoding` などです。デプロイメントターゲットに応じてこれらを調整してください。

## **API の概要**
上記のワークフローは、連携して動作する少数の Aspose.Cells API に依存しています。
- `SparklineGroup` およびコレクションアクセサ `worksheet.getSparklineGroups()` は、各スパークライングループのタイプ（ライン、列、積み上げ）、データ範囲、アンカーセルを宣言するために使用されます。本記事では各グループが単一セルにアンカーされているため、グループは `worksheet.getSparklineGroups().get(i)` を通じてアクセスされます。
- `Sparkline` およびインデクサ `group.getSparklines().get(0)` は、グループ内の個々のスパークラインを返します。例では各グループが正確に 1 つのスパークラインを含むため、`for` ループは必要ありません。
- `Sparkline.toImage(Stream, ImageOrPrintOptions)` は、スパークラインの画像を提供された `Stream` に書き込むレンダリングメソッドです。このメソッドは `void` を返します。呼び出し後にストリームからバイト列を読み取ります。
- `HtmlSaveOptions.setExportActiveWorksheetOnly(boolean)` は、HTML エクスポートをアクティブなワークシートのみに制限します。これは、単一ページレポートを生成する際に `HtmlSaveOptions` で最も一般的に使用されるプロパティの 1 つです。
- `ImageOrPrintOptions.setImageType(ImageType)` は `com.aspose.cells.drawing` パッケージにあり、`toImage` でのレンダリングおよびワークシートを画像に印刷する際に使用される画像フォーマット（例えば `ImageType.PNG`）を選択します。`java
{{% /alert %}}

{{% /alert %}}

{{% /alert %}}

{{< app/cells/assistant language="java" >}}