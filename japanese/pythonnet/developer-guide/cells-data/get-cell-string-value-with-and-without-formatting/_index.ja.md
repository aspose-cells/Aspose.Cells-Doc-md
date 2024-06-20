---
title: フォーマット戦略でセル文字列値を取得する
type: docs
weight: 240
url: /ja/python-net/get-cell-string-value-with-format-strategy/
description: Aspose.Cells for Python via .NET APIを介して、フォーマット付きとフォーマットなしでセル文字列値を取得する方法を学びます。
keywords: Python Excelライブラリ、フォーマット付きとフォーマットなしでセル文字列値を取得するPython、フォーマット付きとフォーマットなしでセル文字列値を取得するPython、フォーマット付きとフォーマットなしでセル文字列値を取得するPython、フォーマット付きとフォーマットなしでセル文字列値を取得するPython
---

{{% alert color="primary" %}}

Aspose.Cells for Python via .NETは、フォーマットを含めるか含めないかに関わらず、セルの文字列値を取得するために使用できる[**Cell.get_string_value(format_strategy)**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_string_value/)メソッドを提供します。例えば、値が0.012345のセルがあり、それを小数点以下2桁のみを表示するようにフォーマットした場合、Excelでは0.01として表示されます。[**Cell.get_string_value(format_strategy)**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_string_value/)メソッドを使用して、0.01または0.012345の両方の文字列値を取得することができます。それは次の値を持つ[**CellValueFormatStrategy**](https://reference.aspose.com/cells/python-net/aspose.cells/cellvalueformatstrategy/)列挙体をパラメータとして受け取ります

- CellValueFormatStrategy.CELL_STYLE
- CellValueFormatStrategy.DISPLAY_STYLE
- CellValueFormatStrategy.DISPLAY_STRING
- CellValueFormatStrategy.NONE

{{% /alert %}}

次のサンプルコードは、[**Cell.get_string_value(format_strategy)**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_string_value/)メソッドの使用方法を説明しています。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-HtmlStringValue-GetStringValueWithOrWithoutFormatting.py" >}}
