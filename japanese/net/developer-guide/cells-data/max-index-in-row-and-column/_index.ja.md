---
title: 行の最大列インデックスと列の最大行インデックスを取得
type: docs
weight: 600
url: /ja/net/get-max-index-in-row-and-column/
description: Aspose.Cells for .NET API を通じて行の最大列インデックスと列の最大行インデックスを取得する方法を学習します。
keywords: Get Max Column Index in Row, Get Max Row Index in Column, Get Max Data Column Index in Row, Get Max Data Row Index in Column. 
---
##  **考えられる使用シナリオ**
行または列の一部のデータのみを操作する必要がある場合は、行と列のデータ範囲を知っておく必要があります。 Aspose.Cells がこの機能を提供しています。行の最大列インデックスを取得するには、[行.最後のセル](https://reference.aspose.com/cells/net/aspose.cells/row/lastcell/)そして[Row.LastDataCell](https://reference.aspose.com/cells/net/aspose.cells/row/lastdatacell/)プロパティを選択し、[Cell.Column](https://reference.aspose.com/cells/net/aspose.cells/cell/column/)プロパティを使用して、最大列インデックスと最大データ列インデックスを取得します。ただし、列の最大行インデックスと最大行データ インデックスを取得するには、列に範囲を作成し、その範囲を走査して最後のセルを見つけ、最後に[Cell.Row](https://reference.aspose.com/cells/net/aspose.cells/cell/row/)セルの属性。

Aspose.Cells は、目標の達成に役立つ次のプロパティとメソッドを提供します。
- [**行.最後のセル**](https://reference.aspose.com/cells/net/aspose.cells/row/lastcell/)
- [**Row.LastDataCell**](https://reference.aspose.com/cells/net/aspose.cells/row/lastdatacell/)
- [**Cell.Column**](https://reference.aspose.com/cells/net/aspose.cells/cell/column/)
- [**Cell.Row**](https://reference.aspose.com/cells/net/aspose.cells/cell/row/)

##  **Aspose.Cells を使用して、行の最大列インデックスと列の最大行インデックスを取得します**
この例では、次の方法を示します。

1. をロードします[サンプルファイル](sample.xlsx).
1. 最大列インデックスと最大データ列インデックスを取得する必要がある行を取得します。
1. 得る[Cell.Column](https://reference.aspose.com/cells/net/aspose.cells/cell/column/)セルの属性。
1. 列に基づいて範囲を作成します。
1. イテレータとトラバース範囲を取得します。
1. 得る[Cell.Row](https://reference.aspose.com/cells/net/aspose.cells/cell/row/)セルの属性。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-max-index-of-row-and-column.cs" >}}