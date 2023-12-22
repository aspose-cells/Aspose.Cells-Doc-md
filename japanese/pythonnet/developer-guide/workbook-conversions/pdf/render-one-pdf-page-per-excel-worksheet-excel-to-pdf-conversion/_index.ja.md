---
title: Excel ワークシートごとに 1 つの PDF ページをレンダリング - Excel から PDF への変換
type: docs
weight: 100
url: /ja/python-net/render-one-pdf-page-per-excel-worksheet-excel-to-pdf-conversion/
description: Excel を Aspose.Cells for Python via .NET API で PDF に変換しながら、Excel ワークシートごとに 1 ページの PDF をレンダリングする方法を学びます。
keywords: Python Render One PDF Page Per Excel Worksheet while saving file to PDF, One PDF Page Per Excel Worksheet while saving Excel to PDF using Python, Python show one page per worksheet when converting Excel to PDF
---
{{% alert color="primary" %}} 

大きな Microsoft Excel ファイル (たとえば、各シートに 50 列と 300 行以上のデータが含まれる多数のシートを含むワークブック) を操作する場合、ワークシートのサイズに関係なく、PDF 出力にワークシートごとに 1 ページを表示することが必要な場合があります。 。これは、各ページのページ サイズが大幅に異なる可能性があることを意味します。これは、Aspose.Cells for Python via .NET API を使用して実現できます。

{{% /alert %}} 

複数のワークシートを含む Excel ファイルを PDF に変換する次のサンプル コードを参照してください。



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-RenderOnePdfPagePerExcelWorksheet-1.py" >}}

{{% alert color="primary" %}} 

もし[PdfSaveOptions.シートごとに 1 ページ](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/one_page_per_sheet/)オプションが *true** に設定されている場合、すべてのシート コンテンツが 1 つの PDF ページにレンダリングされます。

{{% /alert %}} {{% alert color="primary" %}} 

スプレッドシートに数式が含まれている場合は、次のように呼び出すのが最善です。[Workbook.calculate_formula](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/#)これにより、式に依存する値が再計算され、正しい値が PDF にレンダリングされます。

{{% /alert %}}
