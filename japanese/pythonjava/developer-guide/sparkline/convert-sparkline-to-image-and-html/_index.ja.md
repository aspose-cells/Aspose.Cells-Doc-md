---
title: Aspose.Cells for Python via Java でスパークラインを画像と HTML に変換する
linktitle: Aspose.Cells for Python via Java でスパークラインを画像と HTML に変換する
description: Aspose.Cells のスパークラインをセル埋め込み用のスタンドアロン画像にレンダリングする方法、およびスパークラインを含むワークシートを HtmlSaveOptions を使用して HTML にエクスポートする方法を学習します。
keywords: Aspose.Cells, Python via Java, スパークライン, Sparkline.toImage, Cell.embeddedImage, HtmlSaveOptions, スパークラインをレンダリング, スパークラインを画像に変換, スパークラインを HTML にエクスポート
type: docs
weight: 120
url: /ja/python-java/convert-sparkline-to-image-and-html/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
スパークラインはワークシートのセル内に配置されるミニチュアチャートです。Aspose.Cells では、各スパークラインをスタンドアロン画像として抽出（別のセルや外部レポートに埋め込み用）したり、スパークラインを含むワークシート全体を HTML にエクスポートしてブラウザ経由で配信したりすることができます。本記事で使用する `Cell.embedded_image` プロパティは、**Aspose.Cells 26.5 以降** で利用可能です。
{{% /alert %}}

## **はじめに**
スパークラインは、ワークシート内で直接トレンドを視覚化するコンパクトな手段です。Excel ユーザーはセル内でそれを確認しますが、実際にはセル外で利用したいケースが多くあります。たとえば、別のセルに静的な画像として埋め込む場合、自動送信メールに添付する場合、Web に公開する HTML レポートの一部としてレンダリングする場合などです。
Aspose.Cells はこれら両方の操作をサポートしています。`Sparkline.to_image` メソッドは個々のスパークラインをストリームにレンダリングし、そのバイト列を `Cell.embedded_image` に割り当てることで、画像をワークブックの単一セル内に保存できます。別途、`HtmlSaveOptions` を使用すると、ワークブック全体（スパークラインを含む）を自己完結型の HTML ファイルに変換できます。本記事一覧では、両方のワークフローを順に説明します。

## **ワークフロー 1 — スパークラインを画像にレンダリングしてセルに埋め込む**
このワークフローでは、サンプル値を含む小さな範囲を持つワークシートを作成し、その範囲に 3 つの異なるスパークライン グループ（折れ線、縦棒、積み上げ/勝敗）を関連付け、各グループを PNG としてレンダリングし、それらの PNG バイト列を隣接するセルに埋め込み画像として書き込みます。最終結果は、ライブスパークラインとそのレンダリングされた画像の両方を含む単一の `.xlsx` ファイルです。

### **ステップごとの手順**
1. 作業ディレクトリを定義し、ディスク上に存在することを確認します。
2. 新しい `Workbook` を作成し、最初の `Worksheet` への参照を取得します。
3. セル `A1` から `E1` までに 5 つのサンプル数値（たとえば、日次売上や気温の読み取り値など）を入力します。
4. `worksheet.sparkline_groups.add(...)` を呼び出して、ワークシートに 3 つの `SparklineGroup` オブジェクトを追加します：
   - アンカー `F1`、データ範囲 `A1:E1` の `SparklineType.LINE` グループ。
   - アンカー `G1`、データ範囲 `A1:E1` の `SparklineType.COLUMN` グループ。
   - アンカー `H1`、データ範囲 `A1:E1` の `SparklineType.STACKED`（勝敗）グループ。
