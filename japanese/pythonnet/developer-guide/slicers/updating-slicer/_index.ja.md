---
title: スライサーの更新
type: docs
weight: 50
url: /ja/python-net/updating-slicer/
---
##  **考えられる使用シナリオ**

Microsoft Excel でスライサーを更新する場合は、その項目を選択または選択解除すると、それに応じてスライサー テーブルまたはピボット テーブルが更新されます。使ってください[**スライサー.スライサー_キャッシュ.スライサー_キャッシュ_アイテム**](https://reference.aspose.com/cells/python-net/aspose.cells.slicers/slicercache/slicer_cache_items/)Aspose.Cells for Python via .NET を使用してスライサー項目を選択または選択解除してから呼び出します[**スライサー.refresh()**](https://reference.aspose.com/cells/python-net/aspose.cells.slicers/slicer/refresh/#)スライサー テーブルまたはピボット テーブルを更新するメソッド。

##  **スライサーの更新**

次のサンプルコードは、[サンプル Excel ファイル](67338475.xlsx)既存のスライサーが含まれています。スライサーの 2 番目と 3 番目の項目の選択を解除し、スライサーを更新します。次に、ワークブックを次のように保存します。[Excelファイルを出力](67338476.xlsx)。次のスクリーンショットは、サンプル Excel ファイルに対するサンプル コードの効果を示しています。スクリーンショットでわかるように、選択した項目でスライサーを更新すると、それに応じてピボット テーブルも更新されます。

![todo:image_alt_text](updating-slicer_1.png)

##  **サンプルコード**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Slicers-UpdatingSlicer.py" >}}
