---
title: 行と列のグループ化および展開
type: docs
weight: 50
url: /ja/python-net/grouping-and-ungrouping-rows-and-columns/
description: この記事では、Aspose.Cells for Python via .NET API を使用して行と列のグループ化とグループ解除の方法を説明します。
keywords: Python Excel ライブラリ、Python での行と列のグループ化方法、Python での行と列のグループ解除方法、Python における行と列のグループ管理、Python での要約行の詳細の下に設定する方法、Python での要約列の右に設定する方法。
---

## **紹介**

Microsoft Excelファイルでは、データの概要を作成して、1回のマウスクリックで詳細のレベルを表示したり非表示にしたりできます。

**アウトライン記号**の1、2、3、+、および-をクリックして、ワークシートのセクションの要約または見出しを迅速に表示したり、個々の要約または見出しの詳細を表示する際に使用できます。下の図で示されているように、個々の要約または見出しの詳細を表示するためにシンボルを使用できます。

|**行と列のグループ化**|
| :- |
|![todo:image_alt_text](grouping-and-ungrouping-rows-and-columns_1.png)|

## **行と列のグループ管理**

Aspose.Cells for Python via .NET には、Microsoft Excel ファイルを表す [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) クラスが用意されています。[**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) クラスにはExcelファイル内の各ワークシートにアクセスすることを可能にする [**WorksheetCollection**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheetcollection) が含まれています。ワークシートは [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) クラスで表されます。[**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) クラスにはワークシート内のすべてのセルを表す [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) コレクションがあります。

[**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells)コレクションには、ワークシート内の行や列を管理するためのいくつかのメソッドが提供されており、そのうちいくつかについて以下で詳しく説明します。

### **行と列のグループ化方法**

行と列をグループ化するには、[**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells)コレクションの[**group_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/group_rows/#int-int-bool)および[**group_columns**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/group_columns/#int-int-bool)メソッドを呼び出すことができます。両方のメソッドは以下のパラメーターを受け取ります:

- 最初の行/列インデックス、グループ内の最初の行または列
 - グループ内の最後の行/列のインデックス、最後の行または列。
- 非表示かどうか、グループ化後に行または列を非表示にするかどうかを指定するブールパラメータ。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-Grouping-GroupingRowsAndColumns-1.py" >}}

#### **グループ設定**

Microsoft Excelでは、以下を表示するためのグループ設定を構成できます:

- 詳細の下の要約行。
- 詳細の右側の要約列。

開発者は、[**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet)クラスの[**outline**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/outline/)プロパティを使用して、これらのグループ設定を構成できます。

### **要約行を詳細の下に設定する方法**

サマリー行が詳細の下に表示されるかどうかは、[**Outline**](https://reference.aspose.com/cells/python-net/aspose.cells/outline)クラスの[**summary_row_below**](https://reference.aspose.com/cells/python-net/aspose.cells/outline/summary_row_below/)プロパティを**true**または**false**に設定することで制御できます。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-Grouping-SummaryRowBelow-1.py" >}}

### **要約列を詳細の右に設定する方法**

開発者は、[**Outline**](https://reference.aspose.com/cells/python-net/aspose.cells/outline)クラスの[**summary_column_right**](https://reference.aspose.com/cells/python-net/aspose.cells/outline/summary_column_right/)プロパティを**true**または**false**に設定することで、詳細の右側にサマリー列を表示することもできます。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-Grouping-SummaryRowRight-1.py" >}}

## **行と列のグループ解除方法**

グループ化された行または列を解除するには、{1}のコレクションの{2}および{3}メソッドを呼び出します。どちらのメソッドも2つのパラメーターを取ります。

- 最初の行または列のインデックス、グループ化を解除する最初の行/列。
- 最後の行または列のインデックス、グループ化を解除する最後の行/列。

[**ungroup_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/ungroup_rows/#int-int-bool)には、ブール値の第三パラメーターを取るオーバーロードがあります。これを**true**に設定すると、グループ化された情報がすべて削除されます。それ以外の場合は、外部グループ化情報のみが削除されます。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-Grouping-UngroupingRowsAndColumns-1.py" >}}
{{< app/cells/assistant language="python-net" >}}
