---
title: Excelワークシートごとに1つのPDFページをレンダリングする  ExcelからPDFへの変換
type: docs
weight: 40
url: /ja/java/render-one-pdf-page-per-excel-worksheet-excel-to-pdf-conversion/
---

{{% alert color="primary" %}}

大きなMicrosoft Excelファイル（たとえば、各シートに50の列と300行以上のデータがあるワークブック）を扱う際に、ワークシートのサイズに関係なく1ページに1つのワークシートが表示されるようにPDF出力を表示したい場合があります。これにより、各ページのサイズが大きく異なることがあります。これはAspose.Cells for Javaを使用することで実現できます。

{{% /alert %}}

複数のワークシートを持つExcelファイルをPDFに変換するサンプルコードをご確認ください。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ExceltoPDF-ExceltoPDF.java" >}}

{{% alert color="primary" %}}

[**PdfSaveOptions.OnePagePerSheet**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#OnePagePerSheet)オプションが**true**に設定されている場合、すべてのシートの内容が1つのPDFページにレンダリングされます。[**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/PageSetup)で設定された用紙サイズは無効ですが、[**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/PageSetup)で設定された他の設定は引き続き有効です。

{{% /alert %}} {{% alert color="primary" %}}

スプレッドシートに数式が含まれている場合、PDFにレンダリングする直前に[**Workbook.calculateFormula**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula--)メソッドを呼び出すことが最善です。これにより、数式に依存する値が再計算され、PDFに正しい値がレンダリングされます。

{{% /alert %}}
