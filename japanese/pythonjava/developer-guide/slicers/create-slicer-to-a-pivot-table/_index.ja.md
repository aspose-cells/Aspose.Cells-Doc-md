---
title: ピボットテーブルにスライサーを作成する
type: docs
weight: 10
url: /ja/python-java/create-slicer-to-a-pivot-table/
---

## **可能な使用シナリオ**
スライサーはデータのフィルタリングを迅速に行うために使用されます。テーブルまたはピボットテーブルのデータをフィルタリングするために使用できます。Microsoft Excelでは、テーブルまたはピボットテーブルを選択し、*挿入 > スライサー*をクリックすることでスライサーを作成できます。Aspose.Cells for Python via Java では、スライサーを作成するためのWorksheet.getSlicers().add() メソッドが提供されています。
## **ピボットテーブルにスライサーを作成する**
次のコードスニペットは、ピボットテーブルを含む[sample Excel file](106364966.xlsx)をロードします。それから最初の基本ピボットフィールドに基づいてスライサーを作成します。最後に、[output XLSX](106364967.xlsx) サイズでワークブックを保存します。次のスクリーンショットは、Aspose.Cellsによって出力されたExcelファイル内のスライサーを示しています。

![todo:image_alt_text](create-slicer-to-a-pivot-table_1.png)
## **サンプルコード**
{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Slicers-CreateSlicerToPivotTable.py" >}}
