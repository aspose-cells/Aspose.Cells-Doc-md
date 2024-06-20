---
title: 書式設定ありおよびなしでセル文字列の値を取得
type: docs
weight: 240
url: /ja/net/get-cell-string-value-with-and-without-formatting/
description: Aspose.Cells for .NET APIを使用して、書式設定ありとなしでセルの文字列値を取得する方法を学びます。
keywords: 書式設定ありとなしでセルの文字列値を取得する方法、書式設定ありとなしでセルの文字列値を取得する、書式設定ありとなしでセルの文字列値を取得
---

{{% alert color="primary" %}}

Aspose.Cellsには、書式付きまたは書式なしでセルの文字列値を取得するために使用できる[**Cell.GetStringValue()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstringvalue)メソッドが提供されています。例えば、値が0.012345のセルを2桁の小数点で表示するように書式設定した場合、Excelでは0.01と表示されます。[**Cell.GetStringValue()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstringvalue)メソッドを使用して、0.01および0.012345の文字列値を両方取得できます。次の値を持つ[**CellValueFormatStrategy**](https://reference.aspose.com/cells/net/aspose.cells/cellvalueformatstrategy/)列挙型をパラメーターとして受け取ります。

- CellValueFormatStrategy.CellStyle
- CellValueFormatStrategy.DisplayStyle
- CellValueFormatStrategy.DisplayString
- CellValueFormatStrategy.None

{{% /alert %}}

次のサンプルコードは、[**Cell.GetStringValue()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstringvalue)メソッドの使用方法を説明しています。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingRowsColumnsCells-GetStringValue-GetStringValueWithOrWithoutFormatting.cs" >}}
