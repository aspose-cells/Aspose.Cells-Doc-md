---
title: Golang経由のC++で行の最大列インデックスと列の最大行インデックスを取得
linktitle: 行内の最大列インデックスと列内の最大行インデックスの取得
type: docs
weight: 600
url: /ja/go-cpp/get-max-index-in-row-and-column/
description: Aspose.Cells for C++ APIを使用して、行の最大列インデックスと列の最大行インデックスを取得する方法を学びます。
keywords: 行内の最大列インデックス、列内の最大行インデックス、行内の最大データ列インデックス、列内の最大データ行インデックスの取得。
---

## **可能な使用シナリオ**
行または列の一部のデータだけを操作する場合、行と列のデータ範囲を知る必要があります。Aspose.Cellsはこの機能を提供します。行の最大列インデックスを取得するには、[Row.GetLastCell()](https://reference.aspose.com/cells/go-cpp/row/getlastcell/)と[Row.GetLastDataCell()](https://reference.aspose.com/cells/cpp/aspose.cells/row/getlastdatacell/)のプロパティを取得し、次に[Cell.GetColumn()](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getcolumn/)を使用して最大列インデックスと最大データ列インデックスを得ます。一方、列の最大行インデックスと最大行データインデックスを取得するには、列に範囲を作成し、その範囲を遍歴して最後のセルを見つけ、最後にセルの[Cell.GetRow()](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getrow/)属性を取得します。

Aspose.Cellsは、目標を達成するための以下のプロパティとメソッドを提供しています。
- [**Row.GetLastCell()**](https://reference.aspose.com/cells/go-cpp/row/getlastcell/)
- [**Row.GetLastDataCell()**](https://reference.aspose.com/cells/go-cpp/row/getlastdatacell/)
- [**Cell.GetColumn()**](https://reference.aspose.com/cells/go-cpp/cell/getcolumn/)
- [**Cell.GetRow()**](https://reference.aspose.com/cells/go-cpp/cell/getrow/)

## **Aspose.Cellsを使用して行内の最大列インデックスと列内の最大行インデックスの取得**
この例では、次のことができます:

1. [サンプルファイル](sample.xlsx)をロードする。
1. 最大列インデックスと最大データ列インデックスを取得する行を取得します。
1. セルの[Cell.GetColumn()](https://reference.aspose.com/cells/go-cpp/cell/getcolumn/)属性を取得
1. 列に基づいて範囲を作成します。
1. イテレータを取得して範囲をトラバースします。
1. セルの[Cell.GetRow()](https://reference.aspose.com/cells/go-cpp/cell/getrow/)属性を取得

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-MaxIndexInRowAndColumn.go" >}}
