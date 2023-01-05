---
title: GridWeb の行と列をコピーする
type: docs
weight: 80
url: /ja/net/copy-gridweb-rows-and-columns/
---
{{% alert color="primary" %}} 

Aspose.Cells.GridWeb コンポーネントは、GridCells クラスを使用しながら行と列をコピーする手段を提供します。この記事では、Aspose.Cells.GridWeb によって公開された API を使用して、GridWeb インターフェイスで行と列をコピーする方法を示します。

GridCells.CopyRow、GridCells.CopyColumn、GridCells.CopyRows、および GridCells.CopyColumns メソッドは、コンテンツ、スタイリング、数式をソースの行と列からコピー先にコピーします。

{{% /alert %}} 
## **行と列のコピー**
Aspose.Cells.GridWeb コンポーネントについてまだよく知らない場合は、[Aspose.Cells.GridWebのご紹介](https://docs.aspose.com/cells/net/browsers-capabilities/)および詳細な記事[Aspose.Cells.GridWeb コンポーネントを WebForms アプリケーションに追加する方法](https://docs.aspose.com/cells/net/add-gridweb-to-web-form/).
### **単一行のコピー**
例を単純にするために、この記事では 1 行の既存のスプレッドシートと、その行のすべての値を合計する単純な数式を使用します。行をコピーする前に、スプレッドシートが Aspose.Cells.GridWeb インターフェイスにどのように表示されるかを次に示します。

![todo:画像_代替_文章](copy-gridweb-rows-and-columns_1.png)

コード スニペットは、以下に示すように単純です。アクティブなワークシート順序の GridCells オブジェクトにアクセスして、最初の行を次の行にコピーします。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-CopyRowsColumns.aspx-CopyRow.cs" >}}


行のコピー操作後に Aspose.Cells.GridWeb がどのように見えるかを次に示します。

![todo:画像_代替_文章](copy-gridweb-rows-and-columns_2.png)
### **単一列のコピー**
次の例では、1 つの列と列内のすべての値を合計する単純な数式を含む既存のスプレッドシートを使用します。列をコピーする前に、スプレッドシートが Aspose.Cells.GridWeb インターフェイスにどのように表示されるかを次に示します。

![todo:画像_代替_文章](copy-gridweb-rows-and-columns_3.png)

上記の例と同様に、次のコード スニペットは、アクティブなワークシート順序の GridCells オブジェクトにアクセスして、最初の列のコピーを後続の列に作成します。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-CopyRowsColumns.aspx-CopyColumn.cs" >}}



列のコピー操作後の Aspose.Cells.GridWeb の外観を次に示します。

![todo:画像_代替_文章](copy-gridweb-rows-and-columns_4.png)

{{% alert color="primary" %}} 

ループ内で GridCells.CopyRow および GridCells.CopyColumn メソッドを使用して、ソースの行と列をそれぞれ複数の行と列にコピーできます。

{{% /alert %}} 
### **複数行のコピー**
GridCells.CopyRows メソッドを使用して、複数の行を新しい宛先にコピーすることもできます。このメソッドは、整数型の追加パラメーターを使用して、コピーするソース行の数を指定します。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-CopyRowsColumns.aspx-CopyMultipleRows.cs" >}}



行のコピー操作の前後に Aspose.Cells.GridWeb がどのように見えるかを次に示します。

![todo:画像_代替_文章](copy-gridweb-rows-and-columns_5.png)

![todo:画像_代替_文章](copy-gridweb-rows-and-columns_6.png)
### **複数の列のコピー**
GridCells クラスは CopyColumns メソッドも提供します。このメソッドは、整数型の追加パラメーターを使用して、コピーするソース列の数を指定します。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-CopyRowsColumns.aspx-CopyMultipleColumns.cs" >}}



行のコピー操作の前後に Aspose.Cells.GridWeb がどのように見えるかを次に示します。

![todo:画像_代替_文章](copy-gridweb-rows-and-columns_7.png)

![todo:画像_代替_文章](copy-gridweb-rows-and-columns_8.png)
