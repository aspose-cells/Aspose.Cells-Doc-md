---
title: 名前とインデックス
type: docs
weight: 10
url: /ja/cpp/names-and-indices/
---
## **行と列のインデックスから Cell の名前を取得**
行と列のインデックスがあれば、セルの名前を見つけることができます。この記事では、その方法について説明します。
Aspose.Cells は、ICellsHelper.CellIndexToName_i メソッドを提供します。開発者は、行と列のインデックスを提供する場合にセルの名前を取得できます。

{{% alert color="primary" %}} 

行と列のインデックスが 1 から始まる Microsoft Excel とは異なり、Aspose.Cells は行と列のインデックスを 0 から数え始めます。

{{% /alert %}} 

次のサンプル コードは、ICellsHelper.CellIndexToName_i を使用して、既知の行と列のインデックスが指定されたセルの名前にアクセスする方法を示しています。コードは次の出力を生成します。



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-C-main-GetCellNameFromRowAndColumn.cpp" >}}
## **Cell 名前から行と列のインデックスを取得**
名前からセルの行と列のインデックスを見つけることができます。この記事では、その方法について説明します。
Aspose.Cells は、開発者がセルの名前から行と列のインデックスを取得できるようにする ICellsHelper.CellNameToIndex_i メソッドを提供します。

{{% alert color="primary" %}} 

行と列のインデックスが 1 から始まる Microsoft Excel とは異なり、Aspose.Cells は行と列のインデックスを 0 から数え始めます。

{{% /alert %}} 

次のサンプル コードは、CellsHelper.CellNameToIndex を使用して、セルの名前から行と列のインデックスを取得する方法を示しています。コードは次の出力を生成します。



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-C-main-GetRowAndColumnFromCellName.cpp" >}}
