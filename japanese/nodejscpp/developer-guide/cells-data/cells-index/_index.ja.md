---
title: セルのインデックスの取得
type: docs
weight: 600
url: /ja/nodejs-cpp/get-cells-index/
description: 行または列の名前で行または列を取得する方法を学びます。セルの名前を行および列インデックスに変換します。セルの名前によるインデックス、列の名前による列インデックス、行の名前による行インデックス、セルの名前によるインデックスを取得します。
keywords: セルのデフォルトのビューは A1 スタイルの参照です。各列は A、B、C... と定義され、セルは A1、B2、C3... と名前が付けられます。 
---

{{% alert color="primary" %}}
ExcelのデフォルトビューはA1形式の参照です。各列はA、B、C....と定義され、セルはA1、B2、C3...などと名前が付けられます。
このセルがどの行や列にあるか知りたい場合があるかもしれません。

{{% /alert %}}


## **可能な使用シナリオ**
ワークシート上の特定のデータを列や行インデックスで操作する必要がある場合、その特定のセルの列と行のインデックスを知る必要があります。 
Aspose.Cells for Node.js via C++は、行、列、セルの名前から行と列のインデックスを取得するこの機能を提供します。 
Aspose.Cells for Node.js via C++は、次のプロパティとメソッドを提供して、あなたの目標を達成するのに役立ちます。
- [**CellsHelper.cellNameToIndex(string)**](https://reference.aspose.com/cells/nodejs-cpp/cellshelper/#cellNameToIndex-string-)
- [**CellsHelper.columnIndexToName**](https://reference.aspose.com/cells/nodejs-cpp/cellshelper/#columnIndexToName-number-)
- [**CellsHelper.columnNameToIndex**](https://reference.aspose.com/cells/nodejs-cpp/cellshelper/#columnNameToIndex-string-)
- [**CellsHelper.rowIndexToName**](https://reference.aspose.com/cells/nodejs-cpp/cellshelper/#rowIndexToName-number-)
- [**CellsHelper.rowNameToIndex**](https://reference.aspose.com/cells/nodejs-cpp/cellshelper/#rowNameToIndex-string-)

注意：Aspose.Cells for Node.js via C++のインデックスはゼロベースですが、MS Excelの行のIDは1ベースです。

## **Aspose.Cells for Node.js via C++を使用したセルのインデックス取得**
この例では、次のことができます:

1. ワークブックを作成し、いくつかのデータを追加します。
1. 最初のワークシートで特定のセルを見つけます。
1. セルの名前によって行インデックスと列インデックスを取得します。
1. 列の名前によって列インデックスを取得します。
1. 行の名前によって行インデックスを取得します。

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-get-index.js" >}}
