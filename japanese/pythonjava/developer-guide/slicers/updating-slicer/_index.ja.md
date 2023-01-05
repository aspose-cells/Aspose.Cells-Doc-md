---
title: スライサーの更新
type: docs
weight: 60
url: /ja/python-java/updating-slicer/
---
## **スライサーの更新**
Aspose.Cells for Python via Java は、スライサーの更新をサポートしています。このために、API は、スライサー項目を選択または選択解除するために使用される Slicer.SlicerCache.SlicerCacheItems プロパティを提供します。次のコード スニペットは、[サンプル Excel ファイル](106365050.xlsx)スライサーが含まれています。スライサーの 2 番目と 3 番目の項目の選択を解除し、Slicer.refresh() メソッドを使用してスライサーを更新します。次に、ワークブックを[出力エクセルファイル](106365051.xlsx).次のスクリーンショットは、サンプル Excel ファイルに対するサンプル コードの効果を示しています。スクリーンショットでわかるように、選択した項目でスライサーを更新すると、それに応じてピボット テーブルも更新されます。

![todo:画像_代替_文章](Updating-Slicer-using-Aspose.Cells.png)
## **サンプルコード**
{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Slicers-UpdatingSlicer.py" >}}
