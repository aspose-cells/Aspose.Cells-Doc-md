---
title: 列挙子の使用方法と使用場所
linktitle: データの反復処理
type: docs
weight: 55
url: /ja/net/how-and-where-to-use-enumerators/
description: 列挙子の使用方法と使用場所については、Aspose.Cells for .NET API を通じて学習してください。
keywords: How to use Enumerators, Cells Enumerator, Rows Enumerator, Columns Enumerator
---
{{% alert color="primary" %}}

列挙子は、コンテナーまたはコレクションを横断する機能を提供するオブジェクトです。列挙子は、コレクション内のデータを読み取るために使用できますが、基礎となるコレクションを変更するために使用することはできません。一方、IEnumerable は、IEnumerator インターフェイスを返す 1 つのメソッド GetEnumerator を定義するインターフェイスです。これにより、次への読み取り専用アクセスが可能になります。コレクション。

Aspose.Cells API には多数の列挙子が用意されていますが、この記事では主に以下の 3 つのタイプについて説明します。

1. Cells 列挙者
1. 行列挙子
1. 列列挙子

{{% /alert %}}

##  **列挙子の使用方法**

###  **Cells 列挙者**

Cells Enumerator にアクセスするにはさまざまな方法があり、アプリケーションの要件に基づいてこれらの方法のいずれかを使用できます。以下は、セル列挙子を返すメソッドです。

1. [**Cells.GetEnumerator**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/getenumerator)
1. [**Row.GetEnumerator**](https://reference.aspose.com/cells/net/aspose.cells/row/methods/getenumerator)
1. [**Range.GetEnumerator**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/getenumerator)

上記のメソッドはすべて、初期化されたセルのコレクションを走査できる列挙子を返します。

{{% alert color="primary" %}}

セルを走査している間、コレクションを変更しないでください (新しい Cell がインスタンス化されるか、既存の Cell が削除される操作)。そうしないと、列挙子がすべてのセルを正しく走査できない可能性があります (一部の要素が繰り返し走査されたり、スキップされたりする可能性があります)。

{{% /alert %}}

次のコード例は、Cells コレクションの IEnumerator インターフェイスの実装を示しています。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingRowsColumnsCells-HowAndWhereToUseEnumerators-CellsEnumerator.cs" >}}

###  **行列挙子**

行列挙子には、[**RowCollection.GetEnumerator**](https://reference.aspose.com/cells/net/aspose.cells/rowcollection/methods/getenumerator)方法。次のコード例は、IEnumerator インターフェイスの実装を示しています。[**行コレクション**](https://reference.aspose.com/cells/net/aspose.cells/rowcollection).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingRowsColumnsCells-HowAndWhereToUseEnumerators-RowEnumerator.cs" >}}

###  **列列挙子**

列列挙子には、[**ColumnCollection.GetEnumerator**](https://reference.aspose.com/cells/net/aspose.cells/columncollection)方法。次のコード例は、IEnumerator インターフェイスの実装を示しています。[**コラムコレクション**](https://reference.aspose.com/cells/net/aspose.cells/columncollection).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingRowsColumnsCells-HowAndWhereToUseEnumerators-ColumnEnumerator.cs" >}}

##  **列挙子を使用する場所**

列挙子を使用する利点について説明するために、リアルタイムの例を見てみましょう。

**シナリオ**

アプリケーションの要件は、指定されたセル内のすべてのセルを走査することです。[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)彼らの価値観を読み取るために。この目標を実現するにはいくつかの方法が考えられます。以下にいくつかを示します。

###  **表示範囲の使用**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingRowsColumnsCells-HowAndWhereToUseEnumerators-UsingDisplayRange.cs" >}}

###  **MaxDataRow と MaxDataColumn の使用**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingRowsColumnsCells-HowAndWhereToUseEnumerators-UsingMaxDataRowAndMaxDataColumn.cs" >}}

ご覧のとおり、上記のアプローチは両方とも、多かれ少なかれ同様のロジックを使用しています。コレクション内のすべてのセルをループしてセル値を読み取ります。これは、以下で説明するように、さまざまな理由で問題となる可能性があります。

1. などの API[**マックスロウ**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxrow), [**MaxDataRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxdatarow), [**MaxColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxcolumn), [**MaxDataColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxdatacolumn) & [**最大表示範囲**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxdisplayrange)対応する統計を収集するには余分な時間が必要です。データ行列 (行 x 列) が大きい場合、これらの API を使用するとパフォーマンスが低下する可能性があります。
1. ほとんどの場合、特定の範囲内のすべてのセルがインスタンス化されるわけではありません。このような状況では、行列内のすべてのセルをチェックすることは、初期化されたセルのみをチェックする場合に比べてあまり効率的ではありません。
1. ループ内のセルに Cells 行、列としてアクセスすると、範囲内のすべてのセル オブジェクトがインスタンス化され、最終的に OutOfMemoryException が発生する可能性があります。

##  **結論**

上記の事実に基づいて、列挙子を使用する必要がある考えられるシナリオは次のとおりです。

1. セル コレクションへの読み取り専用アクセスが必要です。つまり、必要なのはセルを検査することだけです。
1. 多数のセルを通過する必要があります。
1. 初期化されたセル/行/列のみが走査されます。
