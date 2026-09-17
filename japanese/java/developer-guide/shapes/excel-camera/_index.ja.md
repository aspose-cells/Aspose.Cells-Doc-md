---
title: Aspose.Cells for Java の Excel カメラ
linktitle: Aspose.Cells for Java の Excel カメラ
description: Aspose.Cells for Java で Excel カメラを使用して、セル範囲にリンクされたソースデータの変更に応じて更新され、すべてのソース書式を保持する動的画像を作成する方法を学びます。
keywords: Aspose.Cells, Java, Excel カメラ, 動的画像, リンク画像, Picture.Formula, UpdateSelectedValue, CreateRange, ToImage, ByteArrayInputStream
type: docs
weight: 90
url: /ja/java/excel-camera/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

Excel カメラは、セル範囲のライブ画像をレンダリングし、通常の画像のように描画レイヤーに浮かぶワークシートオブジェクトです。Aspose.Cells は 2 つの作成モードをサポートしています。1 つはソースデータが変更されるたびに自動更新される動的画像、もう 1 つは範囲の 1 回限りのスナップショットをキャプチャする静的画像です。この記事では両方のアプローチを解説するので、レイアウトに合った方法を選択できます。

## What Is Excel Camera?
Excel カメラは、基本的にワークシートの描画レイヤーの特定の行と列に固定された画像オブジェクトです。通常の挿入画像とは異なり、カメラは `"A1:F10"` のような A1 形式の数式を通じてソース範囲にリンクされています。その範囲内のセルが変更されるたびに、カメラの画像は新しい内容を反映して自動的に更新されます。カメラはソース領域のすべての書式を保持します。罫線、背景色、フォント、数値形式です。セル内に表示されるすべての内容もカメラの画像内に表示されます。これにより、カメラはダッシュボード、サマリー、サイドパネル、レポートレイアウトなど、リモート領域のプレビューをスクロールやデータの繰り返しなしで表示したい場合に特に便利です。注意点が 2 つあります。ワークブックを保存する前に `updateSelectedValue()` を呼び出す必要があり、出力ファイルは埋め込まれた画像データに基づく HTML または PDF にエクスポートされます。

## Method 1 — Add a Dynamic Camera Picture
動的なカメラは最も一般的なアプローチであり、Excel の組み込みカメラツールに最も近い方法です。これは、初期画像コンテンツを持たない画像を追加し、その後ソース範囲を参照する `Formula` を割り当てることによって機能します。数式が割り当てられた後、`updateSelectedValue()` を呼び出すと、埋め込まれた画像データが更新され、ミラー化するセルと同期します。カメラは専用のクラスを通じて実装されているわけではなく、標準の `Picture` 型のみで構築されています。
主要な API は次のとおりです。
- `PictureCollection.add(int upperLeftRow, int upperLeftColumn, InputStream stream)` — 指定された行と列に固定された画像を追加します。`stream` パラメータに `null` を渡すと、動的なカメラのプレースホルダーとして機能する空の画像が作成されます。メソッドは新しい画像のインデックスを返します。
- `worksheet.getPictures().get(index)` — コレクションから特定の `Picture` を取得するためのインデクサアクセス。
- `Picture.setFormula(String value)` — カメラがミラー化するソース範囲 (例: `"A1:F10"`) への A1 形式参照を設定します。
- `Picture.updateSelectedValue()` — `Formula` で参照されるセルから埋め込まれた画像データを更新する void メソッド。

{{% alert color="primary" %}}
出力が HTML または PDF の場合、保存前に `updateSelectedValue()` を呼び出す必要があります。呼び出さないと、エクスポートされたファイルに画像データが含まれず、レンダリングされた出力でカメラが空白で表示されます。
{{% /alert %}}

次のコードは、ワークブックを作成し、10 行 6 列に固定された空の画像を追加し、`setFormula` を通じてソース範囲 `A1:F10` にリンクし、埋め込まれた画像データを更新して、ワークブックを保存します。

