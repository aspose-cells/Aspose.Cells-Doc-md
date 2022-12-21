---
title: 書式設定あり/なしで Cell 文字列値を取得する
type: docs
weight: 240
url: /ja/net/get-cell-string-value-with-and-without-formatting/
---
{{% alert color="primary" %}}

Aspose.Cells はメソッドを提供します[**Cell.GetStringValue()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstringvalue)書式設定の有無にかかわらず、セルの文字列値を取得するために使用できます。値が 0.012345 のセルがあり、小数点以下 2 桁のみを表示するように書式設定したとします。 Excel では 0.01 と表示されます。を使用して、文字列値を 0.01 と 0.012345 の両方として取得できます。[**Cell.GetStringValue()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstringvalue)方法。それはとります[**CellValueFormat戦略**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstringvalue)次の値を持つパラメーターとしての列挙型

- CellValueFormatStrategy.CellStyle
- CellValueFormatStrategy.DisplayStyle
- CellValueFormatStrategy.None

{{% /alert %}}

次のサンプル コードは、[**Cell.GetStringValue()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstringvalue)方法。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingRowsColumnsCells-GetStringValue-GetStringValueWithOrWithoutFormatting.cs" >}}
