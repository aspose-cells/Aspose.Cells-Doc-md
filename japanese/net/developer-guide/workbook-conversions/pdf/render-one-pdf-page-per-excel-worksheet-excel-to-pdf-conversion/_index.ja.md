---
title: Excelワークシートごとに1つのPDFページをレンダリングする  ExcelからPDFへの変換
type: docs
weight: 100
url: /ja/net/render-one-pdf-page-per-excel-worksheet-excel-to-pdf-conversion/
---

{{% alert color="primary" %}} 

大きなMicrosoft Excelファイル（たとえば、各50列と300行以上のデータを持つ多くのシートがあるワークブック）を使用して作業する場合、ワークシートごとに1ページでPDF出力されるようにしたい場合があります。これにより、各ページがおそらく大きく異なるページサイズになります。これは、Aspose.Cells for .NETを使用することで達成できます。

{{% /alert %}} 

複数のワークシートを持つExcelファイルをPDFに変換するサンプルコードをご確認ください。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderOnePdfPagePerExcelWorksheet-1.cs" >}}

{{% alert color="primary" %}} 

[OnePagePerSheet](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/onepagepersheet)オプションが**true**に設定されている場合、すべてのシートコンテンツが1つのPDFページにレンダリングされます。

{{% /alert %}} {{% alert color="primary" %}} 

スプレッドシートに数式が含まれている場合、スプレッドシートをPDFにレンダリングする直前に[Workbook.CalculateFormula()](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula)を呼び出すことが最善です。これにより、数式に依存した値が再計算され、正しい値がPDFに表示されます。

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}
