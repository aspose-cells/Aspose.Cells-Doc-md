---
title: 行と列のコピー
type: docs
weight: 30
url: /ja/java/copying-rows-and-columns/
---

## **紹介**
時には、ワークシート全体をコピーせずに行や列をコピーする必要があります。Aspose.Cellsを使用すると、ワークブック内またはワークブック間で行や列をコピーすることができます。

行（または列）をコピーすると、それに含まれるデータ（更新された参照を含む数式、値、コメント、書式設定、非表示セル、画像、その他の図形オブジェクトなど）がコピーされます。
## **Microsoft Excelで行と列をコピーする**
1. コピーしたい行または列を選択します。
1. 行または列をコピーする場合は、**標準**ツールバーの**コピー**をクリックするか、**CTRL**+**C**を押します。
1. コピーする選択範囲の下または右側に行または列を選択します。
1. 行または列をコピーする際に、**挿入**メニューで**コピーしたセル**をクリックします。

{{% alert color="primary" %}} 

**標準**ツールバーの**貼り付け**をクリックするか、**Insert**メニューのコマンドをクリックする代わりに**CTRL**+**V**を押すと、宛先セルの内容が置き換えられます。

{{% /alert %}} 

## **単一行のコピー**

Aspose.Cellsは、[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)クラスの[copyRow](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyRow-com.aspose.cells.Cells-int-int-) メソッドを提供します。このメソッドは、式、値、コメント、セルの書式設定、非表示セル、画像、その他の描画オブジェクトなど、あらゆるタイプのデータをソース行から宛先行へコピーします。

[copyRow](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyRow-com.aspose.cells.Cells-int-int-) メソッドは、次のパラメータを取ります：

- ソースの[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) オブジェクト,
- ソースの行インデックス、および
- 宛先の行インデックス。

このメソッドを使って、シート内または別のシートに行をコピーします。[copyRow](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyRow-com.aspose.cells.Cells-int-int-) はMicrosoft Excelと同様に動作します。たとえば、宛先行の高さを明示的に設定する必要はありません、その値もコピーされるからです。

以下の例は、ワークシート内の行をコピーする方法を示しています。テンプレートのMicrosoft Excelファイルを使用し、2番目の行（データ、書式設定、コメント、画像などを含む）を12番目の行に貼り付けます。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-CopyingRows-CopyingRows.java" >}}



以下は、以下のコードを実行した際の出力です。

**最高度の精度と正確さで行がコピーされます** 

![todo:image_alt_text](copying-rows-and-columns_1.png)

{{% alert color="primary" %}} 

行をコピーする際は、関連する画像、グラフ、またはその他の描画オブジェクトに注目することが重要です。これはMicrosoft Excelと同じです。

1. もしソース行インデックスが5であれば、画像、グラフなどはその3行に含まれている場合にコピーされます（開始行インデックスが4で終了行インデックスが6の場合）。
1. 宛先行にある既存の画像やグラフなどは削除されません。

{{% /alert %}} 

## **複数の行のコピー**

追加の整数型のパラメータを指定する[**Cells.copyRows**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyRow-com.aspose.cells.Cells-int-int-) メソッドを使用して、新しい宛先に複数の行をコピーすることもできます。

以下は、3行のデータを含む入力スプレッドシートのスナップショットですが、以下に提供されているコードスニペットは、すべての3行を7行から始まる新しい場所にコピーします。

![todo:image_alt_text](copy-rows-and-columns_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CopyingMultipleRows-CopyingMultipleRows.java" >}}

上記のコードスニペットを実行した後の結果のスプレッドシートビューは次のようになります。

![todo:image_alt_text](copy-rows-and-columns_4.png)

## **単一列のコピー**

Aspose.Cellsは、[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)クラスの[copyColumn](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyColumn-com.aspose.cells.Cells-int-int-) メソッドを提供します。このメソッドは、式（更新された参照を含む）、値、コメント、セルの書式設定、非表示セル、画像、その他の描画オブジェクトなど、すべてのタイプのデータをソース列から宛先列へコピーします。

[copyColumn](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyColumn-com.aspose.cells.Cells-int-int-) メソッドは、以下のパラメータを取ります：

- ソースの[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) オブジェクト,
- ソースの列インデックス、および
- 宛先の列インデックス。

シート内または他のシートに列をコピーするには、[copyColumn](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyColumn-com.aspose.cells.Cells-int-int-) メソッドを使用します。

この例では、ワークシートから列をコピーして別のブック内のワークシートに貼り付けます。

**列を別のワークブックにコピーする** 

![todo:image_alt_text](copying-rows-and-columns_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-CopyingColumns-CopyingColumns.java" >}}

## **複数の列をコピー**

[**Cells.copyRows**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyRow-com.aspose.cells.Cells-int-int-)メソッドと同様に、Aspose.CellsのAPIは新しい位置に複数のソース列をコピーするための[**Cells.copyColumns**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyColumns-com.aspose.cells.Cells-int-int-int-)メソッドも提供しています。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CopyingMultipleColumns-CopyingMultipleColumns.java" >}}

以下は、Excelでのソースと結果のスプレッドシートの見え方です。

![todo:image_alt_text](copy-rows-and-columns_7.png)

![todo:image_alt_text](copy-rows-and-columns_8.png)


## **貼り付けオプションを使用して行/列を貼り付ける**
Aspose.Cellsは、関数 [CopyRows](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyRows-com.aspose.cells.Cells-int-int-int-com.aspose.cells.CopyOptions-com.aspose.cells.PasteOptions-) と [CopyColumns](https://reference.aspose.com/cells/java/com.aspose.cells/cells#copyColumns-com.aspose.cells.Cells-int-int-int-com.aspose.cells.PasteOptions-) を使用する際に [PasteOptions](https://reference.aspose.com/cells/java/com.aspose.cells/PasteOptions) を提供します。これにより、Excelと類似した貼り付けオプションを設定可能です。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-PastingDataWithPasteOptions.java" >}}

{{< app/cells/assistant language="java" >}}
