---
title: 行内の最大列インデックスと列内の最大行インデックスの取得
type: docs
weight: 600
url: /ja/python-net/get-max-index-in-row-and-column/
description: Aspose.Cells for Python via .NET APIを使用して、行の最大列インデックスと列の最大行インデックスを取得する方法を学びます。
keywords: Python Excel Library、Python Get Max Column Index in Row、Python Get Max Row Index in Column、Python Get Max Data Column Index in Row、Python Get Max Data Row Index in Column。 
---

## **可能な使用シナリオ**
行または列のデータを操作する必要がある場合には、行と列のデータ範囲が必要です。Aspose.Cells for Python via .NETはこの機能を提供しています。行の最大列インデックスを取得するには、[Row.last_cell](https://reference.aspose.com/cells/python-net/aspose.cells/row/last_cell/)と[Row.last_data_cell](https://reference.aspose.com/cells/python-net/aspose.cells/row/last_data_cell/)プロパティを取得し、その後[Cell.column](https://reference.aspose.com/cells/python-net/aspose.cells/cell/column/)プロパティを使用して最大列インデックスと最大データ列インデックスを取得します。ただし、列の最大行インデックスと最大行データインデックスを取得するには、列上に範囲を作成し、範囲をトラバースして最後のセルを見つけ、最後にセルの[Cell.row](https://reference.aspose.com/cells/python-net/aspose.cells/cell/row/)属性を取得する必要があります。

Aspose.Cells for Python via .NETは、目標を達成するための次のプロパティとメソッドを提供しています。
- [**Row.last_cell**](https://reference.aspose.com/cells/python-net/aspose.cells/row/last_cell/)
- [**Row.last_data_cell**](https://reference.aspose.com/cells/python-net/aspose.cells/row/last_data_cell/)
- [**Cell.column**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/column/)
- [**Cell.row**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/row/)

## **Aspose.Cells for Python Excelライブラリを使用して行内の最大列インデックスと列内の最大行インデックスを取得する**
この例では、次のことができます:

1. [サンプルファイル](sample.xlsx)をロードする。
1. 最大列インデックスと最大データ列インデックスを取得する行を取得します。
1. セル上の[Cell.column](https://reference.aspose.com/cells/python-net/aspose.cells/cell/column/)属性を取得します。
1. 列に基づいて範囲を作成します。
1. イテレータを取得して範囲をトラバースします。
1. セル上の[Cell.row](https://reference.aspose.com/cells/python-net/aspose.cells/cell/row/)属性を取得します。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-Cells-max-index-of-row-and-column.py" >}}
