---
title: Excelファイルの行と列の挿入と削除
linktitle: 行と列の挿入と削除
type: docs
weight: 70
url: /ja/net/inserting-and-deleting-rows-and-columns/
---
## **序章**

新しいワークシートをゼロから作成する場合でも、既存のワークシートで作業する場合でも、より多くのデータを収容するために余分な行または列を追加する必要がある場合があります。逆に、ワークシートの指定された位置から行または列を削除する必要がある場合もあります。
これらの要件を満たすために、Aspose.Cells は、以下で説明する非常に単純なクラスとメソッドのセットを提供します。

### **行と列を管理する**

Aspose.Cells はクラスを提供します[**ワークブック**](https://reference.aspose.com/cells/net/aspose.cells/workbook)、Microsoft Excel ファイルを表します。の[**ワークブック**](https://reference.aspose.com/cells/net/aspose.cells/workbook)クラスには[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection)Excel ファイル内の各ワークシートにアクセスできるコレクション。ワークシートは、[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラス。の[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラスは[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)ワークシート内のすべてのセルを表すコレクション。

の[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)コレクションには、ワークシートの行と列を管理するいくつかのメソッドが用意されています。これらのいくつかを以下で説明します。

{{% alert color="primary" %}}

行または列が追加されると、ワークシートのコンテンツは下または右にシフトされ、行または列が削除されると、コンテンツは上または左にシフトされます。

{{% /alert %}}


## **行と列を挿入する**

### **行を挿入する**

を呼び出して、ワークシートの任意の場所に行を挿入します。[**行の挿入**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertrow)の方法[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)コレクション。の[**行の挿入**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertrow)メソッドは、新しい行が挿入される行のインデックスを取ります。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-InsertingAndDeleting-InsertingARow-1.cs" >}}

### **複数の行を挿入**

複数の行をワークシートに挿入するには、[**InsertRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertrows)の方法[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)コレクション。の[**InsertRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertrows)メソッドは次の 2 つのパラメーターを取ります。

- 行インデックス。新しい行が挿入される行のインデックス。
- 行数、挿入する必要がある行の総数。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-InsertingAndDeleting-InsertingMultipleRows-1.cs" >}}

### **書式を設定して行を挿入する**

書式設定オプションを含む行を挿入するには、[**InsertRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertrows)かかるオーバーロード[**挿入オプション**](https://reference.aspose.com/cells/net/aspose.cells/insertoptions)パラメータとして。をセットする[**CopyFormatType**](https://reference.aspose.com/cells/net/aspose.cells/insertoptions/properties/copyformattype)のプロパティ[**挿入オプション**](https://reference.aspose.com/cells/net/aspose.cells/insertoptions)クラス[**CopyFormatType**](https://reference.aspose.com/cells/net/aspose.cells/insertoptions/properties/copyformattype)列挙。の[**CopyFormatType**](https://reference.aspose.com/cells/net/aspose.cells/insertoptions/properties/copyformattype)Enumeration には、以下に示す 3 つのメンバーがあります。

- SameAsAbove: 上の行と同じように行をフォーマットします。
- SameAsBelow: 下の行と同じように行をフォーマットします。
- クリア: フォーマットをクリアします。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-InsertingAndDeleting-InsertingARowWithFormatting-1.cs" >}}

### **列を挿入する**

開発者は、を呼び出して、ワークシートの任意の場所に列を挿入することもできます[**挿入列**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertcolumn)の方法[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)コレクション。の[**挿入列**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertcolumn)メソッドは、新しい列が挿入される列のインデックスを取得します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-InsertingAndDeleting-InsertingAColumn-1.cs" >}}

## **行と列を削除する**

### **複数の行を削除**

ワークシートから複数の行を削除するには、[**行の削除**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deleterows)の方法[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)コレクション。の[**行の削除**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deleterows)メソッドは次の 2 つのパラメーターを取ります。

- 行インデックス。行が削除される行のインデックス。
- 行数、削除する必要がある行の総数。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-InsertingAndDeleting-DeletingMultipleRows-1.cs" >}}


### **列を削除する**

ワークシートの任意の場所から列を削除するには、[**列の削除**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deletecolumn)の方法[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)コレクション。の[**列の削除**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deletecolumn)メソッドは、削除する列のインデックスを取得します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-InsertingAndDeleting-DeletingAColumn-1.cs" >}}
