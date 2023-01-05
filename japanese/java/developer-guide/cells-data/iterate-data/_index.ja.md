---
title: イテレータの使用方法と使用場所
linktitle: データの反復
type: docs
weight: 640
url: /ja/java/how-and-where-to-use-iterators/
---
{{% alert color="primary" %}} 

イテレータ インターフェイスのオブジェクトを使用して、コレクションのすべての要素をトラバースできます。反復子を使用してコレクション内のデータを検査することはできますが、基になるコレクションを変更するために使用することはできません。一般に、反復子を使用してコレクションの内容を循環するには、次の手順を実行する必要があります。

1. コレクションの iterator メソッドを呼び出して、コレクションの先頭への反復子を取得します。
1. hasNext メソッドを呼び出すループを設定します。 hasNext メソッドが true を返す限り、ループを繰り返します。
1. ループ内で、next メソッドを呼び出して各要素を取得します。

Aspose.Cells API には多数のイテレータが用意されていますが、この記事では主に以下に示す 3 つのタイプについて説明します。

1. Cells イテレータ
1. 行反復子
1. 列イテレータ

{{% /alert %}} 
## **イテレータの使い方**
### **Cells イテレータ**
セルの反復子にアクセスするにはさまざまな方法があり、アプリケーションの要件に基づいてこれらの方法のいずれかを使用できます。セルの反復子を返すメソッドは次のとおりです。

1. Cells.iterator
1. Row.iterator
1. Range.iterator

上記のメソッドはすべて、初期化されたセルのコレクションをトラバースできるイテレータを返します。

{{% alert color="primary" %}} 

セルをトラバースしている間は、コレクションを変更しないでください (新しい Cell がインスタンス化されるか、既存の Cell が削除される操作)。そうしないと、反復子がすべてのセルを正しくトラバースできない場合があります (一部の要素が繰り返しトラバースされるか、スキップされる可能性があります)。

{{% /alert %}} 

次のコード例は、セル コレクションの Iterator クラスの実装を示しています。







{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CellsIterator-CellsIterator.java" >}}




##### **行反復子**
Rows Iterator は、RowCollection.iterator メソッドの使用中にアクセスできます。次のコード例は、RowCollection クラスの Iterator の実装を示しています。





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-RowsIterator-RowsIterator.java" >}}




##### **列イテレータ**
ColumnCollection.iterator メソッドの使用中に、Columns Iterator にアクセスできます。次のコード例は、ColumnCollection クラスの Iterator の実装を示しています。





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ColumnsIterator-ColumnsIterator.java" >}}




#### **イテレータを使用する場所**
イテレータを使用する利点を説明するために、リアルタイムの例を見てみましょう。
##### **シナリオ**
アプリケーションの要件は、特定のワークシート内のすべてのセルをトラバースしてそれらの値を読み取ることです。この目標を実現するには、いくつかの方法があります。いくつかを以下に示します。
###### **表示範囲の使用**




{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-UsingDisplayRange-UsingDisplayRange.java" >}}




###### **MaxDataRow と MaxDataColumn の使用**




{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-UsingMaxDataRowAndMaxDataColumn-UsingMaxDataRowAndMaxDataColumn.java" >}}





上記のアプローチの両方が多かれ少なかれ類似したロジックを使用していることがわかります。コレクション内のすべてのセルをループして、セルの値を読み取ります。これは、以下で説明するように、いくつかの理由で問題になる可能性があります。

1. MaxRow、MaxDataRow、MaxColumn、MaxDataColumn、MaxDisplayRange などの API は、対応する統計を収集するために余分な時間を必要とします。データ マトリックス (行 x 列) が大きい場合、これらの API を使用すると、パフォーマンスが低下する可能性があります。
1. ほとんどの場合、特定の範囲内のすべてのセルがインスタンス化されるわけではありません。このような状況では、マトリックス内のすべてのセルをチェックすることは、初期化されたセルのみをチェックする場合に比べて効率的ではありません。
1. Cells.get(rowIndex, columnIndex) としてループ内のセルにアクセスすると、範囲内のすべてのセル オブジェクトがインスタンス化され、最終的に OutOfMemoryError が発生する可能性があります。
##### **結論**
上記の事実に基づいて、イテレータを使用する必要があるシナリオを次に示します。

1. セル コレクションの読み取り専用アクセスが必要です。要件は、セルのみを検査することです。
1. 多数のセルが横断されます。
1. 初期化されたセル/行/列のみがトラバースされます。
