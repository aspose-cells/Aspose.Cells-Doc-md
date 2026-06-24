---
title: Aspose.Cells for Python via Java でスパークラインを画像と HTML に変換
linktitle: Convert Sparkline to Image and HTML
description: HtmlSaveOptions を使用して、セル埋め込み用のスタンドアロン画像として Aspose.Cells のスパークラインをレンダリングし、スパークラインを含むワークシートを HTML にエクスポートする方法を学びます。
keywords: Aspose.Cells, Python via Java, sparkline, Sparkline.toImage, Cell.embeddedImage, HtmlSaveOptions, スパークラインのレンダリング, スパークラインを画像に変換, スパークラインを HTML にエクスポート
type: docs
weight: 120
url: /ja/python-java/convert-sparkline-to-image-and-html/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
スパークラインはワークシートのセル内に配置されるミニチュアグラフです。Aspose.Cells では、各スパークラインをスタンドアロン画像として抽出(別のセルや外部レポートに埋め込むため)したり、スパークラインを含むワークシート全体を HTML にエクスポートしてブラウザベースの配信を行うことができます。この記事で使用されている `Cell.embedded_image` プロパティは **Aspose.Cells 26.5 以降** で利用可能です。
{{% /alert %}}

## **はじめに**

スパークラインは、ワークシート内で直接トレンドを視覚化するためのコンパクトな方法です。Excel ユーザーはそのままの状態で表示しますが、多くの実世界のシナリオでは、スパークラインをセルから取り出す必要があります。例えば、別のセルに静的な画像として埋め込んだり、自動化されたメールに添付したり、Web に公開された HTML レポートの一部としてレンダリングしたりする場合です。

Aspose.Cells はこれらの両方の操作をサポートしています。`Sparkline.to_image` メソッドは個々のスパークラインをストリームにレンダリングし、結果のバイトを `Cell.embedded_image` に割り当てて、画像をワークブックの単一セル内に保存できます。別途、`HtmlSaveOptions` を使用すると、ワークブック全体(スパークラインを含むすべて)を自己完結型の HTML ファイルに変換できます。この記事では、両方のワークフローについて順を追って説明します。

## **ワークフロー 1 — スパークラインを画像にレンダリングしてセルに埋め込む**

このワークフローでは、少量のソース値を含むワークシートを作成し、3 つの異なるスパークライン グループ(Line、Column、Stacked/Win-Loss)をその範囲にアタッチし、各グループを PNG としてレンダリングして、それらの PNG バイトを隣接するセルに埋め込み画像として書き込みます。最終結果は、ライブスパークラインとそのレンダリングされた画像の両方を含む単一の `.xlsx` ファイルです。

### **ステップバイステップの手順**

1. 作業ディレクトリを定義し、ディスク上に存在することを確認します。
2. 新しい `Workbook` を作成し、最初の `Worksheet` への参照を取得します。
3. セル `A1` から `E1` までの 5 つのサンプル数値(例えば、日次売上や温度測定値など)を入力します。
4. `worksheet.sparkline_groups.add(...)` を呼び出して、3 つの `SparklineGroup` オブジェクトをワークシートに追加します:
   - データ範囲 `A1:E1` で `F1` にアンカーされた `SparklineType.LINE` グループ。
   - データ範囲 `A1:E1` で `G1` にアンカーされた `SparklineType.COLUMN` グループ。
   - データ範囲 `A1:E1` で `H1` にアンカーされた `SparklineType.STACKED`(win/loss)グループ。
5. `ImageOrPrintOptions` インスタンスを作成し、その `image_type` を `ImageType.PNG` に設定して、各スパークラインが透明な PNG としてレンダリングされるようにします。
6. 3 つのグループそれぞれについて、`group.sparklines[0].to_image(byte_array_output_stream, image_options)` を使用して単一のスパークラインをレンダリングし、`ByteArrayOutputStream` を `byte[]` に変換(または `to_byte_array()` を Python の `bytes` に読み込み)、バイトをそれぞれ `worksheet.cells["F2"].embedded_image`、`worksheet.cells["G2"].embedded_image`、および `worksheet.cells["H2"].embedded_image` に割り当てます。
7. ワークブックを `output_with_sparklines.xlsx` として保存します。

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, CellArea, SparklineType, ImageType, ImageOrPrintOptions, Sparkline
from jpype import JClass

