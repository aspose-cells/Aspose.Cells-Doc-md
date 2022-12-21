---
title: Excel ワークシートごとに 1 つの PDF ページをレンダリング - Excel から PDF への変換
type: docs
weight: 100
url: /ja/net/render-one-pdf-page-per-excel-worksheet-excel-to-pdf-conversion/
---
{{% alert color="primary" %}} 

大きな Microsoft Excel ファイル (たとえば、50 列と 300 行以上のデータを持つ多数のシートを含むワークブック) を操作する場合、ワークシートのサイズに関係なく、ワークシートごとに 1 ページを表示する PDF 出力が必要になる場合があります。 .これは、各ページのページ サイズが根本的に異なる可能性が高いことを意味します。これは、Aspose.Cells for .NET を使用して実現できます。

{{% /alert %}} 

複数のワークシートを含む Excel ファイルを PDF に変換する次のサンプル コードを参照してください。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderOnePdfPagePerExcelWorksheet-1.cs" >}}

{{% alert color="primary" %}} 

もし[シートごとに 1 ページ](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/onepagepersheet)オプションはに設定されています**真実**、すべてのシート コンテンツが 1 つの PDF ページにレンダリングされます。

{{% /alert %}} {{% alert color="primary" %}} 

スプレッドシートに数式が含まれている場合は、[Workbook.CalculateFormula()](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula)スプレッドシートを PDF にレンダリングする直前。これにより、式に依存する値が再計算され、正しい値が PDF に表示されます。

{{% /alert %}}
