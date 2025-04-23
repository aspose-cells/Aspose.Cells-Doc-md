---
title: セルのインデックスの取得
type: docs
weight: 600
url: /ja/net/get-cells-index/
description: 行または列の名前で行または列を取得する方法を学びます。セルの名前を行および列インデックスに変換します。セルの名前によるインデックス、列の名前による列インデックス、行の名前による行インデックス、セルの名前によるインデックスを取得します。
keywords: セルのデフォルトのビューは A1 スタイルの参照です。各列は A、B、C... と定義され、セルは A1、B2、C3... と名前が付けられます。 
---

{{% alert color="primary" %}}
ExcelのデフォルトビューはA1形式の参照です。各列はA、B、C....と定義され、セルはA1、B2、C3...などと名前が付けられます。
このセルがどの行や列にあるか知りたい場合があるかもしれません。

{{% /alert %}}


## **可能な使用シナリオ**
ワークシート上の特定のデータを列や行インデックスで操作する必要がある場合、その特定のセルの列と行のインデックスを知る必要があります。 
Aspose.Cellsでは、行、列、セルの名前で行や列のインデックスを取得する機能が提供されています。 
Aspose.Cellsは、目標を達成するための以下のプロパティとメソッドを提供しています。
- [**CellsHelper.CellNameToIndex**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/cellnametoindex)
- [**CellsHelper.ColumnIndexToName**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/columnindextoname)
- [**CellsHelper.ColumnNameToIndex**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/columnnametoindex)
- [**CellsHelper.RowIndexToName**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/rowindextoname)
- [**CellsHelper.RowNameToIndex**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/rownametoindex)

注意: Aspose.Cells for .Net ではインデックスは 0 から始まりますが、MS Excel では行の id が 1 から始まります。

## **Aspose.Cells を使用してセルのインデックスを取得**
この例では、次のことができます:

1. ワークブックを作成し、いくつかのデータを追加します。
1. 最初のワークシートで特定のセルを見つけます。
1. セルの名前によって行インデックスと列インデックスを取得します。
1. 列の名前によって列インデックスを取得します。
1. 行の名前によって行インデックスを取得します。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-get-index.cs" >}}
{{< app/cells/assistant language="csharp" >}}
