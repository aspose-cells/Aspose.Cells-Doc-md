---
title: スライサーの挿入
linktitle: スライサー
type: docs
weight: 170
url: /ja/net/create-slicer/
description: Aspose.Cellsを使用してExcelファイルのスライサーを管理します。
---

## **可能な使用シナリオ**

スライサはデータを素早くフィルタリングするために使用されます。テーブルまたはピボットテーブルの両方のデータをフィルタリングするために使用できます。Microsoft Excelでは、テーブルまたはピボットテーブルを選択し、*挿入＞スライサ*をクリックしてスライサを作成できます。Aspose.Cellsでは、[**Worksheet.Slicers.Add()**](https://reference.aspose.com/cells/net/aspose.cells.slicers/slicercollection/methods/add/index)メソッドを使用してスライサを作成することができます。

## **ピボットテーブルにスライサーを作成する**

次のサンプルコードを参照してください。ピボットテーブルを含む[サンプルExcelファイル](67338470.xlsx)を読み込みます。その後、最初の基本ピボットフィールドに基づいてスライサーを作成します。最後に、[output XLSX](67338471.xlsx)および[output XLSB](67338472.xlsb)形式でブックを保存します。次のスクリーンショットは、Aspose.Cellsによって出力Excelファイルに作成されたスライサーを示しています。

![todo:image_alt_text](create-slicer-to-a-pivot-table_1.png)

### **サンプルコード**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Slicers-CreateSlicerToPivotTable.cs" >}}

## **Excelテーブルにスライサーを作成する**

次のサンプルコードをご覧ください。これは、テーブルを含む[サンプルExcelファイル](sampleCreateSlicerToExcelTable.xlsx)を読み込みます。それから最初の列に基づいてスライサーを作成します。最後に、ブックを[出力XLSX](outputCreateSlicerToExcelTable.xlsx)形式で保存します。

### **サンプルコード**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Slicers-CreateSlicerToExcelTable-1.cs" >}}

## **高度なトピック**
- [スライサープロパティを変更する](/cells/ja/net/change-slicer-properties/)
- [ExcelをPDFにレンダリングする際にスライサーを描画する](/cells/ja/net/draw-slicer-while-rendering-excel-to-pdf/)
- [スライサーの書式設定](/cells/ja/net/formatting-slicer/)
- [スライサーの削除](/cells/ja/net/removing-slicer/)
- [スライサーをレンダリングする](/cells/ja/net/rendering-slicer/)
- [スライサーを更新する](/cells/ja/net/updating-slicer/)
