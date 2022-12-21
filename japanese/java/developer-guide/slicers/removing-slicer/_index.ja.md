---
title: スライサーの削除
type: docs
weight: 30
url: /ja/java/removing-slicer/
---
## **考えられる使用シナリオ**
Microsoft Excel でスライサーを削除する場合は、それを選択して、*消去*ボタン。同様に、プログラムで Aspose.Cells API を使用して削除する場合は、[Worksheet.getSlicers().remove()](https://reference.aspose.com/cells/java/com.aspose.cells/slicercollection#remove\(com.aspose.cells.Slicer\)） 方法。ワークシートからスライサーが削除されます。
## **スライサーの削除**
次のサンプル コードは、[サンプル Excel ファイル](67338504.xlsx)既存のスライサーが含まれています。スライサーにアクセスしてから削除します。最後に、ワークブックを次のように保存します。[出力エクセルファイル](67338502.xlsx).次のスクリーンショットは、サンプル コードの実行後に削除されるスライサーを示しています。

![todo:画像_代替_文章](removing-slicer_1.png)
## **サンプルコード**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Slicers-RemovingSlicer.java" >}}
