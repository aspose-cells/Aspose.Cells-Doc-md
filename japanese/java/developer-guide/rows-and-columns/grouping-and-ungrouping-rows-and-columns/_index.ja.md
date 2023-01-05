---
title: 行と列のグループ化とグループ解除
type: docs
weight: 40
url: /ja/java/grouping-and-ungrouping-rows-and-columns/
---
## **序章**
Microsoft Excel ファイルでは、データのアウトラインを作成して、マウスを 1 回クリックするだけで詳細レベルを表示および非表示にすることができます。

クリック**外形記号**、1、2、3、+、および - を使用して、ワークシート内のセクションの要約または見出しを提供する行または列のみをすばやく表示するか、シンボルを使用して、下の図に示すように個々の要約または見出しの下に詳細を表示できます。 :

行と列のグループ化

![todo:画像_代替_文章](grouping-and-ungrouping-rows-and-columns_1.png)
## **行と列のグループ管理**
Aspose.Cells はクラスを提供し、[ワークブック](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)Microsoft Excel ファイルを表します。の[ワークブック](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)クラスには[ワークシート](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection)Excel ファイル内の各ワークシートにアクセスできるコレクション。ワークシートは、[ワークシート](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)クラス。の[ワークシート](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)クラスは[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)ワークシート内のすべてのセルを表すコレクション。

の[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)collection は、ワークシートの行または列を管理するためのいくつかの方法を提供します。これらのいくつかについては、以下で詳しく説明します。
### **行と列のグループ化**
行または列をグループ化するには、[グループ行](https://reference.aspose.com/cells/java/com.aspose.cells/cells#groupRows\(int,%20int,%20boolean\) ） と[グループ列](https://reference.aspose.com/cells/java/com.aspose.cells/cells#groupColumns\(int,%20int,%20boolean\) のメソッド[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)コレクション。どちらのメソッドも、次のパラメーターを取ります。

- 最初の行/列インデックス、グループ内の最初の行または列。
- 最後の行/列インデックス、グループ内の最後の行または列。
- グループ化後に行/列を非表示にするかどうかを指定するブール値パラメーターです。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-RowsAndColumns-GroupingRowsandColumns-1.java" >}}
## **グループ設定**
Microsoft Excel では、表示するグループ設定を構成することもできます。

- 詳細の下の要約行。
- 詳細の右側にある要約列。

**グループ設定** 

![todo:画像_代替_文章](grouping-and-ungrouping-rows-and-columns_2.png)

Worksheet クラスの Outline プロパティを使用して、これらのグループ設定を構成することができます。
### **詳細の下の要約行**
開発者は、[概要](https://reference.aspose.com/cells/java/com.aspose.cells/Outline)クラス'[概要RowBelow](https://reference.aspose.com/cells/java/com.aspose.cells/outline#SummaryRowBelow)方法。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-RowsAndColumns-SummaryRowBelow-1.java" >}}
### **詳細の右側にある要約列**
詳細の右側に要約列を表示するかどうかは、[概要](https://reference.aspose.com/cells/java/com.aspose.cells/Outline)クラス'[サマリー列右](https://reference.aspose.com/cells/java/com.aspose.cells/outline#SummaryColumnRight)方法。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-RowsAndColumns-SummaryRowRight-1.java" >}}
### **行と列のグループ解除**
グループ化された行または列のグループ化を解除するには、[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)コレクションの[行のグループ化を解除](https://reference.aspose.com/cells/java/com.aspose.cells/cells#ungroupRows\(int,%20int\) ） と[列のグループ化を解除](https://reference.aspose.com/cells/java/com.aspose.cells/cells#ungroupColumns\(int,%20int\)) メソッド。どちらのメソッドも同じパラメーターを取ります。

- 最初の行または列のインデックス。グループ化を解除する最初の行/列。
- 最後の行または列のインデックス、グループ化を解除する最後の行/列。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-UngroupingRowsandColumns-UngroupingRowsandColumns.java" >}}
