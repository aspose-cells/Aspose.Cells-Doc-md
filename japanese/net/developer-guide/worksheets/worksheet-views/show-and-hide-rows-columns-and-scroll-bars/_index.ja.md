---
title: 行、列、およびスクロールバーを表示して非表示にする
type: docs
weight: 20
url: /ja/net/show-and-hide-rows-columns-and-scroll-bars/
description: この記事では、C#言語と.NET APIまたはライブラリを使用して、Excelワークシートの行と列をプログラムで表示および非表示にする方法を示します。スクロールバーの表示/非表示を調整することができ、複数の行や列を非表示にすることも可能です。
---

{{% alert color="primary" %}}

Aspose.Cellsはワークシートの行、列、およびスクロールバーの表示を制御する方法を提供しています。

{{% /alert %}}

## **行や列の表示と非表示**

Aspose.Cellsには、Microsoft Excelファイルを表す[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)クラスが提供されています。[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)クラスには[**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)コレクションが含まれ、Excelファイル内の各ワークシートにアクセスできるようになります。ワークシートは[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラスで表されます。[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラスにはワークシート内のすべてのセルを表す[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)コレクションがあります。[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)コレクションには、ワークシート内の行や列を管理するためのいくつかのメソッドが提供されています。そのうちいくつかについて以下で説明します。

### **行と列を表示**

開発者は、[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)コレクションの[**UnhideRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/unhiderow)および[**UnhideColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/unhidecolumn)メソッドを呼び出すことで、非表示になっている任意の行または列を表示することができます。両方のメソッドは2つのパラメーターを取ります。

- **行または列のインデックス** - 特定の行または列を表示するために使用される行または列のインデックス。
- **行の高さまたは列の幅** - 非表示にする行または列に割り当てられた行の高さまたは列の幅。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Hiding-UnhidingRowsAndColumns-1.cs" >}}

{{% alert color="primary" %}}

非表示にしている列を可視化する際、以前に割り当てられた幅に復元する必要がある場合は、負の幅の列を非表示にします。例: worksheet.Cells.UnhideColumn(5, -1)

{{% /alert %}}

### **行と列を非表示**

開発者は、[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)コレクションの[**HideRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/hiderow)および[**HideColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/hidecolumn)メソッドを呼び出すことで、特定の行または列を非表示にすることができます。両方のメソッドは、非表示にする特定の行または列のインデックスを取ります。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Hiding-HidingRowsAndColumns-1.cs" >}}

{{% alert color="primary" %}}

また、行または列を非表示にすることもできます。その際は、行の高さまたは列の幅をそれぞれ0に設定することができます。

{{% /alert %}}

### **複数の行と列を非表示**

開発者は、[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)コレクションの[**HideRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/hiderows)および[**HideColumns**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/hidecolumns)メソッドを呼び出すことで、一度に複数の行または列を非表示にすることができます。両方のメソッドは、非表示にする開始行または列のインデックスと非表示にする行または列の数をパラメーターとして取ります。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Hiding-HidingMultipleRowsAndColumns-1.cs" >}}

## **スクロールバーの表示と非表示**

スクロールバーは、どのファイルの内容をナビゲートするために使用されます。通常、2種類のスクロールバーがあります。

- 垂直スクロールバー
- 水平スクロールバー

Microsoft Excelは、ユーザーがワークシートの内容をスクロールできるように、水平および垂直のスクロールバーを提供しています。Aspose.Cellsを使用すると、Excelファイルの両方のタイプのスクロールバーの表示/非表示を制御することができます。

### **スクロールバーの表示を制御する**

Aspose.CellsはExcelファイルを表す[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)クラスを提供しています。[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)クラスにはExcelファイルを管理するためのさまざまなプロパティやメソッドが含まれています。スクロールバーの表示を制御するためには、[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)クラスの[**WorkbookSettings.IsVScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/isvscrollbarvisible)メソッドや[**WorkbookSettings.IsHScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/ishscrollbarvisible)プロパティを使用します。[**WorkbookSettings.IsVScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/isvscrollbarvisible)と[**WorkbookSettings.IsHScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/ishscrollbarvisible)はBooleanプロパティであり、これらのプロパティには**true**または**false**の値を格納できます。

#### **スクロールバーを表示する**

[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)クラスの[**WorkbookSettings.IsVScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/isvscrollbarvisible)プロパティまたは[**WorkbookSettings.IsHScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/ishscrollbarvisible)プロパティを**true**に設定することで、スクロールバーを表示します。

#### **スクロールバーを非表示にする**

[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)クラスの[**WorkbookSettings.IsVScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/isvscrollbarvisible)プロパティまたは[**WorkbookSettings.IsHScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/ishscrollbarvisible)プロパティを**false**に設定することで、スクロールバーを非表示にします。

**サンプルコード**

以下は、Excelファイルであるbook1.xlsを開き、両方のスクロールバーを非表示にし、変更されたファイルをoutput.xlsとして保存する完全なコードです。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Display-DisplayHideScrollBars-1.cs" >}}
