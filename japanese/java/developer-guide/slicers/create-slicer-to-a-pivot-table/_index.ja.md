---
title: ピボット テーブルにスライサーを作成する
type: docs
weight: 10
url: /ja/java/create-slicer-to-a-pivot-table/
---
## **考えられる使用シナリオ**
スライサーは、データをすばやくフィルター処理するために使用されます。テーブルまたはピボット テーブルの両方でデータをフィルター処理するために使用できます。 Microsoft Excel では、テーブルまたはピボット テーブルを選択してから、*挿入 > スライサー*Aspose.Cells を使用してスライサーを作成することもできます[Worksheet.getSlicers().add()](https://reference.aspose.com/cells/java/com.aspose.cells/slicercollection#add\(com.aspose.cells.PivotTable,%20int,%20int,%20com.aspose.cells.PivotField\)） 方法。
## **ピボット テーブルにスライサーを作成する**
以下のサンプルコードをご覧ください。それは[サンプル Excel ファイル](67338498.xlsx)ピボットテーブルが含まれています。次に、最初のベース ピボット フィールドに基づいてスライサーを作成します。最後に、ワークブックを[出力 XLSX](67338497.xlsx)と[出力 XLSB](67338496.xlsb)フォーマット。次のスクリーンショットは、出力 Excel ファイルで Aspose.Cells によって作成されたスライサーを示しています。

![todo:画像_代替_文章](create-slicer-to-a-pivot-table_1.png)
## **サンプルコード**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Slicers-CreateSlicerToPivotTable.java" >}}
