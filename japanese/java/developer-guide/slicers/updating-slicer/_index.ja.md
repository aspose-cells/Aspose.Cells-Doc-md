---
title: スライサーの更新
type: docs
weight: 50
url: /ja/java/updating-slicer/
---
## **考えられる使用シナリオ**
Microsoft Excel でスライサーを更新する場合は、その項目を選択または選択解除すると、それに応じてスライサー テーブルまたはピボット テーブルが更新されます。使ってください[Slicer.SlicerCache.SlicerCacheItems](https://reference.aspose.com/cells/java/com.aspose.cells/slicercache#SlicerCacheItems)Aspose.Cells でスライサー項目を選択または選択解除してから呼び出す[スライサー.refresh()](https://reference.aspose.com/cells/java/com.aspose.cells/slicer#refresh\(\)) メソッドを使用して、スライサー テーブルまたはピボット テーブルを更新します。
## **スライサーの更新**
次のサンプル コードは、[サンプル Excel ファイル](67338506.xlsx)既存のスライサーが含まれています。スライサーの 2 番目と 3 番目の項目の選択を解除し、スライサーを更新します。次に、ワークブックを[出力エクセルファイル](67338505.xlsx).次のスクリーンショットは、サンプル Excel ファイルに対するサンプル コードの効果を示しています。スクリーンショットでわかるように、選択した項目でスライサーを更新すると、それに応じてピボット テーブルも更新されます。

![todo:画像_代替_文章](updating-slicer_1.png)
## **サンプルコード**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Slicers-UpdatingSlicer.java" >}}
