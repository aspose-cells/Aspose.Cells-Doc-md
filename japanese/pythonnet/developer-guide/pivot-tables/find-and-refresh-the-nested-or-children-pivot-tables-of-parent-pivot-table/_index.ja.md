---
title: 親ピボット テーブルのネストされたピボット テーブルまたは子ピボット テーブルを検索して更新する
type: docs
weight: 60
url: /ja/python-net/find-and-refresh-the-nested-or-children-pivot-tables-of-parent-pivot-table/
description: Aspose.Cells for Python via .NET の親ピボット テーブルのネストされたピボット テーブルまたは子ピボット テーブルを検索して更新する方法。
keywords: Find and Refresh the Nested or Children Pivot Tables of Parent Pivot Table.
---
##  **考えられる使用シナリオ**

場合によっては、あるピボット テーブルが別のピボット テーブルをデータ ソースとして使用するため、子ピボット テーブルまたはネストされたピボット テーブルと呼ばれます。親ピボット テーブルの子ピボット テーブルは、次のコマンドを使用して見つけることができます。[**PivotTable.get_children()**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/get_children/#)方法。

##  **親ピボット テーブルのネストされたピボット テーブルまたは子ピボット テーブルを検索して更新する**

次のサンプルコードは、[サンプル Excel ファイル](61767747.xlsx) 3 つのピボット テーブルが含まれています。このスクリーンショットに示すように、下の 2 つのピボット テーブルは上のピボット テーブルの子です。このコードは、次のコマンドを使用して子のピボット テーブルを検索します。[**PivotTable.get_children()**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/get_children/#)メソッドを使用して、それらを 1 つずつ更新します。

![todo:image_alt_text](find-and-refresh-the-nested-or-children-pivot-tables-of-parent-pivot-table_1.png)

##  **サンプルコード**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-FindAndRefreshNestedOrChildrenPivotTables.py" >}}
