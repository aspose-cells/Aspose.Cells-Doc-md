---
title: 行、列、およびスクロールバーを表示して非表示にする
type: docs
weight: 20
url: /ja/python-net/show-and-hide-rows-columns-and-scroll-bars/
description: この記事は、Aspose.Cells for Python via .NET APIを使用して、Excelワークシートの行と列の表示・非表示をプログラム的に操作する方法を示します。スクロールバーの表示も調整可能で、複数の行と列を非表示にできます。
keywords: Python Excelライブラリ、行と列の表示と非表示、行と列の非表示方法、縦スクロールバーの表示、横スクロールバーの表示、縦スクロールバーの非表示、横スクロールバーの非表示、行・列・スクロールバーの表示・非表示。
---

{{% alert color="primary" %}}

Aspose.Cells for Python via .NETは、ワークシートの行、列、スクロールバーの表示/非表示を制御する方法を提供します。

{{% /alert %}}

## **行や列の表示と非表示**

Aspose.Cells for Python via .NETは、[**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)クラスを提供します。[**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)クラスは、Excelファイル内の各ワークシートにアクセスできる[**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets)コレクションを含みます。[**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet)クラスは、すべてのセルを表す[**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet)コレクションを提供します。[**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells)コレクションは、行や列を管理するいくつかのメソッドを提供します。

### **行と列を表示**

開発者は、[**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells/)コレクションの[**unhide_row**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/unhide_row/)および[**unhide_column**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/unhide_column/)メソッドを呼び出すことで、非表示になっている任意の行または列を表示することができます。両方のメソッドは2つのパラメーターを取ります。

- **行または列のインデックス** - 特定の行または列を表示するために使用される行または列のインデックス。
- **行の高さまたは列の幅** - 非表示にする行または列に割り当てられた行の高さまたは列の幅。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Views-RowsColumns-Hiding-UnhidingRowsAndColumns-1.py" >}}

{{% alert color="primary" %}}

非表示にしている列を可視化する際、以前に割り当てられた幅に復元する必要がある場合は、負の幅の列を非表示にします。例: worksheet.Cells.UnhideColumn(5, -1)

{{% /alert %}}

### **行と列を非表示**

開発者は、[**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells)コレクションの[**hide_row**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/hide_row/)および[**hide_column**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/hide_column/)メソッドを呼び出すことで、特定の行または列を非表示にすることができます。両方のメソッドは、非表示にする特定の行または列のインデックスを取ります。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Views-RowsColumns-Hiding-HidingRowsAndColumns-1.py" >}}

{{% alert color="primary" %}}

また、行または列を非表示にすることもできます。その際は、行の高さまたは列の幅をそれぞれ0に設定することができます。

{{% /alert %}}

### **複数の行と列を非表示**

開発者は、[**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells)コレクションの[**hide_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/hide_rows/)および[**hide_columns**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/hide_columns)メソッドを呼び出すことで、一度に複数の行または列を非表示にすることができます。両方のメソッドは、非表示にする開始行または列のインデックスと非表示にする行または列の数をパラメーターとして取ります。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Views-RowsColumns-Hiding-HidingMultipleRowsAndColumns-1.py" >}}

## **スクロールバーの表示と非表示**

スクロールバーは、どのファイルの内容をナビゲートするために使用されます。通常、2種類のスクロールバーがあります。

- 垂直スクロールバー
- 水平スクロールバー

Microsoft Excelは、ワークシートの内容をスクロールできる水平・垂直のスクロールバーも提供します。Aspose.Cells for Python via .NETを使用して、Excelファイルの両タイプのスクロールバーの表示/非表示を制御できます。

### **スクロールバーの表示を制御する**

Aspose.Cells for Python via .NETは、[**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)クラスを提供します。[**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)クラスは、Excelファイルの管理に幅広いプロパティとメソッドを含みます。スクロールバーの表示を制御するには、 [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)クラスの[**WorkbookSettings.is_v_scroll_bar_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/is_v_scroll_bar_visible)と[**WorkbookSettings.is_h_scroll_bar_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/is_h_scroll_bar_visible)プロパティを使用します。[**WorkbookSettings.is_v_scroll_bar_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/is_v_scroll_bar_visible)と[**WorkbookSettings.is_h_scroll_bar_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/is_h_scroll_bar_visible)は真偽値のプロパティであり、これらのプロパティには**true**または**false**の値のみを格納できます。

#### **スクロールバーを表示する**

[**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)クラスの[**WorkbookSettings.is_v_scroll_bar_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/is_v_scroll_bar_visible)プロパティまたは[**WorkbookSettings.is_h_scroll_bar_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/is_h_scroll_bar_visible)プロパティを**true**に設定することで、スクロールバーを表示します。

#### **スクロールバーを非表示にする**

[**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)クラスの[**WorkbookSettings.is_v_scroll_bar_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/is_v_scroll_bar_visible)プロパティまたは[**WorkbookSettings.is_h_scroll_bar_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/is_h_scroll_bar_visible)プロパティを**false**に設定することで、スクロールバーを非表示にします。

**サンプルコード**

以下は、Excelファイルであるbook1.xlsを開き、両方のスクロールバーを非表示にし、変更されたファイルをoutput.xlsとして保存する完全なコードです。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Views-Worksheets-Display-DisplayHideScrollBars-1.py" >}}
{{< app/cells/assistant language="python-net" >}}
