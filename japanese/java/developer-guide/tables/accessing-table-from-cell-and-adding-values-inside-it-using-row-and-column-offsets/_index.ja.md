---
title: セルからテーブルにアクセスし、行と列のオフセットを使用して値を追加する
type: docs
weight: 110
url: /ja/java/accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets/
---

{{% alert color="primary" %}}

通常、テーブルまたはリストオブジェクト内に値を追加する場合は [**Cell.putValue()**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#putValue(boolean)) メソッドを使用します。ただし、時々、行と列のオフセットを使用してテーブルまたはリストオブジェクト内に値を追加する必要があることがあります。

セルからテーブルまたはリストオブジェクトにアクセスするには、[**Cell.getTable()**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getTable--)メソッドを使用します。そして、行と列のオフセットを使用して内部に値を追加するには、[**ListObject.putCellValue(rowOffset,columnOffset,value)**](https://reference.aspose.com/cells/java/com.aspose.cells/listobject#putCellValue(int,%20int,%20java.lang.Object))メソッドを使用します。

{{% /alert %}}

## 例

### ソースファイルと出力ファイルの比較のスクリーンショット

以下のスクリーンショットは、コード内で使用されるソースエクセルファイルを示しています。空のテーブルが含まれ、テーブル内にあるセル D5 が強調表示されています。このテーブルにセル D5 から [**Cell.getTable()**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getTable--) メソッドを使用してアクセスし、その後、[**Cell.putValue()**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#putValue(boolean)) および [**ListObject.putCellValue(rowOffset,columnOffset,value)**](https://reference.aspose.com/cells/java/com.aspose.cells/listobject#putCellValue(int,%20int,%20java.lang.Object)) メソッドを使用してその内部に値を追加します。

![todo:image_alt_text](accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets_1.png)

以下のスクリーンショットは、コードによって生成された出力エクセルファイルを示しています。セル D5 に値が設定されており、テーブル内のオフセット 2,2 のセル F6 にも値が設定されています。

![todo:image_alt_text](accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets_2.png)

### セルからテーブルにアクセスし、行と列のオフセットを使用して値を追加するためのJavaコード

以下のサンプルコードは、上記のスクリーンショットに示されているソースエクセルファイルを読み込み、テーブル内に値を追加し、それに基づいて出力エクセルファイルを生成します。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-AccessingTablefromCell-AccessingTablefromCell.java" >}}
