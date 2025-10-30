---
title: フォーマットあり・なしのセル文字列値の取得（C++経由のGolang）
linktitle: セル文字列値の取得
type: docs
weight: 240
url: /ja/go-cpp/get-cell-string-value-with-and-without-formatting/
description: Aspose.Cells for C++ APIを使用して、フォーマットの有無に関わらずセルの文字列値を取得する方法を学びます。
keywords: 書式設定ありとなしでセルの文字列値を取得する方法、書式設定ありとなしでセルの文字列値を取得する、書式設定ありとなしでセルの文字列値を取得
---

{{% alert color="primary" %}}

Aspose.Cells は、[**Cell::GetStringValue()**](https://reference.aspose.com/cells/go-cpp/cell/getstringvalue_cellvalueformatstrategy/) というメソッドを提供しており、これを使ってフォーマットの有無に関わらずセルの文字列値を取得できます。例として、値が 0.012345 のセルを持ち、これを小数点以下2桁だけ表示するようにフォーマットしているとします。するとExcel上では 0.01 と表示されます。[**Cell::GetStringValue()**](https://reference.aspose.com/cells/go-cpp/cell/getstringvalue_cellvalueformatstrategy/) メソッドを使用すると、0.01 と 0.012345 の両方の文字列値を取得できます。このメソッドは次の値を持つ [**CellValueFormatStrategy**](https://reference.aspose.com/cells/cpp/aspose.cells/cellvalueformatstrategy/) 列挙型をパラメータとして受け取ります：

- CellValueFormatStrategy::CellStyle
- CellValueFormatStrategy::DisplayStyle
- CellValueFormatStrategy::DisplayString
- CellValueFormatStrategy::None

{{% /alert %}}

次のサンプルコードは、[**Cell::GetStringValue()**](https://reference.aspose.com/cells/go-cpp/cell/getstringvalue_cellvalueformatstrategy/)メソッドの使用方法を説明しています。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-GetCellStringValueWithAndWithoutFormatting.go" >}}
