---
title: 親ピボットテーブルのネストされたピボットテーブルや子ピボットテーブルを見つけて更新する
type: docs
weight: 60
url: /ja/nodejs-cpp/find-and-refresh-the-nested-or-children-pivot-tables-of-parent-pivot-table/
description: 親ピボットテーブルのネストされたピボットテーブルや子ピボットテーブルを見つけて更新する方法 Aspose.Cells for Node.js via C++
keywords: Aspose.Cells for Node.js Excel、Excel Node.jsライブラリ、親ピボットテーブルのネストされたピボットテーブルや子ピボットテーブルの検出と更新 using Aspose.Cells for Node.js Excelライブラリ
---

## **可能な使用シナリオ**

親ピボットテーブルが別のピボットテーブルをデータソースとして使用する場合、それを子ピボットテーブルやネストされたピボットテーブルと呼びます。[**PivotTable.getChildren()**](https://reference.aspose.com/cells/nodejs-cpp/pivottable/#getChildren--)を使用して親ピボットテーブルの子ピボットテーブルを見つけることができます。

## **親ピボットテーブルのネストされたまたは子供のピボットテーブルを検出および更新する方法**

次のサンプルコードでは、3つのピボットテーブルを含む[サンプルExcelファイル](61767747.xlsx)をロードし、その下の2つのピボットテーブルが、このスクリーンショットに示すように、上記のピボットテーブルの子であることを示しています。コードは、[**PivotTable.getChildren()**](https://reference.aspose.com/cells/nodejs-cpp/pivottable/#getChildren--)を使用して子ピボットテーブルを見つけ、それぞれを更新します。

![todo:image_alt_text](find-and-refresh-the-nested-or-children-pivot-tables-of-parent-pivot-table_1.png)

## **サンプルコード**

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "PivotTables-FindAndRefreshNestedOrChildrenPivotTables.js" >}}
