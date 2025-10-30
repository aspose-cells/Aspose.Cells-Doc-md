---
title: セルのインデックスの取得
type: docs
weight: 600
url: /ja/python-net/get-cells-index/
description: Python用Aspose.Cellsにおいて、行の名前を使って行または列、セル名を使って行および列のインデックスを取得する方法、列またはセル。セル名を行と列のインデックス（0から始まる）に変換する方法、Aspose.Cells for Python via .NET APIを介して列の名前から列のインデックスを取得する方法、Aspose.Cells for Python via .NET APIを使用して行の名前から行インデックスを取得する方法、Pythonを使用してセルの名前を使ってインデックスを取得する。
keywords: Python Excel, Pythonを使用してセルの名前によって行インデックスと列インデックスを取得する方法、Pythonを使用して列の名前によって列インデックスを取得する方法、Pythonを使用して行の名前によって行インデックスを取得する方法、Pythonを使用してセルの名前によってインデックスを取得する。 
---

{{% alert color="primary" %}}
ExcelのデフォルトビューはA1形式の参照です。各列はA、B、C....と定義され、セルはA1、B2、C3...などと名前が付けられます。
このセルがどの行や列にあるか知りたい場合があるかもしれません。

{{% /alert %}}


## **可能な使用シナリオ**
ワークシート上の特定のデータを列や行インデックスで操作する必要がある場合、その特定のセルの列と行のインデックスを知る必要があります。 
Aspose.Cells for Python via .NETでは、行と列の名前によって行と列のインデックスを取得する機能を提供しています。 
Aspose.Cells for Python via .NETは、目標を達成するための次のプロパティとメソッドを提供しています。
- [**CellsHelper.cell_name_to_index**](https://reference.aspose.com/cells/python-net/aspose.cells/cellshelper/cell_name_to_index/#str-any-any)
- [**CellsHelper.column_index_to_name**](https://reference.aspose.com/cells/python-net/aspose.cells/cellshelper/column_index_to_name/#int)
- [**CellsHelper.column_name_to_index**](https://reference.aspose.com/cells/python-net/aspose.cells/cellshelper/column_name_to_index/#str)
- [**CellsHelper.row_index_to_name**](https://reference.aspose.com/cells/python-net/aspose.cells/cellshelper/row_index_to_name/#int)
- [**CellsHelper.row_name_to_index**](https://reference.aspose.com/cells/python-net/aspose.cells/cellshelper/row_name_to_index/#str)

注意：Aspose.Cells for Python via .NETではインデックス付けは0から始まりますが、MS Excelでは行のIDは1から始まります。

## **Aspose.Cells for PythonのExcelライブラリを使用してセルのインデックスを取得する**
この例では、次のことができます:

1. ワークブックを作成し、いくつかのデータを追加します。
1. 最初のワークシートで特定のセルを見つけます。
1. セルの名前によって行インデックスと列インデックスを取得します。
1. 列の名前によって列インデックスを取得します。
1. 行の名前によって行インデックスを取得します。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-get-index.py" >}}
{{< app/cells/assistant language="python-net" >}}
