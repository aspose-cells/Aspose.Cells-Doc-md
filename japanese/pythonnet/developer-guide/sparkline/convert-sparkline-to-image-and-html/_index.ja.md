---
title: Aspose.Cells for Python via .NET でスパークラインを画像と HTML に変換する
linktitle: Convert Sparkline to Image and HTML
description: Aspose.Cells のスパークラインをスタンドアロン画像としてレンダリングしてセルに埋め込む方法と、スパークラインを含むワークシートを HtmlSaveOptions を使用して Python via .NET で HTML にエクスポートする方法を学習します。
keywords: Aspose.Cells, Python via .NET, sparkline, sparkline.to_image, cell.embedded_image, HtmlSaveOptions, スパークラインのレンダリング, スパークラインを画像に変換, スパークラインを HTML にエクスポート
type: docs
weight: 120
url: /ja/python-net/convert-sparkline-to-image-and-html/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
スパークラインはワークシートのセル内に配置されるミニチュアグラフです。Aspose.Cells では、各スパークラインをスタンドアロン画像として抽出したり(別のセルや外部レポートに埋め込むため)、スパークラインを含むワークシート全体を HTML にエクスポートしてブラウザベースで配布したりすることができます。本記事で使用されている `cell.embedded_image` プロパティは、**Aspose.Cells 26.5 以降**で利用可能です。
{{% /alert %}}

## **はじめに**

スパークラインは、ワークシート内で直接トレンドを可視化するコンパクトな手段です。Excel ユーザーはワークシート上でスパークラインを確認しますが、実際のシナリオではスパークラインをセルから外に出す必要が生じることがあります。例えば、別のセルに静止画像として埋め込んだり、自動メールに添付したり、Web に公開される HTML レポートの一部としてレンダリングしたりする場合です。

Aspose.Cells はこれらの両方の操作をサポートしています。`sparkline.to_image` メソッドは個々のスパークラインをストリームにレンダリングし、そのバイト配列を `cell.embedded_image` に割り当てることで、画像をワークブックの単一セル内に保存できます。また、`HtmlSaveOptions` を使用すれば、ワークブック全体(スパークラインを含む)を自己完結型の HTML ファイルに変換できます。本記事では両方のワークフローについて詳しく説明します。

## **ワークフロー 1 — スパークラインを画像にレンダリングしてセルに埋め込む**

このワークフローでは、ソース値の小さな範囲を含むワークシートを作成し、3 つの異なるスパークライン グループ(ライン、列、積み上げ/勝ち負け)をその範囲に割り当て、各グループを PNG としてレンダリングし、それらの PNG バイトを隣接するセルに埋め込み画像として書き込みます。最終結果は、ライブ スパークラインとレンダリングされた画像の両方を含む単一の `.xlsx` ファイルです。

### **ステップごとの手順**

1. 作業ディレクトリを定義し、ディスク上に存在することを確認します。
2. 新しい `Workbook` を作成し、最初の `Worksheet` への参照を取得します。
3. セル `A1` から `E1` に 5 つのサンプル数値(例えば、日次売上や気温測定値など)を格納します。
4. `worksheet.sparkline_groups.add(...)` を呼び出して、3 つの `SparklineGroup` オブジェクトをワークシートに追加します。
   - アンカー位置が `F1`、データ範囲が `A1:E1` の `SparklineType.LINE` グループ。
   - アンカー位置が `G1`、データ範囲が `A1:E1` の `SparklineType.COLUMN` グループ。
   - アンカー位置が `H1`、データ範囲が `A1:E1` の `SparklineType.STACKED`(勝ち負け)グループ。
5. `ImageOrPrintOptions` インスタンスを作成し、その `image_type` を `ImageType.PNG` に設定して、各スパークラインが透明な PNG としてレンダリングされるようにします。
6. 3 つのグループそれぞれについて、`group.sparklines[0].to_image(memory_stream, image_options)` を使用して単一のスパークラインをレンダリングし、`BytesIO` ストリームを `bytes` オブジェクトに変換して、配列をそれぞれ `worksheet.cells["F2"].embedded_image`、`worksheet.cells["G2"].embedded_image`、`worksheet.cells["H2"].embedded_image` に割り当てます。
7. ワークブックを `output_with_sparklines.xlsx` として保存します。

