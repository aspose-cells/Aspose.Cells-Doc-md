---
title: 親ピボットテーブルのネストされたピボットテーブルや子ピボットテーブルを見つけて更新する
type: docs
weight: 60
url: /ja/net/find-and-refresh-the-nested-or-children-pivot-tables-of-parent-pivot-table/
---

## **可能な使用シナリオ**

親ピボットテーブルが別のピボットテーブルをデータソースとして使用する場合、それを子ピボットテーブルやネストされたピボットテーブルと呼びます。[**PivotTable.GetChildren()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/methods/getchildren)を使用して親ピボットテーブルの子ピボットテーブルを見つけることができます。

## **親ピボットテーブルのネストされたピボットテーブルや子ピボットテーブルを見つけて更新する**

次のサンプルコードでは、3つのピボットテーブルを含む[サンプルExcelファイル](61767747.xlsx)をロードし、その下の2つのピボットテーブルが、このスクリーンショットに示すように、上記のピボットテーブルの子であることを示しています。コードは、[**PivotTable.GetChildren()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/methods/getchildren)を使用して子ピボットテーブルを見つけ、それぞれを更新します。

![todo:image_alt_text](find-and-refresh-the-nested-or-children-pivot-tables-of-parent-pivot-table_1.png)

## **サンプルコード**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "PivotTables-FindAndRefreshNestedOrChildrenPivotTables.cs" >}}
