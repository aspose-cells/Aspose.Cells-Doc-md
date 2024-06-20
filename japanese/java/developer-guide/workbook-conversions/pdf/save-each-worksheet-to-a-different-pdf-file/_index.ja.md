---
title: 異なるPDFファイルにそれぞれのワークシートを保存する
type: docs
weight: 50
url: /ja/java/save-each-worksheet-to-a-different-pdf-file/
---

{{% alert color="primary" %}}

Aspose.Cellsは、（画像、グラフなどを含む）スプレッドシートファイルをPDFドキュメントに変換することをサポートしています。Aspose.Cells for JavaはスプレッドシートをPDFドキュメントに変換するためにAspose.PDF for Javaを使用する必要はなく、独立して機能します。変換には一時ファイルを作成したり使用したりする必要もありません。全体のプロセスはメモリ内で行うことができます。

{{% /alert %}}

テンプレートのExcelファイル内の各ワークシートを異なるPDFファイルに保存する必要がある場合、これは簡単に実現できます。[**PdfSaveOptions.SheetSet**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions/#setSheetSet-com.aspose.cells.SheetSet-)オプションを使用して、1つのシートインデックスを1回に設定してPDFにレンダリングすることができます。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SaveEachWorksheettoDifferentPDF-SaveEachWorksheettoDifferentPDF.java" >}}

{{% alert color="primary" %}}

スプレッドシートに数式が含まれている場合は、スプレッドシートをPDF形式にレンダリングする直前に[**Workbook.calculateFormula()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula--)メソッドを呼び出すことが最善です。これにより、数式に依存する値が再計算され、PDFに正しい値がレンダリングされます。

{{% /alert %}}