```java
import java.io.InputStream;
import com.aspose.cells.PictureCollection;
import com.aspose.cells.SaveFormat;
import com.aspose.cells.Workbook;
import com.aspose.cells.Worksheet;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
worksheet.setName("CameraDemo");
// Dynamic Camera: add an empty picture, link it via Formula to A1:F10, then refresh
PictureCollection pictures = worksheet.getPictures();
int index = pictures.add(10, 6, (InputStream) null);
pictures.get(index).setFormula("A1:F10");
pictures.get(index).updateSelectedValue();
workbook.save("output_dynamic.xlsx", SaveFormat.XLSX);
```

## Method 2 — Add a Static Camera Picture
静的カメラは、基本的にセル範囲の 1 回限りのレンダリングプレビューです。ライブリンクを維持する代わりに、範囲を画像バイトに一度レンダリングし、それらのバイトを `ByteArrayInputStream` にラップして通常の画像として追加します。画像コンテンツは作成時点で固定され、ソースセルが変更されても自動更新されません。
主要な API は次のとおりです。
- `Cells.createRange(String address)` — `"A1:F10"` のような A1 形式のアドレスから `Range` オブジェクトを構築します。
- `Range.toImage(ImageOrPrintOptions options)` — 範囲を画像バイトにレンダリングします。`null` を渡すとデフォルトのレンダリングオプションが使用されます。出力の詳細制御のためのオーバーロードも存在します。
- `new ByteArrayInputStream(byte[] buffer)` — レンダリングされた画像バイトを `PictureCollection.add` に渡すことができる `ByteArrayInputStream` にラップします。
- `PictureCollection.add(int upperLeftRow, int upperLeftColumn, InputStream stream)` — 今回はレンダリングによって生成された `ByteArrayInputStream` を渡して、指定された行と列に固定された画像を追加します。
次のコードは、ワークブックを作成し、`A1:F10` の `Range` を構築し、`Range.toImage(null)` を通じて画像バイトにレンダリングし、バイトを `ByteArrayInputStream` にラップし、10 行 6 列に固定された画像を追加して、ワークブックを保存します。

```java
import java.io.ByteArrayInputStream;
import com.aspose.cells.PictureCollection;
import com.aspose.cells.Range;
import com.aspose.cells.SaveFormat;
import com.aspose.cells.Workbook;
import com.aspose.cells.Worksheet;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
worksheet.setName("CameraDemo");
// Static Camera: build Range, render to bytes, wrap in ByteArrayInputStream, add as picture
Range range = worksheet.getCells().createRange("A1:F10");
PictureCollection pictures = worksheet.getPictures();
pictures.add(10, 6, new ByteArrayInputStream(range.toImage(null)));
workbook.save("output_static.xlsx", SaveFormat.XLSX);
```

## Choosing Between Dynamic and Static
- **動的なカメラ:** 再計算のたびに更新され、`updateSelectedValue()` の後に HTML と PDF のエクスポートをサポートし、ファイルのライフタイムを通じてライブリンク動作を保持します。
- **静的なカメラ:** 更新されることのない 1 回限りのレンダリングで、データのライブミラーではなくビルド時に固定されたビジュアルスナップショットを埋め込みたい場合に便利です。
Aspose.Cells は、`Picture.Formula` と `updateSelectedValue()` に基づく自動更新される動的なカメラと、`Range.toImage` と `ByteArrayInputStream` に基づく 1 回限りのカメラの両方をサポートしています。出力をソースセルと同期させる必要がある場合は動的なアプローチを選択し、ビルド時に固定されたビジュアルスナップショットのみが必要な場合は静的なアプローチを選択してください。

## Related Articles
- [Aspose.Cells for Java でスパークラインを画像と HTML に変換する](/cells/ja/java/convert-sparkline-to-image-and-html/)
- [セルに画像を挿入する](/cells/ja/java/inserting-an-image-into-a-cell/)
- [Aspose.Cells for Java でピボットテーブルにフィルターフィールドを追加する](/cells/ja/java/add-page-field-in-pivot-table/)
- [Aspose.Cells for Java でピボットテーブルにスタイルを適用する](/cells/ja/java/apply-style-to-pivot-table/)
- [ピボットテーブルでページフィールドのレイアウトを変更する](/cells/ja/java/change-page-field-layout/)

{{< app/cells/assistant language="java" >}}