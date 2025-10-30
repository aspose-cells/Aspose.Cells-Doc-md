---
title: グリッド線と行列ヘッダーの表示および非表示
type: docs
weight: 30
url: /ja/python-net/show-and-hide-gridlines-and-row-column-headers/
description: この記事は、Aspose.Cells for Python via .NET APIを使用して、Excelワークシートのグリッドラインや行と列のヘッダーをプログラム的に非表示または表示するサンプルコードを提供します。
keywords: Python Excelライブラリ、Pythonのグリッドラインの表示と非表示、Pythonで行と列のヘッダーを表示・非表示、グリッドラインや行列ヘッダーの表示・非表示の方法。
---

{{% alert color="primary" %}}

Aspose.Cells for Python via .NETは、デフォルトで表示されるワークシートのグリッドラインの非表示と表示をサポートします。また、ワークシートの行列ヘッダーの表示・非表示も制御できます。

{{% /alert %}}

## **グリッド線の表示と非表示**

すべてのExcelワークシートはデフォルトでグリッド線を持っています。これにより、特定のセルにデータを入力することが簡単になります。グリッド線により、ワークシートをセルのコレクションとして表示し、各セルを簡単に識別することができます。

### **グリッド線の表示の制御**

Aspose.Cells for Python via .NETは、Microsoft Excelファイルを表す[**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/)クラスを提供します。[**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/)クラスは、Excelファイル内の各ワークシートにアクセスできる[**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets/)コレクションを含みます。ワークシートは[**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/)クラスによって表されます。[**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/)クラスは、ワークシートの管理のためのさまざまなプロパティとメソッドを提供します。グリッドラインの表示を制御するには、[**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/)クラスの[**is_gridlines_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_gridlines_visible/)プロパティを使用します。[**is_gridlines_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_gridlines_visible/)は真偽値のプロパティで、「true」または「false」の値だけを格納できます。

#### **グリッド線を表示する**

[**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet)クラスの[**is_gridlines_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_gridlines_visible/)プロパティを**true**に設定することでグリッド線を表示します。

#### **グリッド線を非表示にする**

[**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet)クラスの[**is_gridlines_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_gridlines_visible/)プロパティを**false**に設定することでグリッド線を非表示にします。

以下に完全な例が示されており、[**is_gridlines_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_gridlines_visible/)のプロパティを使用して、Excelファイル（book1.xls）を開き、最初のワークシートでグリッド線を非表示にし、変更されたファイルをoutput.xlsとして保存する方法を示しています。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Views-Display-DisplayHideGridlines-1.py" >}}

## **行列ヘッダーの表示および非表示**

Excelファイル内のすべてのワークシートは、行と列に並ぶセルで構成されています。すべての行と列には、識別やセルを特定するためのユニークな値があります。例えば、行は1, 2, 3, 4などの番号が付けられ、列はアルファベット順にA, B, C, Dなどで表されます。行と列の値はヘッダーに表示されます。Aspose.Cells for Python via .NETを使用すると、これらの行と列のヘッダーの表示/非表示を制御できます。

### **ワークシートの表示を制御する**

Aspose.Cells for Python via .NETは、[**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/)クラスを提供します。[**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/)クラスは、Excelファイル内の各ワークシートにアクセス可能な[**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets/)コレクションを含みます。ワークシートは[**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/)クラスによって表されます。[**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/)クラスは、ワークシートの管理に幅広く使用できるプロパティとメソッドを提供します。行と列のヘッダーの表示・非表示を制御するには、[**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/)クラスの[**is_row_column_headers_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_row_column_headers_visible/)プロパティを使用します。[**is_row_column_headers_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_row_column_headers_visible/)は真偽値のプロパティです。

#### **行/列ヘッダーを表示する**

[**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet)クラスの[**is_row_column_headers_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_row_column_headers_visible/)プロパティを**true**に設定することで行と列のヘッダーを表示します。

#### **行/列ヘッダーを非表示にする**

[**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet)クラスの[**is_row_column_headers_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_row_column_headers_visible/)プロパティを**false**に設定することで行と列のヘッダーを非表示にします。

以下に完全な例が示されており、[**is_row_column_headers_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_row_column_headers_visible/)のプロパティを使用して、Excelファイル（book1.xls）を開き、最初のワークシートで行と列のヘッダーを非表示にし、変更されたファイルをoutput.xlsとして保存する方法を示しています。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Views-Display-DisplayHideRowColumnHeaders-1.py" >}}

{{% alert color="primary" %}}

また、[**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells)クラスの[**unhide_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/unhide_rows)メソッドと[**unhide_columns**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/unhide_columns)メソッドを使用して、複数の行と列を表示したり非表示にしたりすることも可能です。

{{% /alert %}}
{{< app/cells/assistant language="python-net" >}}
