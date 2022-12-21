---
title: ピボット テーブルにスライサーを作成する
type: docs
weight: 10
url: /ja/python-java/create-slicer-to-a-pivot-table/
---
## **考えられる使用シナリオ**
スライサーは、データをすばやくフィルター処理するために使用されます。これらは、テーブルまたはピボット テーブルの両方でデータをフィルター処理するために使用できます。 Microsoft Excel では、テーブルまたはピボット テーブルを選択してから、*挿入 > スライサー*. Aspose.Cells for Python via Java は、スライサーを作成するための Worksheet.getSlicers().add() メソッドを提供します。
## **ピボット テーブルにスライサーを作成する**
次のコード スニペットは、[サンプル Excel ファイル](106364966.xlsx)ピボットテーブルが含まれています。次に、最初のベース ピボット フィールドに基づいてスライサーを作成します。最後に、ワークブックを[出力XLSX](106364967.xlsx)フォーマット。次のスクリーンショットは、出力 Excel ファイルで Aspose.Cells によって作成されたスライサーを示しています。

![todo:画像_代替_文章](create-slicer-to-a-pivot-table_1.png)
## **サンプルコード**
{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Slicers-CreateSlicerToPivotTable.py" >}}
