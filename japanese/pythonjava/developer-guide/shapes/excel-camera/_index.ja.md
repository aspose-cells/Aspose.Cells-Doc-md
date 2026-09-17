---
title: Excel Camera in Aspose.Cells for Python via Java
linktitle: Excel Camera
description: Aspose.Cells for Python via Java で Excel カメラを使用して、セル範囲にリンクされた動的な画像を作成する方法を学びます。ソースデータとともに更新され、すべてのソース書式が保持されます。
keywords: Aspose.Cells, Python via Java, Excel Camera, 動的画像, リンク画像, Picture.formula, updateSelectedValue, createRange, toImage, byte[] 配列
type: docs
weight: 90
url: /ja/python-java/excel-camera/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

Excel カメラは、セル範囲のライブ画像をレンダリングし、通常の画像と同様に描画レイヤーに浮かぶワークシートオブジェクトです。Aspose.Cells for Python via Java は 2 つの作成モードをサポートしています。ソースデータが変更されるたびに自動更新される動的画像と、範囲のワンタイムスナップショットをキャプチャする静的画像です。本記事では両方のアプローチを説明するので、レイアウトに適合するものを選択できます。

## Excel カメラとは?
Excel カメラは基本的に、ワークシートの描画レイヤーの特定の行と列にアンカーされた画像オブジェクトです。通常の挿入画像とは異なり、カメラは `"A1:F10"` などの A1 形式の数式を介してソース範囲にリンクされています。その範囲内のセルが変更されるたびに、カメラの画像は新しい内容を反映して自動的に更新されます。カメラはソース領域の完全な書式設定を保持します。罫線、背景色、フォント、数値書式など、セル内に見えるすべてのものがカメラの画像内にも表示されます。このため、スクロールやデータの繰り返しなしにリモート領域の視覚的なプレビューが必要なダッシュボード、サマリー、サイドパネル、レポートレイアウトで特に便利です。注意が 2 つあります。1 つ目は、ワークブックを保存する前に `updateSelectedValue()` を呼び出す必要があることです。2 つ目は、出力形式が HTML または PDF になることです。これは、これらの形式がライブ再計算ではなく埋め込まれた画像データに依存しているためです。

## 方法 1 — 動的なカメラ画像を追加する
動的なカメラは最も一般的なアプローチであり、Excel の組み込みカメラツールに最も近い一致です。初期の画像コンテンツなしで画像を追加し、ソース範囲を参照する数式を割り当てることによって機能します。数式が割り当てられた後、`updateSelectedValue()` を呼び出すと、埋め込まれた画像データが更新され、ミラー化するセルと同期されます。カメラは専用のクラスを通じて実装されるわけではなく、完全に標準の `Picture` 型に基づいて構築されています。
主要な API は次のとおりです:
- `PictureCollection.add(int upperLeftRow, int upperLeftColumn, input)` — 指定された行と列にアンカーされた画像を追加します。`stream` パラメータに `None` を渡すと、動的なカメラのプレースホルダーとして機能する空の画像が作成されます。このメソッドは新しい画像のインデックスを返します。
- `worksheet.getPictures().get(index)` — コレクションから特定の `Picture` を取得するアクセサ。
- `Picture.getFormula()` / `Picture.setFormula()` — カメラがミラー化するソース範囲への A1 形式参照 (`"A1:F10"` など) を取得/設定します。
- `Picture.updateSelectedValue()` — 数式で参照されるセルから埋め込まれた画像データを更新する void メソッド。

{{% alert color="primary" %}}
`updateSelectedValue()` は、出力が HTML または PDF の場合に保存する前に必ず呼び出す必要があります。そうしないと、エクスポートされたファイルに画像データが含まれず、レンダリングされた出力でカメラが空白として表示されます。
{{% /alert %}}

次のコードは、ワークブックを作成し、行 10、列 6 にアンカーされた空の画像を追加し、`setFormula` メソッドを介してソース範囲 `A1:F10` にリンクし、埋め込まれた画像データを更新して、ワークブックを保存します。

```python
import jpype
import jpype.imports
from asposecells.api import Workbook, SaveFormat
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
worksheet.setName("CameraDemo")
# 動的カメラ: 空の画像を追加し、数式を介して A1:F10 にリンクし、更新します
pictures = worksheet.getPictures()
index = pictures.add(10, 6, None)
pictures.get(index).setFormula("A1:F10")
pictures.get(index).updateSelectedValue()
workbook.save("output_dynamic.xlsx", SaveFormat.XLSX)
```

## 方法 2 — 静的なカメラ画像を追加する
静的カメラは本質的にセル範囲のワンタイムレンダリングプレビューです。ライブリンクを維持する代わりに、範囲を 1 回だけ画像バイトにレンダリングし、それらのバイトを `byte[]` 配列にラップして、通常の画像として追加します。画像コンテンツは作成時に固定され、ソースセルが変更されても自動更新されません。
主要な API は次のとおりです:
- `Cells.createRange(String address)` — `"A1:F10"` などの A1 形式アドレスから `Range` オブジェクトを構築します。
- `Range.toImage(ImageOrPrintOptions options)` — 範囲を画像バイトにレンダリングします。`None` を渡すとデフォルトのレンダリングオプションが使用されます。出力の細かい制御のためのオーバーロードも存在します。
- `byte[] array(byte[] buffer)` — レンダリングされた画像バイトを `PictureCollection.add` に渡せる `byte[] array` にラップします。
- `PictureCollection.add(int upperLeftRow, int upperLeftColumn, input)` — 指定された行と列にアンカーされた画像を追加します。今回はレンダリングによって生成された `byte[] array` を渡します。
次のコードは、ワークブックを作成し、`A1:F10` の `Range` を構築し、`Range.toImage(None)` を介して画像バイトにレンダリングし、バイトを `byte[]` 配列にラップし、行 10、列 6 にアンカーされた画像を追加して、ワークブックを保存します。

```python
import jpype
import jpype.imports
from asposecells.api import Workbook, SaveFormat
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
worksheet.setName("CameraDemo")
# 静的カメラ: 範囲を構築し、バイトにレンダリングし、ByteArrayInputStreamでラップして、画像として追加
range_ = worksheet.getCells().createRange("A1:F10")
image_bytes = range_.toImage(None)
pictures = worksheet.getPictures()
pictures.add(10, 6, jpype.JArray(jpype.JByte)(image_bytes))
workbook.save("output_static.xlsx", SaveFormat.XLSX)
```

## 動的と静的のどちらを選択するか
- **動的なカメラ:** 再計算のたびに更新され、`updateSelectedValue()` の後に HTML と PDF のエクスポートをサポートし、ファイルの存続期間にわたってライブリンクの動作を保持します。
- **静的なカメラ:** ワンタイムレンダリングで更新されることはなく、データのライブミラーではなくビルド時に埋め込まれた固定のビジュアルスナップショットが必要な場合に役立ちます。
Aspose.Cells for Python via Java は、`setFormula` と `updateSelectedValue()` に基づいて構築された動的で自動更新されるカメラと、`toImage` と `byte[] array` に基づいて構築された静的なワンショットカメラの両方をサポートしています。出力をソースセルと同期させる必要がある場合は動的アプローチを選択し、ビルド時に固定のビジュアルスナップショットのみが必要な場合は静的アプローチを選択してください。

{{< app/cells/assistant language="python" >}}