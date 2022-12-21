---
title: 親ピボット テーブルのネストされたピボット テーブルまたは子ピボット テーブルを検索して更新する
type: docs
weight: 60
url: /ja/net/find-and-refresh-the-nested-or-children-pivot-tables-of-parent-pivot-table/
---
## **考えられる使用シナリオ**

あるピボット テーブルが別のピボット テーブルをデータ ソースとして使用する場合があるため、子ピボット テーブルまたはネストされたピボット テーブルと呼ばれます。親ピボット テーブルの子ピボット テーブルは、[**ピボットテーブル.GetChildren()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/methods/getchildren)方法。

## **親ピボット テーブルのネストされたピボット テーブルまたは子ピボット テーブルを検索して更新する**

次のサンプル コードは、[サンプル Excel ファイル](61767747.xlsx) 3 つのピボット テーブルが含まれています。下の 2 つのピボット テーブルは、このスクリーンショットに示すように、上のピボット テーブルの子です。コードは、[**ピボットテーブル.GetChildren()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/methods/getchildren)メソッドを呼び出してから、それらを 1 つずつ更新します。

![todo:画像_代替_文章](find-and-refresh-the-nested-or-children-pivot-tables-of-parent-pivot-table_1.png)

## **サンプルコード**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "PivotTables-FindAndRefreshNestedOrChildrenPivotTables.cs" >}}
