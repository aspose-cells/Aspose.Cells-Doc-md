---
title: ワークシートのすべての列を 1 つの PDF ページに収める
type: docs
weight: 160
url: /ja/net/fit-all-worksheet-columns-on-single-pdf-page/
---
{{% alert color="primary" %}}

ワークシートのすべての列を 1 ページに収める PDF ファイルを生成したい場合があります。の[**PdfSaveOptions.AllColumnsInOnePagePerSheet**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/allcolumnsinonepagepersheet)プロパティは、この機能を非常に使いやすい方法で提供します。出力 PDF の高さや幅などの複雑な計算は内部で処理され、ワークシートのデータに基づいています。

{{% /alert %}}

## **単一の PDF ページにワークシートの列を合わせる**

[**PdfSaveOptions.AllColumnsInOnePagePerSheet**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/allcolumnsinonepagepersheet)ワークシートのすべての列が 1 つの PDF ページにレンダリングされますが、ワークシートのデータによっては行が複数のページに展開される場合があります。

以下のサンプルコードは、使用方法を示しています[**PdfSaveOptions.AllColumnsInOnePagePerSheet**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/allcolumnsinonepagepersheet)プロパティを使用して、100 列の大きなワークシートをレンダリングします。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-FitAllWorksheetColumns-1.cs" >}}

{{% alert color="primary" %}}

特定のワークシートに多くの列がある場合、レンダリングされた PDF ファイルではコンテンツが非常に小さいサイズで表示されることがあります。 Acrobat Reader などの表示アプリケーションで拡大しても、読み取り可能です。

{{% /alert %}} {{% alert color="primary" %}}

スプレッドシートに数式が含まれている場合は、[**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula)スプレッドシートを PDF 形式にレンダリングする直前。そうすることで、数式に依存する値が再計算され、正しい値が PDF に表示されます。

{{% /alert %}}
