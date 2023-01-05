---
title: ピボット テーブルでピボット フィールドをグループ化する
type: docs
weight: 90
url: /ja/java/group-pivot-fields-in-the-pivot-table/
---
## **考えられる使用シナリオ**

Microsoft Excel では、ピボット テーブルのピボット フィールドをグループ化できます。ピボット フィールドに関連するデータが大量にある場合、それらをセクションにグループ化すると便利なことがよくあります。 Aspose.Cells も、[**PivotTable.setManualGroupField()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#setManualGroupField(com.aspose.cells.PivotField,%20com.aspose.cells.DateTime,%20com.aspose.cells.DateTime,%20java.util.ArrayList,%20int)） 方法。

## **ピボット テーブルでピボット フィールドをグループ化する**

次のサンプル コードは、[サンプル Excel ファイル](64716838.xlsx)を使用して最初のピボット フィールドでグループ化を実行します。[**PivotTable.setManualGroupField()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#setManualGroupField(com.aspose.cells.PivotField,%20com.aspose.cells.DateTime,%20com.aspose.cells.DateTime,%20java.util.ArrayList,%20int)） 方法。次に、ピボット テーブルのデータを更新して計算し、ワークブックを[出力エクセルファイル](64716837.xlsx).スクリーンショットは、サンプル Excel ファイルに対するサンプル コードの効果を示しています。スクリーンショットでわかるように、最初のピボット フィールドは月と四半期でグループ化されています。

![todo:画像_代替_文章](group-pivot-fields-in-the-pivot-table_1.png)

## **サンプルコード**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "PivotTables-GroupPivotFieldsInPivotTable.java" >}}
