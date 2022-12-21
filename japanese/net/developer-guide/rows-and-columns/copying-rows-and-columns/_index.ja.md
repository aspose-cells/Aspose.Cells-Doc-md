---
title: 行と列のコピー
type: docs
weight: 40
url: /ja/net/copying-rows-and-columns/
---
## **序章**

ワークシート全体をコピーせずに、ワークシートの行と列をコピーする必要がある場合があります。 Aspose.Cells を使用すると、ブック内またはブック間で行と列をコピーできます。
行 (または列) がコピーされると、そこに含まれるデータ (参照が更新された数式を含む) と、値、コメント、書式設定、非表示のセル、画像、およびその他の描画オブジェクトもコピーされます。

## **Microsoft Excel で行と列をコピーする**

1. コピーする行または列を選択します。
1. 行または列をコピーするには、**コピー**上で**標準**ツールバー、または**CTRL**+**C**.
1. 選択範囲をコピーする場所の下または右にある行または列を選択します。
1. 行または列をコピーする場合は、**Cellsをコピーしました**上で**入れる**メニュー。

{{% alert color="primary" %}}

クリックすると**ペースト**上で**標準**ツールバーまたはプレス**CTRL**+**V** のコマンドをクリックする代わりに**挿入** メニューでは、挿入先セルの内容がすべて置き換えられます。

{{% /alert %}}

## **Microsoft Excel で貼り付けオプションを使用して行と列を貼り付ける**

1. コピーするデータまたはその他の属性を含むセルを選択します。
1.  [ホーム] タブで、**コピー**.
1. 目的の領域の最初のセルをクリックします。**ペースト**あなたがコピーしたもの。
1.  [ホーム] タブで、**ペースト**を選択し、**ペースト**特別な。
1. を選択**オプション**あなたがしたい。

## **Aspose.Cells を使用**

## **単一行のコピー**

Aspose.Cells は[**行のコピー**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copyrow)の方法[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)クラス。このメソッドは、数式、値、コメント、セル形式、非表示のセル、画像、およびその他の描画オブジェクトを含むすべての種類のデータをソース行から宛先行にコピーします。

の[**行のコピー**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copyrow)メソッドは次のパラメータを取ります。

- 起源[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)物体、
- ソース行インデックス、および
- 宛先行インデックス。

このメソッドを使用して、シート内の行をコピーするか、別のシートにコピーします。の[**行のコピー**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copyrow)メソッドは、Microsoft Excel と同様に機能します。したがって、たとえば、宛先行の高さを明示的に設定する必要はありません。その値もコピーされます。

次の例は、ワークシートの行をコピーする方法を示しています。テンプレート Microsoft の Excel ファイルを使用し、2 行目を (データ、書式設定、コメント、画像などを含めて) コピーし、同じワークシートの 12 行目に貼り付けます。

を使用してソース行の高さを取得するステップをスキップできます。[**Cells.GetRowHeight**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/getrowheight)メソッドを使用して、目的の行の高さを設定します。[**Cells.SetRowHeight**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/setrowheight)メソッドとして[**行のコピー**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copyrow)メソッドは行の高さを自動的に処理します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Copying-CopyingRows-1.cs" >}}

{{% alert color="primary" %}}

行をコピーするときは、関連する画像、チャート、またはその他の描画オブジェクトに注意することが重要です。これは Microsoft Excel と同じです。

1. ソース行インデックスが 5 の場合、イメージ、チャートなどが 3 つの行に含まれていればコピーされます (開始行インデックスは 4、終了行インデックスは 6)。
1. 宛先行の既存の画像、チャートなどは削除されません。

{{% /alert %}}

## **複数行のコピー**

を使用しながら、複数の行を新しい宛先にコピーすることもできます。[**Cells.CopyRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copyrows/index)コピーするソース行の数を指定する整数型の追加パラメータを取るメソッド。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CopyRowsColumns-CopyingMultipleRows-1.cs" >}}


## **列のコピー**

Aspose.Cells は[**コピー列**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copycolumn)の方法[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)クラスの場合、このメソッドは、数式 (更新された参照を含む) および値、コメント、セル形式、非表示のセル、画像、およびその他の描画オブジェクトを含むすべての種類のデータをソース列から宛先列にコピーします。

の[**コピー列**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copycolumn)メソッドは次のパラメータを取ります。

- 起源[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)物体、
- ソース列インデックス、および
- 宛先列のインデックス。

使用[**コピー列**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copycolumn)シート内または別のシートに列をコピーするメソッド。

次の使用例は、ワークシートから列をコピーし、別のブックのワークシートに貼り付けます。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Copying-CopyingColumns-1.cs" >}}

## **複数の列のコピー**

に似ている[**Cells.CopyRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copyrows/index)メソッド、Aspose.Cells API は、[**Cells.CopyColumns**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/copycolumns/index)複数のソース列を新しい場所にコピーするためのメソッド。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CopyRowsColumns-CopyingMultipleColumns-1.cs" >}}


## **貼り付けオプションを使用した行/列の貼り付け**

Aspose.Cells が提供するようになりました[**貼り付けオプション**](https://reference.aspose.com/cells/net/aspose.cells/pasteoptions)関数の使用中[**行のコピー**](https://reference.aspose.com/cells/net/aspose.cells.cells/copyrows/methods/2)と[**コピー列**](https://reference.aspose.com/cells/net/aspose.cells.cells/copycolumns/methods/1). Excel と同様に、適切な貼り付けオプションを設定できます。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Copying-PastingRowsColumnsWithPasteOptions-1.cs" >}}

