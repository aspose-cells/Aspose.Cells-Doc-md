---
title: スライサーの削除
type: docs
weight: 40
url: /ja/python-java/removing-slicer/
---

## **スライサーの削除**
Microsoft Excelでスライサーを削除するには、単純にスライサーを選択し、* Delete *ボタンを押します。Aspose.Cells for Python via Java を使用してこれを達成するには、Worksheet.getSlicers().remove() メソッドを使用します。これにより、ワークシートからスライサーが削除されます。 

次のコードスニペットは、既存のスライサーを含む[sample Excel file](106364970.xlsx)をロードし、スライサーにアクセスして削除し、[output Excel file](106364971.xlsx)として保存します。次のスクリーンショットは、削除されるスライサーを示しています。

![todo:image_alt_text](Removing-Slicer-using-Aspose.Cells.png)
## **サンプルコード**
{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Slicers-RemovingSlicer.py" >}}
