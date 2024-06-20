---
title: ピボットテーブル内のPivot Fieldをグループ化
type: docs
weight: 80
url: /ja/net/group-pivot-fields-in-the-pivot-table/
---

## **可能な使用シナリオ**

Microsoft Excelには、ピボットテーブルのピボットフィールドをグループ化する機能があります。ピボットフィールドに関連するデータが多い場合、それをセクションにグループ化することはしばしば役立ちます。Aspose.Cellsも[**PivotTable.SetManualGroupField()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/methods/setmanualgroupfield/index)メソッドを使用して、この機能を提供します。

## **ピボットテーブル内のPivot Fieldをグループ化**

以下のサンプルコードは、[サンプルExcelファイル](64716818.xlsx)をロードし、[**PivotTable.SetManualGroupField()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/methods/setmanualgroupfield/index)メソッドを使用して最初のピボットフィールドにグループ化を行います。それからピボットテーブルのデータをリフレッシュして計算し、ブックを[出力Excelファイル](64716817.xlsx)として保存します。スクリーンショットは、サンプルコードのサンプルExcelファイルに対する効果を示しています。スクリーンショットに示されているように、最初のピボットフィールドは現在月ごとと四半期ごとにグループ化されています。

![todo:image_alt_text](group-pivot-fields-in-the-pivot-table_1.png)

## **サンプルコード**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "PivotTables-GroupPivotFieldsInPivotTable.cs" >}}
