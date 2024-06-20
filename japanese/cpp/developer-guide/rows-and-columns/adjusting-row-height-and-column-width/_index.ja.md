---
title: 行の高さと列の幅の調整
type: docs
weight: 10
url: /ja/cpp/adjusting-row-height-and-column-width/
---

{{% alert color="primary" %}} 

スプレッドシートで行や列にデータを追加する際、行の高さや列の幅を変更する必要があることがあります。時々、行や列に書式を適用することで、データを表示するために現在の高さや幅を変更する必要があります。通常、ユーザーはMicrosoft Excelを使用してWYSIWYG環境で行の高さと列の幅を調整します。しかし、Aspose.Cellsを使用すると、開発者はランタイムでこれらの操作を実行できます。

{{% /alert %}} 
## **行で操作する**
### **行の高さを調整**
Aspose.Cellsは、Microsoft Excelファイルを表す[Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) クラスを提供します。[Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) クラスには、Excelファイル内の各ワークシートにアクセスできる[WorksheetCollection](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/)が含まれています。ワークシートは[Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) クラスで表されます。[Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) クラスは、ワークシート内のすべてのセルを表す[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) コレクションを提供します。[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) コレクションには、ワークシート内の行や列を管理するためのいくつかのメソッドが提供されています。これについて詳しくは、以下で説明します。
#### **1行の高さを設定する**
[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) コレクションの[SetRowHeight](https://reference.aspose.com/cells/cpp/aspose.cells/cells/setrowheight/) メソッドを呼び出すことで、単一の行の高さを設定できます。[SetRowHeight](https://reference.aspose.com/cells/cpp/aspose.cells/cells/setrowheight/) メソッドは、次のようなパラメータを取ります。

- **行インデックス**：高さを変更する行のインデックス。
- **行の高さ**：行に適用する行の高さ。



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-AdjustingRowHeightAndColumnWidth-SettingHeightOfRow-new.cpp" >}}


#### **ワークシート内のすべての行の高さを設定する**
ワークシート内のすべての行に同じ行の高さを設定する場合、[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) コレクションの[SetStandardHeight](https://reference.aspose.com/cells/cpp/aspose.cells/cells/setstandardheight/) メソッドを使用できます。



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-AdjustingRowHeightAndColumnWidth-SettingHeightOfAllRowsInWorksheet-new.cpp" >}}
## **列で操作する**
### **列の幅を設定する**
[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) コレクションの[SetColumnWidth](https://reference.aspose.com/cells/cpp/aspose.cells/cells/setcolumnwidth/) メソッドを呼び出すことで、単一の列の幅を設定できます。[SetColumnWidth](https://reference.aspose.com/cells/cpp/aspose.cells/cells/setcolumnwidth/) メソッドは、次のようなパラメータを取ります。

- **列インデックス**：幅を変更する列のインデックス。
- **列の幅**：設定したい列の幅。



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-AdjustingRowHeightAndColumnWidth-SettingWidthOfColumn-new.cpp" >}}
### **ワークシート内のすべての列の幅を設定する**
ワークシートのすべての列に同じ列幅を設定する場合は、[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) コレクションの [SetStandardWidth](https://reference.aspose.com/cells/cpp/aspose.cells/cells/setstandardwidth/) メソッドを使用します。



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-AdjustingRowHeightAndColumnWidth-SettingWidthOfAllColumnsInWorksheet-new.cpp" >}}
