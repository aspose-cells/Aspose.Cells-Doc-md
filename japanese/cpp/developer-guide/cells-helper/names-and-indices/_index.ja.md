---
title: 名前とインデックス
type: docs
weight: 10
url: /ja/cpp/names-and-indices/
---
##  **行と列のインデックスから Cell の名前を取得する**
行と列のインデックスを指定すると、セルの名前を見つけることができます。この記事ではその方法を説明します。
 Aspose.Cells は、[CellsHelper::CellIndexToName](https://reference.aspose.com/cells/cpp/aspose.cells/cellshelper/cellindextoname/)このメソッドを使用すると、開発者は行と列のインデックスを指定した場合にセルの名前を取得できます。

{{% alert color="primary" %}} 

行と列のインデックスが 1 から始まる Microsoft Excel とは異なり、Aspose.Cells は行と列のインデックスを 0 から数え始めます。

{{% /alert %}} 

次のサンプル コードは、使用方法を示しています。[CellsHelper::CellIndexToName](https://reference.aspose.com/cells/cpp/aspose.cells/cellshelper/cellindextoname/)既知の行と列のインデックスを指定してセルの名前にアクセスします。このコードは次の出力を生成します。



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-C-main-GetCellNameFromRowAndColumn-new.cpp" >}}
##  **Cell 名前から行と列のインデックスを取得**
セルの名前からセルの行と列のインデックスを見つけることができます。この記事ではその方法を説明します。
 Aspose.Cells は、[CellsHelper.CellNameToIndex](https://reference.aspose.com/cells/cpp/aspose.cells/cellshelper/cellnametoindex/)このメソッドを使用すると、開発者はセルの名前から行と列のインデックスを取得できます。

{{% alert color="primary" %}} 

行と列のインデックスが 1 から始まる Microsoft Excel とは異なり、Aspose.Cells は行と列のインデックスを 0 から数え始めます。

{{% /alert %}} 

次のサンプル コードは、使用方法を示しています。[CellsHelper::CellNameToIndex](https://reference.aspose.com/cells/cpp/aspose.cells/cellshelper/cellnametoindex/)セルの名前から行と列のインデックスを取得します。このコードは次の出力を生成します。



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-C-main-GetRowAndColumnFromCellName-new.cpp" >}}
