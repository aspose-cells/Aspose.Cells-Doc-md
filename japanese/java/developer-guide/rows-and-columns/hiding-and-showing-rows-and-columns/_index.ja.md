---
title: 行と列の非表示および表示
type: docs
weight: 50
url: /ja/java/hiding-and-showing-rows-and-columns/
---

## **紹介**
時には、ユーザーがワークシートの特定の行または列を非表示にし、後で表示する必要がある場合があります。Microsoft Excelではこの機能を提供しており、Aspose.Cellsも同様です。
## **行と列の表示を制御する**
Aspose.Cellsは、Microsoft Excelファイルを表す[Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)クラスを提供します。[Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) クラスには、Excelファイル内の各ワークシートへのアクセスを可能にする[WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) が含まれています。ワークシートは[Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) クラスによって表されます。[Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) クラスは、ワークシート内のすべてのセルを表す[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) コレクションを提供します。[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)[ ](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)コレクションには、ワークシート内の行または列を管理するためのいくつかのメソッドが提供されています。以下ではそのうちのいくつかを説明します。
### **行または列の非表示**
開発者は、[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) コレクションの [HideRow](https://reference.aspose.com/cells/java/com.aspose.cells/cells#hideRow-int-) と [HideColumn](https://reference.aspose.com/cells/java/com.aspose.cells/cells#hideColumn-int-) メソッドを呼び出して、行や列を非表示にできます。両方のメソッドは、非表示にしたい特定の行または列のインデックスをパラメータとして取ります。

{{% alert color="primary" %}} 

注: 行または列を非表示にすることは、行の高さまたは列の幅をそれぞれ0に設定することで可能です。

{{% /alert %}} 

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-HidingRowsandColumns-HidingRowsandColumns.java" >}}
### **行と列の表示**
開発者は、[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) コレクションの [UnhideRow](https://reference.aspose.com/cells/java/com.aspose.cells/cells#unhideRow-int-double-) と [UnhideColumn](https://reference.aspose.com/cells/java/com.aspose.cells/cells#unhideColumn-int-double-) メソッドを呼び出して、隠れている行や列を表示できます。両方のメソッドは2つのパラメータを取ります：

- **行または列のインデックス** - 特定の行または列を表示するために使用される行または列のインデックス。
- **行の高さまたは列の幅** - 表示された後の行の高さまたは列の幅。すると行または列はその後元の幅または高さに戻ります。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-UnhidingRowsandColumns-UnhidingRowsandColumns.java" >}}

{{% alert color="primary" %}} 

非表示の行/列を表示する際、以前に割り当てられた幅または高さ、または元の幅または高さに復元する必要がある場合は、負の幅または高さで行または列を非表示にした後、その行または列を再表示してください。例: worksheet.getCells().unhideColumn(5, -1)

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
