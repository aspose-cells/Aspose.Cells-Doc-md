---
title: 行と列の表示と非表示
type: docs
weight: 50
url: /ja/java/hiding-and-showing-rows-and-columns/
---
## **序章**
場合によっては、ワークシートの特定の行または列を非表示にして後で表示する必要がある場合もあります。 Microsoft Excel はこの機能を提供し、Aspose.Cells と同様です。
## **行と列の可視性の制御**
Aspose.Cells はクラスを提供し、[ワークブック](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)、Microsoft Excel ファイルを表します。の[ワークブック](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)クラスには[ワークシート コレクション](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection)これにより、Excel ファイル内の各ワークシートにアクセスできます。ワークシートは、[ワークシート](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)クラス。の[ワークシート](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)クラスは[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)ワークシート内のすべてのセルを表すコレクション。の[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)[](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)コレクションには、ワークシートの行または列を管理するためのメソッドがいくつか用意されています。これらのいくつかを以下で説明します。
### **行または列を非表示にする**
開発者は、を呼び出して行または列を非表示にできます。[行を非表示](https://reference.aspose.com/cells/java/com.aspose.cells/cells#hideRow\(int\) ） と[HideColumn](https://reference.aspose.com/cells/java/com.aspose.cells/cells#hideColumn\(int\) のメソッド[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)それぞれコレクション。どちらのメソッドも、特定の行または列を非表示にするために、行/列のインデックスをパラメーターとして受け取ります。

{{% alert color="primary" %}} 

注: 行の高さまたは列の幅をそれぞれ 0 に設定すると、行または列を非表示にすることもできます。

{{% /alert %}} 

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-HidingRowsandColumns-HidingRowsandColumns.java" >}}
### **行と列の表示**
開発者は、非表示の行または列を再表示できます。[再表示行](https://reference.aspose.com/cells/java/com.aspose.cells/cells#unhideRow\(int,%20double\) ） と[列を非表示にしない](https://reference.aspose.com/cells/java/com.aspose.cells/cells#unhideColumn\(int,%20double\) のメソッド[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)それぞれコレクション。どちらのメソッドも次の 2 つのパラメーターを取ります。

- **行または列のインデックス** 特定の行または列を表示するために使用される行または列のインデックス。
- **行の高さまたは列の幅** 行または列が表示された後に割り当てられる行の高さまたは列の幅。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-UnhidingRowsandColumns-UnhidingRowsandColumns.java" >}}

{{% alert color="primary" %}} 

非表示の列/行を表示しているときに、以前に割り当てられた幅または高さ、または元の幅または高さに戻す必要がある場合は、負の幅または高さの列または行を再表示してください。たとえば、worksheet.getCells().unhideColumn(5, -1)

{{% /alert %}}
