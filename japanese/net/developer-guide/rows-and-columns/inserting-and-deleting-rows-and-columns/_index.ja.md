---
title: Excelファイルの行と列の挿入と削除
linktitle: 行と列の挿入と削除
type: docs
weight: 70
url: /ja/net/inserting-and-deleting-rows-and-columns/
description: この記事では、Aspose.Cells for .NET API による行と列の挿入と削除の方法を示します。
keywords: Aspose.Cells C# manage rows and columns, insert rows and columns, delete rows and columns
---
##  **導入**

新しいワークシートを最初から作成する場合でも、既存のワークシートで作業する場合でも、より多くのデータを収容するために行や列を追加する必要がある場合があります。逆に、ワークシート内の指定された位置から行または列を削除する必要がある場合もあります。
これらの要件を満たすために、Aspose.Cells は、以下で説明する非常に単純なクラスとメソッドのセットを提供します。

###  **行と列の管理**

Aspose.Cells はクラスを提供します[**ワークブック**](https://reference.aspose.com/cells/net/aspose.cells/workbook)、これは Microsoft Excel ファイルを表します。の[**ワークブック**](https://reference.aspose.com/cells/net/aspose.cells/workbook)クラスには[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection)Excel ファイル内の各ワークシートへのアクセスを許可するコレクション。ワークシートは次のように表されます。[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラス。の[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラスが提供するのは[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)ワークシート内のすべてのセルを表すコレクション。

の[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)collection には、ワークシート内の行と列を管理するいくつかのメソッドが用意されています。これらのいくつかについては以下で説明します。

{{% alert color="primary" %}}

行または列を追加すると、ワークシート内のコンテンツは下または右に移動し、行または列を削除すると、コンテンツは上または左に移動します。

{{% /alert %}}


##  **行と列の挿入**

###  **行を挿入する方法**

を呼び出して、ワークシートの任意の場所に行を挿入します。[**行の挿入**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertrow)の方法[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)コレクション。の[**行の挿入**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertrow)このメソッドは、新しい行が挿入される行のインデックスを取得します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-InsertingAndDeleting-InsertingARow-1.cs" >}}

###  **複数の行を挿入する方法**

ワークシートに複数の行を挿入するには、[**行の挿入**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertrows)の方法[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)コレクション。の[**行の挿入**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertrows)このメソッドは 2 つのパラメータを取ります。

- 行インデックス。新しい行が挿入される行のインデックス。
- 行数。挿入する必要がある行の合計数。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-InsertingAndDeleting-InsertingMultipleRows-1.cs" >}}

###  **書式設定を使用して行を挿入する方法**

書式設定オプションを使用して行を挿入するには、[**行の挿入**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertrows)かかる過負荷[**挿入オプション**](https://reference.aspose.com/cells/net/aspose.cells/insertoptions)パラメータとして。をセットする[**コピーフォーマットタイプ**](https://reference.aspose.com/cells/net/aspose.cells/insertoptions/properties/copyformattype)の財産[**挿入オプション**](https://reference.aspose.com/cells/net/aspose.cells/insertoptions)とのクラス[**コピーフォーマットタイプ**](https://reference.aspose.com/cells/net/aspose.cells/insertoptions/properties/copyformattype)列挙。の[**コピーフォーマットタイプ**](https://reference.aspose.com/cells/net/aspose.cells/insertoptions/properties/copyformattype)Enumeration には以下に示す 3 つのメンバーがあります。

- SameAsAbove: 行を上の行と同じ形式に設定します。
- SameAsBelow: 行を下の行と同じ形式に設定します。
- クリア：書式設定をクリアします。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-InsertingAndDeleting-InsertingARowWithFormatting-1.cs" >}}

###  **列を挿入する方法**

開発者は、[**列の挿入**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertcolumn)の方法[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)コレクション。の[**列の挿入**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertcolumn)このメソッドは、新しい列が挿入される列のインデックスを取得します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-InsertingAndDeleting-InsertingAColumn-1.cs" >}}

##  **行と列の削除**

###  **複数の行を削除する方法**

ワークシートから複数の行を削除するには、[**行の削除**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deleterows)の方法[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)コレクション。の[**行の削除**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deleterows)このメソッドは 2 つのパラメータを取ります。

- 行インデックス。行が削除される行のインデックス。
- 行数。削除する必要がある行の合計数。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-InsertingAndDeleting-DeletingMultipleRows-1.cs" >}}


###  **列を削除する方法**

ワークシートの任意の場所から列を削除するには、[**列の削除**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deletecolumn)の方法[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)コレクション。の[**列の削除**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deletecolumn)このメソッドは、削除する列のインデックスを取得します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-InsertingAndDeleting-DeletingAColumn-1.cs" >}}
