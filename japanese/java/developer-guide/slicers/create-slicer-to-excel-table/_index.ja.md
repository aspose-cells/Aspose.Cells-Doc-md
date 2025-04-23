---
title: Excelテーブルにスライサーを作成する
type: docs
weight: 15
url: /ja/java/create-slicer-to-excel-table/
---

## **可能な使用シナリオ**

スライサはデータを素早くフィルタリングするために使用されます。テーブルまたはピボットテーブルの両方のデータをフィルタリングするために使用できます。Microsoft Excelでは、テーブルまたはピボットテーブルを選択し、*挿入＞スライサ*をクリックしてスライサを作成できます。Aspose.Cellsでは、[**Worksheet.Slicers.Add()**](https://reference.aspose.com/cells/java/com.aspose.cells/slicercollection#add-com.aspose.cells.ListObject-com.aspose.cells.ListColumn-int-int-)メソッドを使用してスライサを作成することができます。

## **Excelテーブルにスライサーを作成する**

次のサンプルコードをご覧ください。これは、テーブルを含む[サンプルExcelファイル](sampleCreateSlicerToExcelTable.xlsx)を読み込みます。それから最初の列に基づいてスライサーを作成します。最後に、ブックを[出力XLSX](outputCreateSlicerToExcelTable.xlsx)形式で保存します。

## **サンプルコード**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Slicers-CreateSlicerToExcelTable-1.java" >}}
{{< app/cells/assistant language="java" >}}
