---
title: ワークシートのすべての列を 1 つの PDF ページに収める
type: docs
weight: 160
url: /ja/python-net/fit-all-worksheet-columns-on-single-pdf-page/
description: Aspose.Cells for Python via .NET API を使用して、ワークシートのすべての列を 1 つの PDF ページに収める方法を学習します。
keywords: Python Fit All Worksheet Columns on Single PDF Page, Fit Worksheet Columns on Single PDF Page using Python, Python Save All Worksheet Columns to a PDF Page, Save All Columns to single PDF Page in Python
---
{{% alert color="primary" %}}

ワークシートのすべての列を 1 ページに収める PDF ファイルを生成したい場合があります。の[**PdfSaveOptions.all_columns_in_one_page_per_sheet**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/all_columns_in_one_page_per_sheet/)プロパティは、この機能を非常に使いやすい方法で提供します。出力 PDF の高さと幅などの複雑な計算は内部で処理され、ワークシート内のデータに基づいて行われます。

{{% /alert %}}

##  **ワークシートの列を 1 つの PDF ページに合わせる**

[**PdfSaveOptions.all_columns_in_one_page_per_sheet**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/all_columns_in_one_page_per_sheet/)ワークシート内のすべての列が単一の PDF ページにレンダリングされるようにしますが、ワークシート内のデータによっては行が複数のページに拡張される場合があります。

以下のサンプルコードは使用方法を示しています[**PdfSaveOptions.all_columns_in_one_page_per_sheet**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/all_columns_in_one_page_per_sheet/)プロパティを使用して、100 列の大きなワークシートをレンダリングします。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-FitAllWorksheetColumns-1.py" >}}

{{% alert color="primary" %}}

特定のワークシートに多くの列がある場合、レンダリングされた PDF ファイルのコンテンツが非常に小さいサイズで表示されることがあります。 Acrobat Reader などの表示アプリケーションで拡大しても読むことができます。

{{% /alert %}} {{% alert color="primary" %}}

スプレッドシートに数式が含まれている場合は、次のように呼び出すのが最善です。[Workbook.calculate_formula](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/#)スプレッドシートを PDF 形式にレンダリングする直前のメソッド。そうすることで、式に依存する値が再計算され、PDF に正しい値が表示されるようになります。

{{% /alert %}}
