---
title: スライサーの更新
type: docs
weight: 60
url: /ja/python-java/updating-slicer/
---

## **スライサーを更新する**
Aspose.Cells for Python via Java は、スライサーを更新することをサポートしています。このために、APIはSlicer.SlicerCache.SlicerCacheItems プロパティを提供しており、これを使用してスライサーアイテムの選択または選択解除ができます。次のコードスニペットは、スライサーを含む[sample Excel file](106365050.xlsx)をロードし、スライサーの2番目と3番目のアイテムの選択を解除し、Slicer.refresh() メソッドを使用してスライサーを更新し、それを[output Excel file](106365051.xlsx)として保存します。次のスクリーンショットは、サンプルExcelファイルに対するサンプルコードの効果を示しています。スクリーンショットに示されているように、選択されたアイテムを持つスライサーを更新すると、ピボットテーブルもそれに応じて更新されます。

![todo:image_alt_text](Updating-Slicer-using-Aspose.Cells.png)
## **サンプルコード**
{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Slicers-UpdatingSlicer.py" >}}
