---
title: ワークシートのすべての列を単一の PDF ページに収める
type: docs
weight: 160
url: /ja/python-net/fit-all-worksheet-columns-on-single-pdf-page/
description: Aspose.Cells for Python via .NET APIを使用してPDFに変換する際に、ワークシートのすべての列を1つのPDFページに収める方法を学びます。
keywords: Pythonを使用してPDFに変換する際に、ワークシートのすべての列を1つのPDFページに収め、Pythonを使用してPDFページにワークシートのすべての列をフィットさせ、Pythonですべての列を1つのPDFページに保存し、Pythonですべての列を1つのPDFページに保存します。
---

{{% alert color="primary" %}}

時々、ワークシートの全列を1ページに収めたPDFファイルを生成したいことがあります。[**PdfSaveOptions.all_columns_in_one_page_per_sheet**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/all_columns_in_one_page_per_sheet/)プロパティはその機能を非常に簡単に使用できます。ワークシートのデータに基づいて、出力PDFの高さや幅などの複雑な計算は内部で処理されます。

{{% /alert %}}

## **ワークシートの列を単一の PDF ページに収める**

[**PdfSaveOptions.all_columns_in_one_page_per_sheet**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/all_columns_in_one_page_per_sheet/)は、ワークシート内のすべての列が1つのPDFページにレンダリングされることを保証します。ただし、ワークシートのデータに応じて、行が複数のページに拡張される場合があります。

以下のサンプルコードは、100列の大きなワークシートをレンダリングするために[**PdfSaveOptions.all_columns_in_one_page_per_sheet**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/all_columns_in_one_page_per_sheet/)プロパティを使用する方法を示しています。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-FitAllWorksheetColumns-1.py" >}}

{{% alert color="primary" %}}

あるワークシートに多くの列がある場合、レンダリングされたPDFファイルでは内容が非常に小さくなる場合があります。Acrobat Readerなどの閲覧アプリケーションで拡大するとまだ読める場合があります。

{{% /alert %}} {{% alert color="primary" %}}

スプレッドシートに数式が含まれている場合、スプレッドシートをPDF形式にレンダリングする直前に[Workbook.calculate_formula](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/#)メソッドを呼び出すのが最適です。これにより、数式に依存する値が再計算され、PDFに正しい値がレンダリングされます。

{{% /alert %}}
