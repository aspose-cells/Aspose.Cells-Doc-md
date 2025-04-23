---
title: 行と列の非表示および表示
type: docs
weight: 60
url: /ja/net/hiding-and-showing-rows-and-columns/
---

{{% alert color="primary" %}}

時々、ワークシートに特定の行または列を非表示にして後で表示することが理にかなっています。Microsoft Excelはこの機能を提供し、Aspose.Cellsも同様です。

{{% /alert %}}

## **行と列の可視性の制御**

Aspose.Cellsは、Microsoft Excelファイルを表す[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)クラスを提供します。[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)クラスには[**WorksheetCollection**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection)が含まれており、Excelファイルの各ワークシートにアクセスできるように開発者に提供します。ワークシートは[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラスで表されます。[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラスは、ワークシート内のすべてのセルを表す[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)コレクションを提供します。[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)コレクションは、ワークシートの行または列を管理するためのいくつかのメソッドを提供します。そのうちのいくつかについては以下で説明します。

### **行と列の非表示**

開発者は、[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)コレクションの[**HideRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/hiderow)および[**HideColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/hidecolumn)メソッドを呼び出すことで、特定の行または列を非表示にすることができます。両方のメソッドは、非表示にする特定の行または列のインデックスを取ります。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Hiding-HidingRowsAndColumns-1.cs" >}}

{{% alert color="primary" %}}

また、行または列を非表示にすることもできます。その際は、行の高さまたは列の幅をそれぞれ0に設定することができます。

{{% /alert %}}

### **行と列の表示**

開発者は、[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)コレクションの[**UnhideRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/unhiderow)および[**UnhideColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/unhidecolumn)メソッドを呼び出すことで、非表示になっている任意の行または列を表示することができます。両方のメソッドは2つのパラメーターを取ります。

- **行または列のインデックス** - 特定の行または列を表示するために使用される行または列のインデックス。
- **行の高さまたは列の幅** - 非表示にする行または列に割り当てられた行の高さまたは列の幅。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Hiding-UnhidingRowsAndColumns-1.cs" >}}

{{% alert color="primary" %}}

非表示にしている列を可視化する際、以前に割り当てられた幅に復元する必要がある場合は、負の幅の列を非表示にします。例: worksheet.Cells.UnhideColumn(5, -1)

{{% /alert %}}

### **複数の行および列の非表示**

開発者は、[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)コレクションの[**HideRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/hiderows)および[**HideColumns**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/hidecolumns)メソッドを呼び出すことで、一度に複数の行または列を非表示にすることができます。両方のメソッドは、非表示にする開始行または列のインデックスと非表示にする行または列の数をパラメーターとして取ります。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Hiding-HidingMultipleRowsAndColumns-1.cs" >}}

{{% alert color="primary" %}}

また、複数の行と列を表示するために[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)クラスの[**UnhideRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/unhiderows)および[**UnhideColumns**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/unhidecolumns)メソッドを使用することもできます。

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}
