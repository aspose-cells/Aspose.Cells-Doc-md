---
title: Excel ワークシートごとに 1 つの PDF ページをレンダリング - Excel から PDF への変換
type: docs
weight: 40
url: /ja/java/render-one-pdf-page-per-excel-worksheet-excel-to-pdf-conversion/
---
{{% alert color="primary" %}}

大きな Microsoft Excel ファイル (たとえば、50 列と 300 行以上のデータを含む多数のシートを含むワークブック) を操作する場合、ワークシートのサイズに関係なく、PDF の出力でワークシートごとに 1 ページを表示することが必要な場合があります。 .これは、各ページのページ サイズが根本的に異なる可能性が高いことを意味します。これは、Aspose.Cells for Java を使用して実現できます。

{{% /alert %}}

複数のワークシートを含む Excel ファイルを PDF に変換する次のサンプル コードを参照してください。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ExceltoPDF-ExceltoPDF.java" >}}

{{% alert color="primary" %}}

もし[**PdfSaveOptions.OnePagePerSheet**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#OnePagePerSheet)オプションはに設定されています**真実**、すべてのシート コンテンツが 1 つの PDF ページにレンダリングされます。で設定した用紙サイズ[**ページ設定**](https://reference.aspose.com/cells/java/com.aspose.cells/PageSetup)無効ですが、で設定された他の設定[**ページ設定**](https://reference.aspose.com/cells/java/com.aspose.cells/PageSetup)まだ有効です。

{{% /alert %}} {{% alert color="primary" %}}

スプレッドシートに数式が含まれている場合は、[**Workbook.calculateFormula**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula()メソッドをスプレッドシートを PDF にレンダリングする直前に実行します。これにより、式に依存する値が再計算され、正しい値が PDF にレンダリングされます。

{{% /alert %}}
