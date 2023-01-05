---
title: 行と列の表示と非表示
type: docs
weight: 60
url: /ja/net/hiding-and-showing-rows-and-columns/
---
{{% alert color="primary" %}}

場合によっては、ワークシートの特定の行または列を非表示にして後で表示することが理にかなっていることがあります。 Microsoft Excel はこの機能を提供し、Aspose.Cells も同様です。

{{% /alert %}}

## **行と列の可視性の制御**

Aspose.Cells はクラスを提供し、[**ワークブック**](https://reference.aspose.com/cells/net/aspose.cells/workbook)、Microsoft Excel ファイルを表します。の[**ワークブック**](https://reference.aspose.com/cells/net/aspose.cells/workbook)クラスには[**ワークシート コレクション**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection)これにより、開発者は Excel ファイル内の各ワークシートにアクセスできます。ワークシートは、[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラス。の[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラスは[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)ワークシート内のすべてのセルを表すコレクション。の[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)コレクションには、ワークシートの行または列を管理するためのメソッドがいくつか用意されています。これらのいくつかを以下で説明します。

### **行と列を非表示にする**

開発者は、を呼び出して行または列を非表示にできます。[**行を非表示**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/hiderow)と[**HideColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/hidecolumn)のメソッド[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)それぞれコレクション。どちらのメソッドも、特定の行または列を非表示にするために、行と列のインデックスをパラメーターとして受け取ります。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Hiding-HidingRowsAndColumns-1.cs" >}}

{{% alert color="primary" %}}

行の高さまたは列の幅をそれぞれ 0 に設定して、行または列を非表示にすることもできます。

{{% /alert %}}

### **行と列の表示**

開発者は、非表示の行または列を表示するには、[**再表示行**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/unhiderow)と[**列を非表示にしない**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/unhidecolumn)のメソッド[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)それぞれコレクション。どちらのメソッドも次の 2 つのパラメーターを取ります。

- **行または列のインデックス** 特定の行または列を表示するために使用される行または列のインデックス。
- **行の高さまたは列の幅** - 再表示後に行または列に割り当てられた行の高さまたは列の幅。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Hiding-UnhidingRowsAndColumns-1.cs" >}}

{{% alert color="primary" %}}

非表示の列を表示しているときに、以前に割り当てられた幅または元の幅に戻す必要がある場合は、負の幅の列を再表示してください。例: worksheet.Cells.UnhideColumn(5, -1)

{{% /alert %}}

### **複数の行と列を非表示にする**

開発者は、複数の行または列を一度に非表示にするには、[**HideRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/hiderows)と[**HideColumns**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/hidecolumns)のメソッド[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)それぞれコレクション。どちらのメソッドも、開始行または列のインデックスと、非表示にする行または列の数をパラメーターとして受け取ります。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Hiding-HidingMultipleRowsAndColumns-1.cs" >}}

{{% alert color="primary" %}}

を使用することも可能です[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)クラス'[**再表示行**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/unhiderows)と[**非表示の列**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/unhidecolumns)複数の行と列を表示するメソッド。

{{% /alert %}}
