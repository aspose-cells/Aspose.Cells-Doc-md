---
title: 行と列のグループ化および展開
type: docs
weight: 50
url: /ja/net/grouping-and-ungrouping-rows-and-columns/
---

## **紹介**

Microsoft Excelファイルでは、データの概要を作成して、1回のマウスクリックで詳細のレベルを表示したり非表示にしたりできます。

**アウトライン記号**の1、2、3、+、および-をクリックして、ワークシートのセクションの要約または見出しを迅速に表示したり、個々の要約または見出しの詳細を表示する際に使用できます。下の図で示されているように、個々の要約または見出しの詳細を表示するためにシンボルを使用できます。

|**行と列のグループ化**|
| :- |
|![todo:image_alt_text](grouping-and-ungrouping-rows-and-columns_1.png)|

## **行と列のグループ管理**

Aspose.CellsはMicrosoft Excelファイルを表す[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)クラスを提供しており、[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)クラスにはExcelファイル内の各ワークシートにアクセスするための[**WorksheetCollection**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection)が含まれています。ワークシートは[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラスによって表されます。[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラスはワークシート内のすべてのセルを表す[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)コレクションを提供します。

[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)コレクションには、ワークシート内の行や列を管理するためのいくつかのメソッドが提供されており、そのうちいくつかについて以下で詳しく説明します。

### **行と列のグループ化**

行と列をグループ化するには、[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)コレクションの[**GroupRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/grouprows/index)および[**GroupColumns**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/groupcolumns/index)メソッドを呼び出すことができます。両方のメソッドは以下のパラメーターを受け取ります:

- 最初の行/列インデックス、グループ内の最初の行または列
 - グループ内の最後の行/列のインデックス、最後の行または列。
- 非表示かどうか、グループ化後に行または列を非表示にするかどうかを指定するブールパラメータ。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Grouping-GroupingRowsAndColumns-1.cs" >}}

#### **グループ設定**

Microsoft Excelでは、以下を表示するためのグループ設定を構成できます:

- 詳細の下の要約行。
- 詳細の右側の要約列。

開発者は、[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラスの[**Outline**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/outline)プロパティを使用して、これらのグループ設定を構成できます。

### **詳細の下にサマリー行**

サマリー行が詳細の下に表示されるかどうかは、[**Outline**](https://reference.aspose.com/cells/net/aspose.cells/outline)クラスの[**SummaryRowBelow**](https://reference.aspose.com/cells/net/aspose.cells/outline/properties/summaryrowbelow)プロパティを**true**または**false**に設定することで制御できます。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Grouping-SummaryRowBelow-1.cs" >}}

### **詳細の右側にサマリー列**

開発者は、[**Outline**](https://reference.aspose.com/cells/net/aspose.cells/outline)クラスの[**SummaryColumnRight**](https://reference.aspose.com/cells/net/aspose.cells/outline/properties/summarycolumnright)プロパティを**true**または**false**に設定することで、詳細の右側にサマリー列を表示することもできます。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Grouping-SummaryRowRight-1.cs" >}}

## **行と列のグループ解除**

グループ化された行または列を解除するには、{1}のコレクションの{2}および{3}メソッドを呼び出します。どちらのメソッドも2つのパラメーターを取ります。

- 最初の行または列のインデックス、グループ化を解除する最初の行/列。
- 最後の行または列のインデックス、グループ化を解除する最後の行/列。

[**UngroupRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/ungrouprows/index)には、ブール値の第三パラメーターを取るオーバーロードがあります。これを**true**に設定すると、グループ化された情報がすべて削除されます。それ以外の場合は、外部グループ化情報のみが削除されます。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Grouping-UngroupingRowsAndColumns-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
