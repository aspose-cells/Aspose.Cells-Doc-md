---
title: 行と列のコピー
type: docs
weight: 30
url: /ja/java/copying-rows-and-columns/
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

## **単一行のコピー**

Aspose.Cells は[copyRow](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyRow\(com.aspose.cells.Cells,%20int,%20int\) ) の方法[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)クラス。このメソッドは、数式、値、コメント、セル形式、非表示のセル、画像、およびその他の描画オブジェクトを含むすべての種類のデータをソース行から宛先行にコピーします。

の[copyRow](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyRow\(com.aspose.cells.Cells,%20int,%20int\)メソッドは、次のパラメーターを取ります。

- 起源[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)物体、
- ソース行インデックス、および
- 宛先行インデックス。

このメソッドを使用して、シート内の行をコピーするか、別のシートにコピーします。の[copyRow](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyRow\(com.aspose.cells.Cells,%20int,%20int\)メソッドは、Microsoft Excel と同様に機能します。したがって、たとえば、宛先行の高さを明示的に設定する必要はありません。その値もコピーされます。

次の例は、ワークシートの行をコピーする方法を示しています。テンプレート Microsoft の Excel ファイルを使用し、2 行目を (データ、書式設定、コメント、画像などを含めて) コピーし、同じワークシートの 12 行目に貼り付けます。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-CopyingRows-CopyingRows.java" >}}



以下のコードを実行すると、次の出力が生成されます。

**行は最高の精度と精度でコピーされます** 

![todo:画像_代替_文章](copying-rows-and-columns_1.png)

{{% alert color="primary" %}} 

行をコピーするときは、関連する画像、チャート、またはその他の描画オブジェクトに注意することが重要です。これは Microsoft Excel と同じです。

1. ソース行インデックスが 5 の場合、イメージ、チャートなどが 3 つの行に含まれていればコピーされます (開始行インデックスは 4、終了行インデックスは 6)。
1. 宛先行の既存の画像、チャートなどは削除されません。

{{% /alert %}} 

## **複数行のコピー**

を使用しながら、複数の行を新しい宛先にコピーすることもできます。[**Cells.copyRows**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyRow(com.aspose.cells.Cells,%20int,%20int)) コピーするソース行の数を指定する整数型の追加パラメータを取るメソッド。

以下は、3 行のデータを含む入力スプレッドシートのスナップショットですが、以下に示すコード スニペットは、7 行目から始まる新しい場所に 3 行すべてをコピーします。

![todo:画像_代替_文章](copy-rows-and-columns_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CopyingMultipleRows-CopyingMultipleRows.java" >}}

上記のコード スニペットを実行した結果のスプレッドシート ビューを次に示します。

![todo:画像_代替_文章](copy-rows-and-columns_4.png)

## **単一列のコピー**

Aspose.Cells は[コピー列](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyColumn\(com.aspose.cells.Cells,%20int,%20int\) ) の方法[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)クラスの場合、このメソッドは、数式 (更新された参照を含む) および値、コメント、セル形式、非表示のセル、画像、およびその他の描画オブジェクトを含むすべての種類のデータをソース列から宛先列にコピーします。

の[コピー列](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyColumn\(com.aspose.cells.Cells,%20int,%20int\)メソッドは、次のパラメーターを取ります。

- 起源[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)物体、
- ソース列インデックス、および
- 宛先列のインデックス。

使用[コピー列](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyColumn\(com.aspose.cells.Cells,%20int,%20int\)) メソッドを使用して、シート内または別のシートに列をコピーします。

次の使用例は、ワークシートから列をコピーし、別のブックのワークシートに貼り付けます。

**あるワークブックから別のワークブックに列がコピーされる** 

![todo:画像_代替_文章](copying-rows-and-columns_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-CopyingColumns-CopyingColumns.java" >}}

## **複数の列のコピー**

に似ている[**Cells.copyRows**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyRow(com.aspose.cells.Cells,%20int,%20int) メソッド、Aspose.Cells API は、[**Cells.copyColumns**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyColumns(com.aspose.cells.Cells,%20int,%20int,%20int)) メソッドを使用して、複数のソース列を新しい場所にコピーします。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CopyingMultipleColumns-CopyingMultipleColumns.java" >}}

ソースと結果のスプレッドシートが Excel でどのように表示されるかを次に示します。

![todo:画像_代替_文章](copy-rows-and-columns_7.png)

![todo:画像_代替_文章](copy-rows-and-columns_8.png)


## **貼り付けオプションを使用した行/列の貼り付け**
Aspose.Cells が提供するようになりました[貼り付けオプション](https://reference.aspose.com/cells/java/com.aspose.cells/PasteOptions)関数の使用中[行のコピー](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyRows\(com.aspose.cells.Cells,%20int,%20int,%20int,%20com.aspose.cells.CopyOptions,%20com.aspose.cells.PasteOptions\) ） と[コピー列](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyColumns\(com.aspose.cells.Cells,%20int,%20int,%20int,%20com.aspose.cells.PasteOptions\)）。 Excel と同様に、適切な貼り付けオプションを設定できます。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-PastingDataWithPasteOptions.java" >}}

