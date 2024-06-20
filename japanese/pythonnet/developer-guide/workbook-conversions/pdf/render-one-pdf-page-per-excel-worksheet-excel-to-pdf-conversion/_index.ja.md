---
title: Excelワークシートごとに1つのPDFページをレンダリングする  ExcelからPDFへの変換
type: docs
weight: 100
url: /ja/python-net/render-one-pdf-page-per-excel-worksheet-excel-to-pdf-conversion/
description: Aspose.Cells for Python via .NET APIを使用してExcelをPDFに変換する際に、1つのExcelワークシートごとに1つのPDFページをレンダリングする方法を学びます。
keywords: PythonでExcelワークシートごとに1ページのPDFをレンダリングし、ExcelをPDFに保存する際に1ページごとにExcelワークシートを表示する方法
---

{{% alert color="primary" %}} 

大量のMicrosoft Excelファイルを使用する場合（たとえば、各シートに50列以上300行以上のデータがあるワークブック）、PDF出力はワークシートごとに1ページで表示したい場合があります。これにより、各ページのページサイズが大幅に異なる可能性があります。これは、Aspose.Cells for Python via .NET APIを使用して達成できます。

{{% /alert %}} 

複数のワークシートを持つExcelファイルをPDFに変換するサンプルコードをご確認ください。



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-RenderOnePdfPagePerExcelWorksheet-1.py" >}}

{{% alert color="primary" %}} 

[PdfSaveOptions.one_page_per_sheet](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/one_page_per_sheet/)オプションが**true**に設定されている場合、すべてのシートの内容が1つのPDFページにレンダリングされます。

{{% /alert %}} {{% alert color="primary" %}} 

スプレッドシートに数式が含まれている場合は、PDFに変換する前に[Workbook.calculate_formula](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/#)メソッドを呼び出すことが最善です。これにより、数式に依存する値が再計算され、正しい値がPDFにレンダリングされます。

{{% /alert %}}
