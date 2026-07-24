---
title: PivotTableのPivotFieldのDisplayNameによってCellオブジェクトを取得する
type: docs
weight: 70
url: /ja/python-net/get-the-cell-object-by-displayname-of-pivotfield-of-pivottable/
description: Aspose.Cells for Python via .NETで、PivotTableのPivotFieldのDisplayNameによってCellオブジェクトを取得する方法
keywords: Python用のExcel、Excel PythonライブラリのAspose.Cellsを使用して、PivotTableのPivotFieldのDisplayNameによってCellオブジェクトを取得します。
---

{{% alert color="primary" %}}

Aspose.Cells for Python via .NETでは、ピボットフィールドのディスプレイ名によってセルオブジェクトにアクセスするために使用できる[**PivotTable.get_cell_by_display_name(display_name)**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/get_cell_by_display_name/#str)メソッドを提供しています。このメソッドは、ピボットフィールドヘッダーを強調表示または書式設定したい場合に役立ちます。この記事では、データフィールドの表示名によってセルオブジェクトを取得し、その後書式設定を適用する方法について説明しています。

{{% /alert %}}

## **PivotTableのPivotFieldのDisplayNameによってCellオブジェクトを取得する方法**

以下のコードは、ワークシートの最初のピボットテーブルにアクセスし、ピボットテーブルの2番目のデータフィールドのDisplay名によるセルを取得します。そして、セルの塗りつぶし色とフォント色をそれぞれライトブルーとブラックに変更します。以下のスクリーンショットは、コードの実行前と後のピボットテーブルの様子を示しています。

|**ピボットテーブル - 実行前**|
| :- |
|![todo:image_alt_text](get-the-cell-object-by-displayname-of-pivotfield-of-pivottable_1.png)|

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-GetCellByDisplayName-GetCellObjectByDisplayName.py" >}}

|**ピボットテーブル - 実行後**|
| :- |
|![todo:image_alt_text](get-the-cell-object-by-displayname-of-pivotfield-of-pivottable_2.png)|
{{< app/cells/assistant language="python-net" >}}
