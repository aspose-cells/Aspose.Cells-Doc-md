---
title: ピボットテーブルにスライサーを作成する
type: docs
weight: 10
url: /ja/java/create-slicer-to-a-pivot-table/
---

## **可能な使用シナリオ**
スライサーはデータを素早くフィルタリングするために使用されます。テーブルまたはピボットテーブルの両方でデータをフィルタリングすることが可能です。Microsoft Excelでは、テーブルまたはピボットテーブルを選択し、*挿入 > スライサー*をクリックすることでスライサーを作成できます。Aspose.Cellsもまた、[Worksheet.getSlicers().add()](https://reference.aspose.com/cells/java/com.aspose.cells/slicercollection#add-com.aspose.cells.PivotTable-int-int-com.aspose.cells.PivotField-) メソッドを使用してスライサーを作成できます。
## **ピボットテーブルにスライサーを作成する**
次のサンプルコードをご覧ください。ピボットテーブルが含まれる[sample Excel file](67338498.xlsx)をロードします。次に、最初の基本ピボットフィールドに基づいてスライサーを作成します。最後に、[output XLSX](67338497.xlsx)および[output XLSB](67338496.xlsb)形式のワークブックを保存します。スクリーンショットをご覧になりますが、Aspose.Cellsによって作成されたスライサーが出力されたExcelファイルに表示されます。

![todo:image_alt_text](create-slicer-to-a-pivot-table_1.png)
## **サンプルコード**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Slicers-CreateSlicerToPivotTable.java" >}}
{{< app/cells/assistant language="java" >}}
