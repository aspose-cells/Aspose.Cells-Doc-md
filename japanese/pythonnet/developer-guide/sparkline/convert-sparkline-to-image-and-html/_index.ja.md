---
title: Aspose.Cells for Python via .NET でスパークラインを画像と HTML に変換する
linktitle: Aspose.Cells for Python via .NET でスパークラインを画像と HTML に変換する
description: Aspose.Cells のスパークラインをセル埋め込み用の独立した画像としてレンダリングする方法と、スパークラインを含むワークシートを HtmlSaveOptions を使用して HTML にエクスポートする方法を Python via .NET で学びます。
keywords: Aspose.Cells, Python via .NET, スパークライン, sparkline.to_image, cell.embedded_image, HtmlSaveOptions, スパークラインのレンダリング, スパークラインを画像に変換, スパークラインを HTML にエクスポート
type: docs
weight: 120
url: /ja/python-net/convert-sparkline-to-image-and-html/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
スパークラインはワークシートのセル内に配置された小さなグラフです。Aspose.Cells では、各スパークラインを独立した画像として抽出（別のセルや外部レポートへの埋め込み用）したり、スパークラインを含むワークシート全体をブラウザで配布するために HTML にエクスポートしたりすることができます。本記事で使用する `cell.embedded_image` プロパティは **Aspose.Cells 26.5 以降** で利用可能です。
{{% /alert %}}

## **Introduction**
スパークラインは、ワークシート内で直接トレンドを視覚化するコンパクトな方法です。Excel ユーザーはそのまま表示しますが、多くの実際のシナリオでは、スパークラインをセルから取り出して使用する必要があります。例えば、静的な画像として別のセルに埋め込んだり、自動メールに添付したり、Web に公開された HTML レポートの一部としてレンダリングしたりする場合です。
Aspose.Cells はこれらの両方の操作をサポートしています。`sparkline.to_image` メソッドは個々のスパークラインをストリームにレンダリングし、結果のバイトを `cell.embedded_image` に割り当てて、画像をワークブックの単一セル内に保存できます。別途，`HtmlSaveOptions` を使用すると、ワークブック全体（スパークラインを含むすべて）を自己完結型の HTML ファイルに変換できます。本記事では両方のワークフローをエンドツーエンドで説明します。

## **Workflow 1 — Render Sparklines to Images and Embed Them into Cells**
このワークフローでは、ソース値の小さな範囲を含むワークシートを作成し、3 つの異なるスパークライン グループ（ライン、列、積み上げ/勝敗）をその範囲に割り当て、各グループを PNG としてレンダリングして、それらの PNG バイトを隣接するセルに埋め込み画像として書き込みます。最終結果は、生のスパークラインとそのレンダリングされた画像の両方を含む単一の `.xlsx` ファイルです。

### **Step-by-Step Instructions**
1. 作業ディレクトリを定義し、ディスク上に存在することを確認します。
2. 新しい `Workbook` を作成し、最初の `Worksheet` の参照を取得します。
3. セル `A1` から `E1` に 5 つのサンプル数値（例えば、日次売上や気温測定値など）を入力します。
4. `worksheet.sparkline_groups.add(...)` を呼び出して、ワークシートに 3 つの `SparklineGroup` オブジェクトを追加します。
   - データ範囲 `A1:E1` で `F1` にアンカーされた `SparklineType.LINE` グループ。
   - データ範囲 `A1:E1` で `G1` にアンカーされた `SparklineType.COLUMN` グループ。
   - データ範囲 `A1:E1` で `H1` にアンカーされた `SparklineType.STACKED`（勝敗）グループ。
5. `ImageOrPrintOptions` インスタンスを作成し、`image_type` を `ImageType.PNG` に設定して、各スパークラインが透明な PNG としてレンダリングされるようにします。
7. ワークブックを `output_with_sparklines.xlsx` として保存します。

```python
import aspose.cells as ac
# Create a new workbook and access the first worksheet
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
# Populate sample data in cells A1:E1
worksheet.cells["A1"].put_value(5)
worksheet.cells["B1"].put_value(-3)
worksheet.cells["C1"].put_value(8)
worksheet.cells["D1"].put_value(-2)
worksheet.cells["E1"].put_value(6)
# Add a Line sparkline group anchored at F1 (column 5, row 0)
line_area = ac.CellArea()
line_area.start_column = 5
line_area.end_column = 5
line_area.start_row = 0
line_area.end_row = 0
line_idx = worksheet.sparkline_groups.add(ac.SparklineType.LINE, "A1:E1", False, line_area)
# Add a Column sparkline group anchored at G1 (column 6, row 0)
column_area = ac.CellArea()
column_area.start_column = 6
column_area.end_column = 6
column_area.start_row = 0
column_area.end_row = 0
column_idx = worksheet.sparkline_groups.add(ac.SparklineType.COLUMN, "A1:E1", False, column_area)
# Add a Win/Loss (Stacked) sparkline group anchored at H1 (column 7, row 0)
stacked_area = ac.CellArea()
stacked_area.start_column = 7
stacked_area.end_column = 7
stacked_area.start_row = 0
stacked_area.end_row = 0
stacked_idx = worksheet.sparkline_groups.add(ac.SparklineType.STACKED, "A1:E1", False, stacked_area)
# Configure image options for PNG output
image_options = ac.ImageOrPrintOptions()
image_options.image_type = ac.ImageType.PNG
# Convert the Line sparkline to image and embed it in cell F2
line_sp = worksheet.sparkline_groups[line_idx].sparklines[0]
ms = ac.MemoryStream()
line_sp.to_image(ms, image_options)
worksheet.cells["F2"].embedded_image = ms.to_array()
# Convert the Column sparkline to image and embed it in cell G2
column_sp = worksheet.sparkline_groups[column_idx].sparklines[0]
ms = ac.MemoryStream()
column_sp.to_image(ms, image_options)
worksheet.cells["G2"].embedded_image = ms.to_array()
# Convert the Win/Loss sparkline to image and embed it in cell H2
stacked_sp = worksheet.sparkline_groups[stacked_idx].sparklines[0]
ms = ac.MemoryStream()
stacked_sp.to_image(ms, image_options)
worksheet.cells["H2"].embedded_image = ms.to_array()
# Save the workbook to disk
workbook.save("output_with_sparklines.xlsx")
```

