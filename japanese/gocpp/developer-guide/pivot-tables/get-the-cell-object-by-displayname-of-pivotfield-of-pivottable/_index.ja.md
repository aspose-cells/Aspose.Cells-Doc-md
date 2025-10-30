---
title: Golang経由でC++を使ったピボットフィールドの表示名からセルオブジェクトを取得
linktitle: ピボットテーブルのピボットフィールドの表示名からセルオブジェクトを取得する方法
type: docs
weight: 70
url: /ja/go-cpp/get-the-cell-object-by-displayname-of-pivotfield-of-pivottable/
description: ピボットフィールドの表示名からセルオブジェクトを取得し、書式設定を適用する方法をAspose.Cells for C++を使って学びます。
---

{{% alert color="primary" %}}

 Aspose.Cellsは [**PivotTable::GetCellByDisplayName()**](https://reference.aspose.com/cells/go-cpp/pivottable/getcellbydisplayname/) メソッドを提供しており、これを使ってピボットフィールドの表示名からセルオブジェクトにアクセスできます。このメソッドはピボットフィールドヘッダーをハイライトまたは書式設定したいときに便利です。この記事では、データフィールドの表示名からセルオブジェクトを取得し、それに書式設定を適用する方法を説明しています。

{{% /alert %}}

## ** ピボットテーブルの表示名からセルオブジェクトを取得する**

 次のコードは、シートの最初のピボットテーブルにアクセスし、次にピボットテーブルの2番目のデータフィールドの表示名からセルを取得します。次に、そのセルの塗りつぶし色とフォント色をライトブルーと黒に変更します。以下はコード実行前後のピボットテーブルの見た目を示すスクリーンショットです。

|**ピボットテーブル - 実行前**|
| :- |
|![todo:image_alt_text](get-the-cell-object-by-displayname-of-pivotfield-of-pivottable_1.png)|

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-GetTheCellObjectByDisplaynameOfPivotfieldOfPivottable.go" >}}
|**ピボットテーブル - 実行後**|
| :- |
|![todo:image_alt_text](get-the-cell-object-by-displayname-of-pivotfield-of-pivottable_2.png)|