```python
import aspose.cells as ac

# 新しいワークブックを作成し、最初のワークシートにアクセスします
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]

# セルA1:E1にサンプルデータを入力します
worksheet.cells["A1"].put_value(5)
worksheet.cells["B1"].put_value(-3)
worksheet.cells["C1"].put_value(8)
worksheet.cells["D1"].put_value(-2)
worksheet.cells["E1"].put_value(6)

# F1（列5、行0）にアンカーされた折れ線スパークライングループを追加します
line_area = ac.CellArea()
line_area.start_column = 5
line_area.end_column = 5
line_area.start_row = 0
line_area.end_row = 0
line_idx = worksheet.sparkline_groups.add(ac.SparklineType.LINE, "A1:E1", False, line_area)

# G1（列6、行0）にアンカーされた縦棒スパークライングループを追加します
column_area = ac.CellArea()
column_area.start_column = 6
column_area.end_column = 6
column_area.start_row = 0
column_area.end_row = 0
column_idx = worksheet.sparkline_groups.add(ac.SparklineType.COLUMN, "A1:E1", False, column_area)

# H1（列7、行0）にアンカーされたWin/Loss（積み上げ）スパークライングループを追加します
stacked_area = ac.CellArea()
stacked_area.start_column = 7
stacked_area.end_column = 7
stacked_area.start_row = 0
stacked_area.end_row = 0
stacked_idx = worksheet.sparkline_groups.add(ac.SparklineType.STACKED, "A1:E1", False, stacked_area)

# PNG出力用の画像オプションを設定します
image_options = ac.ImageOrPrintOptions()
image_options.image_type = ac.ImageType.PNG

# 折れ線スパークラインを画像に変換し、セルF2に埋め込みます
line_sp = worksheet.sparkline_groups[line_idx].sparklines[0]
ms = ac.MemoryStream()
line_sp.to_image(ms, image_options)
worksheet.cells["F2"].embedded_image = ms.to_array()

# 縦棒スパークラインを画像に変換し、セルG2に埋め込みます
column_sp = worksheet.sparkline_groups[column_idx].sparklines[0]
ms = ac.MemoryStream()
column_sp.to_image(ms, image_options)
worksheet.cells["G2"].embedded_image = ms.to_array()

# Win/Lossスパークラインを画像に変換し、セルH2に埋め込みます
stacked_sp = worksheet.sparkline_groups[stacked_idx].sparklines[0]
ms = ac.MemoryStream()
stacked_sp.to_image(ms, image_options)
worksheet.cells["H2"].embedded_image = ms.to_array()

# ワークブックをディスクに保存します
workbook.save("output_with_sparklines.xlsx")
```

上記のコードは、スパークラインの各ビジュアル表現が 2 つの形式で複製されるワークブックを生成します。1 行目にアンカー配置されたライブのネイティブ スパークラインと、2 行目の隣接セルに直接埋め込まれた静止 PNG 画像です。画像がファイル自体内に格納されているため、ワークブックは埋め込み画像参照が壊れることなく、単一の自己完結型の成果物としてメール送信やアーカイブが可能です。各スパークライン グループを PNG としてレンダリングし、`BytesIO` ストリームを `bytes` オブジェクトに変換して、対象セルの `embedded_image` プロパティにバイトを割り当てます — この割り当てによって、画像はセルに保存されるコンテンツの一部となります。

{{% alert color="primary" %}}
各スパークライン グループは単一のセルにアンカーされるため、`for` ループで列挙する代わりにインデクサ `group.sparklines[0]` を通じてアクセスできます。これにより、レンダリング コードを簡潔に保ち、「アンカー セルごとに 1 つのスパークライン」という典型的なパターンと一致します。`cell.embedded_image` を介して画像のバイトを保存するには、Aspose.Cells 26.5 以降が必要です。
{{% /alert %}}

## **ワークフロー 2 — スパークラインのワークシートを HTML にエクスポートする**

