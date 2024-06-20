---
title: 元の値を使用してデータを検索
type: docs
weight: 380
url: /ja/python-net/search-data-using-original-values/
description: Aspose.Cells for Python via .NET API を通じて、元の値を使用してデータを検索する方法を学びます。
keywords: Python Excel ライブラリ、元の値を使用してデータを検索するPython、元の値を使用してデータを検索するPython、元の値でデータを検索するPython、元の値でデータを検索するPython
---

{{% alert color="primary" %}}

データの値がフォーマットされているため、隠されている場合があります。たとえば、セルD4にはformula =Sum(A1:A2) があり、その値は20ですが、--- という形式にフォーマットされているため、値20は隠され、Microsoft Excelの検索オプションでは見つけることができません。しかし、Aspose.Cells for Python via .NET を使用して [**LookInType.ORIGINAL_VALUES**](https://reference.aspose.com/cells/python-net/aspose.cells/lookintype) でそれを見つけることができます。

{{% /alert %}}

以下のサンプルコードは上記の点を説明しています。Microsoft Excelの検索オプションでは見つけることができないセルD4を見つけますが、Aspose.Cellsを使用して[**LookInType.ORIGINAL_VALUES**](https://reference.aspose.com/cells/python-net/aspose.cells/lookintype)を使用してそれを見つけることができます。詳細については、コード内のコメントをお読みください。

## 元の値を使用してデータを検索するPythonコード

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-SearchDataUsingOriginalValues.py" >}}

## サンプルコードによって生成されたコンソール出力

上記のサンプルコードのコンソール出力は次の通りです。

{{< highlight java >}}

Aspose.Cells.Cell [ D4; ValueType : IsNumeric; Value : ---; Formula:=SUM(A1:A2)]

{{< /highlight >}}
