---
title: Cells インデックスを取得
type: docs
weight: 600
url: /ja/net/get-cells-index/
description: row 、 columns 、または cell の名前によって行または列を取得する方法を学びます。セルの名前を行と列のインデックスを 0 から始まるものに変換します。
keywords: Get Row index and Column index by the name of the cell, Get Column index by the name of the column, Get Row index by the name of the row, Get the index by the name of cell. 
---
{{% alert color="primary" %}}
Excel のデフォルトのビューは A1 スタイル参照で、各列は A、B、C... として定義され、セルの名前は A1、B2、C3... などとなります。
このセルがどの行と列にあるかを知りたい場合があります。

{{% /alert %}}


##  **考えられる使用シナリオ**
ワークシート上の特定のデータを行と列のインデックスによってのみ操作する必要がある場合は、その特定のセルの列と列のインデックスを知っておく必要があります。
 Aspose.Cells は、行、列、セルの名前によって行と列のインデックスを取得するこの機能を提供します。
Aspose.Cells は、目標の達成に役立つ次のプロパティとメソッドを提供します。
- [**CellsHelper.CellNameToIndex**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/cellnametoindex)
- [**CellsHelper.ColumnIndexToName**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/columnindextoname)
- [**CellsHelper.ColumnNameToIndex**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/columnnametoindex)
- [**CellsHelper.RowIndexToName**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/rowindextoname)
- [**CellsHelper.RowNameToIndex**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/rownametoindex)

注: .Net では、インデックス付けは Aspose.Cells で 0 から始まりますが、MS Excel では行の ID は 1 から始まります。

##  **Aspose.Cells を使用して Cells インデックスを取得する**
この例では、次の方法を示します。

1. ワークブックを作成し、データを追加します。
1. 最初のワークシートで特定のセルを見つけます。
1. セル名から行インデックスと列インデックスを取得します。
1. 列の名前から列インデックスを取得します。
1. 行の名前から行インデックスを取得します。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-get-index.cs" >}}