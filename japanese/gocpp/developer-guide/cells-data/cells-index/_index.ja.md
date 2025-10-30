---
title: GolangをC++経由でセルのインデックスを取得する
linktitle: セルのインデックスの取得
type: docs
weight: 600
url: /ja/go-cpp/get-cells-index/
description: 行、列、またはセルの名前から行または列のインデックスを取得する方法を学習します。Aspose.Cellsを使用してセル名を行と列のインデックスに変換します（ゼロベース）。
keywords: セルのデフォルトのビューは A1 スタイルの参照です。各列は A、B、C... と定義され、セルは A1、B2、C3... と名前が付けられます。
---

{{% alert color="primary" %}}
ExcelのデフォルトビューはA1スタイルの参照で、各列はA、B、C... と定義され、セルはA1、B2、C3...と名前付けられます。
このセルがどの行と列にあるのか知りたい場合もあります。

{{% /alert %}}

## **可能な使用シナリオ**

特定のデータのみを行と列のインデックスで操作したい場合、その特定のセルの行と列のインデックスを知る必要があります。
Aspose.Cellsは、行名、列名、セル名からこれらのインデックスを取得する機能を提供します。
Aspose.Cellsは目標を達成するための次のプロパティとメソッドを提供します：

- [**CellsHelper::CellNameToIndex**](https://reference.aspose.com/cells/go-cpp/cellshelper/cellnametoindex/)
- [**CellsHelper::ColumnIndexToName**](https://reference.aspose.com/cells/go-cpp/cellshelper/columnindextoname/)
- [**CellsHelper::ColumnNameToIndex**](https://reference.aspose.com/cells/go-cpp/cellshelper/columnnametoindex/)
- [**CellsHelper::RowIndexToName**](https://reference.aspose.com/cells/go-cpp/cellshelper/rowindextoname/)
- [**CellsHelper::RowNameToIndex**](https://reference.aspose.com/cells/go-cpp/cellshelper/rownametoindex/)

注：インデックスは Aspose.Cells for C++ ではゼロベースですが、MS Excel の行のIDは1ベースです。

## **Aspose.Cells を使用してセルのインデックスを取得**

この例では、次のことができます:

1. ワークブックを作成し、いくつかのデータを追加します。
1. 最初のワークシートで特定のセルを見つけます。
1. セルの名前によって行インデックスと列インデックスを取得します。
1. 列の名前によって列インデックスを取得します。
1. 行の名前によって行インデックスを取得します。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CellsIndex.go" >}}
