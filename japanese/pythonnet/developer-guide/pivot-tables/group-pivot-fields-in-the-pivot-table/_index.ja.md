---
title: ピボットテーブル内のPivot Fieldをグループ化
type: docs
weight: 80
url: /ja/python-net/group-pivot-fields-in-the-pivot-table/
description: Aspose.Cells for Python via .NETを使用したPivot TableでPivot Fieldsをグループ化する方法。
keywords: Python用のExcel、Excel PythonライブラリのAspose.Cellsを使用してPivot TableでPivot Fieldsをグループ化する。
---

## **可能な使用シナリオ**

Microsoft Excelでは、ピボットテーブルのPivot Fieldをグループ化することができます。ピボットフィールドに関連するデータが大量の場合、それらをセクションにグループ化することはしばしば有用です。Aspose.Cells for Python via .NETも、[**PivotTable.set_manual_group_field()**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/set_manual_group_field/#int-float-float-list-float)メソッドを使用してこの機能を提供します。

## **Pivot TableでPivot Fieldsをグループ化する方法**

以下のサンプルコードは、[サンプルExcelファイル](64716818.xlsx)をロードし、[**PivotTable.set_manual_group_field()**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/set_manual_group_field/#int-float-float-list-float)メソッドを使用して最初のピボットフィールドにグループ化を行います。それからピボットテーブルのデータをリフレッシュして計算し、ブックを[出力Excelファイル](64716817.xlsx)として保存します。スクリーンショットは、サンプルコードのサンプルExcelファイルに対する効果を示しています。スクリーンショットに示されているように、最初のピボットフィールドは現在月ごとと四半期ごとにグループ化されています。

![todo:image_alt_text](group-pivot-fields-in-the-pivot-table_1.png)

## **サンプルコード**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "PivotTables-GroupPivotFieldsInPivotTable.py" >}}
