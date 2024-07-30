---
title: ページブレークの管理
type: docs
weight: 30
url: /ja/python-net/managing-page-breaks/
description: この記事では、Aspose.Cells for Python via .NETAPIを使用して、Excelワークシートにページ区切りを追加、ページ区切りをクリア、または特定のページ区切りをプログラムで削除する方法とサンプルコードを提供します。
keywords: Python Excelライブラリ、Pythonページ区切り、Pythonでのエクセルのページ区切り、Pythonでのページ区切りのクリア
---

{{% alert color="primary" %}}

定義によると、ページブレークはテキストフローの中で１つのページが終わり、次のページが始まる場所です。Microsoft Excelでは、ユーザーは任意の選択したワークシートのセルにページブレークを追加できます。

ページ区切りが追加されるセルの位置、ページが終了し、ページ区切り後の残りのデータが次のページで印刷されます。簡単に言えば、ページ区切りは、指定に従ってワークシートを複数のページに分割します。Aspose.Cells for Python via .NETを使用して、ランタイムでワークシートにページ区切りを追加することもできます。Aspose.Cells for Python via .NETでは、2種類のページ区切りを追加できます。

- 水平ページブレーク
- 垂直ページブレーク

今後の議論では、Aspose.Cells for Python via .NETを使用してワークシートに水平または垂直のページ区切りを追加する方法について説明します。

{{% /alert %}}

## **ページブレーク**

Aspose.Cells for Python via .NETは、Excelファイルを表す[**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)クラスを提供します。[**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)クラスには、Excelファイル内の各ワークシートにアクセスできる[**Worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets)コレクションが含まれています。

ワークシートは[**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet)クラスによって表されます。[**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet)クラスは、ワークシートを管理するために使用される幅広い範囲のプロパティとメソッドを提供しています。

ページブレークを追加するには、[**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet)クラスの[**horizontal_page_breaks**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/horizontal_page_breaks)および[**vertical_page_breaks**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/vertical_page_breaks)プロパティを使用します。

[**horizontal_page_breaks**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/horizontal_page_breaks)および[**vertical_page_breaks**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/vertical_page_breaks)プロパティは、いくつかのページブレークを含む可能性があるコレクションであり、各コレクションには水平および垂直ページブレークを管理するためのいくつかのメソッドが含まれています。

## **ページ区切りの追加方法**

ワークシートにページ区切りを追加するには、指定されたセルに垂直および水平のページ区切りを挿入し、[**HorizontalPageBreakCollection.add()**](https://reference.aspose.com/cells/python-net/aspose.cells/horizontalpagebreakcollection/add/#str)および[**VerticalPageBreakCollection.add()**](https://reference.aspose.com/cells/python-net/aspose.cells/verticalpagebreakcollection/add/#str)メソッドを呼び出します。各**add**メソッドは、ページ区切りを追加するセルの名前を取ります。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Value-AddingPageBreaks-1.py" >}}

{{% alert color="primary" %}}

ページビューモードまたは印刷プレビューモードで、これらの改ページがどのように動作するかを確認できます。

{{% /alert %}}


## **重要なこと**

ページ設定の設定で**FitToPages**プロパティ（すなわち[**fit_to_pages_tall**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/fit_to_pages_tall)および[**fit_to_pages_wide**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/fit_to_pages_wide)）を設定すると、ページブレークの設定が影響を受けます。そのため、ワークシートを印刷する場合、ページブレークの設定は考慮されませんが、それらはまだ設定されています。
