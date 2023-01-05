---
title: 列挙子を使用する方法と場所
linktitle: データの反復
type: docs
weight: 55
url: /ja/net/how-and-where-to-use-enumerators/
---
{{% alert color="primary" %}}

列挙子は、コンテナーまたはコレクションを走査する機能を提供するオブジェクトです。列挙子は、コレクション内のデータを読み取るために使用できますが、基になるコレクションを変更するために使用することはできません。一方、IEnumerable は、IEnumerator インターフェイスを返す 1 つのメソッド GetEnumerator を定義するインターフェイスであり、これにより、次への読み取り専用アクセスが許可されます。コレクション。

Aspose.Cells API は多数の列挙子を提供しますが、この記事では主に以下に示す 3 つのタイプについて説明します。

1. Cells 列挙子
1. 行列挙子
1. 列列挙子

{{% /alert %}}

## **列挙子の使用方法**

### **Cells 列挙子**

Cells 列挙子にアクセスするにはさまざまな方法があり、アプリケーションの要件に基づいてこれらの方法のいずれかを使用できます。セル列挙子を返すメソッドは次のとおりです。

1. [**Cells.GetEnumerator**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/getenumerator)
1. [**Row.GetEnumerator**](https://reference.aspose.com/cells/net/aspose.cells/row/methods/getenumerator)
1. [**Range.GetEnumerator**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/getenumerator)

上記のすべてのメソッドは、初期化されたセルのコレクションをトラバースできる列挙子を返します。

{{% alert color="primary" %}}

セルをトラバースしている間は、コレクションを変更しないでください (新しい Cell がインスタンス化されるか、既存の Cell が削除される操作)。そうしないと、列挙子がすべてのセルを正しく走査できない場合があります (一部の要素が繰り返し走査されるか、スキップされる可能性があります)。

{{% /alert %}}

次のコード例は、Cells コレクションの IEnumerator インターフェイスの実装を示しています。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingRowsColumnsCells-HowAndWhereToUseEnumerators-CellsEnumerator.cs" >}}

### **行列挙子**

 Rows Enumerator は、[**RowCollection.GetEnumerator**](https://reference.aspose.com/cells/net/aspose.cells/rowcollection/methods/getenumerator)方法。次のコード例は、IEnumerator インターフェイスの実装を示しています。[**行コレクション**](https://reference.aspose.com/cells/net/aspose.cells/rowcollection).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingRowsColumnsCells-HowAndWhereToUseEnumerators-RowEnumerator.cs" >}}

### **列列挙子**

 Columns Enumerator は、[**ColumnCollection.GetEnumerator**](https://reference.aspose.com/cells/net/aspose.cells/columncollection)方法。次のコード例は、IEnumerator インターフェイスの実装を示しています。[**列コレクション**](https://reference.aspose.com/cells/net/aspose.cells/columncollection).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingRowsColumnsCells-HowAndWhereToUseEnumerators-ColumnEnumerator.cs" >}}

## **列挙子を使用する場所**

列挙子を使用する利点を説明するために、リアルタイムの例を見てみましょう。

**シナリオ**

アプリケーション要件は、特定のセル内のすべてのセルをトラバースすることです。[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)それらの値を読み取ります。この目標を実現するには、いくつかの方法があります。いくつかを以下に示します。

### **表示範囲の使用**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingRowsColumnsCells-HowAndWhereToUseEnumerators-UsingDisplayRange.cs" >}}

### **MaxDataRow と MaxDataColumn の使用**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingRowsColumnsCells-HowAndWhereToUseEnumerators-UsingMaxDataRowAndMaxDataColumn.cs" >}}

上記のアプローチの両方が多かれ少なかれ同様のロジックを使用していることがわかります。コレクション内のすべてのセルをループして、セルの値を読み取ります。これは、以下で説明するように、いくつかの理由で問題になる可能性があります。

1. などの API[**最大行**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxrow), [**MaxDataRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxdatarow), [**最大列**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxcolumn), [**MaxDataColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxdatacolumn) & [**MaxDisplayRange**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxdisplayrange)対応する統計を収集するために余分な時間が必要です。データ マトリックス (行 x 列) が大きい場合、これらの API を使用すると、パフォーマンスが低下する可能性があります。
1. ほとんどの場合、特定の範囲内のすべてのセルがインスタンス化されるわけではありません。このような状況では、マトリックス内のすべてのセルをチェックすることは、初期化されたセルのみをチェックする場合に比べて効率的ではありません。
1. Cells 行、列としてループ内のセルにアクセスすると、範囲内のすべてのセル オブジェクトがインスタンス化され、最終的に OutOfMemoryException が発生する可能性があります。

## **結論**

上記の事実に基づいて、列挙子を使用する必要があるシナリオを次に示します。

1. セル コレクションへの読み取り専用アクセスが必要です。要件は、セルのみを検査することです。
1. 多数のセルをトラバースする必要があります。
1. 初期化されたセル/行/列のみが走査されます。