5. `ImageOrPrintOptions` インスタンスを作成し、各スパークラインが透明な PNG としてレンダリングされるように `image_type` を `ImageType.PNG` に設定します。
7. ワークブックを `output_with_sparklines.xlsx` として保存します。

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, Worksheet, CellArea, SparklineType, ImageType, ImageOrPrintOptions, Sparkline
from jpype import JClass
ByteArrayOutputStream = JClass('java.io.ByteArrayOutputStream')
# Create a new workbook and access the first worksheet
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
# Populate sample data in cells A1:E1
worksheet.getCells().get("A1").putValue(5)
worksheet.getCells().get("B1").putValue(-3)
worksheet.getCells().get("C1").putValue(8)
worksheet.getCells().get("D1").putValue(-2)
worksheet.getCells().get("E1").putValue(6)
# Add a Line sparkline group anchored at F1 (column 5, row 0)
lineArea = CellArea()
lineArea.StartColumn = 5
lineArea.EndColumn = 5
lineArea.StartRow = 0
lineArea.EndRow = 0
lineIdx = worksheet.getSparklineGroups().add(SparklineType.LINE, "A1:E1", False, lineArea)
# Add a Column sparkline group anchored at G1 (column 6, row 0)
columnArea = CellArea()
columnArea.StartColumn = 6
columnArea.EndColumn = 6
columnArea.StartRow = 0
columnArea.EndRow = 0
columnIdx = worksheet.getSparklineGroups().add(SparklineType.COLUMN, "A1:E1", False, columnArea)
# Add a Win/Loss (Stacked) sparkline group anchored at H1 (column 7, row 0)
stackedArea = CellArea()
stackedArea.StartColumn = 7
stackedArea.EndColumn = 7
stackedArea.StartRow = 0
stackedArea.EndRow = 0
stackedIdx = worksheet.getSparklineGroups().add(SparklineType.STACKED, "A1:E1", False, stackedArea)
# Configure image options for PNG output
imageOptions = ImageOrPrintOptions()
imageOptions.setImageType(ImageType.PNG)
# Convert the Line sparkline to image and embed it in cell F2
lineSp = worksheet.getSparklineGroups().get(lineIdx).getSparklines().get(0)
ms = ByteArrayOutputStream()
lineSp.toImage(ms, imageOptions)
worksheet.getCells().get("F2").setEmbeddedImage(ms.toByteArray())
# Convert the Column sparkline to image and embed it in cell G2
columnSp = worksheet.getSparklineGroups().get(columnIdx).getSparklines().get(0)
ms = ByteArrayOutputStream()
columnSp.toImage(ms, imageOptions)
worksheet.getCells().get("G2").setEmbeddedImage(ms.toByteArray())
# Convert the Win/Loss sparkline to image and embed it in cell H2
stackedSp = worksheet.getSparklineGroups().get(stackedIdx).getSparklines().get(0)
ms = ByteArrayOutputStream()
stackedSp.toImage(ms, imageOptions)
worksheet.getCells().get("H2").setEmbeddedImage(ms.toByteArray())
# Save the workbook to disk
workbook.save("output_with_sparklines.xlsx")
jpype.shutdownJVM()
```

上記のコードは、スパークラインの各ビジュアル表現が 2 つの形式で複製されたワークブックを生成します。1 行目にアンカーされたネイティブのライブスパークラインと、2 行目の隣接セルに直接埋め込まれた静的な PNG 画像の 2 つの形式で表現されます。画像がファイル自体に保存されているため、ワークブックは埋め込まれた画像参照が壊れることなく、単一の自己完結型アーティファクトとしてメール送信やアーカイブが可能です。各スパークライン グループを PNG としてレンダリングし、`ByteArrayOutputStream` を `byte[]` に変換（または Python の `bytes` オブジェクトを取得するために `to_byte_array()` を使用）して、配列を対象セルの `embedded_image` プロパティに割り当てます。この代入によって画像がセルの保存内容の一部になります。

{{% alert color="primary" %}}
各スパークライン グループは単一セルにアンカーされているため、`for` ループで列挙する代わりにインデクサ `group.sparklines[0]` でアクセスできます。これにより、レンダリングコードを簡潔に保ち、一般的な「アンカーセル 1 つに対して 1 つのスパークライン」というパターンに一致します。`Cell.embedded_image` を介して画像バイト列を保存するには、Aspose.Cells 26.5 以降が必要です。
{{% /alert %}}

## **ワークフロー 2 — スパークラインのワークシートを HTML にエクスポートする**
ワークブックにライブスパークライン（および必要に応じて埋め込み画像のコピー）が含まれている場合、ワークシート全体を HTML として保存することで Web に公開できます。`HtmlSaveOptions` クラスには、このエクスポートを制御するための項目が用意されています。このワークフローでは、ワークフロー 1 で生成された `output_with_sparklines.xlsx` ファイルを再利用し、簡潔な単一ページの HTML ドキュメントに変換します。

### **ステップごとの手順**
1. ワークフロー 1 で生成された `output_with_sparklines.xlsx` ファイルが、作業ディレクトリに存在することを確認します。
2. そのファイルを新しい `Workbook` インスタンスにロードします。
3. `HtmlSaveOptions` をインスタンス化し、`export_active_worksheet_only` プロパティを `True` に設定して、結果の HTML ファイルにワークブック全体ではなくアクティブなワークシートのみが含まれるようにします。
4. `workbook.save("sparklines.html", html_options)` を呼び出して、HTML 出力をディスクに書き込みます。

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, HtmlSaveOptions
workbook = Workbook("output_with_sparklines.xlsx")
htmlOptions = HtmlSaveOptions()
htmlOptions.setExportActiveWorksheetOnly(True)
workbook.save("sparklines.html", htmlOptions)
jpype.shutdownJVM()
```

