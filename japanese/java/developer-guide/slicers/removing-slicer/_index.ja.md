---
title: スライサーの削除
type: docs
weight: 30
url: /ja/java/removing-slicer/
---

## **可能な使用シナリオ**
Microsoft Excelでスライサーを削除するには、それを選択し、*削除*ボタンを押してください。同様に、Aspose.Cells APIを使用してそれを削除する場合は、[Worksheet.getSlicers().remove()](https://reference.aspose.com/cells/java/com.aspose.cells/slicercollection#remove(com.aspose.cells.Slicer))メソッドを使用してください。 
## **スライサーの削除**
次のサンプルコードは、既存のスライサーが含まれる[sample Excel file](67338504.xlsx)をロードし、スライサーにアクセスしてからそれを削除します。最後に、ワークブックを[output Excel file](67338502.xlsx)として保存します。スクリーンショットは、サンプルコードの実行後に削除されるスライサーを示しています。

![todo:image_alt_text](removing-slicer_1.png)
## **サンプルコード**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Slicers-RemovingSlicer.java" >}}
