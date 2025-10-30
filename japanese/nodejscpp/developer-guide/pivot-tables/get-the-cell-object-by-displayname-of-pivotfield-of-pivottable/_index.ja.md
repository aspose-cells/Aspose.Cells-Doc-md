---
title: PivotTableのPivotFieldのDisplayNameによってCellオブジェクトを取得する
type: docs
weight: 70
url: /ja/nodejs-cpp/get-the-cell-object-by-displayname-of-pivotfield-of-pivottable/
description: Aspose.Cells for Node.js via C++を使ったピボットテーブルのDisplayNameからセルオブジェクトを取得する方法
keywords: Aspose.Cells for Node.js via C++ Excel、Excel Node.jsライブラリ、ピボットテーブルのPivotFieldのDisplayNameからセルオブジェクトを取得 Aspose.Cells for Node.js via C++ Excelライブラリを使って
---

{{% alert color="primary" %}}

Aspose.Cells for Node.js via C++は、ピボットフィールドの表示名からセルオブジェクトにアクセスできる [**PivotTable.getCellByDisplayName(string)**](https://reference.aspose.com/cells/nodejs-cpp/pivottable/#getCellByDisplayName-string-) メソッドを提供します。このメソッドは、ピボットフィールドのヘッダーをハイライトしたり書式設定したいときに役立ちます。この記事では、データフィールドの表示名からセルオブジェクトを取得し、その後書式設定を適用する方法について説明します。

{{% /alert %}}

## **PivotTableのPivotFieldのDisplayNameによってCellオブジェクトを取得する方法**

以下のコードは、ワークシートの最初のピボットテーブルにアクセスし、ピボットテーブルの2番目のデータフィールドのDisplay名によるセルを取得します。そして、セルの塗りつぶし色とフォント色をそれぞれライトブルーとブラックに変更します。以下のスクリーンショットは、コードの実行前と後のピボットテーブルの様子を示しています。

|**ピボットテーブル - 実行前**|
| :- |
|![todo:image_alt_text](get-the-cell-object-by-displayname-of-pivotfield-of-pivottable_1.png)|

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "PivotTables-GetCellByDisplayName-GetCellObjectByDisplayName.js" >}}

|**ピボットテーブル - 実行後**|
| :- |
|![todo:image_alt_text](get-the-cell-object-by-displayname-of-pivotfield-of-pivottable_2.png)|
{{< app/cells/assistant language="nodejs-cpp" >}}
