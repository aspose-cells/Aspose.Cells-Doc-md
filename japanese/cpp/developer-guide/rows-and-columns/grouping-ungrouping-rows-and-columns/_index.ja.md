---
title: 行と列のグループ化、グループ解除
type: docs
weight: 30
url: /ja/cpp/grouping-ungrouping-rows-and-columns/
---
##  **導入**
Microsoft Excel ファイルでは、データのアウトラインを作成して、マウスを 1 回クリックするだけで詳細レベルの表示と非表示を切り替えることができます。

*アウトライン記号**、1、2、3、+、および - をクリックすると、ワークシート内のセクションの概要や見出しを提供する行または列のみがすばやく表示されます。また、記号を使用して、個々の概要やセクションの詳細を表示することもできます。見出し。
##  **行と列のグループ管理**
Aspose.Cells はクラスを提供します。[ワークブック](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)これは Microsoft Excel ファイルを表します。の[ワークブック](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)クラスには[ワークシート](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/)Excel ファイル内の各ワークシートへのアクセスを許可するコレクション。ワークシートは次のように表されます。[ワークシート](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)クラス。の[ワークシート](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)クラスが提供する[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)ワークシート内のすべてのセルを表すコレクション。

の[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)collection には、ワークシート内の行または列を管理するためのメソッドがいくつか用意されていますが、そのうちのいくつかについては以下で詳しく説明します。
###  **行と列のグループ化**
を呼び出すことで行または列をグループ化できます。[グループ行](https://reference.aspose.com/cells/cpp/aspose.cells/cells/grouprows/)そして[グループ列](https://reference.aspose.com/cells/cpp/aspose.cells/cells/groupcolumns/)のメソッド[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)コレクション。どちらのメソッドも次のパラメータを受け取ります。

- 最初の行/列のインデックス、グループ内の最初の行または列。
- 最後の行/列のインデックス、グループ内の最後の行または列。
- hidden は、グループ化後に行/列を非表示にするかどうかを指定するブール型パラメーターです。



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-GroupingUngroupingRowsAndColumns-GroupingRowsColumns-new.cpp" >}}
####  **グループ設定**
Microsoft Excel では、以下を表示するためのグループ設定を構成できます。

- 詳細の下の概要行。
- 詳細の右側にある概要列。
##  **行と列のグループ化を解除する**
グループ化された行または列のグループ化を解除するには、[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)コレクションの[行のグループ化を解除する](https://reference.aspose.com/cells/cpp/aspose.cells/cells/ungrouprows/)そして[列のグループ化を解除する](https://reference.aspose.com/cells/cpp/aspose.cells/cells/ungroupcolumns/)メソッド。どちらのメソッドも次の 2 つのパラメータを取ります。

- 最初の行または列のインデックス、グループ化を解除する最初の行/列。
- 最後の行または列のインデックス、グループ化を解除する最後の行/列。



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-GroupingUngroupingRowsAndColumns-UnGroupingRowsColumns-new.cpp" >}}
