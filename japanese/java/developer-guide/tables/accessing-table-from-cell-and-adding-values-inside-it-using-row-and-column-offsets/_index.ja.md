---
title: Cell からテーブルにアクセスし、行と列のオフセットを使用してテーブル内に値を追加する
type: docs
weight: 110
url: /ja/java/accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets/
---
{{% alert color="primary" %}}

通常、次を使用してテーブルまたはリスト オブジェクト内に値を追加します。[**Cell.putValue()**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#putValue(boolean)） 方法。ただし、場合によっては、行と列のオフセットを使用して、テーブルまたはリスト オブジェクト内に値を追加する必要がある場合があります。

セルからテーブルまたはリスト オブジェクトにアクセスするには、[**Cell.getTable()**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getTable() ） 方法。行と列のオフセットを使用して内部に値を追加するには、[**ListObject.putCellValue(rowOffset,columnOffset,value)**](https://reference.aspose.com/cells/java/com.aspose.cells/listobject#putCellValue(int,%20int,%20java.lang.Object)） 方法。

{{% /alert %}}

## 例

### ソース ファイルと出力ファイルを比較するスクリーンショット

次のスクリーンショットは、コード内で使用されるソース Excel ファイルを示しています。空のテーブルが含まれており、テーブル内にあるセル D5 が強調表示されています。を使用して、セル D5 からこのテーブルにアクセスします。[**Cell.getTable()**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getTable() ) メソッドを使用して、その中に値を追加します。[**Cell.putValue()**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#putValue(boolean) ） と[**ListObject.putCellValue(rowOffset,columnOffset,value)**](https://reference.aspose.com/cells/java/com.aspose.cells/listobject#putCellValue(int,%20int,%20java.lang.Object)メソッド。

![todo:画像_代替_文章](accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets_1.png)

次のスクリーンショットは、コードによって生成された出力 Excel ファイルを示しています。ご覧のとおり、セル D5 には値があり、テーブルのオフセット 2,2 にあるセル F6 には値があります。

![todo:画像_代替_文章](accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets_2.png)

### Java セルからテーブルにアクセスし、行と列のオフセットを使用してその中に値を追加するコード

次のサンプル コードは、上記のスクリーンショットに示すようにソース Excel ファイルを読み込み、テーブル内に値を追加して、上記のように出力 Excel ファイルを生成します。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-AccessingTablefromCell-AccessingTablefromCell.java" >}}
