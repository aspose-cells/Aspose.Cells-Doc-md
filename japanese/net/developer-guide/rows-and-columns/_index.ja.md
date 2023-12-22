---
title: 行と列の書式設定
linktitle: 行と列
type: docs
weight: 100
url: /ja/net/adjusting-row-height-and-column-width/
description: Aspose.Cells for .NET は、行の高さまたは列の幅の変更、および行または列の書式設定の適用をサポートできます。
keywords: Set row height and column width, Adjust row height and column width, change the row height or column width, format rows and columns, how to set row height and column width.
---
{{% alert color="primary" %}}

スプレッドシートを操作して行や列にデータを追加する場合、行の高さまたは列の幅の変更が必要になる場合があります。行または列に書式設定を適用すると、データを表示するために現在の高さまたは幅を変更する必要がある場合があります。通常、ユーザーは Microsoft Excel を使用して WYSIWYG 環境で行の高さと列の幅を調整します。ただし、Aspose.Cells を使用すると、開発者は実行時にこれらの操作を実行できます。

{{% /alert %}}

##  **行の操作**

###  **行の高さを調整する方法**

Aspose.Cells はクラスを提供します。[**ワークブック**](https://reference.aspose.com/cells/net/aspose.cells/workbook)、これは Microsoft Excel ファイルを表します。の[**ワークブック**](https://reference.aspose.com/cells/net/aspose.cells/workbook)クラスには[**ワークシートコレクション**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection)これにより、Excel ファイル内の各ワークシートにアクセスできるようになります。ワークシートは次のように表されます。[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラス。の[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラスが提供するのは[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)ワークシート内のすべてのセルを表すコレクション。

の[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)コレクションには、ワークシート内の行または列を管理するためのいくつかのメソッドが用意されています。これらのいくつかについては、以下で詳しく説明します。

###  **行の高さを設定する方法**

を呼び出すことで単一行の高さを設定できます。[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)コレクションの[**SetRowHeight**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/setrowheight)方法。の[**SetRowHeight**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/setrowheight)メソッドは次のようにパラメータを受け取ります。

- *行インデックス**、高さを変更する行のインデックス。
- *行の高さ**、行に適用する行の高さ。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-HeightAndWidth-SettingHeightOfRow-1.cs" >}}

###  **ワークシート内のすべての行の高さを設定する方法**

開発者がワークシート内のすべての行に同じ行の高さを設定する必要がある場合は、[**標準高さ**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/standardheight)の財産[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)コレクション。

**例：**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-HeightAndWidth-SettingHeightAllRows-1.cs" >}}

##  **列の操作**

###  **列の幅を設定する方法**

を呼び出して列の幅を設定します。[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)コレクションの[**SetColumnWidth**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/setcolumnwidth)方法。の[**SetColumnWidth**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/setcolumnwidth)メソッドは次のパラメータを受け取ります。

- *列インデックス**、幅を変更する列のインデックス。
- *列幅**、目的の列幅。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-HeightAndWidth-SettingWidthOfColumn-1.cs" >}}

###  **列幅をピクセル単位で設定する方法**

を呼び出して列の幅を設定します。[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)コレクションの[**SetColumnWidthPixel**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/setcolumnwidthpixel)方法。の[**SetColumnWidthPixel**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/setcolumnwidthpixel)メソッドは次のパラメータを受け取ります。

- *列インデックス**、幅を変更する列のインデックス。
- *列幅**、ピクセル単位で指定する必要な列幅。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-HeightAndWidth-SetColumnWidthInPixels-1.cs" >}}

###  **ワークシート内のすべての列の幅を設定する方法**

ワークシート内のすべての列に同じ列幅を設定するには、[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)コレクションの[**標準幅**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/standardwidth)財産。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-HeightAndWidth-SettingWidthOfAllColumns-1.cs" >}}

##  **アドバンストトピック**
- [行と列の自動調整](/cells/ja/net/autofit-rows-and-columns/)
- [Aspose.Cells を使用してテキストを列に変換する](/cells/ja/net/convert-text-to-columns-using-aspose-cells/)
- [行と列のコピー](/cells/ja/net/copying-rows-and-columns/)
- [ワークシート内の空白の行と列を削除する](/cells/ja/net/delete-blank-rows-and-columns-in-a-worksheet/)
- [行と列のグループ化とグループ解除](/cells/ja/net/grouping-and-ungrouping-rows-and-columns/)
- [行と列の表示と非表示を切り替える](/cells/ja/net/hiding-and-showing-rows-and-columns/)
- [Excel ワークシートでの行の挿入または削除](/cells/ja/net/insert-or-delete-rows-in-an-excel-worksheet/)
- [Excelファイルの行と列の挿入と削除](/cells/ja/net/inserting-and-deleting-rows-and-columns/)
- [ワークシート内の重複行を削除する](/cells/ja/net/remove-duplicate-rows-in-a-worksheet/)
- [ワークシート内の空白の列と行を削除しながら、他のワークシートの参照を更新する](/cells/ja/net/update-references-in-other-worksheets-while-deleting-blank-columns-and-rows-in-a-worksheet/)
