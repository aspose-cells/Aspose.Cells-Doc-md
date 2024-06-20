---
title: イテレータの使用方法と場所
linktitle: データの反復
type: docs
weight: 640
url: /ja/java/how-and-where-to-use-iterators/
---

{{% alert color="primary" %}} 

イテレータ インターフェースのオブジェクトを使用してコレクションのすべての要素を反復処理できます。イテレータはコレクションのデータを調査するために使用できますが、基礎となるコレクションを変更することはできません。一般的に、コレクションの内容をサイクルさせるためにイテレータを使用するには、以下の手順を実行する必要があります：

1. コレクションの iterator メソッドを呼び出して、コレクションの先頭に対するイテレータを取得します。
1. hasNext メソッドを呼び出して続行するループを設定します。hasNext メソッドが true を返す限り、ループを繰り返します。
1. ループ内で、next メソッドを呼び出してそれぞれの要素を取得します。

Aspose.Cells API は多くのイテレータを提供していますが、この記事では主に以下にリストされている 3 種類について説明します。

1. セル イテレータ
1. 行 イテレータ
1. 列 イテレータ

{{% /alert %}} 
## **反復子の使用方法**
### **セル反復子**
セルの反復子にアクセスする方法はさまざまであり、アプリケーションの要件に基づいてこれらの方法のいずれかを使用することができます。 以下に、セルの反復子を返すメソッドが示されています。

1. Cells.iterator
1. Row.iterator
1. Range.iterator

上記のすべての方法は、初期化されたセルのコレクションを走査することを可能にする反復子を返します。

{{% alert color="primary" %}} 

セルを走査する際、コレクションを変更してはいけません（新しいセルを生成する操作や既存のセルを削除する操作を行ってはいけません）。そうでないと、反復子がすべてのセルを正しく走査できない場合があります（一部の要素が繰り返し走査されたり、スキップされたりする可能性があります）。

{{% /alert %}} 

次のコード例は、セルコレクションの反復子の実装を示しています。







{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CellsIterator-CellsIterator.java" >}}




##### **行の反復子**
RowCollection.iterator メソッドを使用すると、行の反復子にアクセスできます。 以下のコード例は、RowCollection クラスの反復子の実装を示しています。





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-RowsIterator-RowsIterator.java" >}}




##### **列の反復子**
ColumnCollection.iterator メソッドを使用すると、列の反復子にアクセスできます。 以下のコード例は、ColumnCollection クラスの反復子の実装を示しています。





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ColumnsIterator-ColumnsIterator.java" >}}




#### **反復子の使用場所**
反復子を使用する利点について議論するために、実際の例を取り上げましょう。
##### **シナリオ**
アプリケーションの要件は、指定されたワークシート内のすべてのセルを走査してそれらの値を読むことです。 この目標を実装するためのいくつかの方法があります。 そのうちのいくつかを以下で示します。
###### **表示範囲を使用する**




{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-UsingDisplayRange-UsingDisplayRange.java" >}}




###### **MaxDataRowおよびMaxDataColumnを使用する**




{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-UsingMaxDataRowAndMaxDataColumn-UsingMaxDataRowAndMaxDataColumn.java" >}}





上記の2つのアプローチともに、コレクション内のすべてのセルをループしてセルの値を読み取るというロジックを使用していることがわかります。 以下で説明する理由により、これはいくつかの理由で問題があるかもしれません。

1. MaxRow、MaxDataRow、MaxColumn、MaxDataColumn、および MaxDisplayRange などの API は、対応する統計情報を収集するための余分な時間を要求します。 データマトリックス（行×列）が大きい場合、これらの API を使用するとパフォーマンスにペナルティが課せられる可能性があります。
1. ほとんどの場合、指定された範囲内のすべてのセルがインスタンス化されていません。そのような状況では、行列内のすべてのセルを確認することは、初期化されたセルのみを確認する場合と比べて効率的ではありません。
3. Cells.get(rowIndex, columnIndex) をループ内でアクセスすると、範囲内のすべてのセルオブジェクトが初期化されるため、最終的に OutOfMemoryError が発生する可能性があります。
##### **結論**
上記の事実に基づいて、反復子を使用すべき可能性のあるシナリオは次のとおりです。

1. セルコレクションの読み取り専用アクセスが必要な場合、つまり、セルを検査するだけの要求がある場合。
2. 多数のセルを走査する必要がある場合。
3. 初期化されたセル/行/列のみを走査する必要がある場合。
