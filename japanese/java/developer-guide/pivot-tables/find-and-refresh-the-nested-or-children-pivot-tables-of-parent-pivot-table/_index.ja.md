---
title: 親ピボット テーブルのネストされたピボット テーブルまたは子ピボット テーブルを検索して更新する
type: docs
weight: 50
url: /ja/java/find-and-refresh-the-nested-or-children-pivot-tables-of-parent-pivot-table/
---
## **考えられる使用シナリオ**

あるピボット テーブルが別のピボット テーブルをデータ ソースとして使用する場合があるため、子ピボット テーブルまたはネストされたピボット テーブルと呼ばれます。親ピボット テーブルの子ピボット テーブルは、[**ピボットテーブル.getChildren()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#getChildren()） 方法。

## **親ピボット テーブルのネストされたピボット テーブルまたは子ピボット テーブルを検索して更新する**

次のサンプル コードは、[サンプル Excel ファイル](61767766.xlsx)3 つのピボット テーブルが含まれています。下の 2 つのピボット テーブルは、このスクリーンショットに示すように、上のピボット テーブルの子です。コードは、[**ピボットテーブル.getChildren()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#getChildren()) メソッドを実行し、それらを 1 つずつ更新します。

![todo:画像_代替_文章](find-and-refresh-the-nested-or-children-pivot-tables-of-parent-pivot-table_1.png)

## **サンプルコード**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "PivotTables-FindAndRefreshNestedOrChildrenPivotTables.java" >}}
