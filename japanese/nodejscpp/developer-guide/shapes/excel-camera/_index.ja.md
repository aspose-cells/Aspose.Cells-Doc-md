---
title: Aspose.Cells for Node.js via C++ の Excel カメラ
linktitle: Aspose.Cells for Node.js via C++ の Excel カメラ
description: Aspose.Cells for Node.js via C++ で Excel カメラを使用して、セル範囲にリンクされた動的画像を作成する方法を学びます。ソースデータで更新され、すべてのソース書式が保持されます。
keywords: Aspose.Cells, Aspose.Cells for Node.js via C++, Excel カメラ, 動的画像, リンク画像, Picture.formula, updateSelectedValue, createRange, toImage, Buffer
type: docs
weight: 90
url: /ja/nodejs-cpp/excel-camera/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

Excel カメラは、セル範囲のライブ画像をレンダリングし、通常の画像と同じように描画レイヤーに浮かぶワークシートオブジェクトです。Aspose.Cells は 2 つの作成モードをサポートしています。ソースデータが変更されるたびに自動更新される動的画像と、範囲のワンタイムスナップショットをキャプチャする静的画像です。この記事では両方のアプローチを解説し、レイアウトに合った方を選択できるようにします。

## Excel カメラとは?
Excel カメラは、本質的にはワークシートの描画レイヤーの特定の行と列に固定された画像オブジェクトです。通常の挿入画像とは異なり、カメラは `"A1:F10"` などの A1 形式の数式を通じてソース範囲にリンクされています。範囲内のセルが変更されるたびに、カメラの画像は新しい内容を反映して自動的に更新されます。カメラはソース領域の完全な書式を保持します。罫線、背景色、フォント、および数値書式が保持されるため、セル内に表示されているすべての内容がカメラの画像内にも表示されます。このため、カメラはダッシュボード、サマリー、サイドパネル、およびリモート領域をスクロールやデータの繰り返しなしでプレビュー表示したいレポートレイアウトに特に役立ちます。2 つの注意点があります。ワークブックを保存する前に `updateSelectedValue()` を呼び出す必要があります。また、これらの形式はライブ再計算ではなく埋め込まれた画像データに依存しているため、ファイルは HTML または PDF にエクスポートする必要があります。

## 方法 1 — 動的なカメラ画像を追加する
動的カメラは最も一般的なアプローチであり、Excel の組み込みカメラツールに最も近い方法です。これは、初期画像コンテンツなしで画像を追加し、ソース範囲を参照する `Formula` を割り当てることによって機能します。数式が割り当てられた後、`updateSelectedValue()` を呼び出すと、埋め込まれた画像データが更新され、ミラー化するセルと同期されます。カメラは専用のクラスを通じて実装されていません。標準の `Picture` 型のみで構築されています。
主要な API は次のとおりです。
- `Pictures.add(int upperLeftRow, int upperLeftColumn, null)` — 指定された行と列に固定された画像を追加します。`stream` パラメータに `null` を渡すと、空の画像が作成され、動的カメラのプレースホルダーとして機能します。このメソッドは新しい画像のインデックスを返します。
- `pictures.get(index)` — インデックスによってコレクションから特定の `Picture` を取得します。
- `Picture.formula` — カメラがミラー化するソース範囲への A1 形式参照を保持する文字列プロパティ (get/set)。例: `"A1:F10"`。
- `Picture.updateSelectedValue()` — `formula` で参照されているセルから埋め込まれた画像データを更新する void メソッド。

{{% alert color="primary" %}}
出力が HTML または PDF の場合、保存前に `updateSelectedValue()` を必ず呼び出してください。呼び出さないと、エクスポートされたファイルに画像データが含まれず、レンダリングされた出力でカメラが空白で表示されてしまいます。
{{% /alert %}}

次のコードは、ワークブックを作成し、行 10 列 6 に固定された空の画像を追加し、`Formula` プロパティを通じてソース範囲 `A1:F10` にリンクし、埋め込まれた画像データを更新して、ワークブックを保存します。

```javascript
const aspose = require("aspose.cells");
let workbook = new aspose.Workbook();
let worksheet = workbook.getWorksheets().get(0);
worksheet.setName("CameraDemo");
// 動的カメラ: 空の画像を追加し、FormulaでA1:F10にリンクし、更新します
let pictures = worksheet.getPictures();
let index = pictures.add(10, 6, null);
pictures.get(index).setFormula("A1:F10");
pictures.get(index).updateSelectedValue();
workbook.save("output_dynamic.xlsx", aspose.SaveFormat.Xlsx);
```

## 方法 2 — 静的なカメラ画像を追加する
静的カメラは、本質的にセル範囲のワンタイムレンダリングプレビューです。ライブリンクを維持する代わりに、範囲を 1 回だけ画像バイトにレンダリングし、それらのバイトを `Buffer` でラップして、通常の画像として追加します。画像コンテンツは作成時に固定され、ソースセルが変更されても自動更新されません。
主要な API は次のとおりです。
- `Cells.createRange(address)` — `"A1:F10"` などの A1 形式アドレスから `Range` オブジェクトを構築します。
- `Range.toImage(ImageOrPrintOptions options)` — 範囲を画像バイトにレンダリングします。`null` を渡すとデフォルトのレンダリングオプションが使用されます。出力の細かい制御用のオーバーロードも存在します。
- `new Buffer(byte[] buffer)` — レンダリングされた画像バイトを `getPictures().add` に渡せる `Buffer` でラップします。
- `Pictures.add(int upperLeftRow, int upperLeftColumn, null)` — 指定された行と列に画像を固定します。今回はレンダリングによって生成された `Buffer` を渡します。
次のコードは、ワークブックを作成し、`A1:F10` の `Range` を構築し、`range.toImage(null)` を通じて画像バイトにレンダリングし、バイトを `Buffer` でラップし、行 10 列 6 に固定された画像を追加して、ワークブックを保存します。

```javascript
const aspose = require("aspose.cells");
const { MemoryStream } = require("aspose.cells");
let workbook = new aspose.Workbook();
let worksheet = workbook.getWorksheets().get(0);
worksheet.setName("CameraDemo");
// Static Camera: build Range, render to bytes, wrap in MemoryStream, add as picture
let range = worksheet.getCells().createRange("A1:F10");
let imageBytes = range.toImage(null);
let stream = new MemoryStream();
stream.write(imageBytes);
let pictures = worksheet.getPictures();
pictures.add(10, 6, stream);
workbook.save("output_static.xlsx", aspose.SaveFormat.Xlsx);
```

## 動的と静的のどちらを選択するか
- **動的カメラ:** 再計算のたびに更新され、`updateSelectedValue()` 後の HTML および PDF エクスポートをサポートし、ファイルの存続期間にわたってライブリンクの動作を保持します。
- **静的カメラ:** 更新されないワンタイムレンダリングで、ライブなデータのミラーではなく、ビルド時に固定されたビジュアルスナップショットを埋め込みたい場合に便利です。
Aspose.Cells は、`Picture.formula` と `updateSelectedValue()` に基づく動的で自動更新されるカメラと、`Range.toImage` と `Buffer` に基づく静的でワンショットのカメラの両方をサポートしています。出力をソースセルと期させる必要がある場合は動的アプローチを、ビルド時に固定されたビジュアルスナップショットのみが必要な場合は静的アプローチを選択してください。

{{< app/cells/assistant language="nodejs-cpp" >}}