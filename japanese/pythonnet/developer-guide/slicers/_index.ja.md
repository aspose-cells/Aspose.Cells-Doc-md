---
title: インサートスライサー
linktitle: スライサー
type: docs
weight: 170
url: /ja/python-net/create-slicer/
description: Excel ファイルのスライサーを Aspose.Cells で管理します。
---
##  **考えられる使用シナリオ**

スライサーは、データを迅速にフィルタリングするために使用されます。テーブルまたはピボット テーブルの両方でデータをフィルターするために使用できます。 Microsoft Excel では、テーブルまたはピボット テーブルを選択し、*挿入 > スライサー* をクリックしてスライサーを作成できます。 Aspose.Cells for Python via .NET を使用してスライサーを作成することもできます。[**Worksheet.slicers.add()**](https://reference.aspose.com/cells/python-net/aspose.cells.slicers/slicercollection/add/#aspose.cells.pivot.PivotTable-int-int-aspose.cells.pivot.PivotField)方法。

##  **ピボットテーブルにスライサーを作成する**

次のサンプルコードを参照してください。それはロードします[サンプル Excel ファイル](67338470.xlsx)ピボットテーブルが含まれています。次に、最初のベース ピボット フィールドに基づいてスライサーを作成します。最後に、ワークブックを次の場所に保存します。[出力XLSX](67338471.xlsx)そして[出力XLSB](67338472.xlsb)フォーマット。次のスクリーンショットは、出力 Excel ファイル内で Aspose.Cells によって作成されたスライサーを示しています。

![todo:image_alt_text](create-slicer-to-a-pivot-table_1.png)

###  **サンプルコード**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Slicers-CreateSlicerToPivotTable.py" >}}

##  **Excel テーブルへのスライサーの作成**

次のサンプルコードを参照してください。それはロードします[サンプル Excel ファイル](sampleCreateSlicerToExcelTable.xlsx)テーブルが含まれています。次に、最初の列に基づいてスライサーを作成します。最後に、ワークブックを次の場所に保存します。[出力XLSX](outputCreateSlicerToExcelTable.xlsx)フォーマット。

###  **サンプルコード**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Examples-CSharp-Slicers-CreateSlicerToExcelTable-1.py" >}}

##  **アドバンストトピック**
- [スライサーのプロパティの変更](/cells/ja/python-net/change-slicer-properties/)
- [Excel を PDF にレンダリングするときにスライサーを描画する](/cells/ja/python-net/draw-slicer-while-rendering-excel-to-pdf/)
- [書式設定スライサー](/cells/ja/python-net/formatting-slicer/)
- [スライサーの削除](/cells/ja/python-net/removing-slicer/)
- [レンダリングスライサー](/cells/ja/python-net/rendering-slicer/)
- [スライサーの更新](/cells/ja/python-net/updating-slicer/)
