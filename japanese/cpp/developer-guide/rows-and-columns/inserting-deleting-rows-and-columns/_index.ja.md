---
title: 行と列の挿入、削除
type: docs
weight: 40
url: /ja/cpp/inserting-deleting-rows-and-columns/
---
##  **導入**
新しいワークシートを最初から作成する場合でも、既存のワークシートで作業する場合でも、より多くのデータを収容するために行や列を追加する必要がある場合があります。逆に、ワークシート内の指定された位置から行または列を削除する必要がある場合もあります。これらの要件を満たすために、Aspose.Cells は、以下で説明する非常に単純なクラスとメソッドのセットを提供します。
###  **行と列の管理**
Aspose.Cells はクラスを提供します。[ワークブック](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)、これは Microsoft Excel ファイルを表します。の[ワークブック](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)クラスには[ワークシート](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/)Excel ファイル内の各ワークシートへのアクセスを許可するコレクション。ワークシートは次のように表されます。[ワークシート](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)クラス。の[ワークシート](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)クラスが提供する[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)ワークシート内のすべてのセルを表すコレクション。

の[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)collection には、ワークシート内の行と列を管理するいくつかのメソッドが用意されています。これらのいくつかについては以下で説明します。

{{% alert color="primary" %}} 

行または列を追加すると、ワークシート内のコンテンツは下または右に移動し、行または列を削除すると、コンテンツは上または左に移動します。

{{% /alert %}} 
####  **行を挿入する**
を呼び出して、ワークシートの任意の場所に行を挿入します。[行の挿入](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertrow/)の方法[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)コレクション。の[行の挿入](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertrow/)このメソッドは、新しい行が挿入される行のインデックスを取得します。



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-InsertingDeletingRowsAndColumns-InsertRow-new.cpp" >}}


####  **複数の行の挿入**
ワークシートに複数の行を挿入するには、[行の挿入](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertrows/)の方法[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)コレクション。の[行の挿入](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertrows/)このメソッドは 2 つのパラメータを取ります。

- 行インデックス。新しい行が挿入される行のインデックス。
- 行数。挿入する必要がある行の合計数。



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-InsertingDeletingRowsAndColumns-InsertingMultipleRows-new.cpp" >}}


####  **複数の行の削除**
ワークシートから複数の行を削除するには、[行の削除](https://reference.aspose.com/cells/cpp/aspose.cells/cells/deleterows/)の方法[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)コレクション。の[行の削除](https://reference.aspose.com/cells/cpp/aspose.cells/cells/deleterows/)このメソッドは 2 つのパラメータを取ります。

- 行インデックス。行が削除される行のインデックス。
- 行数。削除する必要がある行の合計数。



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-InsertingDeletingRowsAndColumns-DeletingMultipleRows-new.cpp" >}}


####  **列を挿入する**
開発者は、[列の挿入](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertcolumn/)の方法[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)コレクション。[列の挿入](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertcolumn/)このメソッドは、新しい列が挿入される列のインデックスを取得します。



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-InsertingDeletingRowsAndColumns-InsertColumn-new.cpp" >}}


####  **列を削除する**
ワークシートの任意の場所から列を削除するには、[列の削除](https://reference.aspose.com/cells/cpp/aspose.cells/cells/deletecolumn/)の方法[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)コレクション。の[列の削除](https://reference.aspose.com/cells/cpp/aspose.cells/cells/deletecolumn/)このメソッドは、削除する列のインデックスを取得します。



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-InsertingDeletingRowsAndColumns-DeleteColumn-new.cpp" >}}
