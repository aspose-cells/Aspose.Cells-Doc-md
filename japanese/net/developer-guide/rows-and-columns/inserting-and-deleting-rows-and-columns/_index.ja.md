---
title: Excelファイルの行と列の挿入と削除
linktitle: Excelファイルの行と列の挿入と削除
type: docs
weight: 70
url: /ja/net/inserting-and-deleting-rows-and-columns/
description: この記事では、Aspose.Cells for .NET APIを使用して行や列を挿入および削除する方法を示しています。
keywords: Aspose.Cells C# で行と列を管理し、行と列を挿入および削除します
---

## **紹介**

ワークシートをゼロから作成するか、既存のワークシートで作業する場合、さらなるデータを収容するために追加の行や列を必要とする場合があります。逆に、ワークシート内の特定の位置から行や列を削除する必要がある場合もあります。
これらの要件を満たすために、Aspose.Cellsは以下で説明されている非常にシンプルな一連のクラスとメソッドを提供しています。

### **行と列の管理**

Aspose.Cellsには、Microsoft Excelファイルを表す[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)クラスが提供されています。[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)クラスには、Excelファイル内の各ワークシートへのアクセスを可能にする[**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection)コレクションが含まれています。ワークシートは[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラスで表されます。[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラスには、ワークシート内のすべてのセルを表す[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)コレクションが提供されています。

[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) コレクションには、ワークシート内の行と列を管理するためのいくつかのメソッドが提供されています。そのうちのいくつかについて以下で説明します。

{{% alert color="primary" %}}

行または列が追加されると、ワークシート内のコンテンツは下方向にシフトされます。行または列が削除されると、コンテンツは上方向にシフトされます。

{{% /alert %}}


## **行と列の挿入**

### **行の挿入方法**

[**InsertRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertrow) コレクションの[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) メソッドを呼び出すことで、ワークシートの任意の位置に行を挿入できます。[**InsertRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertrow) メソッドは新しい行が挿入される行のインデックスを取ります。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-InsertingAndDeleting-InsertingARow-1.cs" >}}

### **複数の行を挿入する方法**

ワークシートに複数の行を挿入するには、[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) コレクションの[**InsertRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertrows) メソッドを呼び出します。[**InsertRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertrows) メソッドは2つのパラメータを取ります:

- 行インデックス、新しい行が挿入される行のインデックス。
- 行数、挿入する必要がある行の合計数。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-InsertingAndDeleting-InsertingMultipleRows-1.cs" >}}

### **書式付きで行を挿入する方法**

書式オプションを指定して行を挿入するには、パラメータとして[**InsertOptions**](https://reference.aspose.com/cells/net/aspose.cells/insertoptions)を取る[**InsertRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertrows) オーバーロードを使用します。[**InsertOptions**](https://reference.aspose.com/cells/net/aspose.cells/insertoptions)クラスの[**CopyFormatType**](https://reference.aspose.com/cells/net/aspose.cells/insertoptions/properties/copyformattype)プロパティを[**CopyFormatType**](https://reference.aspose.com/cells/net/aspose.cells/insertoptions/properties/copyformattype) 列挙型で設定します。[**CopyFormatType**](https://reference.aspose.com/cells/net/aspose.cells/insertoptions/properties/copyformattype) 列挙型には次の3つのメンバーがあります。

- SameAsAbove: 上の行と同じ書式を適用します。
- SameAsBelow: 下の行と同じ書式を適用します。
- Clear: 書式をクリアします。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-InsertingAndDeleting-InsertingARowWithFormatting-1.cs" >}}

### **列の挿入方法**

開発者は、[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) コレクションの[**InsertColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertcolumn) メソッドを呼び出すことで、ワークシートの任意の位置に列を挿入することもできます。[**InsertColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertcolumn) メソッドは、新しい列が挿入される列のインデックスを取ります。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-InsertingAndDeleting-InsertingAColumn-1.cs" >}}

## **行と列の削除**

### **複数の行を削除する方法**

ワークシートから複数の行を削除するには、[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) コレクションの[**DeleteRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deleterows) メソッドを呼び出します。[**DeleteRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deleterows) メソッドは2つのパラメータを取ります:

- 行インデックス、削除される行のインデックス。
- 行数、削除する必要がある行の合計数。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-InsertingAndDeleting-DeletingMultipleRows-1.cs" >}}


### **列を削除する方法**

ワークシートから任意の位置に列を削除するには、[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) コレクションの[**DeleteColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deletecolumn) メソッドを呼び出します。[**DeleteColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deletecolumn) メソッドは削除する列のインデックスを取ります。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-InsertingAndDeleting-DeletingAColumn-1.cs" >}}