上記のコードは、スパークラインの各視覚表現が 2 つの形式で複製されたワークブックを生成します。行 1 にアンカーされたライブのネイティブ スパークラインと、行 2 の隣接するセルに直接埋め込まれた静的な PNG 画像です。画像はファイル自体内に存在するため、ワークブックは埋め込み画像参照を壊すことなくメール送信やアーカイブ可能な単一の自己完結型アーティファクトとして維持されます。各スパークライン グループを PNG としてレンダリングし、`BytesIO` ストリームを `bytes` オブジェクトに変換して、バイトを対象セルの `embedded_image` プロパティに割り当てます。この割り当てによって、画像はセルの保存内容の一部になります。

{{% alert color="primary" %}}
各スパークライン グループは単一のセルにアンカーされるため、`for` ループで列挙する代わりにインデクサ `group.sparklines[0]` を通じてアクセスできます。これによりレンダリング コードを短く保ち、一般的な「アンカー セルごとに 1 つのスパークライン」パターンと一致します。`cell.embedded_image` を介して画像バイトを保存するには Aspose.Cells 26.5 以降が必要です。

## **Workflow 2 — Export the Sparkline Worksheet to HTML**
ワークブックにライブ スパークライン（およびオプションで埋め込み画像の対応物）が含まれたら、ワークシート全体を HTML として保存することで Web に公開できます。`HtmlSaveOptions` クラスは、このエクスポートを制御するために必要な設定を公開しています。このワークフローでは、ワークフロー 1 で生成された `output_with_sparklines.xlsx` ファイルを再利用して、クリーンな単一ページ HTML ドキュメントに変換します。

### **Step-by-Step Instructions**
1. ワークフロー 1 で生成された `output_with_sparklines.xlsx` ファイルが作業ディレクトリ内のディスク上で利用可能であることを確認します。
2. そのファイルを新しい `Workbook` インスタンスに読み込みます。
3. `HtmlSaveOptions` をインスタンス化し、その `export_active_worksheet_only` プロパティを `True` に設定して、結果の HTML ファイルにワークブック全体ではなくアクティブなワークシートのみが含まれるようにします。
4. `workbook.save("sparklines.html", html_options)` を呼び出して、HTML 出力をディスクに書き込みます。

```python
import aspose.cells as ac
workbook = ac.Workbook("output_with_sparklines.xlsx")
html_options = ac.HtmlSaveOptions()
html_options.export_active_worksheet_only = True
workbook.save("sparklines.html", html_options)
```

上記のコードは、ワークフロー 1 からのスパークラインを含むワークブックを取得し、ポータブルな HTML ファイルに変換します。スパークラインは、エクスポート モードに応じて、生成された HTML 内にインライン SVG または PNG レンダリングとして保持されるため、エンドユーザーは Excel をインストールすることなく、どの最新ブラウザでもトレンドを表示できます。`export_active_worksheet_only` を `True` に設定することで、非表示シートや補助データを誤って公開することを避け、現在ユーザーに表示されているワークシートのみがエクスポートされます。
{{% /alert %}}

{{% alert color="primary" %}}
`HtmlSaveOptions` クラスは、`export_hidden_worksheet`、`export_images_as_base64`、`encoding` など、出力を微調整するための追加プロパティを提供します。デプロイメント ターゲットに応じてこれらを調整してください。

## **API Summary**
上記のワークフローは、少数の Aspose.Cells API の連携に依存しています。
- `SparklineGroup` とコレクション アクセサー `worksheet.sparkline_groups` は、各スパークライン グループのタイプ（ライン、列、積み上げ）、データ範囲、アンカー セルを宣言するために使用されます。本記事では各グループは単一セルにアンカーされているため、グループは `worksheet.sparkline_groups[i]` を通じてアクセスされます。
- `Sparkline` とインデクサ `group.sparklines[0]` は、グループ内の個々のスパークラインを返します。例のすべてのグループには正確に 1 つのスパークラインが含まれているため、`for` ループは不要です。
- `sparkline.to_image(Stream, ImageOrPrintOptions)` は、スパークラインの画像を指定されたストリームに書き込むレンダリング メソッドです。このメソッドは `None` を返します。呼び出し後にストリームからバイトを読み取ります。
- `html_save_options.export_active_worksheet_only`（`bool`）は、HTML エクスポートをアクティブなワークシートに制限します。単一ページ レポートを生成する際に、`HtmlSaveOptions` で最も一般的に使用されるプロパティの 1 つです。
- `image_or_print_options.image_type` は `aspose.cells.drawing` 名前空間に存在し、`to_image` でのレンダリングおよびワークシートの画像印刷時に使用される画像形式（例えば `ImageType.PNG`）を選択します。

## **Related Articles**
- [セルへの画像の挿入](/cells/ja/python-net/inserting-an-image-into-a-cell/)
{{% /alert %}}

{{< app/cells/assistant language="python" >}}