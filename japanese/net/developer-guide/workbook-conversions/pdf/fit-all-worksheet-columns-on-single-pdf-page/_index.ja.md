---
title: ワークシートのすべての列を単一の PDF ページに収める
type: docs
weight: 160
url: /ja/net/fit-all-worksheet-columns-on-single-pdf-page/
---

{{% alert color="primary" %}}

時々、ワークシートの全列を1ページに収めたPDFファイルを生成したいことがあります。[**PdfSaveOptions.AllColumnsInOnePagePerSheet**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/allcolumnsinonepagepersheet)プロパティはその機能を非常に簡単に使用できます。ワークシートのデータに基づいて、出力PDFの高さや幅などの複雑な計算は内部で処理されます。

{{% /alert %}}

## **ワークシートの列を単一の PDF ページに収める**

[**PdfSaveOptions.AllColumnsInOnePagePerSheet**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/allcolumnsinonepagepersheet)は、ワークシート内のすべての列が1つのPDFページにレンダリングされることを保証します。ただし、ワークシートのデータに応じて、行が複数のページに拡張される場合があります。

以下のサンプルコードは、100列の大きなワークシートをレンダリングするために[**PdfSaveOptions.AllColumnsInOnePagePerSheet**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/allcolumnsinonepagepersheet)プロパティを使用する方法を示しています。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-FitAllWorksheetColumns-1.cs" >}}

{{% alert color="primary" %}}

あるワークシートに多くの列がある場合、レンダリングされたPDFファイルでは内容が非常に小さくなる場合があります。Acrobat Readerなどの閲覧アプリケーションで拡大するとまだ読める場合があります。

{{% /alert %}} {{% alert color="primary" %}}

スプレッドシートに数式が含まれている場合、PDF形式に変換する直前に [**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula) を呼び出すことが最善です。これにより、数式に依存する値が再計算され、PDFで正しい値がレンダリングされます。

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}
