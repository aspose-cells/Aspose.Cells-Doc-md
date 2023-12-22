---
title: 行と列のコピー
type: docs
weight: 40
url: /ja/net/copying-rows-and-columns/
description: この記事では、Aspose.Cells for .NET API を通じて行と列をコピーする方法を説明します。
keywords: C# How to Copy Rows and Columns, Copy Rows in C#, Copy Columns using C#, How to Paste Rows and Columns using Aspose.Cells for .NET, Paste multiple rows and columns, How to Copy and paste Single Row or Column.
---
##  **導入**

場合によっては、ワークシート全体をコピーせずに、ワークシート内の行と列をコピーする必要があります。 Aspose.Cells を使用すると、ワークブック内またはワークブック間で行と列をコピーできます。
行 (または列) がコピーされると、そこに含まれるデータ (更新された参照を含む数式、値、コメント、書式設定、非表示セル、画像、その他の描画オブジェクトなど) もコピーされます。

##  **Microsoft Excel で行と列をコピーする方法**

1. コピーする行または列を選択します。
1. 行または列をコピーするには、**コピー**で**標準**ツールバー、または を押します**CTRL**+*C**。
1. 選択内容をコピーする場所の下または右にある行または列を選択します。
1. 行または列をコピーするときに、**Cellsをコピーしました**で**入れる**メニュー。

{{% alert color="primary" %}}

クリックすると**ペースト**で**標準**ツールバーまたはプレス**CTRL**+****挿入のコマンドをクリックする代わりに V****メニューでは、宛先セルの内容はすべて置き換えられます。

{{% /alert %}}

##  **Microsoft Excel で貼り付けオプションを使用して行と列を貼り付ける方法**

1. コピーするデータまたはその他の属性を含むセルを選択します。
1. [ホーム] タブで、[*コピー**] をクリックします。
1. 表示したい領域の最初のセルをクリックします。**ペースト**コピーしたもの。
1.  [ホーム] タブで、次の矢印をクリックします。**貼り付け**し、**貼り付けを選択します**特別。
1. を選択**オプション**あなたが欲しいのです。

##  **Aspose.Cells for .NET を使用して行と列をコピーする方法**

##  **単一行をコピーする方法**

 Aspose.Cells は、[**コピー行**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copyrow)の方法[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)クラス。このメソッドは、数式、値、コメント、セル形式、非表示セル、画像、その他の描画オブジェクトを含むすべての種類のデータをソース行から宛先行にコピーします。

の[**コピー行**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copyrow)メソッドは次のパラメータを受け取ります。

- 起源[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)物体、
- ソース行インデックス、および
- 宛先行インデックス。

このメソッドを使用して、シート内の行をコピーしたり、別のシートに行をコピーしたりできます。の[**コピー行**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copyrow)このメソッドは Microsoft Excel と同様に機能します。したがって、たとえば、宛先行の高さを明示的に設定する必要はなく、その値もコピーされます。

次の例は、ワークシート内の行をコピーする方法を示しています。テンプレート Microsoft Excel ファイルを使用し、2 行目 (データ、書式設定、コメント、画像などを含む) をコピーし、同じワークシートの 12 行目に貼り付けます。

を使用して、ソース行の高さを取得するステップをスキップできます。[**Cells.GetRowHeight**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/getrowheight)メソッドを使用して宛先行の高さを設定します。[**Cells.SetRowHeight**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/setrowheight)としてのメソッド[**コピー行**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copyrow)このメソッドは行の高さを自動的に処理します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Copying-CopyingRows-1.cs" >}}

{{% alert color="primary" %}}

行をコピーするときは、関連する画像、グラフ、またはその他の描画オブジェクトに注意することが重要です。これは Microsoft Excel でも同様です。

1. ソース行インデックスが 5 の場合、画像やグラフなどが 3 つの行 (開始行インデックスは 4、終了行インデックスは 6) に含まれていればコピーされます。
1. 宛先行にある既存の画像、グラフなどは削除されません。

{{% /alert %}}

##  **複数の行をコピーする方法**

を使用しながら、複数の行を新しい宛先にコピーすることもできます。[**Cells.CopyRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copyrows/index)このメソッドは、整数型の追加パラメータを取得して、コピーするソース行の数を指定します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CopyRowsColumns-CopyingMultipleRows-1.cs" >}}


##  **列をコピーする方法**

 Aspose.Cells は、[**列のコピー**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copycolumn)の方法[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)クラスの場合、このメソッドは、更新された参照を含む数式、値、コメント、セル形式、非表示セル、画像、その他の描画オブジェクトを含むすべての種類のデータをソース列から宛先列にコピーします。

の[**列のコピー**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copycolumn)メソッドは次のパラメータを受け取ります。

- 起源[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)物体、
- ソース列インデックス、および
- 宛先列のインデックス。

使用[**列のコピー**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copycolumn)シート内または別のシートに列をコピーするメソッド。

この例では、ワークシートから列をコピーし、別のブックのワークシートに貼り付けます。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Copying-CopyingColumns-1.cs" >}}

##  **複数の列をコピーする方法**

に似ている[**Cells.CopyRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copyrows/index)メソッドと同様に、Aspose.Cells API は[**Cells.CopyColumns**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copycolumns/index)メソッドを使用して、複数のソース列を新しい場所にコピーします。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CopyRowsColumns-CopyingMultipleColumns-1.cs" >}}


##  **貼り付けオプションを使用して行と列を貼り付ける方法**

 Aspose.Cells が提供するようになりました[**貼り付けオプション**](https://reference.aspose.com/cells/net/aspose.cells/pasteoptions)機能使用時[**行のコピー**](https://reference.aspose.com/cells/net/aspose.cells.cells/copyrows/methods/2)そして[**列のコピー**](https://reference.aspose.com/cells/net/aspose.cells.cells/copycolumns/methods/1)。 Excel と同様に、適切な貼り付けオプションを設定できます。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Copying-PastingRowsColumnsWithPasteOptions-1.cs" >}}

