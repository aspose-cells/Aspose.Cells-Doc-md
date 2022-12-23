---
title: 行、列、およびスクロール バーの表示と非表示
type: docs
weight: 20
url: /ja/net/show-and-hide-rows-columns-and-scroll-bars/
description: この記事では、C# 言語と .NET API またはライブラリを使用して、Excel ワークシートの行と列をプログラムで表示および非表示にする方法を示します。スクロール バーの表示を調整したり、いくつかの行や列を非表示にしたりできます。
---
{{% alert color="primary" %}}

Aspose.Cells は、ワークシートの行、列、およびスクロール バーの表示を制御する方法を提供します。

{{% /alert %}}

## **行と列の表示と非表示**

Aspose.Cells はクラスを提供し、[**ワークブック**](https://reference.aspose.com/cells/net/aspose.cells/workbook)、Microsoft Excel ファイルを表します。の[**ワークブック**](https://reference.aspose.com/cells/net/aspose.cells/workbook)クラスには[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)開発者が Excel ファイル内の各ワークシートにアクセスできるようにするコレクション。ワークシートは、[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラス。の[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラスは[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)ワークシート内のすべてのセルを表すコレクション。の[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)コレクションには、ワークシートの行または列を管理するためのメソッドがいくつか用意されています。これらのいくつかを以下で説明します。

### **行と列を表示**

開発者は、非表示の行または列を表示するには、[**再表示行**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/unhiderow)と[**列を非表示にしない**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/unhidecolumn)のメソッド[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)それぞれコレクション。どちらのメソッドも次の 2 つのパラメーターを取ります。

- **行または列のインデックス** 特定の行または列を表示するために使用される行または列のインデックス。
- **行の高さまたは列の幅** - 再表示後に行または列に割り当てられた行の高さまたは列の幅。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Hiding-UnhidingRowsAndColumns-1.cs" >}}

{{% alert color="primary" %}}

非表示の列を表示しているときに、以前に割り当てられた幅または元の幅に戻す必要がある場合は、負の幅の列を再表示してください。例: worksheet.Cells.UnhideColumn(5, -1)

{{% /alert %}}

### **行と列を非表示にする**

開発者は、を呼び出して行または列を非表示にできます。[**行を非表示**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/hiderow)と[**HideColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/hidecolumn)のメソッド[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)それぞれコレクション。どちらのメソッドも、特定の行または列を非表示にするために、行と列のインデックスをパラメーターとして受け取ります。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Hiding-HidingRowsAndColumns-1.cs" >}}

{{% alert color="primary" %}}

行の高さまたは列の幅をそれぞれ 0 に設定して、行または列を非表示にすることもできます。

{{% /alert %}}

### **複数の行と列を非表示にする**

開発者は、複数の行または列を一度に非表示にするには、[**HideRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/hiderows)と[**HideColumns**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/hidecolumns)のメソッド[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)それぞれコレクション。どちらのメソッドも、開始行または列のインデックスと、非表示にする行または列の数をパラメーターとして受け取ります。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Hiding-HidingMultipleRowsAndColumns-1.cs" >}}

## **スクロール バーの表示と非表示**

スクロール バーは、ファイルの内容をナビゲートするために使用されます。通常、スクロール バーには次の 2 種類があります。

- 垂直スクロール バー
- 水平スクロール バー

Microsoft Excel には、ユーザーがワークシートの内容をスクロールできるように、水平および垂直のスクロール バーも用意されています。 Aspose.Cells を使用すると、開発者は Excel ファイルで両方のタイプのスクロール バーの表示を制御できます。

### **スクロール バーの表示を制御する**

Aspose.Cells はクラスを提供し、[**ワークブック**](https://reference.aspose.com/cells/net/aspose.cells/workbook)これは Excel ファイルを表します。の[**ワークブック**](https://reference.aspose.com/cells/net/aspose.cells/workbook)クラスには、Excel ファイルを管理するためのさまざまなプロパティとメソッドが用意されています。スクロール バーの表示を制御するには、[**ワークブック**](https://reference.aspose.com/cells/net/aspose.cells/workbook)クラス'[**WorkbookSettings.IsVScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/isvscrollbarvisible)と[**WorkbookSettings.IsHScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/ishscrollbarvisible)プロパティ。[**WorkbookSettings.IsVScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/isvscrollbarvisible)と[**WorkbookSettings.IsHScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/ishscrollbarvisible)はブール型のプロパティです。つまり、これらのプロパティは格納のみ可能です。**真実**また**間違い**値。

#### **スクロール バーを表示する**

を設定して、スクロール バーを表示します。[**ワークブック**](https://reference.aspose.com/cells/net/aspose.cells/workbook)クラス'[**WorkbookSettings.IsVScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/isvscrollbarvisible)また[**WorkbookSettings.IsHScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/ishscrollbarvisible)プロパティへ**真実**.

#### **スクロール バーを非表示にする**

を設定してスクロール バーを非表示にします。[**ワークブック**](https://reference.aspose.com/cells/net/aspose.cells/workbook)クラス'[**WorkbookSettings.IsVScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/isvscrollbarvisible)また[**WorkbookSettings.IsHScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/ishscrollbarvisible)プロパティへ**間違い**.

**サンプルコード**

以下は、Excel ファイル book1.xls を開き、両方のスクロール バーを非表示にしてから、変更したファイルを output.xls として保存する完全なコードです。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Display-DisplayHideScrollBars-1.cs" >}}
