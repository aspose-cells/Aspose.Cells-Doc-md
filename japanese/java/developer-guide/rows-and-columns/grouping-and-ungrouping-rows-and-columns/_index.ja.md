---
title: 行と列のグループ化および展開
type: docs
weight: 40
url: /ja/java/grouping-and-ungrouping-rows-and-columns/
---

## **紹介**
Microsoft Excelファイルでは、データの概要を作成して、1回のマウスクリックで詳細のレベルを表示したり非表示にしたりできます。

**アウトライン記号**の1、2、3、+、および-をクリックして、ワークシートのセクションの要約または見出しを迅速に表示したり、個々の要約または見出しの詳細を表示する際に使用できます。下の図で示されているように、個々の要約または見出しの詳細を表示するためにシンボルを使用できます。

行と列のグループ化 

![todo:image_alt_text](grouping-and-ungrouping-rows-and-columns_1.png)
## **行と列のグループ管理**
Aspose.Cellsは、Microsoft Excelファイルを表す[Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) クラスを提供しています。[Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) クラスには、Excelファイル内の各ワークシートにアクセスする機能を提供する[Worksheets](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) コレクションが含まれています。ワークシートは[Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) クラスによって表されます。[Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) クラスは、ワークシート内のすべてのセルを表す[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) コレクションを提供します。

[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) コレクションには、ワークシート内の行または列を管理するための複数のメソッドが提供されています。これについての詳細は、以下でさらに説明します。
### **行と列のグループ化**
[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) コレクションの [groupRows](https://reference.aspose.com/cells/java/com.aspose.cells/cells#groupRows-int-int-boolean-) と [groupColumns](https://reference.aspose.com/cells/java/com.aspose.cells/cells#groupColumns-int-int-boolean-) メソッドを呼び出すことで、行または列をグループ化できます。両方のメソッドは次のパラメータを取ります：

- 最初の行/列インデックス、グループ内の最初の行または列
 - グループ内の最後の行/列のインデックス、最後の行または列。
- 非表示かどうか、グループ化後に行または列を非表示にするかどうかを指定するブールパラメータ。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-RowsAndColumns-GroupingRowsandColumns-1.java" >}}
## **グループ設定**
Microsoft Excelでは、**グループ設定**を表示するための設定を構成することもできます。

- 詳細の下の要約行。
- 詳細の右側に要約列を設定します。

**グループ設定** 

![todo:image_alt_text](grouping-and-ungrouping-rows-and-columns_2.png)

WorksheetクラスのOutlineプロパティを使用して、これらのグループ設定を構成することが可能です。
### **詳細の下の要約行**
開発者は、[Outline](https://reference.aspose.com/cells/java/com.aspose.cells/Outline)クラスの[SummaryRowBelow](https://reference.aspose.com/cells/java/com.aspose.cells/outline#SummaryRowBelow)メソッドを使用して、詳細の下に要約行を表示するかを制御することができます。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-RowsAndColumns-SummaryRowBelow-1.java" >}}
### **詳細の右側にサマリー列**
開発者は、[Outline](https://reference.aspose.com/cells/java/com.aspose.cells/Outline)クラスの[SummaryColumnRight](https://reference.aspose.com/cells/java/com.aspose.cells/outline#SummaryColumnRight)メソッドを使用して、要約列が詳細の右側に表示されるかどうかを制御することができます。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-RowsAndColumns-SummaryRowRight-1.java" >}}
### **行と列のグループ解除**
グループ化された行や列を解除するには、[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) コレクションの [UngroupRows](https://reference.aspose.com/cells/java/com.aspose.cells/cells#ungroupRows-int-int-) と [UngroupColumns](https://reference.aspose.com/cells/java/com.aspose.cells/cells#ungroupColumns-int-int-) メソッドを呼び出します。両方のメソッドは同じパラメータを取ります：

- 最初の行または列のインデックス、グループ化を解除する最初の行/列。
- 最後の行または列のインデックス、グループ化を解除する最後の行/列。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-UngroupingRowsandColumns-UngroupingRowsandColumns.java" >}}
{{< app/cells/assistant language="java" >}}
