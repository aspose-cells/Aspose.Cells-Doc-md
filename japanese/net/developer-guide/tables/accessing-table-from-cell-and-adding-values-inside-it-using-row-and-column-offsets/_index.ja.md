---
title: Cell からテーブルにアクセスし、行と列のオフセットを使用してテーブル内に値を追加する
type: docs
weight: 230
url: /ja/net/accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets/
---
{{% alert color="primary" %}}

通常、次を使用してテーブルまたはリスト オブジェクト内に値を追加します。[**Cell.PutValue()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/putvalue/index)方法。ただし、場合によっては、行と列のオフセットを使用して、テーブルまたはリスト オブジェクト内に値を追加する必要がある場合があります。

セルからテーブルまたはリスト オブジェクトにアクセスするには、[**Cell.GetTable()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/gettable)方法。行と列のオフセットを使用して内部に値を追加するには、[**ListObject.PutCellValue**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject/methods/putcellvalue)方法。

{{% /alert %}}

次のスクリーンショットは、コード内で使用されるソース Excel ファイルを示しています。空のテーブルが含まれており、テーブル内にあるセル D5 が強調表示されています。を使用して、セル D5 からこのテーブルにアクセスします。[**Cell.GetTable()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/gettable)メソッドを作成し、両方を使用してその中に値を追加します[**Cell.PutValue()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/putvalue/index)と[**ListObject.PutCellValue**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject/methods/putcellvalue)メソッド。

## 例

### ソース ファイルと出力ファイルを比較するスクリーンショット

|![todo:画像_代替_文章](accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets_1.png)|
|:- |

次のスクリーンショットは、コードによって生成された出力 Excel ファイルを示しています。ご覧のとおり、セル D5 には値があり、テーブルのオフセット 2,2 にあるセル F6 には値があります。

|![todo:画像_代替_文章](accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets_2.png)|
|:- |

### C# セルからテーブルにアクセスし、行と列のオフセットを使用してその中に値を追加するコード

次のサンプル コードは、上記のスクリーンショットに示すようにソース Excel ファイルを読み込み、テーブル内に値を追加して、上記のように出力 Excel ファイルを生成します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingRowsColumnsCells-AccessTableFromCellAndAddValue-AccessTableFromCellAndAddValue.cs" >}}
