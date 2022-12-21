---
title: 行と列のグループ化とグループ解除
type: docs
weight: 50
url: /ja/net/grouping-and-ungrouping-rows-and-columns/
---
## **序章**

Microsoft Excel ファイルでは、データのアウトラインを作成して、マウスを 1 回クリックするだけで詳細レベルを表示および非表示にすることができます。

クリック**外形記号**、1、2、3、+、および - を使用して、ワークシート内のセクションの要約または見出しを提供する行または列のみをすばやく表示するか、シンボルを使用して、下の図に示すように個々の要約または見出しの下に詳細を表示できます。 :

|**行と列のグループ化。**|
|:- |
|![todo:画像_代替_文章](grouping-and-ungrouping-rows-and-columns_1.png)|

## **行と列のグループ管理**

Aspose.Cells はクラスを提供し、[**ワークブック**](https://reference.aspose.com/cells/net/aspose.cells/workbook) Microsoft Excel ファイルを表します。の[**ワークブック**](https://reference.aspose.com/cells/net/aspose.cells/workbook)クラスには[**ワークシート コレクション**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection)これにより、Excel ファイル内の各ワークシートにアクセスできます。ワークシートは、[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラス。の[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラスは[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)ワークシート内のすべてのセルを表すコレクション。

の[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)collection は、ワークシートの行または列を管理するためのいくつかの方法を提供します。これらのいくつかについては、以下で詳しく説明します。

### **行と列のグループ化**

行または列をグループ化するには、[**グループ行**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/grouprows/index)と[**グループ列**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/groupcolumns/index)のメソッド[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)コレクション。どちらのメソッドも、次のパラメーターを取ります。

- 最初の行/列インデックス、グループ内の最初の行または列。
- 最後の行/列インデックス、グループ内の最後の行または列。
- グループ化後に行/列を非表示にするかどうかを指定するブール値パラメーターです。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Grouping-GroupingRowsAndColumns-1.cs" >}}

#### **グループ設定**

Microsoft Excel では、表示するグループ設定を構成できます。

- 詳細の下の要約行。
- 詳細の右側にある要約列。

開発者は、[**概要**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/outline)のプロパティ[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラス。

### **詳細の下への要約行**

を設定することで、要約行を詳細の下に表示するかどうかを制御できます。[**概要**](https://reference.aspose.com/cells/net/aspose.cells/outline)クラス'[**概要RowBelow**](https://reference.aspose.com/cells/net/aspose.cells/outline/properties/summaryrowbelow)プロパティへ**真実**また**間違い**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Grouping-SummaryRowBelow-1.cs" >}}

### **詳細の右側にある要約列**

開発者は、詳細の右側に表示される集計列を制御することもできます。[**サマリー列右**](https://reference.aspose.com/cells/net/aspose.cells/outline/properties/summarycolumnright)のプロパティ[**概要**](https://reference.aspose.com/cells/net/aspose.cells/outline)クラスへ**真実**また**間違い**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Grouping-SummaryRowRight-1.cs" >}}

## **行と列のグループ解除**

グループ化された行または列のグループ化を解除するには、[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)コレクションの[**行のグループ化を解除**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/ungrouprows/index)と[**列のグループ化を解除**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/ungroupcolumns)メソッド。どちらのメソッドも次の 2 つのパラメーターを取ります。

- 最初の行または列のインデックス。グループ化を解除する最初の行/列。
- 最後の行または列のインデックス、グループ化を解除する最後の行/列。

[**行のグループ化を解除**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/ungrouprows/index)Boolean の 3 番目のパラメーターを取るオーバーロードがあります。に設定する**真実**グループ化されたすべての情報を削除します。それ以外の場合は、外側のグループ情報のみが削除されます。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Grouping-UngroupingRowsAndColumns-1.cs" >}}
