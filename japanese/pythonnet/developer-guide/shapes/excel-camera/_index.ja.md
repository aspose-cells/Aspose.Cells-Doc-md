---
title: Aspose.Cells for Python via .NET の Excel カメラ
linktitle: Aspose.Cells for Python via .NET の Excel カメラ
description: Aspose.Cells for Python via .NET で Excel カメラを使用して、セル範囲にリンクされ、ソースデータの変更時に更新され、すべてのソース書式を保持する動的なピクチャを作成する方法を学習します。
keywords: Aspose.Cells, Python, Excel カメラ, 動的ピクチャ, リンク付きピクチャ, Picture.Formula, UpdateSelectedValue, CreateRange, ToImage, BytesIO
type: docs
weight: 90
url: /ja/python-net/excel-camera/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

Excel カメラは、セル範囲のライブ画像をレンダリングし、通常のピクチャのように描画レイヤーにフロート表示するワークシートオブジェクトです。Aspose.Cells は、ソースデータが変更されるたびに自動更新される動的ピクチャと、範囲のワンタイムスナップショットをキャプチャする静的ピクチャの 2 つの作成モードをサポートしています。この記事では両方のアプローチを解説し、レイアウトに合った方を選択できるようにします。

## Excel カメラとは?
Excel カメラは、本質的にはワークシートの描画レイヤーの特定の行と列にアンカーされたピクチャオブジェクトです。通常の挿入ピクチャとは異なり、カメラは `"A1:F10"` などの A1 形式の数式を介してソース範囲にリンクされています。その範囲内のセルが変更されるたびに、カメラの画像は新しい内容を反映して自動的に更新されます。カメラはソース領域のすべての書式 — 罫線、背景色、フォント、数値形式 — を保持するため、セル内に見えるすべてのものがカメラの画像内にも表示されます。これにより、ダッシュボード、サマリー、サイドパネル、レポートレイアウトなど、スクロールやデータの繰り返しを行わずにリモート領域の視覚的なプレビューを表示したい場合に特に役立ちます。2 つの注意点があります。1 つ目は、ワークブックを保存する前に `update_selected_value()` を呼び出す必要があることです。2 つ目は、ファイルは HTML または PDF 形式でエクスポートする必要があることです。これは、これらの形式がライブ再計算ではなく、埋め込まれた画像データに依存しているためです。

## 方法 1 — 動的なカメラピクチャの追加
動的カメラは最も一般的なアプローチであり、Excel の組み込みカメラツールに最も近いものです。これは、初期画像コンテンツなしでピクチャを追加し、ソース範囲を参照する `formula` を割り当てることによって機能します。数式が割り当てられた後、`update_selected_value()` を呼び出すことで、埋め込まれた画像データがミラーするセルと同期するように更新されます。カメラは専用のクラスを通じて実装されているわけではなく、標準の `Picture` 型のみで構築されています。
主要な API は次のとおりです。
- `PictureCollection.add(int upperLeftRow, int upperLeftColumn, Stream stream)` — 指定された行と列にアンカーされたピクチャを追加します。`stream` パラメータに `None` を渡すと、動的カメラのプレースホルダーとして機能する空のピクチャが作成されます。メソッドは新しいピクチャのインデックスを返します。
- `worksheet.pictures[index]` — コレクションから特定の `Picture` を取得するためのインデクサーアクセス。
- `picture.formula` — カメラがミラーするソース範囲への A1 形式参照を保持する文字列プロパティ (get/set)。たとえば `"A1:F10"` などです。
- `picture.update_selected_value()` — `formula` で参照されるセルから埋め込まれた画像データを更新する void メソッド。

{{% alert color="primary" %}}
出力が HTML または PDF の場合、保存前に `update_selected_value()` を呼び出す必要があります。呼び出さないと、エクスポートされたファイルにピクチャデータが含まれず、レンダリングされた出力でカメラが空白として表示されます。
{{% /alert %}}

次のコードは、ワークブックを作成し、行 10、列 6 にアンカーされた空のピクチャを追加し、`formula` プロパティを介してソース範囲 `A1:F10` にリンクし、埋め込まれた画像データを更新して、ワークブックを保存します。

```python
from aspose.cells import Workbook, SaveFormat
workbook = Workbook()
worksheet = workbook.worksheets[0]
worksheet.name = "CameraDemo"
# ダイナミックカメラ: 空の画像を追加し、数式を使用して A1:F10 にリンクし、更新する
pictures = worksheet.pictures
index = pictures.add(10, 6, None)
pictures[index].formula = "A1:F10"
pictures[index].update_selected_value()
workbook.save("output_dynamic.xlsx", SaveFormat.XLSX)
```

## 方法 2 — 静的なカメラピクチャの追加
静的カメラは、本質的にはセル範囲のワンタイムレンダリングプレビューです。ライブリンクを維持する代わりに、範囲を画像バイトに 1 回レンダリングし、それらのバイトを `BytesIO` でラップして、通常のピクチャとして追加します。画像コンテンツは作成時点で固定され、ソースセルが変更されても自動更新されません。
主要な API は次のとおりです。
- `Cells.create_range(string address)` — `"A1:F10"` などの A1 形式アドレスから `Range` オブジェクトを構築します。
- `Range.to_image(ImageOrPrintOptions options)` — 範囲を画像バイトにレンダリングします。`None` を渡すとデフォルトのレンダリングオプションが使用されます。出力の細かい制御用のオーバーロードも存在します。
- `BytesIO(byte[] buffer)` — レンダリングされた画像バイトを `PictureCollection.add` に渡せる `BytesIO` でラップします。
- `PictureCollection.add(int upperLeftRow, int upperLeftColumn, Stream stream)` — 指定された行と列にピクチャを追加します。今回はレンダリングによって生成された `BytesIO` を渡します。
次のコードは、ワークブックを作成し、`A1:F10` の `Range` を構築し、`Range.to_image(null)` を介して画像バイトにレンダリングし、バイトを `BytesIO` でラップし、行 10、列 6 にアンカーされたピクチャを追加し、ワークブックを保存します。

```python
from io import BytesIO
from aspose.cells import Workbook, SaveFormat
workbook = Workbook()
worksheet = workbook.worksheets[0]
worksheet.name = "CameraDemo"
# 静的カメラ: Range を構築し、バイトにレンダリングし、BytesIO でラップしてピクチャとして追加
range_ = worksheet.cells.create_range("A1:F10")
pictures = worksheet.pictures
pictures.add(10, 6, BytesIO(range_.to_image(None)))
workbook.save("output_static.xlsx", SaveFormat.XLSX)
```

## 動的と静的の選択
- **動的カメラ:** 再計算のたびに更新され、`update_selected_value()` の後に HTML と PDF のエクスポートをサポートし、ファイルのライフタイム全体でライブリンクの動作を保持します。
- **静的カメラ:** 更新されることのないワンタイムレンダリングで、データのライブミラーではなく、ビルド時に埋め込まれた固定ビジュアルスナップショットが必要な場合に役立ちます。
Aspose.Cells は、`picture.formula` と `update_selected_value()` で構築される自動更新される動的カメラと、`Range.to_image` と `BytesIO` で構築されるワンショットの静的カメラの両方をサポートしています。出力をソースセルと同期させる必要がある場合は動的アプローチを、ビルド時に固定ビジュアルスナップショットのみが必要な場合は静的アプローチを選択してください。

{{< app/cells/assistant language="python-net" >}}