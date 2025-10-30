---
title: スライサーの挿入
linktitle: スライサー
type: docs
weight: 170
url: /ja/python-net/create-slicer/
description: Aspose.Cellsを使用してExcelファイルのスライサーを管理します。
keywords: Python Excel用Aspose.Cells、Excel Pythonライブラリ、Python Create Slicer without Excel、Aspose.Cells for Pythonを使用したSlicerの追加、Aspose.Cells for Pythonを使用したSlicerの挿入
---

## **可能な使用シナリオ**

スライサーはデータを素早くフィルタリングするために使用されます。それは表またはピボットテーブルの両方でデータをフィルタリングするために使用できます。 Microsoft Excelでは、表またはピボットテーブルを選択して *挿入 > スライサー* をクリックしてスライサーを作成できます。Aspose.Cells for Python via .NETでは、[**Worksheet.slicers.add()**](https://reference.aspose.com/cells/python-net/aspose.cells.slicers/slicercollection/add/#aspose.cells.pivot.PivotTable-int-int-aspose.cells.pivot.PivotField)メソッドを使用してスライサーを作成することも可能です。

## **Aspose.Cells for Python Excelライブラリを使用してピボットテーブルにスライサーを作成する方法**

次のサンプルコードを参照してください。ピボットテーブルを含む[サンプルExcelファイル](67338470.xlsx)を読み込みます。その後、最初の基本ピボットフィールドに基づいてスライサーを作成します。最後に、[output XLSX](67338471.xlsx)および[output XLSB](67338472.xlsb)形式でブックを保存します。次のスクリーンショットは、Aspose.Cellsによって出力Excelファイルに作成されたスライサーを示しています。

![todo:image_alt_text](create-slicer-to-a-pivot-table_1.png)

### **サンプルコード**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Slicers-CreateSlicerToPivotTable.py" >}}

## **Aspose.Cells for Python Excelライブラリを使用してExcelテーブルにスライサーを作成する方法**

次のサンプルコードをご覧ください。これは、テーブルを含む[サンプルExcelファイル](sampleCreateSlicerToExcelTable.xlsx)を読み込みます。それから最初の列に基づいてスライサーを作成します。最後に、ブックを[出力XLSX](outputCreateSlicerToExcelTable.xlsx)形式で保存します。

### **サンプルコード**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Examples-CSharp-Slicers-CreateSlicerToExcelTable-1.py" >}}

## **高度なトピック**
- [スライサープロパティを変更する](/cells/ja/python-net/change-slicer-properties/)
- [ExcelをPDFにレンダリングする際にスライサーを描画する](/cells/ja/python-net/draw-slicer-while-rendering-excel-to-pdf/)
- [スライサーの書式設定](/cells/ja/python-net/formatting-slicer/)
- [スライサーの削除](/cells/ja/python-net/removing-slicer/)
- [スライサーをレンダリングする](/cells/ja/python-net/rendering-slicer/)
- [スライサーを更新する](/cells/ja/python-net/updating-slicer/)
{{< app/cells/assistant language="python-net" >}}
