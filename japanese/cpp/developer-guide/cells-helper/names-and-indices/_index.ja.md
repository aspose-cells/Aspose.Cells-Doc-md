---
title: 名前とインデックス
type: docs
weight: 10
url: /ja/cpp/names-and-indices/
---

## **行と列のインデックスからセル名を取得**
行と列のインデックスを指定すると、セルの名前を見つけることが可能です。 この記事では、その方法について説明します。
Aspose.Cells は [CellsHelper::CellIndexToName](https://reference.aspose.com/cells/cpp/aspose.cells/cellshelper/cellindextoname/) メソッドを提供しており、行と列のインデックスを指定した場合、セルの名前を取得できます。

{{% alert color="primary" %}} 

Microsoft Excel では行と列のインデックスは1から始まりますが、Aspose.Cells では行と列のインデックスは0から始まります。

{{% /alert %}} 

下記のサンプルコードは、既知の行と列のインデックスからセルの名前を取得するために [CellsHelper::CellIndexToName](https://reference.aspose.com/cells/cpp/aspose.cells/cellshelper/cellindextoname/) を使用する方法を示しています。 コードにより、以下の出力が生成されます。



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-C-main-GetCellNameFromRowAndColumn-new.cpp" >}}
## **セル名から行と列のインデックスを取得**
セルの名前から行と列のインデックスを見つけることが可能です。 この記事では、その方法について説明します。
Aspose.Cells は [CellsHelper.CellNameToIndex](https://reference.aspose.com/cells/cpp/aspose.cells/cellshelper/cellnametoindex/) メソッドを提供しており、セルの名前から行と列のインデックスを取得できます。

{{% alert color="primary" %}} 

Microsoft Excel では行と列のインデックスは1から始まりますが、Aspose.Cells では行と列のインデックスは0から始まります。

{{% /alert %}} 

下記のサンプルコードは、セルの名前から行と列のインデックスを取得するために [CellsHelper::CellNameToIndex](https://reference.aspose.com/cells/cpp/aspose.cells/cellshelper/cellnametoindex/) を使用する方法を示しています。 コードにより、以下の出力が生成されます。



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-C-main-GetRowAndColumnFromCellName-new.cpp" >}}
{{< app/cells/assistant language="cpp" >}}
