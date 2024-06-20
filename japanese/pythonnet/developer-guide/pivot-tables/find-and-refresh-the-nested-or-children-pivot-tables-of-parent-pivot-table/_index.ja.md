---
title: 親ピボットテーブルのネストされたピボットテーブルや子ピボットテーブルを見つけて更新する
type: docs
weight: 60
url: /ja/python-net/find-and-refresh-the-nested-or-children-pivot-tables-of-parent-pivot-table/
description: Aspose.Cells for Python via .NETで親Pivot Tableのネストされたまたは子Pivot Tableを検索および更新する方法
keywords: Aspose.Cells for Python Excel、Excel Pythonライブラリを使用して親ピボットテーブルの子ネストされたまたは子供のピボットテーブルを見つけて更新する方法
---

## **可能な使用シナリオ**

親ピボットテーブルが別のピボットテーブルをデータソースとして使用する場合、それを子ピボットテーブルやネストされたピボットテーブルと呼びます。[**PivotTable.get_children()**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/get_children/#)を使用して親ピボットテーブルの子ピボットテーブルを見つけることができます。

## **親ピボットテーブルのネストされたまたは子供のピボットテーブルを検出および更新する方法**

次のサンプルコードでは、3つのピボットテーブルを含む[サンプルExcelファイル](61767747.xlsx)をロードし、その下の2つのピボットテーブルが、このスクリーンショットに示すように、上記のピボットテーブルの子であることを示しています。コードは、[**PivotTable.get_children()**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/get_children/#)を使用して子ピボットテーブルを見つけ、それぞれを更新します。

![todo:image_alt_text](find-and-refresh-the-nested-or-children-pivot-tables-of-parent-pivot-table_1.png)

## **サンプルコード**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-FindAndRefreshNestedOrChildrenPivotTables.py" >}}
