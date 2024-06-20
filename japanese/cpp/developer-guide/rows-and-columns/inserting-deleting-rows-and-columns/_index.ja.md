---
title: 行と列の挿入、削除
type: docs
weight: 40
url: /ja/cpp/inserting-deleting-rows-and-columns/
---

## **紹介**
新規ワークシートを作成したり、既存のワークシートで作業したりする際に、データの追加のために行や列を追加する必要があるかもしれません。逆に、ワークシート内の特定の位置から行または列を削除する必要があるかもしれません。これらの要件を満たすために、Aspose.Cellsは、以下で説明する非常にシンプルなクラスとメソッドを提供しています。
### **行と列の管理**
Aspose.Cellsは、Microsoft Excelファイルを表す[Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)クラスを提供しています。[Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)クラスには、Excelファイル内の各ワークシートにアクセスを許可する[Worksheets](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/)コレクションが含まれています。ワークシートは[Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)クラスによって表されます。[Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)クラスは、ワークシート内のすべてのセルを表す[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)コレクションを提供します。

[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)コレクションには、ワークシート内の行や列を管理するためのいくつかのメソッドが提供されています。以下ではその一部を詳しく説明します。

{{% alert color="primary" %}} 

行または列が追加されると、ワークシート内のコンテンツは下方向にシフトされます。行または列が削除されると、コンテンツは上方向にシフトされます。

{{% /alert %}} 
#### **行の挿入**
ワークシートに新しい行をどこにでも挿入するには、[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)コレクションの[InsertRow](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertrow/)メソッドを呼び出します。[InsertRow](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertrow/)メソッドは、新しい行が挿入される行のインデックスを取ります。



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-InsertingDeletingRowsAndColumns-InsertRow-new.cpp" >}}


#### **複数の行の挿入**
ワークシートに複数の行を挿入するには、[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)コレクションの[InsertRows](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertrows/)メソッドを呼び出します。[InsertRows](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertrows/)メソッドは2つのパラメータを取ります:

- 行インデックス、新しい行が挿入される行のインデックス。
- 行数、挿入する必要がある行の合計数。



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-InsertingDeletingRowsAndColumns-InsertingMultipleRows-new.cpp" >}}


#### **複数の行の削除**
ワークシートから複数の行を削除するには、[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)コレクションの[DeleteRows](https://reference.aspose.com/cells/cpp/aspose.cells/cells/deleterows/)メソッドを呼び出します。[DeleteRows](https://reference.aspose.com/cells/cpp/aspose.cells/cells/deleterows/)メソッドは2つのパラメータを取ります:

- 行インデックス、削除される行のインデックス。
- 行数、削除する必要がある行の合計数。



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-InsertingDeletingRowsAndColumns-DeletingMultipleRows-new.cpp" >}}


#### **列の挿入**
開発者は、任意の位置にワークシートに列を挿入するために、[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)コレクションの[InsertColumn](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertcolumn/)メソッドを呼び出すこともできます。[InsertColumn](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertcolumn/)メソッドは、新しい列が挿入される列のインデックスを取ります。



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-InsertingDeletingRowsAndColumns-InsertColumn-new.cpp" >}}


#### **列の削除**
任意の位置にワークシートから列を削除するには、[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)コレクションの[DeleteColumn](https://reference.aspose.com/cells/cpp/aspose.cells/cells/deletecolumn/)メソッドを呼び出します。[DeleteColumn](https://reference.aspose.com/cells/cpp/aspose.cells/cells/deletecolumn/)メソッドは、削除する列のインデックスを取ります。



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-InsertingDeletingRowsAndColumns-DeleteColumn-new.cpp" >}}
