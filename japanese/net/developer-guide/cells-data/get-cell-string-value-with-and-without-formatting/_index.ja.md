---
title: 書式設定ありまたはなしで Cell 文字列値を取得する
type: docs
weight: 240
url: /ja/net/get-cell-string-value-with-and-without-formatting/
description: Aspose.Cells for .NET API を通じて、書式設定ありまたは書式なしで Cell 文字列値を取得する方法を学習します。
keywords: Get Cell String Value with and without Formatting, Retrieve Cell String Value with and without Formatting, Obtain Cell String Value with and without Formatting
---
{{% alert color="primary" %}}

Aspose.Cells が方法を提供します[**Cell.GetStringValue()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstringvalue)これは、書式設定の有無にかかわらず、セルの文字列値を取得するために使用できます。値が 0.012345 のセルがあり、小数点以下 2 桁のみを表示するように書式設定しているとします。 Excel では 0.01 と表示されます。次のコマンドを使用すると、文字列値を 0.01 と 0.012345 の両方で取得できます。[**Cell.GetStringValue()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstringvalue)方法。かかる[**CellValueFormat戦略**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstringvalue)次の値を持つパラメータとしての enum

- CellValueFormatStrategy.CellStyle
- CellValueFormatStrategy.DisplayStyle
- CellValueFormatStrategy.None

{{% /alert %}}

次のサンプルコードは、[**Cell.GetStringValue()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstringvalue)方法。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingRowsColumnsCells-GetStringValue-GetStringValueWithOrWithoutFormatting.cs" >}}
