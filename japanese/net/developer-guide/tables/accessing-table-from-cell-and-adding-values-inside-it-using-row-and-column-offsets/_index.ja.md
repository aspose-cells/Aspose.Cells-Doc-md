---
title: セルからテーブルにアクセスし、行と列のオフセットを使用して値を追加する
type: docs
weight: 230
url: /ja/net/accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets/
---

{{% alert color="primary" %}}

通常、テーブルまたはリストオブジェクト内に値を追加する場合は [**Cell.PutValue()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/putvalue/index) メソッドを使用します。ただし、時々、行と列のオフセットを使用してテーブルまたはリストオブジェクト内に値を追加する必要があることがあります。

セルからテーブルまたはリストオブジェクトにアクセスするには、[**Cell.GetTable()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/gettable) メソッドを使用します。行と列のオフセットを使用してその内部に値を追加するには、[**ListObject.PutCellValue**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject/methods/putcellvalue) メソッドを使用します。

{{% /alert %}}

以下のスクリーンショットは、コード内で使用されるソースエクセルファイルを示しています。空のテーブルが含まれ、テーブル内にあるセル D5 が強調表示されています。このテーブルにセル D5 から [**Cell.GetTable()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/gettable) メソッドを使用してアクセスし、その後、[**Cell.PutValue()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/putvalue/index) および [**ListObject.PutCellValue**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject/methods/putcellvalue) メソッドを使用してその内部に値を追加します。

## 例

### ソースファイルと出力ファイルの比較のスクリーンショット

|![todo:image_alt_text](accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets_1.png)|
| :- |

以下のスクリーンショットは、コードによって生成された出力エクセルファイルを示しています。セル D5 に値が設定されており、テーブル内のオフセット 2,2 のセル F6 にも値が設定されています。

|![todo:image_alt_text](accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets_2.png)|
| :- |

### セルからテーブルにアクセスし、行と列のオフセットを使用して値を追加するC#コード

以下のサンプルコードは、上記のスクリーンショットに示されているソースエクセルファイルを読み込み、テーブル内に値を追加し、それに基づいて出力エクセルファイルを生成します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingRowsColumnsCells-AccessTableFromCellAndAddValue-AccessTableFromCellAndAddValue.cs" >}}
{{< app/cells/assistant language="csharp" >}}
