---
title: Aspose.Cells for .NET の Excel カメラ
linktitle: Aspose.Cells for .NET の Excel カメラ
description: Aspose.Cells for .NET で Excel カメラを使用して、セル範囲にリンクされソースデータと共に更新される動的画像を作成し、すべてのソース書式を保持する方法を学習します。
keywords: Aspose.Cells, .NET, Excel カメラ, 動的画像, リンク画像, Picture.Formula, UpdateSelectedValue, CreateRange, ToImage, MemoryStream
type: docs
weight: 90
url: /ja/net/excel-camera/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

Excel カメラは、セル範囲のライブ画像を描画するワークシートオブジェクトであり、通常の画像と同じように描画レイヤーに浮かんで表示されます。Aspose.Cells は 2 つの作成モードをサポートしています。1 つはソースデータが変更されるたびに自動更新される動的画像、もう 1 つは範囲のワンタイムスナップショットをキャプチャする静的画像です。この記事ではレイアウトに適合する方を選択できるよう、両方のアプローチを順に説明します。

## What Is Excel Camera?
Excel カメラは基本的に、ワークシートの描画レイヤーの特定の行と列にアンカーされた画像オブジェクトです。通常の挿入画像とは異なり、カメラは `"A1:F10"` のような A1 形式の式を通じてソース範囲にリンクされています。その範囲内のセルが変更されるたびに、カメラの画像は新しい内容を反映して自動的に更新されます。カメラはソース領域の完全な書式を保持します — 罫線、背景色、フォント、数値書式など、セル内に表示されているすべてのものがカメラの画像内にも表示されます。これにより、スクロールやデータの繰り返しなしで離れた領域の視覚的なプレビューを表示したいダッシュボード、サマリー、サイドパネル、レポートレイアウトでカメラは特に便利です。2 つの注意点があります。ワークブックを保存する前に `UpdateSelectedValue()` を呼び出す必要があり、ファイルは HTML または PDF にエクスポートされます。これは、これらの形式がライブ再計算ではなく埋め込まれた画像データに依存しているためです。

## Method 1 — Add a Dynamic Camera Picture
動的カメラは最も一般的なアプローチであり、Excel の組み込みカメラツールに最も近いものです。これは、初期画像コンテンツを持たない画像を追加し、ソース範囲を参照する `Formula` を割り当てることによって機能します。式が割り当てられた後、`UpdateSelectedValue()` を呼び出すことで、埋め込まれた画像データがミラー化するセルと同期するように更新されます。カメラは専用のクラスを通じて実装されているわけではなく、完全に標準の `Picture` 型上に構築されています。
主要な API は次のとおりです:
- `PictureCollection.Add(int upperLeftRow, int upperLeftColumn, Stream stream)` — 指定された行と列にアンカーされた画像を追加します。`stream` パラメータに `null` を渡すと、動的カメラのプレースホルダーとして機能する空の画像が作成されます。メソッドは新しい画像のインデックスを返します。
- `worksheet.Pictures[index]` — コレクションから特定の `Picture` を取得するためのインデクサーアクセスです。
- `Picture.Formula` — `"A1:F10"` のような、カメラがミラー化するソース範囲への A1 形式参照を保持する文字列プロパティ(get/set)です。
- `Picture.UpdateSelectedValue()` — `Formula` で参照されるセルから埋め込まれた画像データを更新する void メソッドです。

{{% alert color="primary" %}}
出力が HTML または PDF の場合、`UpdateSelectedValue()` は保存前に必ず呼び出す必要があります。そうしないと、エクスポートされたファイルに画像データが含まれず、レンダリングされた出力でカメラが空白として表示されます。
{{% /alert %}}

次のコードは、ワークブックを作成し、行 10 列 6 にアンカーされた空の画像を追加し、`Formula` プロパティを通じてソース範囲 `A1:F10` にリンクし、埋め込まれた画像データを更新して、ワークブックを保存します。

