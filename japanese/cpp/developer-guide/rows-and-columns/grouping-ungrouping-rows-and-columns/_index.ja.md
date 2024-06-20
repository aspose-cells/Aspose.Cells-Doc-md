---
title: 行と列のグルーピングおよびグループ解除
type: docs
weight: 30
url: /ja/cpp/grouping-ungrouping-rows-and-columns/
---

## **紹介**
Microsoft Excelファイルでは、データの概要を作成して、1回のマウスクリックで詳細のレベルを表示したり非表示にしたりできます。

「アウトライン記号」の**1、2、3、+、-**をクリックして、ワークシート内のセクションの要約または見出しを提供する行または列のみをすばやく表示するか、個々の要約または見出しの下に詳細を表示するためにこの記号を使用できます。
## **行と列のグループ管理**
Aspose.Cellsは、Microsoft Excelファイルを表す[Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)クラスを提供しています。[Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)クラスには、Excelファイル内の各ワークシートにアクセスを許可する[Worksheets](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/)コレクションが含まれています。ワークシートは[Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)クラスによって表されます。[Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)クラスは、ワークシート内のすべてのセルを表す[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)コレクションを提供します。

[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)コレクションには、ワークシート内の行や列を管理するためのいくつかのメソッドが提供されており、そのうちのいくつかについて詳しく説明します。
### **行と列のグループ化**
[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)コレクションの[GroupRows](https://reference.aspose.com/cells/cpp/aspose.cells/cells/grouprows/)および[GroupColumns](https://reference.aspose.com/cells/cpp/aspose.cells/cells/groupcolumns/)メソッドを呼び出すことで、行または列をグループ化することができます。両方のメソッドは、以下のパラメータを取ります:

- 最初の行/列インデックス、グループ内の最初の行または列。
- 最後の行/列インデックス、グループ内の最後の行または列。
- 非表示かどうか、グループ化後に行または列を非表示にするかどうかを指定するブールパラメータ。



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-GroupingUngroupingRowsAndColumns-GroupingRowsColumns-new.cpp" >}}
#### **グループ設定**
Microsoft Excelでは、以下を表示するためのグループ設定を構成できます:

- 詳細の下の要約行。
- 詳細の右側の要約列。
## **行と列のグループ解除**
グループ化された行や列を解除するには、[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)コレクションの[UngroupRows](https://reference.aspose.com/cells/cpp/aspose.cells/cells/ungrouprows/)および[UngroupColumns](https://reference.aspose.com/cells/cpp/aspose.cells/cells/ungroupcolumns/)メソッドを呼び出します。両方のメソッドは2つのパラメータを取ります:

- 最初の行または列インデックス、解除される最初の行または列。
- 最後の行または列インデックス、解除される最後の行または列。



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-GroupingUngroupingRowsAndColumns-UnGroupingRowsColumns-new.cpp" >}}
