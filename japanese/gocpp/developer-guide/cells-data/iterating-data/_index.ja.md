---
title: Golang経由のC++で列挙子を使用する方法と場所
linktitle: データの反復
type: docs
weight: 55
url: /ja/go-cpp/how-and-where-to-use-enumerators/
description: Aspose.Cells for C++ APIを通じて、C++で列挙子（エナムレーター）の使い方と位置付けを学びます。
keywords: 列挙子の使用方法、セル列挙子、行列挙子、列列挙子
---

{{% alert color="primary" %}}

列挙子は、コンテナまたはコレクションを横断する能力を提供するオブジェクトです。列挙子はコレクション内のデータを読むことができますが、基礎となるコレクションの変更はできません。一方、IEnumerableは、GetEnumeratorメソッドを定義し、IEnumeratorインターフェースを返すインターフェースで、このインターフェースはコレクションへの読み取り専用アクセスを可能にします。

Aspose.CellsのAPIはたくさんの列挙子を提供していますが、この記事では主に以下にリストされている3つのタイプについて説明しています。

1. セル列挙子
1. 行列挙子
1. 列列挙子

{{% /alert %}}

## **列挙子の使用方法**

### **セル列挙子**

セル列挙子へのアクセス方法にはさまざまな方法があり、アプリケーションの要件に基づいてこれらのメソッドのいずれかを使用できます。セル列挙子を返すメソッドは次のとおりです。

1. [**Cells.GetEnumerator**](https://reference.aspose.com/cells/go-cpp/cells/getenumerator/)
1. [**Row.GetEnumerator**](https://reference.aspose.com/cells/go-cpp/row/getenumerator/)
1. [**Range.GetEnumerator**](https://reference.aspose.com/cells/go-cpp/range/getenumerator/)

上記のすべての方法は、初期化されたセルコレクションをトラバースする列挙子を返します。

{{% alert color="primary" %}}

セルをトラバースする際には、コレクションを修正してはいけません（新しいセルを作成する操作や既存のセルを削除する操作）。そうしない場合、列挙子はすべてのセルを正しくトラバースできなくなる可能性があります（一部の要素が繰り返しトラバースされたり、スキップされたりすることがあります）。

{{% /alert %}}

以下のコード例は、CellsコレクションのIEnumeratorインターフェースの実装を示しています。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-IteratingData.go" >}}
### **行列挙子**

行の列挙子は [**RowCollection.GetEnumerator**](https://reference.aspose.com/cells/go-cpp/rowcollection/getenumerator/) メソッドを使用してアクセス可能です。以下のコード例は、[**RowCollection**](https://reference.aspose.com/cells/cpp/aspose.cells/rowcollection/) のための IEnumerator インターフェースの実装を示しています。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-IteratingData-1.go" >}}
### **列の取得**

列は [**ColumnCollection.Get**](https://reference.aspose.com/cells/go-cpp/columncollection/get/) メソッドを使用してアクセス可能です。以下のコード例は、[**ColumnCollection**](https://reference.aspose.com/cells/cpp/aspose.cells/columncollection/) の Get メソッドの実装を示しています。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-IteratingData-2.go" >}}
## **列挙子の使用場所**

列挙子の利点を議論するために、実際の例を使って説明しましょう。

**シナリオ**

特定の [**Worksheet**](https://reference.aspose.com/cells/go-cpp/worksheet/) 内のすべてのセルを走査し、その値を読み取ることがアプリケーションの要件です。これを実現する方法はいくつかあります。以下にいくつか例を示します。

### **表示範囲を使用する**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-IteratingData-3.go" >}}
### **MaxDataRowおよびMaxDataColumnを使用する**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-IteratingData-4.go" >}}
上記のアプローチのそれぞれがほとんど同じロジックを使用していることがわかります。つまり、コレクション内のすべてのセルをループしてセルの値を読み取ります。これにはいくつかの理由で問題が生じる可能性があります。

1. [**GetMaxRow()**](https://reference.aspose.com/cells/go-cpp/cells/getmaxrow/)、[**GetMaxDataRow()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/getmaxdatarow/)、[**GetMaxColumn()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/getmaxcolumn/)、[**GetMaxDataColumn()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/getmaxdatacolumn/)、[**GetMaxDisplayRange()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/getmaxdisplayrange/) などのAPIは、対応する統計情報を収集するのに追加の時間が必要です。行×列のデータマトリックスが大きい場合、これらのAPIを使用するとパフォーマンスに影響を及ぼす可能性があります。
1. ほとんどの場合、指定された範囲内のすべてのセルがインスタンス化されていません。そのような状況では、行列内のすべてのセルを確認することは、初期化されたセルのみを確認する場合と比べて効率的ではありません。
1. Cells row、columnとしてセルにアクセスすることは、範囲内のすべてのセルオブジェクトをインスタンス化することになり、最終的にOutOfMemoryExceptionを引き起こす可能性があります。

## **結論**

上記の事実に基づいて、列挙子を使用すべき可能なシナリオが以下に示されています。

1. セルコレクションの読み取り専用アクセスが必要な場合、つまり、セルの確認のみが必要な場合。
1. 多数のセルを走査する必要がある場合。
1. 初期化されたセル/行/列のみを走査する必要がある場合。
