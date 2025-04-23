---
title: 名前とインデックス
type: docs
weight: 10
url: /ja/go-cpp/names-and-indices/
---

## **行と列のインデックスからセル名を取得**

行と列のインデックスを指定すると、セルの名前を見つけることが可能です。 この記事では、その方法について説明します。
 Aspose.Cellsは[CellsHelper_CellIndexToName](https://reference.aspose.com/cells/go-cpp/cellshelper/cellshelper_cellindextoname/)メソッドを提供しており、行と列のインデックスを指定するとセルの名前を取得できます。

{{% alert color="primary" %}}

Microsoft Excel では行と列のインデックスは1から始まりますが、Aspose.Cells では行と列のインデックスは0から始まります。

{{% /alert %}}

以下のサンプルコードは、既知の行と列のインデックスを用いて[CellsHelper_CellIndexToName](https://reference.aspose.com/cells/go-cpp/cellshelper/cellshelper_cellindextoname/)を使用し、セルの名前にアクセスする方法を示しています。このコードは次の出力を生成します：

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-GetCellNameFromRowAndColumn.go" >}}

## **セル名から行と列のインデックスを取得**

セルの名前から行と列のインデックスを見つけることが可能です。 この記事では、その方法について説明します。
Aspose.Cellsは[CellsHelper_CellNameToIndex](https://reference.aspose.com/cells/go-cpp/cellshelper/cellshelper_cellnametoindex/)メソッドも提供しており、セルの名前から行と列のインデックスを取得できます。

{{% alert color="primary" %}}

Microsoft Excel では行と列のインデックスは1から始まりますが、Aspose.Cells では行と列のインデックスは0から始まります。

{{% /alert %}}

次のサンプルコードは、[CellsHelper_CellNameToIndex](https://reference.aspose.com/cells/go-cpp/cellshelper/cellshelper_cellnametoindex/)を使ってセルの名前から行と列のインデックスを取得する方法を示しています。このコードは以下の出力を生成します：

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-GetRowAndColumnFromCellName.go" >}}
