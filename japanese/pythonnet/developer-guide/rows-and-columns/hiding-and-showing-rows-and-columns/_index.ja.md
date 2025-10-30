---
title: 行と列の非表示および表示
type: docs
weight: 60
url: /ja/python-net/hiding-and-showing-rows-and-columns/
description: この記事では、Aspose.Cells for Python via .NET API を使用して行と列の非表示と表示方法を説明します。
keywords: Python Excel ライブラリ、Aspose.Cells Python による行と列の非表示と表示、Python での行と列の非表示、Python での行と列の表示。
---

{{% alert color="primary" %}}

ワークシートの特定の行または列を非表示にして後で表示することは、時々意味をなします。Microsoft Excel がこの機能を提供しているように、Aspose.Cells for Python via .NET も同様の機能を提供しています。

{{% /alert %}}

## **行と列の可視性の制御**

Aspose.Cells for Python via .NETは、Microsoft Excelファイルを表す[**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)クラスを提供します。[**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)クラスには、Excelファイル内の各ワークシートにアクセスするための[**WorksheetCollection**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheetcollection)が含まれています。ワークシートは[**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet)クラスによって表されます。[**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet)クラスは、ワークシート内のすべてのセルを表す[**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells)コレクションを提供します。[**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells)コレクションには、ワークシート内の行や列を管理するためのいくつかのメソッドが用意されています。そのうちのいくつかについて以下で説明します。

## **行や列の非表示方法**

開発者は、[**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells)コレクションの[**hide_row**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/hide_row/)および[**hide_column**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/hide_column/)メソッドを呼び出すことで、特定の行または列を非表示にすることができます。両方のメソッドは、非表示にする特定の行または列のインデックスを取ります。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-Hiding-HidingRowsAndColumns-1.py" >}}

{{% alert color="primary" %}}

また、行または列を非表示にすることもできます。その際は、行の高さまたは列の幅をそれぞれ0に設定することができます。

{{% /alert %}}

## **行や列の表示方法**

開発者は、[**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells)コレクションの[**unhide_row**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/unhide_row/)および[**unhide_column**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/unhide_column/)メソッドを呼び出すことで、非表示になっている任意の行または列を表示することができます。両方のメソッドは2つのパラメーターを取ります。

- **行または列のインデックス** - 特定の行または列を表示するために使用される行または列のインデックス。
- **行の高さまたは列の幅** - 非表示にする行または列に割り当てられた行の高さまたは列の幅。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-Hiding-UnhidingRowsAndColumns-1.py" >}}

{{% alert color="primary" %}}

非表示にしている列を可視化する際、以前に割り当てられた幅に復元する必要がある場合は、負の幅の列を非表示にします。例: worksheet.Cells.UnhideColumn(5, -1)

{{% /alert %}}

## **複数の行や列を非表示にする方法**

開発者は、[**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells)コレクションの[**hide_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/hide_rows/)および[**hide_columns**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/hide_columns/)メソッドを呼び出すことで、一度に複数の行または列を非表示にすることができます。両方のメソッドは、非表示にする開始行または列のインデックスと非表示にする行または列の数をパラメーターとして取ります。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-Hiding-HidingMultipleRowsAndColumns-1.py" >}}

{{% alert color="primary" %}}

また、複数の行と列を表示するために[**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells)クラスの[**unhide_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/unhide_rows/)および[**unhide_columns**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/unhide_columns/)メソッドを使用することもできます。

{{% /alert %}}
{{< app/cells/assistant language="python-net" >}}
