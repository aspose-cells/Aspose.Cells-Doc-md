---
title: ピボットテーブル内のPivot Fieldをグループ化
type: docs
weight: 90
url: /ja/java/group-pivot-fields-in-the-pivot-table/
---

## **可能な使用シナリオ**

Microsoft Excelでは、ピボットテーブルのピボットフィールドをグループ化することができます。ピボットフィールドに関連するデータが多い場合、それらをセクションにグループ化することはよく行われます。Aspose.Cellsも[**PivotTable.setManualGroupField()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#setManualGroupField-com.aspose.cells.PivotField-com.aspose.cells.DateTime-com.aspose.cells.DateTime-java.util.ArrayList-int-)メソッドを使用してこの機能を提供しています。

## **ピボットテーブル内のPivot Fieldをグループ化**

以下のサンプルコードは、[サンプルExcelファイル](64716838.xlsx)を読み込み、ピボットテーブルの最初のピボットフィールドを[**PivotTable.setManualGroupField()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#setManualGroupField-com.aspose.cells.PivotField-com.aspose.cells.DateTime-com.aspose.cells.DateTime-java.util.ArrayList-int-)メソッドを使用してグループ化します。その後、ピボットテーブルのデータを更新して計算し、ワークブックを[出力Excelファイル](64716837.xlsx)として保存します。スクリーンショットでは、サンプルコードのサンプルExcelファイルへの影響が示されています。スクリーンショットで示されているように、最初のピボットフィールドは現在、月と四半期によるグループ化が行われています。

![todo:image_alt_text](group-pivot-fields-in-the-pivot-table_1.png)

## **サンプルコード**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "PivotTables-GroupPivotFieldsInPivotTable.java" >}}
{{< app/cells/assistant language="java" >}}
