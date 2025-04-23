---
title: 行と列の挿入、削除
type: docs
weight: 40
url: /ja/go-cpp/inserting-deleting-rows-and-columns/
---

## **紹介**

新規ワークシートを作成したり、既存のワークシートで作業したりする際に、データの追加のために行や列を追加する必要があるかもしれません。逆に、ワークシート内の特定の位置から行または列を削除する必要があるかもしれません。これらの要件を満たすために、Aspose.Cellsは、以下で説明する非常にシンプルなクラスとメソッドを提供しています。

### **行と列の管理**

Aspose.Cellsは、Microsoft Excelファイルを表す [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) クラスを提供します。 [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) クラスには、Excelファイル内の各ワークシートにアクセス可能な [Worksheets](https://reference.aspose.com/cells/go-cpp/worksheetcollection/) コレクションが含まれています。ワークシートは [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/) クラスで表されます。 [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/) クラスは、すべてのセルを表す [Cells](https://reference.aspose.com/cells/go-cpp/cells/) コレクションを提供します。

[Cells](https://reference.aspose.com/cells/go-cpp/cells/) コレクションは、ワークシート内の行と列を管理するための複数のメソッドを提供します。その一部を以下で解説します。

{{% alert color="primary" %}}

行または列が追加されると、ワークシート内のコンテンツは下方向にシフトされます。行または列が削除されると、コンテンツは上方向にシフトされます。

{{% /alert %}}

任意の場所に行を挿入するには、 [Cells](https://reference.aspose.com/cells/go-cpp/cells/) コレクションの [InsertRow](https://reference.aspose.com/cells/go-cpp/cells/insertrow/) メソッドを呼び出します。 [InsertRow](https://reference.aspose.com/cells/go-cpp/cells/insertrow/) は挿入する行のインデックスを引数とします。
{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-InsertRow.go" >}}

#### **複数の行の挿入**

複数行を挿入するには、 [Cells](https://reference.aspose.com/cells/go-cpp/cells/) コレクションの [InsertRows](https://reference.aspose.com/cells/go-cpp/cells/insertrows_int_int/) メソッドを使用します。 [InsertRows](https://reference.aspose.com/cells/go-cpp/cells/insertrowinsertrows_int_ints/) は2つのパラメータを取ります。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-InsertingMultipleRows.go" >}}

#### **複数の行の削除**

複数行を削除するには、 [Cells](https://reference.aspose.com/cells/go-cpp/cells/) コレクションの [DeleteRows](https://reference.aspose.com/cells/go-cpp/cells/deleterows_int_int_bool/) メソッドを呼び出します。 [DeleteRows](https://reference.aspose.com/cells/go-cpp/cells/deleterows_int_int_bool/) は2つのパラメータを取ります。

- 行インデックス、削除される行のインデックス。
- 行数、削除する必要がある行の合計数。

#### **列の挿入**

開発者は、任意の場所に列を挿入するために、 [Cells](https://reference.aspose.com/cells/go-cpp/cells/) コレクションの [InsertColumn](https://reference.aspose.com/cells/go-cpp/cells/insertcolumn_int/) メソッドを呼び出すこともできます。 [InsertColumn](https://reference.aspose.com/cells/go-cpp/cells/insertcolumn_int/) は挿入する列のインデックスを引数とします。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-InsertColumn.go" >}}

任意の場所に列を削除するには、 [Cells](https://reference.aspose.com/cells/go-cpp/cells/) コレクションの [DeleteColumn](https://reference.aspose.com/cells/go-cpp/cells/deletecolumn_int/) メソッドを呼び出します。 [DeleteColumn](https://reference.aspose.com/cells/go-cpp/cells/deletecolumn_int/) は削除する列のインデックスを引数とします。
{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DeleteColumn.go" >}}