ワークブックにライブ スパークライン(およびオプションで埋め込み画像の対応物)が含まれたら、ワークシート全体を HTML として保存することで Web に公開できます。`HtmlSaveOptions` クラスには、このエクスポートを制御するためのオプションがあります。このワークフローでは、ワークフロー 1 で生成された `output_with_sparklines.xlsx` ファイルを再利用し、クリーンな単一ページの HTML ドキュメントに変換します。

### **ステップごとの手順**

1. ワークフロー 1 で生成された `output_with_sparklines.xlsx` ファイルが、作業ディレクトリ内のディスク上で利用可能であることを確認します。
2. そのファイルを新しい `Workbook` インスタンスに読み込みます。
3. `HtmlSaveOptions` をインスタンス化し、その `export_active_worksheet_only` プロパティを `True` に設定して、結果として生成される HTML ファイルにワークブック全体ではなくアクティブなワークシートのみが含まれるようにします。
4. `workbook.save("sparklines.html", html_options)` を呼び出して、HTML 出力をディスクに書き込みます。

```python
import aspose.cells as ac

workbook = ac.Workbook("output_with_sparklines.xlsx")
html_options = ac.HtmlSaveOptions()
html_options.export_active_worksheet_only = True
workbook.save("sparklines.html", html_options)
```

上記のコードは、ワークフロー 1 からのスパークラインを含むワークブックを、ポータブルな HTML ファイルに変換します。スパークラインは、エクスポート モードに応じてインライン SVG または PNG レンダリングとして生成される HTML 内に保持されるため、エンドユーザーは Excel がインストールされていなくても、最新のブラウザでトレンドを確認できます。`export_active_worksheet_only` を `True` に設定することで、非表示シートや補助データを誤って公開することを回避できます。ユーザーに現在表示されているワークシートのみがエクスポートされます。

{{% alert color="primary" %}}
`HtmlSaveOptions` クラスには、`export_hidden_worksheet`、`export_images_as_base64`、`encoding` など、出力を細かく調整するための追加プロパティがあります。デプロイ先のターゲットに応じてこれらを適宜調整してください。
{{% /alert %}}

## **API 概要**

上記のワークフローは、少数の Aspose.Cells API の連携に依存しています。

- `SparklineGroup` およびコレクション アクセサ `worksheet.sparkline_groups` は、各スパークライン グループのタイプ(Line、Column、Stacked)、データ範囲、アンカー セルを宣言するために使用されます。本記事では各グループが単一のセルにアンカーされているため、グループは `worksheet.sparkline_groups[i]` を通じてアクセスされます。
- `Sparkline` およびインデクサ `group.sparklines[0]` は、グループ内の個々のスパークラインを返します。例では各グループに正確に 1 つのスパークラインが含まれているため、`for` ループは不要です。
- `sparkline.to_image(Stream, ImageOrPrintOptions)` は、スパークラインの画像を提供されたストリームに書き込むレンダリング メソッドです。このメソッドは `None` を返します。呼び出し後にストリームからバイトを読み取ります。
- `cell.embedded_image` は、単一セル内に画像を保存する `bytes` プロパティです。これは **Aspose.Cells 26.5 以降**で利用可能であり、`to_image` でレンダリングされたスパークラインを同じワークブックにラウンドトリップさせるための推奨される方法です。
- `html_save_options.export_active_worksheet_only`(`bool`) は、HTML エクスポートをアクティブなワークシートに限定します。これは、単一ページ レポートを生成する際に `HtmlSaveOptions` で最も一般的に使用されるプロパティの 1 つです。
- `image_or_print_options.image_type` は `aspose.cells.drawing` 名前空間に存在し、`to_image` でのレンダリング時およびワークシートを画像に印刷する際に使用される画像フォーマット(例えば `ImageType.PNG`)を選択します。

## **関連記事**

- [Sparklines in Aspose.Cells for Python via .NET](/cells/ja/python-net/sparkline/)
- [Inserting an Image into a Cell](/cells/ja/python-net/inserting-an-image-into-a-cell/)
- [SmartMarker Single Cell Array Rendering | Aspose.Cells for Python via .NET](/cells/ja/python-net/SmartMarker-Single-Cell-Array-Rendering/)

{{< app/cells/assistant language="python" >}}