```csharp
using System;
using System.IO;
using System.Drawing;
using Aspose.Cells;
using Aspose.Cells.Drawing;
var workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];
worksheet.Name = "CameraDemo";
// Dynamic Camera: add an empty picture, link it via Formula to A1:F10, then refresh
var pictures = worksheet.Pictures;
int index = pictures.Add(10, 6, (Stream)null);
pictures[0].Formula = "A1:F10";
pictures[0].UpdateSelectedValue();
workbook.Save("output_dynamic.xlsx", SaveFormat.Xlsx);
```

## Method 2 — Add a Static Camera Picture
静的カメラは本質的にセル範囲のワンタイムレンダリングプレビューです。ライブリンクを維持する代わりに、範囲を画像バイトに一度レンダリングし、それらのバイトを `MemoryStream` でラップして通常の画像として追加します。画像の内容は作成時に固定され、ソースセルが変更されても自動更新されません。
主要な API は次のとおりです:
- `Cells.CreateRange(string address)` — `"A1:F10"` のような A1 形式アドレスから `Range` オブジェクトを構築します。
- `Range.ToImage(ImageOrPrintOptions options)` — 範囲を画像バイトにレンダリングします。`null` を渡すとデフォルトのレンダリングオプションが使用されます。出力をより細かく制御するためのオーバーロードも存在します。
- `new MemoryStream(byte[] buffer)` — レンダリングされた画像バイトを `PictureCollection.Add` に渡すことができる `MemoryStream` でラップします。
- `PictureCollection.Add(int upperLeftRow, int upperLeftColumn, Stream stream)` — 今回はレンダリングによって生成された `MemoryStream` を渡して、指定された行と列にアンカーされた画像を追加します。
次のコードは、ワークブックを作成し、`A1:F10` の `Range` を構築し、`Range.ToImage(null)` を通じて画像バイトにレンダリングし、バイトを `MemoryStream` でラップし、行 10 列 6 にアンカーされた画像を追加して、ワークブックを保存します。

```csharp
using System;
using System.IO;
using System.Drawing;
using Aspose.Cells;
using Aspose.Cells.Drawing;
var workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];
worksheet.Name = "CameraDemo";
// Static Camera: build Range, render to bytes, wrap in MemoryStream, add as picture
var range = workbook.Worksheets[0].Cells.CreateRange("A1:F10");
var pictures = worksheet.Pictures;
pictures.Add(10, 6, new MemoryStream(range.ToImage(null)));
workbook.Save("output_static.xlsx", SaveFormat.Xlsx);
```

## Choosing Between Dynamic and Static
- **動的カメラ:** 再計算のたびに更新され、`UpdateSelectedValue()` の後に HTML および PDF エクスポートをサポートし、ファイルのライフタイム全体にわたってライブリンク動作を保持します。
- **静的カメラ:** 一度だけレンダリングされ更新されない画像で、データのライブミラーではなくビルド時に固定されたビジュアルスナップショットを埋め込みたい場合に便利です。
Aspose.Cells は、`Picture.Formula` と `UpdateSelectedValue()` 上に構築された自動更新される動的カメラと、`Range.ToImage` と `MemoryStream` 上に構築されたワンショット静的カメラの両方をサポートしています。出力がソースセルと同期する必要がある場合は動的アプローチを選択し、ビルド時に固定されたビジュアルスナップショットのみが必要な場合は静的アプローチを選択してください。

## Related Articles
- [Aspose.Cells for .NET でスパークラインをイメージと HTML に変換する](/cells/ja/net/convert-sparkline-to-image-and-html/)
- [セルに画像を挿入する](/cells/ja/net/inserting-an-image-into-a-cell/)
- [Aspose.Cells for .NET でピボットテーブルにフィルターフィールドを追加する](/cells/ja/net/add-page-field-in-pivot-table/)
- [Aspose.Cells for .NET でピボットテーブルにスタイルを適用する](/cells/ja/net/apply-style-to-pivot-table/)
- [ピボットテーブルのページフィールドレイアウトを変更する](/cells/ja/net/change-page-field-layout/)

{{< app/cells/assistant language="csharp" >}}