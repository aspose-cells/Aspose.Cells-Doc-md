---
title: PivotTableのPivotFieldのDisplayNameによってCellオブジェクトを取得する
type: docs
weight: 70
url: /ja/net/get-the-cell-object-by-displayname-of-pivotfield-of-pivottable/
---

{{% alert color="primary" %}}

Aspose.Cellsは、PivotFieldの表示名でセルオブジェクトにアクセスできる[**PivotTable.GetCellByDisplayName()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/methods/getcellbydisplayname)メソッドを提供しています。このメソッドは、ピボットフィールドのヘッダーを強調表示または書式設定したいときに便利です。この記事では、データフィールドの表示名によってセルオブジェクトを取得し、その後書式を適用する方法について説明します。

{{% /alert %}}

## **PivotTableのPivotFieldのDisplayNameによってCellオブジェクトを取得する**

以下のコードは、ワークシートの最初のピボットテーブルにアクセスし、ピボットテーブルの2番目のデータフィールドのDisplay名によるセルを取得します。そして、セルの塗りつぶし色とフォント色をそれぞれライトブルーとブラックに変更します。以下のスクリーンショットは、コードの実行前と後のピボットテーブルの様子を示しています。

|**ピボットテーブル - 実行前**|
| :- |
|![todo:image_alt_text](get-the-cell-object-by-displayname-of-pivotfield-of-pivottable_1.png)|

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-PivotTablesAndPivotCharts-GetCellByDisplayName-GetCellObjectByDisplayName.cs" >}}

|**ピボットテーブル - 実行後**|
| :- |
|![todo:image_alt_text](get-the-cell-object-by-displayname-of-pivotfield-of-pivottable_2.png)|
{{< app/cells/assistant language="csharp" >}}
