---
title: 行の高さと列の幅を調整する
type: docs
weight: 10
url: /ja/cpp/adjusting-row-height-and-column-width/
---
{{% alert color="primary" %}} 

スプレッドシートを操作して行や列にデータを追加する場合、行の高さまたは列の幅の変更が必要になる場合があります。行または列に書式設定を適用すると、データを表示するために現在の高さまたは幅を変更する必要がある場合があります。通常、ユーザーは Microsoft Excel を使用して WYSIWYG 環境で行の高さと列の幅を調整します。ただし、Aspose.Cells を使用すると、開発者は実行時にこれらの操作を実行できます。

{{% /alert %}} 
##  **行の操作**
###  **行の高さの調整**
Aspose.Cells はクラスを提供します。[ワークブック](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)これは Microsoft Excel ファイルを表します。の[ワークブック](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)クラスには[ワークシートコレクション](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/)これにより、Excel ファイル内の各ワークシートにアクセスできるようになります。ワークシートは次のように表されます。[ワークシート](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)クラス。の[ワークシート](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)クラスが提供するのは[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)ワークシート内のすべてのセルを表すコレクション。の[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)コレクションには、ワークシート内の行または列を管理するためのいくつかのメソッドが用意されています。これらのいくつかについては、以下で詳しく説明します。
####  **行の高さの設定**
を呼び出すことで単一行の高さを設定できます。[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)コレクションの[SetRowHeight](https://reference.aspose.com/cells/cpp/aspose.cells/cells/setrowheight/)方法。の[SetRowHeight](https://reference.aspose.com/cells/cpp/aspose.cells/cells/setrowheight/)メソッドは次のようにパラメータを受け取ります。

- *行インデックス**、高さを変更する行のインデックス。
- *行の高さ**、行に適用する行の高さ。



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-AdjustingRowHeightAndColumnWidth-SettingHeightOfRow-new.cpp" >}}


####  **ワークシート内のすべての行の高さの設定**
開発者がワークシート内のすべての行に同じ行の高さを設定する必要がある場合は、[標準高さを設定](https://reference.aspose.com/cells/cpp/aspose.cells/cells/setstandardheight/)の方法[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)コレクション。



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-AdjustingRowHeightAndColumnWidth-SettingHeightOfAllRowsInWorksheet-new.cpp" >}}
##  **列の操作**
###  **列の幅の設定**
を呼び出して列の幅を設定します。[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)コレクションの[SetColumnWidth](https://reference.aspose.com/cells/cpp/aspose.cells/cells/setcolumnwidth/)方法。の[SetColumnWidth](https://reference.aspose.com/cells/cpp/aspose.cells/cells/setcolumnwidth/)メソッドは次のパラメータを受け取ります。

- *列インデックス**、幅を変更する列のインデックス。
- *列幅**、目的の列幅。



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-AdjustingRowHeightAndColumnWidth-SettingWidthOfColumn-new.cpp" >}}
###  **ワークシート内のすべての列の幅を設定する**
ワークシート内のすべての列に同じ列幅を設定するには、[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)コレクションの[SetStandardWidth](https://reference.aspose.com/cells/cpp/aspose.cells/cells/setstandardwidth/)方法。



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-AdjustingRowHeightAndColumnWidth-SettingWidthOfAllColumnsInWorksheet-new.cpp" >}}
