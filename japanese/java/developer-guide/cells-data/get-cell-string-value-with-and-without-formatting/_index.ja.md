---
title: 書式設定あり/なしで Cell 文字列値を取得する
type: docs
weight: 230
url: /ja/java/get-cell-string-value-with-and-without-formatting/
---
{{% alert color="primary" %}} 

Aspose.Cells はメソッドを提供します[Cell.getStringValue()](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getStringValue\(int\) を使用して、書式設定の有無にかかわらず、セルの文字列値を取得できます。値が 0.012345 のセルがあり、小数点以下 2 桁のみを表示するように書式設定したとします。 Excel では 0.01 と表示されます。を使用して、文字列値を 0.01 と 0.012345 の両方として取得できます。[Cell.getStringValue()](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getStringValue\(int\) ） 方法。それはとります[CellValueFormat戦略](https://reference.aspose.com/cells/java/com.aspose.cells/CellValueFormatStrategy)次の値を持つパラメーターとしての列挙型

- [CellValueFormatStrategy.CELL_STYLE](https://reference.aspose.com/cells/java/com.aspose.cells/cellvalueformatstrategy#CELL_STYLE)
- [CellValueFormatStrategy.DISPLAY_STYLE](https://reference.aspose.com/cells/java/com.aspose.cells/cellvalueformatstrategy#DISPLAY_STYLE)
- [CellValueFormatStrategy.NONE](https://reference.aspose.com/cells/java/com.aspose.cells/cellvalueformatstrategy#NONE)

{{% /alert %}} 
## **書式設定あり/なしで Cell 文字列値を取得する**
次のサンプル コードは、[Cell.getStringValue()](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getStringValue\(int\)） 方法。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-GetCellStringValue-GetCellStringValue.java" >}}
## **コンソール出力**
以下は、上記のサンプル コードのコンソール出力です。

{{< highlight "java" >}}

 0.01

0.012345

{{< /highlight >}}
