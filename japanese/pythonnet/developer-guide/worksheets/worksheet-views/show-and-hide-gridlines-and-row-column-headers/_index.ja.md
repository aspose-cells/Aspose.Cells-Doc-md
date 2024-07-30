---
title: グリッド線と行列ヘッダーの表示および非表示
type: docs
weight: 30
url: /ja/python-net/show-and-hide-gridlines-and-row-column-headers/
description: この記事は、Aspose.Cells for Python via .NET API を使用して Excel ワークシートのグリッド線、行、列見出しをプログラムで非表示または表示するためのサンプルコードを提供しています。
keywords: Python Excel ライブラリ、Python でのグリッド線の表示と非表示、Python での行列見出しの表示と非表示、Python でのグリッド線と行列見出しの表示と非表示の方法。
---

{{% alert color="primary" %}}

Aspose.Cells for Python via .NET は、デフォルトで表示されているワークシートのグリッド線を非表示または表示する機能をサポートしています。また、ワークシートの行列見出しの可視性を制御する機能も提供しています。

{{% /alert %}}

## **グリッド線の表示と非表示**

すべてのExcelワークシートはデフォルトでグリッド線を持っています。これにより、特定のセルにデータを入力することが簡単になります。グリッド線により、ワークシートをセルのコレクションとして表示し、各セルを簡単に識別することができます。

### **グリッド線の表示の制御**

Aspose.Cells for Python via .NET は、Microsoft Excel ファイルを表す [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/) クラスを提供します。[**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/) クラスには、Excel ファイル内の各ワークシートにアクセスできる [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets/) コレクションが含まれています。ワークシートは [**Worksheet**](https://reference.aspose.com/cells/python-et/aspose.cells/worksheet/) クラスによって表されます。[**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/) クラスは、ワークシートを操作するための幅広いプロパティやメソッドを提供します。グリッド線の可視性を制御するには、[**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/) クラスの [**is_gridlines_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_gridlines_visible/) プロパティを使用します。[**is_gridlines_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_gridlines_visible/) は、**true** または **false** の値のみを保持できるブール型のプロパティです。

#### **グリッド線を表示する**

[**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet)クラスの[**is_gridlines_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_gridlines_visible/)プロパティを**true**に設定することでグリッド線を表示します。

#### **グリッド線を非表示にする**

[**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet)クラスの[**is_gridlines_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_gridlines_visible/)プロパティを**false**に設定することでグリッド線を非表示にします。

以下に完全な例が示されており、[**is_gridlines_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_gridlines_visible/)のプロパティを使用して、Excelファイル（book1.xls）を開き、最初のワークシートでグリッド線を非表示にし、変更されたファイルをoutput.xlsとして保存する方法を示しています。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Views-Display-DisplayHideGridlines-1.py" >}}

## **行列ヘッダーの表示および非表示**

Excel ファイルのすべてのワークシートは、行と列で配置されたセルで構成されています。すべての行と列には、それぞれ固有の値があり、それらを識別し、個々のセルを識別するために使用されます。例えば、行は 1、2、3、4 などに番号が付けられ、列はアルファベット順に A、B、C、D などに並べられます。行と列の値は見出しに表示されます。Aspose.Cells for Python via .NET を使用すると、これらの行と列の見出しの表示を制御することができます。

### **ワークシートの表示を制御する**

Aspose.Cells for Python via .NET は、Microsoft Excel ファイルを表す [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/) クラスを提供します。[**Workbook**](https://reference.aspose.com/cells/pytho-net/aspose.cells/workbook/) クラスには、Excel ファイル内の各ワークシートにアクセスできる [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets/) コレクションが含まれています。ワークシートは [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/) クラスによって表されます。[**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/) クラスは、ワークシートを管理するための幅広いプロパティやメソッドを提供します。行と列見出しの可視性を制御するには、[**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/) クラスの [**is_row_column_headers_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_row_column_headers_visible/) プロパティを使用します。[**is_row_column_headers_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_row_column_headers_visible/) は、**true** または **false** の値のみを保持できるブール型のプロパティです。

#### **行/列ヘッダーを表示する**

[**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet)クラスの[**is_row_column_headers_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_row_column_headers_visible/)プロパティを**true**に設定することで行と列のヘッダーを表示します。

#### **行/列ヘッダーを非表示にする**

[**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet)クラスの[**is_row_column_headers_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_row_column_headers_visible/)プロパティを**false**に設定することで行と列のヘッダーを非表示にします。

以下に完全な例が示されており、[**is_row_column_headers_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_row_column_headers_visible/)のプロパティを使用して、Excelファイル（book1.xls）を開き、最初のワークシートで行と列のヘッダーを非表示にし、変更されたファイルをoutput.xlsとして保存する方法を示しています。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Views-Display-DisplayHideRowColumnHeaders-1.py" >}}

{{% alert color="primary" %}}

また、[**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells)クラスの[**unhide_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/unhide_rows)メソッドと[**unhide_columns**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/unhide_columns)メソッドを使用して、複数の行と列を表示したり非表示にしたりすることも可能です。

{{% /alert %}}
