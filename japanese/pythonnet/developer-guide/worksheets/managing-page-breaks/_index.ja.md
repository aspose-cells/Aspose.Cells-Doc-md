---
title: ページブレークの管理
type: docs
weight: 30
url: /ja/python-net/managing-page-breaks/
description: このこの記事では、サンプルコードを提供し、Aspose.Cells for Python via .NET APIを使用して、Excelワークシートにページ区切りを追加、クリア、または特定のページ区切りを削除する方法を解説します。
keywords: Python Excelライブラリ、Pythonのページ区切り、PythonのExcelページ区切り、Pythonでページ区切りをクリア
---

{{% alert color="primary" %}}

定義によると、ページブレークはテキストフローの中で１つのページが終わり、次のページが始まる場所です。Microsoft Excelでは、ユーザーは任意の選択したワークシートのセルにページブレークを追加できます。

ページ区切りを追加したセルの位置、そのページを終了し、ページ区切りの後のデータが次のページに印刷される。簡単に言えば、ページ区切りはあなたの仕様に従ってワークシートを複数ページに分割します。また、Aspose.Cells for Python via .NETを使用して実行時にワークシートにページ区切りを追加することも可能です。Aspose.Cells for Python via .NETは、2種類のページ区切りを追加できます：

- 水平ページブレーク
- 垂直ページブレーク

残りの議論では、Aspose.Cells for Python via .NETを使用してワークシートに横方向または縦方向のページ区切りを追加する方法について説明します。

{{% /alert %}}

## **ページブレーク**

Aspose.Cells for Python via .NETは、**[**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)**クラスを提供し、Excelファイルを表します。[**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)クラスには、Excelファイル内の各ワークシートにアクセスできる**[**Worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets)**コレクションが含まれています。

ワークシートは[**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet)クラスによって表されます。[**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet)クラスは、ワークシートを管理するために使用される幅広い範囲のプロパティとメソッドを提供しています。

ページブレークを追加するには、[**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet)クラスの[**horizontal_page_breaks**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/horizontal_page_breaks)および[**vertical_page_breaks**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/vertical_page_breaks)プロパティを使用します。

[**horizontal_page_breaks**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/horizontal_page_breaks)および[**vertical_page_breaks**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/vertical_page_breaks)プロパティは、いくつかのページブレークを含む可能性があるコレクションであり、各コレクションには水平および垂直ページブレークを管理するためのいくつかのメソッドが含まれています。

## **ページ区切りの追加方法**

ワークシートにページブレークを追加するには、指定されたセルで垂直および水平のページブレークを挿入します。[**HorizontalPageBreakCollection.add()**](https://reference.aspose.com/cells/python-net/aspose.cells/horizontalpagebreakcollection/add/#str)と[**VerticalPageBreakCollection.add()**](https://reference.aspose.com/cells/python-net/aspose.cells/verticalpagebreakcollection/add/#str)メソッドを呼び出します。各**add**メソッドは、ブレークを追加するセルの名前を受け取ります。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Value-AddingPageBreaks-1.py" >}}

{{% alert color="primary" %}}

ページビューモードまたは印刷プレビューモードで、これらの改ページがどのように動作するかを確認できます。

{{% /alert %}}


## **重要なこと**

ページ設定の設定で**FitToPages**プロパティ（すなわち[**fit_to_pages_tall**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/fit_to_pages_tall)および[**fit_to_pages_wide**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/fit_to_pages_wide)）を設定すると、ページブレークの設定が影響を受けます。そのため、ワークシートを印刷する場合、ページブレークの設定は考慮されませんが、それらはまだ設定されています。
{{< app/cells/assistant language="python-net" >}}
