---
title: 親ピボットテーブルのネストされたピボットテーブルや子ピボットテーブルを見つけて更新する
type: docs
weight: 50
url: /ja/java/find-and-refresh-the-nested-or-children-pivot-tables-of-parent-pivot-table/
---

## **可能な使用シナリオ**

親ピボットテーブルが別のピボットテーブルをデータソースとして使用する場合、それを子ピボットテーブルやネストされたピボットテーブルと呼びます。[**PivotTable.getChildren()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#getChildren--)を使用して親ピボットテーブルの子ピボットテーブルを見つけることができます。

## **親ピボットテーブルのネストされたピボットテーブルや子ピボットテーブルを見つけて更新する**

次のサンプルコードは、3つのピボットテーブルを含む[sample Excel file](61767766.xlsx)をロードします。下の2つのピボットテーブルは、スクリーンショットに示すように、上記のピボットテーブルの子供です。コードは[**PivotTable.getChildren()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#getChildren--)メソッドを使用して子のピボットテーブルを見つけ、それらを1つずつ更新します。

![todo:image_alt_text](find-and-refresh-the-nested-or-children-pivot-tables-of-parent-pivot-table_1.png)

## **サンプルコード**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "PivotTables-FindAndRefreshNestedOrChildrenPivotTables.java" >}}
