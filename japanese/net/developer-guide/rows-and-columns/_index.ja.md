---
title: 行と列のフォーマット
linktitle: 行と列
type: docs
weight: 100
url: /ja/net/adjusting-row-height-and-column-width/
description: Aspose.Cells for .NETは、行の高さや列の幅を変更したり、行や列に書式を適用したりすることができます。
keywords: 行の高さと列の幅を設定し、行の高さと列の幅を調整し、行の高さや列の幅を変更し、行と列の書式を設定する方法
---


{{% alert color="primary" %}}

スプレッドシートで作業し、行や列にデータを追加する際に、行の高さや列の幅を変更する必要が生じることがあります。時には、行や列に書式を適用することで、現在の高さや幅を変更してデータを表示する必要があります。通常、ユーザーはMicrosoft Excelを使用してWYSIWYG環境で行の高さや列の幅を調整しますが、Aspose.Cellsでは開発者が実行時にこれらの操作を行うことができます。

{{% /alert %}}

## **行で操作する**

### **行の高さの調整方法**

Aspose.CellsはMicrosoft Excelファイルを表す[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)クラスを提供します。[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)クラスにはExcelファイル内の各ワークシートにアクセスできる[**WorksheetCollection**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection)が含まれています。ワークシートは[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラスで表されます。[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラスはワークシート内のすべてのセルを表す[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)コレクションを提供します。

[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)コレクションには、ワークシート内の行や列を管理するためのいくつかのメソッドが用意されています。以下では、そのうちいくつかを詳しく説明します。

### **行の高さを設定する方法**

行の高さを単一の行に設定することができます。[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)コレクションの[**SetRowHeight**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/setrowheight)メソッドを呼び出すことで行の高さを設定できます。[**SetRowHeight**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/setrowheight)メソッドは以下のパラメータを取ります。

- **行インデックス**：高さを変更する行のインデックス。
- **行の高さ**：行に適用する行の高さ。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-HeightAndWidth-SettingHeightOfRow-1.cs" >}}

### **ワークシート内のすべての行の高さを設定する方法**

開発者がワークシート内のすべての行に同じ行の高さを設定する必要がある場合、[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)コレクションの[**StandardHeight**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/standardheight)プロパティを使用して行の高さを設定できます。

**例:**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-HeightAndWidth-SettingHeightAllRows-1.cs" >}}

## **列で操作する**

### **列の幅を設定する方法**

列の幅を変更する列のインデックスを指定して、[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)コレクションの[**SetColumnWidth**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/setcolumnwidth)メソッドを呼び出すことで列の幅を設定する。[**SetColumnWidth**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/setcolumnwidth)メソッドは次のパラメータを取ります:

- **列インデックス**：幅を変更する列のインデックス。
- **列の幅**：設定したい列の幅。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-HeightAndWidth-SettingWidthOfColumn-1.cs" >}}

### **ピクセル単位で列幅を設定する方法**

列の幅を変更する列のインデックスを指定して、[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)コレクションの[**SetColumnWidthPixel**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/setcolumnwidthpixel)メソッドを呼び出すことで列の幅を設定する。[**SetColumnWidthPixel**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/setcolumnwidthpixel)メソッドは次のパラメータを取ります:

- **列インデックス**：幅を変更する列のインデックス。
- **列の幅**、ピクセル単位での所望の列の幅。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-HeightAndWidth-SetColumnWidthInPixels-1.cs" >}}

### **ワークシート内のすべての列の幅を設定する方法**

ワークシート内のすべての列に同じ列の幅を設定するには、[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)コレクションの[**StandardWidth**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/standardwidth)プロパティを使用します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-HeightAndWidth-SettingWidthOfAllColumns-1.cs" >}}

## **高度なトピック**
- [行と列の自動調整](/cells/ja/net/autofit-rows-and-columns/)
- [Aspose.Cellsを使用したテキストを列に変換する](/cells/ja/net/convert-text-to-columns-using-aspose-cells/)
- [行と列のコピー](/cells/ja/net/copying-rows-and-columns/)
- [ワークシート内の空白の行と列を削除](/cells/ja/net/delete-blank-rows-and-columns-in-a-worksheet/)
- [行と列のグループ化および解除](/cells/ja/net/grouping-and-ungrouping-rows-and-columns/)
- [行と列の非表示および表示](/cells/ja/net/hiding-and-showing-rows-and-columns/)
- [Excelワークシートに行を挿入または削除](/cells/ja/net/insert-or-delete-rows-in-an-excel-worksheet/)
- [Excelファイルの行と列の挿入と削除](/cells/ja/net/inserting-and-deleting-rows-and-columns/)
- [ワークシート内の重複する行を削除する](/cells/ja/net/remove-duplicate-rows-in-a-worksheet/)
- [ワークシート内の空白の列と行を削除する際に、他のワークシートの参照を更新する](/cells/ja/net/update-references-in-other-worksheets-while-deleting-blank-columns-and-rows-in-a-worksheet/)
{{< app/cells/assistant language="csharp" >}}
