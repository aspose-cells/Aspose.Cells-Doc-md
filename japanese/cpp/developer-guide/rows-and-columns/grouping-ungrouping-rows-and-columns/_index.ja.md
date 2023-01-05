---
title: 行と列のグループ化、グループ解除
type: docs
weight: 30
url: /ja/cpp/grouping-ungrouping-rows-and-columns/
---
## **序章**
Microsoft Excel ファイルでは、データのアウトラインを作成して、マウスを 1 回クリックするだけで詳細レベルを表示および非表示にすることができます。

クリック**外形記号**、1、2、3、+、および - を使用して、ワークシート内のセクションの要約または見出しを提供する行または列のみをすばやく表示したり、記号を使用して個々の要約または見出しの下に詳細を表示したりできます。
## **行と列のグループ管理**
Aspose.Cells はクラスを提供し、[Iワークブック](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook)Microsoft Excel ファイルを表します。の[Iワークブック](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook)クラスには[Iワークシート](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet_collection)Excel ファイル内の各ワークシートにアクセスできるコレクション。ワークシートは、[Iワークシート](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet)クラス。の[Iワークシート](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet)クラスは[Iセル](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell)ワークシート内のすべてのセルを表すコレクション。

の[Iセル](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell)collection は、ワークシートの行または列を管理するためのいくつかの方法を提供します。これらのいくつかについては、以下で詳しく説明します。
### **行と列のグループ化**
行または列をグループ化するには、[グループ行](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a88e0180ed1a4a423e0bd3ac599ef9332)と[グループ列](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#aaa14179e2a84ba5c2857f8434570d3d8)のメソッド[Iセル](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell)コレクション。どちらのメソッドも、次のパラメーターを取ります。

- 最初の行/列インデックス、グループ内の最初の行または列。
- 最後の行/列インデックス、グループ内の最後の行または列。
- グループ化後に行/列を非表示にするかどうかを指定するブール値パラメーターです。



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-GroupingUngroupingRowsAndColumns-GroupingRowsColumns.cpp" >}}
#### **グループ設定**
Microsoft Excel では、表示するグループ設定を構成できます。

- 詳細の下の要約行。
- 詳細の右側にある要約列。
## **行と列のグループ解除**
グループ化された行または列のグループ化を解除するには、[Iセル](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell)コレクションの[行のグループ化を解除](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#adc1f6418506854ab41707bfef453ddb1)と[列のグループ化を解除](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#aa3bf9a9510d4e85f68db9ebdcadc8406)メソッド。どちらのメソッドも次の 2 つのパラメーターを取ります。

- 最初の行または列のインデックス、グループ化を解除する最初の行/列。
- 最後の行または列のインデックス、グループ化を解除する最後の行/列。



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-GroupingUngroupingRowsAndColumns-UnGroupingRowsColumns.cpp" >}}
