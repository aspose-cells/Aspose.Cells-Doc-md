---
title: Aspose.Cells for Node.js via Java の Excel カメラ
linktitle: Aspose.Cells for Node.js via Java の Excel カメラ
description: Aspose.Cells for Node.js via Java の Excel カメラを使用して、セル範囲にリンクされ、ソースデータと共に更新され、すべてのソース書式を保持する動的画像を作成する方法について説明します。
keywords: Aspose.Cells, Aspose.Cells for Node.js via Java, Excel カメラ, 動的画像, リンクされた画像, Picture.Formula, UpdateSelectedValue, CreateRange, ToImage, Buffer
type: docs
weight: 90
url: /ja/nodejs-java/excel-camera/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

Excel カメラは、セル範囲のライブ画像をレンダリングし、通常の画像のように描画レイヤーにフロートするワークシートオブジェクトです。Aspose.Cells は、ソースデータが変更されるたびに自動更新される動的画像と、範囲の 1 回限りのスナップショットをキャプチャする静的画像という 2 つの作成モードをサポートしています。この記事では両方のアプローチについて説明し、レイアウトに適したものを選択できるようにします。

## Excel カメラとは？
Excel カメラは、基本的に、ワークシートの描画レイヤーの特定の行と列に固定された画像オブジェクトです。通常の挿入画像とは異なり、カメラは `"A1:F10"` などの A1 形式の数式を介してソース範囲にリンクされています。その範囲内のセルが変更されるたびに、カメラの画像は新しいコンテンツを反映して自動的に更新されます。カメラはソース領域の完全な書式（罫線、背景色、フォント、および数値書式）を保持するため、セル内に表示されるすべてがカメラの画像内にも表示されます。これにより、カメラは、スクロールやデータの繰り返しを行わずにリモート領域の視覚的なプレビューが必要なダッシュボード、サマリー、サイドパネル、レポートレイアウトで特に役立ちます。2 つの注意事項があります。ワークブックを保存する前に `updateSelectedValue()` を呼び出す必要があり、また、カメラはライブ再計算ではなく埋め込まれた画像データに依存しているため、ファイルは HTML または PDF にエクスポートする必要があります。

## 方法 1 — 動的カメラ画像を追加する
動的カメラは最も一般的なアプローチであり、Excel の組み込みカメラツールに最も近いものです。これは、初期画像コンテンツのない画像を追加し、ソース範囲を参照する `Formula` を割り当てることで機能します。数式が割り当てられた後、`updateSelectedValue()` を呼び出すと、埋め込まれた画像データが更新され、ミラーするセルと同期されます。カメラは専用のクラスでは実装されておらず、標準の `Picture` 型のみで構築されています。
主要な API は次のとおりです:
- `PictureCollection.add(int upperLeftRow, int upperLeftColumn, InputStream stream)` — 指定された行と列に固定された画像を追加します。`stream` パラメータに `null` を渡すと、動的カメラのプレースホルダーとして機能する空の画像が作成されます。このメソッドは新しい画像のインデックスを返します。
- `worksheet.getPictures().get(index)` — コレクションから特定の `Picture` を取得するためのインデクサーアクセス。
- `Picture.Formula` — カメラがミラーするソース範囲への A1 形式の参照（例：`"A1:F10"`）を保持する文字列プロパティ（`getFormula()`/`setFormula()`）。
- `Picture.updateSelectedValue()` — `Formula` で参照されるセルから埋め込まれた画像データを更新する void メソッド。

{{% alert color="primary" %}}
出力が HTML または PDF の場合、保存前に `updateSelectedValue()` を呼び出す必要があります。そうしないと、エクスポートされたファイルに画像データが含まれず、レンダリングされた出力でカメラが空白で表示されます。
{{% /alert %}}

次のコードは、ワークブックを作成し、行 10 列 6 に固定された空の画像を追加し、`Formula` プロパティを介してソース範囲 `A1:F10` にリンクし、埋め込まれた画像データを更新し、ワークブックを保存します。

```javascript
const aspose = require("aspose.cells");
let workbook = new aspose.Workbook();
let worksheet = workbook.getWorksheets().get(0);
worksheet.setName("CameraDemo");
// 動的カメラ: 空の画像を追加し、数式を使ってA1:F10にリンクし、更新する
let pictures = worksheet.getPictures();
let index = pictures.add(10, 6, null);
pictures.get(index).setFormula("A1:F10");
pictures.get(index).updateSelectedValue();
workbook.save("output_dynamic.xlsx", aspose.SaveFormat.XLSX);
```

## 方法 2 — 静的カメラ画像を追加する
静的カメラは、基本的に、セル範囲の 1 回限りのレンダリングプレビューです。ライブリンクを維持する代わりに、範囲を画像バイトに 1 回レンダリングし、それらのバイトを `ByteArrayInputStream` でラップして、通常の画像として追加します。画像コンテンツは作成時に固定され、ソースセルが変更されても自動更新されません。
主要な API は次のとおりです:
- `Cells.createRange(String address)` — `"A1:F10"` などの A1 形式のアドレスから `Range` オブジェクトを構築します。
- `Range.toImage(ImageOrPrintOptions options)` — 範囲を画像バイトにレンダリングします。`null` を渡すとデフォルトのレンダリングオプションが使用されます。出力のより細かい制御のためにオーバーロードが存在します。
- `new ByteArrayInputStream(byte[] buffer)` — レンダリングされた画像バイトを `PictureCollection.add` に渡すことができる `ByteArrayInputStream` でラップします。
- `PictureCollection.add(int upperLeftRow, int upperLeftColumn, InputStream stream)` — 指定された行と列に固定された画像を追加します。今回はレンダリングによって生成された `ByteArrayInputStream` を渡します。
次のコードは、ワークブックを作成し、`A1:F10` の `Range` を構築し、`range.toImage(null)` を通じて画像バイトにレンダリングし、バイトを `ByteArrayInputStream` でラップし、行 10 列 6 に固定された画像を追加し、ワークブックを保存します。

```javascript
const aspose = require("aspose.cells");
let workbook = new aspose.Workbook();
let worksheet = workbook.getWorksheets().get(0);
worksheet.setName("CameraDemo");
// 静的カメラ: 範囲を作成し、バイトにレンダリングしてByteArrayInputStreamでラップし、画像として追加する
let range = worksheet.getCells().createRange("A1:F10");
let imageBytes = range.toImage(null);
let pictures = worksheet.getPictures();
pictures.add(10, 6, new aspose.ByteArrayInputStream(imageBytes));
workbook.save("output_static.xlsx", aspose.SaveFormat.XLSX);
```

## 動的と静的の選択
- **動的カメラ:** 再計算のたびに更新され、`updateSelectedValue()` の後に HTML および PDF のエクスポートをサポートし、ファイルの存続期間にわたってライブリンクの動作を保持します。
- **静的カメラ:** 更新されることのない 1 回限りのレンダリングで、データのライブミラーではなく、ビルド時に埋め込まれた固定のビジュアルスナップショットが必要な場合に役立ちます。
Aspose.Cells は、`Picture.Formula` と `updateSelectedValue()` に基づく自動更新される動的カメラと、`Range.toImage` と `ByteArrayInputStream` に基づく 1 回限りの静的カメラの両方をサポートしています。出力をソースセルと同期させる必要がある場合は動的アプローチを選択し、ビルド時に固定のビジュアルスナップショットのみが必要な場合は静的アプローチを選択してください。

{{< app/cells/assistant language="nodejs-java" >}}