ByteArrayOutputStream = JClass('java.io.ByteArrayOutputStream')

# 新しいワークブックを作成し、最初のワークシートにアクセスします
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)

# セルA1:E1にサンプルデータを入力します
worksheet.getCells().get("A1").putValue(5)
worksheet.getCells().get("B1").putValue(-3)
worksheet.getCells().get("C1").putValue(8)
worksheet.getCells().get("D1").putValue(-2)
worksheet.getCells().get("E1").putValue(6)

# F1（列5、行0）に配置される折れ線スパークライングループを追加します
lineArea = CellArea()
lineArea.setStartColumn(5)
lineArea.setEndColumn(5)
lineArea.setStartRow(0)
lineArea.setEndRow(0)
lineIdx = worksheet.getSparklineGroups().add(SparklineType.Line, "A1:E1", False, lineArea)

# G1（列6、行0）に配置される縦棒スパークライングループを追加します
columnArea = CellArea()
columnArea.setStartColumn(6)
columnArea.setEndColumn(6)
columnArea.setStartRow(0)
columnArea.setEndRow(0)
columnIdx = worksheet.getSparklineGroups().add(SparklineType.Column, "A1:E1", False, columnArea)

# H1（列7、行0）に配置される勝敗（積み上げ）スパークライングループを追加します
stackedArea = CellArea()
stackedArea.setStartColumn(7)
stackedArea.setEndColumn(7)
stackedArea.setStartRow(0)
stackedArea.setEndRow(0)
stackedIdx = worksheet.getSparklineGroups().add(SparklineType.Stacked, "A1:E1", False, stackedArea)

# PNG出力用の画像オプションを設定します
imageOptions = ImageOrPrintOptions()
imageOptions.setImageType(ImageType.Png)

# 折れ線スパークラインを画像に変換し、セルF2に埋め込みます
lineSp = worksheet.getSparklineGroups().get(lineIdx).getSparklines().get(0)
ms = ByteArrayOutputStream()
lineSp.toImage(ms, imageOptions)
worksheet.getCells().get("F2").setEmbeddedImage(ms.toByteArray())

# 縦棒スパークラインを画像に変換し、セルG2に埋め込みます
columnSp = worksheet.getSparklineGroups().get(columnIdx).getSparklines().get(0)
ms = ByteArrayOutputStream()
columnSp.toImage(ms, imageOptions)
worksheet.getCells().get("G2").setEmbeddedImage(ms.toByteArray())

# 勝敗スパークラインを画像に変換し、セルH2に埋め込みます
stackedSp = worksheet.getSparklineGroups().get(stackedIdx).getSparklines().get(0)
ms = ByteArrayOutputStream()
stackedSp.toImage(ms, imageOptions)
worksheet.getCells().get("H2").setEmbeddedImage(ms.toByteArray())

# ワークブックをディスクに保存します
workbook.save("output_with_sparklines.xlsx")

