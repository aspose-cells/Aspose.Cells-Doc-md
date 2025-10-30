---
title: 行と列のフォーマット
linktitle: 行と列
type: docs
weight: 100
url: /ja/python-net/adjusting-row-height-and-column-width/
description: Aspose.Cells for Python via .NETでは、行の高さや列の幅の変更、また行や列の書式設定をサポートしています。
keywords: Python Excelライブラリ、Python 行の高さと列の幅の設定、Python 行の高さと列の幅の調整、Python 行の高さや列の幅の変更、Python 行と列の書式設定、Python 行の高さや列の幅の設定方法。
---


{{% alert color="primary" %}}

スプレッドシートでデータを行や列に追加する際には、行の高さや列の幅を変更する必要があるかもしれません。時には、行や列に書式を適用することで現在の高さや幅を変更してデータを表示する必要があります。通常、ユーザーはMicrosoft Excelを使用してWYSIWYG環境で行の高さや列の幅を調整します。しかし、Aspose.Cells for Python via .NETを使用すると、開発者はこれらの操作をランタイムで実行できます。

{{% /alert %}}

## **行で操作する**

### **行の高さの調整方法**

Aspose.Cells for Python via .NETでは、Microsoft Excelファイルを表す[**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)クラスを提供します。[**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)クラスには、Excelファイル内の各ワークシートにアクセスできる[**WorksheetCollection**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheetcollection)が含まれています。ワークシートは[**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet)クラスで表されます。[**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet)クラスには、ワークシート内のすべてのセルを表す[**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells)コレクションが提供されます。

[**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells)コレクションには、ワークシート内の行や列を管理するためのいくつかのメソッドが用意されています。以下では、そのうちいくつかを詳しく説明します。

### **行の高さを設定する方法**

行の高さを単一の行に設定することができます。[**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells)コレクションの[**set_row_height**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/set_row_height/#int-float)メソッドを呼び出すことで行の高さを設定できます。[**set_row_height**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/set_row_height/#int-float)メソッドは以下のパラメータを取ります。

- **row**、行のインデックス、その行の高さを変更します。
- **height**、行に適用する行の高さ。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-HeightAndWidth-SettingHeightOfRow-1.py" >}}

### **ワークシート内のすべての行の高さを設定する方法**

開発者がワークシート内のすべての行に同じ行の高さを設定する必要がある場合、[**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells)コレクションの[**standard_height**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/standard_height)プロパティを使用して行の高さを設定できます。

**例:**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-HeightAndWidth-SettingHeightAllRows-1.py" >}}

## **列で操作する**

### **列の幅を設定する方法**

列の幅を変更する列のインデックスを指定して、[**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells)コレクションの[**set_column_width**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/set_column_width/#int-float)メソッドを呼び出すことで列の幅を設定する。[**set_column_width**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/set_column_width/#int-float)メソッドは次のパラメータを取ります:

- **column**: 幅を変更する列のインデックス。
- **width**: 望ましい列の幅。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-HeightAndWidth-SettingWidthOfColumn-1.py" >}}

### **ピクセル単位で列幅を設定する方法**

列の幅を変更する列のインデックスを指定して、[**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells)コレクションの[**set_column_width_pixel**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/set_column_width_pixel/#int-int)メソッドを呼び出すことで列の幅を設定する。[**set_column_width_pixel**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/set_column_width_pixel/#int-int)メソッドは次のパラメータを取ります:

- **column**: 幅を変更する列のインデックス。
- **pixels**: ピクセル単位での望ましい列の幅。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-HeightAndWidth-SetColumnWidthInPixels-1.py" >}}

### **ワークシート内のすべての列の幅を設定する方法**

ワークシート内のすべての列に同じ列の幅を設定するには、[**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells)コレクションの[**standard_width**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/standard_width)プロパティを使用します。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-HeightAndWidth-SettingWidthOfAllColumns-1.py" >}}

## **高度なトピック**
- [行と列の自動調整](/cells/ja/python-net/autofit-rows-and-columns/)
- [Aspose.Cellsを使用したテキストを列に変換する](/cells/ja/python-net/convert-text-to-columns-using-aspose-cells/)
- [行と列のコピー](/cells/ja/python-net/copying-rows-and-columns/)
- [ワークシート内の空白の行と列を削除](/cells/ja/python-net/delete-blank-rows-and-columns-in-a-worksheet/)
- [行と列のグループ化および解除](/cells/ja/python-net/grouping-and-ungrouping-rows-and-columns/)
- [行と列の非表示および表示](/cells/ja/python-net/hiding-and-showing-rows-and-columns/)
- [Excelワークシートに行を挿入または削除](/cells/ja/python-net/insert-or-delete-rows-in-an-excel-worksheet/)
- [Excelファイルの行と列の挿入と削除](/cells/ja/python-net/inserting-and-deleting-rows-and-columns/)
- [ワークシート内の重複する行を削除する](/cells/ja/python-net/remove-duplicate-rows-in-a-worksheet/)
- [ワークシート内の空白の列と行を削除する際に、他のワークシートの参照を更新する](/cells/ja/python-net/update-references-in-other-worksheets-while-deleting-blank-columns-and-rows-in-a-worksheet/)
{{< app/cells/assistant language="python-net" >}}
