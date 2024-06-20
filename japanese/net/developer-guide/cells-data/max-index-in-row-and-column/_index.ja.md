---
title: 行内の最大列インデックスと列内の最大行インデックスの取得
type: docs
weight: 600
url: /ja/net/get-max-index-in-row-and-column/
description: Aspose.Cells for .NET APIを通じて行内の最大列インデックスと列内の最大行インデックスの取得方法を学ぶ。
keywords: 行内の最大列インデックス、列内の最大行インデックス、行内の最大データ列インデックス、列内の最大データ行インデックスの取得。 
---

## **可能な使用シナリオ**
行または列上の一部のデータを操作する必要がある場合、行と列のデータ範囲を知る必要があります。Aspose.Cellsはこの機能を提供しています。行の最大列インデックスを取得するには、[Row.LastCell](https://reference.aspose.com/cells/net/aspose.cells/row/lastcell/) および [Row.LastDataCell](https://reference.aspose.com/cells/net/aspose.cells/row/lastdatacell/) プロパティを取得し、その後、 [Cell.Column](https://reference.aspose.com/cells/net/aspose.cells/cell/column/) プロパティを使用して最大列インデックスおよび最大データ列インデックスを取得します。ただし、列の最大行インデックスと最大行データインデックスを取得するには、列に範囲を作成して、範囲を走査して最後のセルを検索し、最終的に [Cell.Row](https://reference.aspose.com/cells/net/aspose.cells/cell/row/) 属性を取得する必要があります。

Aspose.Cellsは、目標を達成するための以下のプロパティとメソッドを提供しています。
- [**Row.LastCell**](https://reference.aspose.com/cells/net/aspose.cells/row/lastcell/)
- [**Row.LastDataCell**](https://reference.aspose.com/cells/net/aspose.cells/row/lastdatacell/)
- [**Cell.Column**](https://reference.aspose.com/cells/net/aspose.cells/cell/column/)
- [**Cell.Row**](https://reference.aspose.com/cells/net/aspose.cells/cell/row/)

## **Aspose.Cellsを使用して行内の最大列インデックスと列内の最大行インデックスの取得**
この例では、次のことができます:

1. [サンプルファイル](sample.xlsx)をロードする。
1. 最大列インデックスと最大データ列インデックスを取得する行を取得します。
1. セル上の[Cell.Column](https://reference.aspose.com/cells/net/aspose.cells/cell/column/)属性を取得します。
1. 列に基づいて範囲を作成します。
1. イテレータを取得して範囲をトラバースします。
1. セル上の[Cell.Row](https://reference.aspose.com/cells/net/aspose.cells/cell/row/)属性を取得します。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-max-index-of-row-and-column.cs" >}}
