---
title: Excelファイルの行と列の挿入と削除
linktitle: Excelファイルの行と列の挿入と削除
type: docs
weight: 70
url: /ja/python-net/inserting-and-deleting-rows-and-columns/
description: この記事では、Aspose.Cells for Python via .NET APIを使用して行と列を挿入および削除する方法を示しています。
keywords: Python Excelライブラリ、Aspose.Cells Pythonによる行と列の管理、Pythonによる行と列の挿入、Pythonによる行と列の削除、PythonによるExcelの行と列の削除
---

## **紹介**

ワークシートをゼロから作成するか、既存のワークシートで作業する場合、さらなるデータを収容するために追加の行や列を必要とする場合があります。逆に、ワークシート内の特定の位置から行や列を削除する必要がある場合もあります。
これらの要件を満たすために、Aspose.Cells for Python via .NETでは、以下で説明する非常にシンプルなクラスとメソッドのセットを提供しています。

### **行と列の管理**

Aspose.Cells for Python via .NETは、Microsoft Excelファイルを表す[**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)クラスを提供します。[**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)クラスには、Excelファイル内の各ワークシートへのアクセスを可能にする[**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheetcollection)コレクションが含まれています。ワークシートは[**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet)クラスによって表されます。[**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet)クラスは、ワークシート内のすべてのセルを表す[**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells)コレクションを提供します。

[**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells) コレクションには、ワークシート内の行と列を管理するためのいくつかのメソッドが提供されています。そのうちのいくつかについて以下で説明します。

{{% alert color="primary" %}}

行または列が追加されると、ワークシート内のコンテンツは下方向にシフトされます。行または列が削除されると、コンテンツは上方向にシフトされます。

{{% /alert %}}


## **行と列の挿入**

### **行の挿入方法**

[**insert_row**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/insert_row/) コレクションの[**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells) メソッドを呼び出すことで、ワークシートの任意の位置に行を挿入できます。[**insert_row**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/insert_row/) メソッドは新しい行が挿入される行のインデックスを取ります。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-InsertingAndDeleting-InsertingARow-1.py" >}}

### **複数の行を挿入する方法**

ワークシートに複数の行を挿入するには、[**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells) コレクションの[**insert_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/insert_rows/#int-int) メソッドを呼び出します。[**insert_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/insert_rows/#int-int) メソッドは2つのパラメータを取ります:

- 行インデックス、新しい行が挿入される行のインデックス。
- 行数、挿入する必要がある行の合計数。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-InsertingAndDeleting-InsertingMultipleRows-1.py" >}}

### **書式付きで行を挿入する方法**

書式オプションを指定して行を挿入するには、パラメータとして[**InsertOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/insertoptions)を取る[**insert_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/insert_rows/#int-int-aspose.cells.InsertOptions) オーバーロードを使用します。[**InsertOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/insertoptions)クラスの[**copy_format_type**](https://reference.aspose.com/cells/python-net/aspose.cells/insertoptions/copy_format_type/)プロパティを[**CopyFormatType**](https://reference.aspose.com/cells/python-net/aspose.cells/copyformattype/) 列挙型で設定します。[**CopyFormatType**](https://reference.aspose.com/cells/python-net/aspose.cells/copyformattype/) 列挙型には次の3つのメンバーがあります。

- SAME_AS_ABOVE：前の行と同じ形式にします。
- SAME_AS_BELOW：次の行と同じ形式にします。
- CLEAR：書式をクリアします。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-InsertingAndDeleting-InsertingARowWithFormatting-1.py" >}}

### **列の挿入方法**

開発者は、[**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells) コレクションの[**insert_column**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/insert_column/#int) メソッドを呼び出すことで、ワークシートの任意の位置に列を挿入することもできます。[**insert_column**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/insert_column/#int) メソッドは、新しい列が挿入される列のインデックスを取ります。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-InsertingAndDeleting-InsertingAColumn-1.py" >}}

## **行と列の削除**

### **複数の行を削除する方法**

ワークシートから複数の行を削除するには、[**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells) コレクションの[**delete_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/delete_rows/#int-int) メソッドを呼び出します。[**delete_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/delete_rows/#int-int) メソッドは2つのパラメータを取ります:

- 行インデックス、削除される行のインデックス。
- 行数、削除する必要がある行の合計数。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-InsertingAndDeleting-DeletingMultipleRows-1.py" >}}


### **列を削除する方法**

ワークシートから任意の位置に列を削除するには、[**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells) コレクションの[**delete_column**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/delete_column/#int) メソッドを呼び出します。[**delete_column**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/delete_column/#int) メソッドは削除する列のインデックスを取ります。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-InsertingAndDeleting-DeletingAColumn-1.py" >}}
