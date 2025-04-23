---
title: スライサーの更新
type: docs
weight: 50
url: /ja/java/updating-slicer/
---

## **可能な使用シナリオ**
Microsoft Excelでスライサーを更新したい場合は、その項目を選択または選択解除すると、それに応じてスライサーテーブルまたはピボットテーブルが更新されます。Aspose.Cellsを使用してスライサーアイテムを選択または選択解除するには、[Slicer.SlicerCache.SlicerCacheItems](https://reference.aspose.com/cells/java/com.aspose.cells/slicercache#SlicerCacheItems) を使用し、その後 [Slicer.refresh()](https://reference.aspose.com/cells/java/com.aspose.cells/slicer#refresh--) メソッドを呼び出してスライサーテーブルまたはピボットテーブルを更新します。 
## **スライサーを更新する**
次のサンプルコードは、既存のスライサーが含まれる[sample Excel file](67338506.xlsx)をロードし、スライサーの2番目と3番目のアイテムを選択解除し、スライサーをリフレッシュします。最後に、ワークブックを[output Excel file](67338505.xlsx)として保存します。スクリーンショットは、サンプルコードのサンプルExcelファイルに対する影響を示しています。

![todo:image_alt_text](updating-slicer_1.png)
## **サンプルコード**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Slicers-UpdatingSlicer.java" >}}
{{< app/cells/assistant language="java" >}}
