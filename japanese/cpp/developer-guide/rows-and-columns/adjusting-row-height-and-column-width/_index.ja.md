---
title: 行の高さと列の幅の調整
type: docs
weight: 10
url: /ja/cpp/adjusting-row-height-and-column-width/
---
{{% alert color="primary" %}} 

スプレッドシートを操作して行または列にデータを追加する場合、行の高さまたは列の幅を変更する必要がある場合があります。行または列に書式を適用すると、データを表示するために現在の高さまたは幅を変更する必要がある場合があります。通常、ユーザーは Microsoft Excel を使用して WYSIWYG 環境で行の高さと列の幅を調整します。ただし、Aspose.Cells を使用すると、開発者は実行時にこれらの操作を実行できます。

{{% /alert %}} 
## **行の操作**
### **行の高さを調整する**
Aspose.Cells はクラスを提供し、[Iワークブック](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook)Microsoft Excel ファイルを表します。の[Iワークブック](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook)クラスには[IWorksheetCollection](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet_collection)これにより、Excel ファイル内の各ワークシートにアクセスできます。ワークシートは、[Iワークシート](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet)クラス。の[Iワークシート](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet)クラスは[Iセル](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell)ワークシート内のすべてのセルを表すコレクション。の[Iセル](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell)コレクションには、ワークシートの行または列を管理するためのメソッドがいくつか用意されています。これらのいくつかについては、以下で詳しく説明します。
#### **行の高さの設定**
を呼び出して、単一の行の高さを設定することができます。[Iセル](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell)コレクションの[SetRowHeight](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a7aa441877e03639232299627261a7d1f)方法。の[SetRowHeight](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a7aa441877e03639232299627261a7d1f)メソッドは、次のように次のパラメーターを取ります。

- **行インデックス**、高さを変更する行のインデックス。
- **行の高さ**、行に適用する行の高さ。



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-AdjustingRowHeightAndColumnWidth-SettingHeightOfRow.cpp" >}}


#### **ワークシートのすべての行の高さの設定**
開発者がワークシートのすべての行に同じ行の高さを設定する必要がある場合は、[標準高さの設定](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a0b79a3163e2b601aa1b6a6a1e3f1467f)の方法[Iセル](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell)コレクション。



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-AdjustingRowHeightAndColumnWidth-SettingHeightOfAllRowsInWorksheet.cpp" >}}
## **列の操作**
### **列の幅の設定**
を呼び出して、列の幅を設定します。[Iセル](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell)コレクションの[列幅の設定](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#ab1c6a4e89760d2a022d5bfba8bc40987)方法。の[列幅の設定](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#ab1c6a4e89760d2a022d5bfba8bc40987)メソッドは次のパラメータを取ります。

- **列インデックス**、幅を変更する列のインデックス。
- **列幅**、目的の列幅。



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-AdjustingRowHeightAndColumnWidth-SettingWidthOfColumn.cpp" >}}
### **ワークシートのすべての列の幅を設定する**
ワークシートのすべての列に同じ列幅を設定するには、[Iセル](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell)コレクションの[標準幅の設定](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a48f5dbccc3bf4bb9e6e882094b500bd7)方法。



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-AdjustingRowHeightAndColumnWidth-SettingWidthOfAllColumnsInWorksheet.cpp" >}}