jpype.shutdownJVM()
```

上記のコードは、スパークラインの各視覚表現が 2 つの形式で複製されたワークブックを生成します: 行 1 にアンカーされたライブでネイティブなスパークラインと、行 2 の隣接するセルに直接埋め込まれた静的な PNG 画像です。画像はファイル自体に保存されているため、ワークブックは単一の自己完結型の成果物のままで、埋め込まれた画像参照を壊すことなくメールで送信したりアーカイブしたりできます。各スパークライン グループを PNG としてレンダリングし、`ByteArrayOutputStream` を `byte[]` に変換(または `to_byte_array()` を使用して Python の `bytes` オブジェクトを取得)、配列をターゲット セルの `embedded_image` プロパティに割り当てます。この割り当てによって、画像はセルの保存内容の一部となります。

{{% alert color="primary" %}}
各スパークライン グループは単一のセルにアンカーされるため、`for` ループで列挙する代わりにインデクサー `group.sparklines[0]` を通じてアクセスできます。これにより、レンダリングコードが簡潔になり、典型的な「アンカー セルごとに 1 つのスパークライン」パターンに適合します。`Cell.embedded_image` 経由での画像のバイト保存には、Aspose.Cells 26.5 以降が必要です。
{{% /alert %}}

## **ワークフロー 2 — スパークラインのワークシートを HTML にエクスポートする**

ワークブックにライブスパークライン(およびオプションで埋め込まれた画像)が含まれるようになると、ワークシート全体を HTML として保存することで Web に公開できます。`HtmlSaveOptions` クラスは、このエクスポートを制御するために必要なオプションを公開しています。このワークフローでは、ワークフロー 1 で生成された `output_with_sparklines.xlsx` ファイルを再利用し、クリーンな単一ページの HTML ドキュメントに変換します。

### **ステップバイステップの手順**

1. ワークフロー 1 で生成された `output_with_sparklines.xlsx` ファイルが、作業ディレクトリ内のディスク上で利用可能であることを確認します。
2. そのファイルを新しい `Workbook` インスタンスに読み込みます。
3. `HtmlSaveOptions` をインスタンス化し、その `export_active_worksheet_only` プロパティを `True` に設定して、結果の HTML ファイルにワークブック全体ではなくアクティブなワークシートのみが含まれるようにします。
4. `workbook.save("sparklines.html", html_options)` を呼び出して、HTML 出力をディスクに書き込みます。

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, HtmlSaveOptions

workbook = Workbook("output_with_sparklines.xlsx")
htmlOptions = HtmlSaveOptions()
htmlOptions.setExportActiveWorksheetOnly(True)
workbook.save("sparklines.html", htmlOptions)

jpype.shutdownJVM()
```

上記のコードは、ワークフロー 1 からのスパークラインを含むワークブックを取得し、ポータブルな HTML ファイルに変換します。スパークラインは、エクスポートモードに応じて、生成された HTML 内にインライン SVG または PNG レンダリングとして保存されるため、エンドユーザーは Excel をインストールせずに最新のブラウザでトレンドを表示できます。`export_active_worksheet_only` を `True` に設定することで、非表示シートや補助データを誤って公開することを避け、現在ユーザーに表示されているワークシートのみがエクスポートされます。

{{% alert color="primary" %}}
`HtmlSaveOptions` クラスは、`export_hidden_worksheet`、`export_images_as_base64`、および `encoding` など、出力を微調整するための追加プロパティを提供します。デプロイメント ターゲットに応じてこれらを調整してください。
{{% /alert %}}

## **API 概要**

上記のワークフローは、一緒に機能する Aspose.Cells API の小さなセットに依存しています。

- `SparklineGroup` とコレクション アクセサー `worksheet.sparkline_groups` は、各スパークライン グループのタイプ(Line、Column、Stacked)、データ範囲、アンカー セルを宣言するために使用されます。この記事では、各グループは単一のセルにアンカーされているため、グループは `worksheet.sparkline_groups[i]` を通じてアクセスされます。
- `Sparkline` とインデクサー `group.sparklines[0]` は、グループ内の個々のスパークラインを返します。例のすべてのグループには正確に 1 つのスパークラインが含まれているため、`for` ループは必要ありません。
- `Sparkline.to_image(OutputStream, ImageOrPrintOptions)` は、スパークラインの画像を提供された `OutputStream`(`ByteArrayOutputStream` など)に書き込むレンダリングメソッドです。このメソッドは `void` を返します。呼び出し後にストリームからバイトを読み取ります。
- `Cell.embedded_image` は、単一セル内に画像を保存する `byte[]` プロパティです。これは **Aspose.Cells 26.5 以降** で利用可能であり、`to_image` でレンダリングされたスパークラインを同じワークブックにラウンドトリップする推奨方法です。
- `HtmlSaveOptions.export_active_worksheet_only`(`bool`)は、HTML エクスポートをアクティブなワークシートに制限します。これは、単一ページ レポートを生成する際に `HtmlSaveOptions` で最も一般的に使用されるプロパティの 1 つです。
- `ImageOrPrintOptions.image_type` は `com.aspose.cells.drawing` 名前空間にあり、`to_image` を使用してレンダリングするとき、およびワークシートを画像に印刷するときに使用される画像形式(例えば `ImageType.PNG`)を選択します。

## **関連記事**

- [Aspose.Cells for Python via Java の Aspose.Cells でのスパークライン](/cells/ja/python-java/sparkline/)
- [セルへの画像の挿入](/cells/ja/python-java/inserting-an-image-into-a-cell/)

{{< app/cells/assistant language="python" >}}