上記のコードは、ワークフロー 1 のスパークラインを含むワークブックを、ポータブルな HTML ファイルに変換します。スパークラインは、エクスポートモードに応じて生成された HTML 内にインラインの SVG または PNG として保持されるため、エンドユーザーは Excel をインストールすることなく、あらゆるモダンブラウザでトレンドを表示できます。`export_active_worksheet_only` を `True` に設定することで、非表示シートや補助データが誤って公開されることを防ぎ、現在ユーザーに表示されているワークシートのみがエクスポートされます。

{{% alert color="primary" %}}
`HtmlSaveOptions` クラスには、`export_hidden_worksheet`、`export_images_as_base64`、`encoding` など、出力を微調整するための追加プロパティがあります。デプロイメントターゲットに応じてこれらを適宜調整してください。
{{% /alert %}}

## **API 概要**
上記のワークフローは、少数の Aspose.Cells API が連携して動作することで実現されています。
- `SparklineGroup` およびコレクションアクセサ `worksheet.sparkline_groups` は、各スパークライン グループのタイプ（折れ線、縦棒、積み上げ）、データ範囲、アンカーセルを宣言するために使用されます。本記事では各グループを単一セルにアンカーしているため、`worksheet.sparkline_groups[i]` でグループにアクセスします。
- `Sparkline` およびインデクサ `group.sparklines[0]` は、グループ内の個々のスパークラインを返します。例のすべてのグループにはちょうど 1 つのスパークラインが含まれているため、`for` ループは不要です。
- `Sparkline.to_image(OutputStream, ImageOrPrintOptions)` は、スパークラインの画像を指定された `OutputStream`（`ByteArrayOutputStream` など）に書き込むレンダリングメソッドです。このメソッドは `void` を返します。呼び出し後にストリームからバイト列を読み取ります。
- `HtmlSaveOptions.export_active_worksheet_only`（`bool` 型）は、HTML エクスポートをアクティブなワークシートのみに制限します。これは、単一ページレポートを生成する際に `HtmlSaveOptions` で最も一般的に使用されるプロパティの 1 つです。
- `ImageOrPrintOptions.image_type` は `com.aspose.cells.drawing` 名前空間に属し、`to_image` でのレンダリングおよびワークシートの画像印刷時に使用される画像形式（たとえば `ImageType.PNG`）を選択します。
- [Aspose.Cells for Python via Java のスパークライン](/cells/ja/python-java/sparkline/)

{{< app/cells/assistant language="python" >}}