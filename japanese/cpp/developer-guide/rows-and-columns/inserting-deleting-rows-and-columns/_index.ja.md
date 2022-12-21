---
title: 行と列の挿入、削除
type: docs
weight: 40
url: /ja/cpp/inserting-deleting-rows-and-columns/
---
## **序章**
新しいワークシートをゼロから作成する場合でも、既存のワークシートで作業する場合でも、より多くのデータを収容するために余分な行または列を追加する必要がある場合があります。逆に、ワークシートの指定された位置から行または列を削除する必要がある場合もあります。これらの要件を満たすために、Aspose.Cells は、以下で説明する非常に単純なクラスとメソッドのセットを提供します。
### **行と列の管理**
Aspose.Cells はクラスを提供し、[Iワークブック](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook)、Microsoft Excel ファイルを表します。の[Iワークブック](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook)クラスには[Iワークシート](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet_collection)Excel ファイル内の各ワークシートにアクセスできるコレクション。ワークシートは、[Iワークシート](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet)クラス。の[Iワークシート](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet)クラスは[Iセル](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell)ワークシート内のすべてのセルを表すコレクション。

の[Iセル](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell)コレクションには、ワークシートの行と列を管理するいくつかのメソッドが用意されています。これらのいくつかを以下で説明します。

{{% alert color="primary" %}} 

行または列が追加されると、ワークシートのコンテンツは下または右にシフトされ、行または列が削除されると、コンテンツは上または左にシフトされます。

{{% /alert %}} 
#### **行を挿入する**
を呼び出して、ワークシートの任意の場所に行を挿入します。[行の挿入](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#ad9c067ccb5f34a7740f5d1cc3dbefbe7)の方法[Iセル](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell)コレクション。の[行の挿入](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#ad9c067ccb5f34a7740f5d1cc3dbefbe7)メソッドは、新しい行が挿入される行のインデックスを取ります。



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-InsertingDeletingRowsAndColumns-InsertRow.cpp" >}}


#### **複数行の挿入**
複数の行をワークシートに挿入するには、[InsertRows](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a61e4cd6dcaeeb0d11afd54616df75ee0)の方法[Iセル](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell)コレクション。の[InsertRows](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a61e4cd6dcaeeb0d11afd54616df75ee0)メソッドは次の 2 つのパラメーターを取ります。

- 行インデックス。新しい行が挿入される行のインデックス。
- 行数、挿入する必要がある行の総数。



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-InsertingDeletingRowsAndColumns-InsertingMultipleRows.cpp" >}}


#### **複数行の削除**
ワークシートから複数の行を削除するには、[行の削除](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a251261027b564ebdf27c2c6d5149c0e1)の方法[Iセル](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell)コレクション。の[行の削除](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a251261027b564ebdf27c2c6d5149c0e1)メソッドは次の 2 つのパラメーターを取ります。

- 行インデックス。行が削除される行のインデックス。
- 行数、削除する必要がある行の総数。



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-InsertingDeletingRowsAndColumns-DeletingMultipleRows.cpp" >}}


#### **列を挿入する**
開発者は、を呼び出して、ワークシートの任意の場所に列を挿入することもできます[挿入列](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a8e8cb6d0812129669258378649b3fd55)の方法[Iセル](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell)コレクション。[挿入列](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a8e8cb6d0812129669258378649b3fd55)メソッドは、新しい列が挿入される列のインデックスを取得します。



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-InsertingDeletingRowsAndColumns-InsertColumn.cpp" >}}


#### **列を削除する**
ワークシートの任意の場所から列を削除するには、[列の削除](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#ae00721fd2be220e7b73b2cab6a70e89b)の方法[Iセル](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell)コレクション。の[列の削除](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#ae00721fd2be220e7b73b2cab6a70e89b)メソッドは、削除する列のインデックスを取得します。



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-InsertingDeletingRowsAndColumns-DeleteColumn.cpp" >}}
