---
title: 列挙子の使用方法と場所
linktitle: データの反復
type: docs
weight: 55
url: /ja/net/how-and-where-to-use-enumerators/
description: Aspose.Cells for .NET APIを利用した列挙子の使用方法と場所について学ぶ
keywords: 列挙子の使用方法、セル列挙子、行列挙子、列列挙子
---

{{% alert color="primary" %}}

列挙子は、コンテナやコレクションをトラバースする能力を提供するオブジェクトです。列挙子はコレクション内のデータを読むために使用できますが、基礎となるコレクションを変更することはできません。一方、IEnumerableは、GetEnumeratorメソッドを定義するインターフェースであり、これにより読み取り専用アクセスが可能なICollectionインターフェースが返されます。

Aspose.CellsのAPIはたくさんの列挙子を提供していますが、この記事では主に以下にリストされている3つのタイプについて説明しています。

1. セル列挙子
1. 行列挙子
1. 列列挙子

{{% /alert %}}

## **列挙子の使用方法**

### **セル列挙子**

セル列挙子へのアクセス方法にはさまざまな方法があり、アプリケーションの要件に基づいてこれらのメソッドのいずれかを使用できます。セル列挙子を返すメソッドは次のとおりです。

1. [**Cells.GetEnumerator**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/getenumerator)
1. [**Row.GetEnumerator**](https://reference.aspose.com/cells/net/aspose.cells/row/methods/getenumerator)
1. [**Range.GetEnumerator**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/getenumerator)

上記のすべての方法は、初期化されたセルコレクションをトラバースする列挙子を返します。

{{% alert color="primary" %}}

セルをトラバースする際には、コレクションを修正してはいけません（新しいセルを作成する操作や既存のセルを削除する操作）。そうしない場合、列挙子はすべてのセルを正しくトラバースできなくなる可能性があります（一部の要素が繰り返しトラバースされたり、スキップされたりすることがあります）。

{{% /alert %}}

以下のコード例は、CellsコレクションのIEnumeratorインターフェースの実装を示しています。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingRowsColumnsCells-HowAndWhereToUseEnumerators-CellsEnumerator.cs" >}}

### **行列挙子**

[**RowCollection.GetEnumerator**](https://reference.aspose.com/cells/net/aspose.cells/rowcollection/methods/getenumerator)メソッドを使用しながら行列挙子にアクセスできます。次のコード例は、[**RowCollection**](https://reference.aspose.com/cells/net/aspose.cells/rowcollection)のIEnumeratorインターフェースの実装を示しています。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingRowsColumnsCells-HowAndWhereToUseEnumerators-RowEnumerator.cs" >}}

### **列列挙子**

列の列挙子は、[**ColumnCollection.GetEnumerator**](https://reference.aspose.com/cells/net/aspose.cells/columncollection)メソッドを使用している間にアクセスできます。次のコード例では、[**ColumnCollection**](https://reference.aspose.com/cells/net/aspose.cells/columncollection)のIEnumeratorインターフェイスの実装を示します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingRowsColumnsCells-HowAndWhereToUseEnumerators-ColumnEnumerator.cs" >}}

## **列挙子の使用場所**

列挙子の利点を議論するために、実際の例を使って説明しましょう。

**シナリオ**

アプリケーションの要件は、与えられた[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)内のすべてのセルを走査してその値を読み取ることです。この目標を実装するための方法はいくつかあります。いくつかを以下で示します。

### **表示範囲を使用する**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingRowsColumnsCells-HowAndWhereToUseEnumerators-UsingDisplayRange.cs" >}}

### **MaxDataRowおよびMaxDataColumnを使用する**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingRowsColumnsCells-HowAndWhereToUseEnumerators-UsingMaxDataRowAndMaxDataColumn.cs" >}}

上記のアプローチのそれぞれがほとんど同じロジックを使用していることがわかります。つまり、コレクション内のすべてのセルをループしてセルの値を読み取ります。これにはいくつかの理由で問題が生じる可能性があります。

1. [**MaxRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxrow)、[**MaxDataRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxdatarow)、[**MaxColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxcolumn)、および[**MaxDataColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxdatacolumn) などのAPIは、対応する統計情報を収集するための追加時間を必要とします。データ行列（行×列）が大きい場合、これらのAPIを使用するとパフォーマンスにペナルティが課される場合があります。
1. ほとんどの場合、指定された範囲内のすべてのセルがインスタンス化されていません。そのような状況では、行列内のすべてのセルを確認することは、初期化されたセルのみを確認する場合と比べて効率的ではありません。
1. Cells row、columnとしてセルにアクセスすることは、範囲内のすべてのセルオブジェクトをインスタンス化することになり、最終的にOutOfMemoryExceptionを引き起こす可能性があります。

## **結論**

上記の事実に基づいて、列挙子を使用すべき可能なシナリオが以下に示されています。

1. セルコレクションの読み取り専用アクセスが必要な場合、つまり、セルの確認のみが必要な場合。
1. 多数のセルを走査する必要がある場合。
1. 初期化されたセル/行/列のみを走査する必要がある場合。
{{< app/cells/assistant language="csharp" >}}
