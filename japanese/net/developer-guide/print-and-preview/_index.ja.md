---
title: ワークブックの印刷とプレビュー
linktitle: 印刷とプレビュー
type: docs
weight: 70
url: /ja/net/workbook-and-worksheet-print-preview/
description: Aspose.Cellsは、Microsoft ExcelのインストールなしでExcelファイルを印刷およびプレビューする機能をサポートしています。
---

{{% alert color="primary" %}}

ワークシートを作成した後、通常はそれを印刷したいと思うことがあります。この記事ではAspose.Cellsを使用してスプレッドシートを印刷する方法について説明しています。

{{% /alert %}}

## **印刷の概要**

Microsoft Excelは、選択を指定しない限り、ワークシート全体を印刷すると仮定しています。Aspose.Cellsを使用して印刷するには、まずAspose.Cells.Rendering名前空間をプログラムにインポートします。これにはいくつかの有用なクラスがあり、たとえば、[**SheetRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender)と[**WorkbookRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookrender)があります。

### **SheetRenderを使用して印刷**

[**Aspose.Cells.Rendering.SheetRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender) クラスはワークシートを表し、[**ToPrinter**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender/methods/toprinter/index) メソッドはワークシートを印刷することができます。次のサンプルコードは、ワークシートを印刷する方法を示しています。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderingAndPrinting-PrintingUsingSheetRender-PrintingExcelWorkbookUsingSheetRender.cs" >}}

### **WorkbookRenderを使用して印刷**

ワークブック全体を印刷するには、シートをイテレートして印刷するか、[**WorkbookRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookrender)を使用します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderingAndPrinting-PrintingUsingWorkbookRender-1.cs" >}}

{{% alert color="primary" %}}

Aspose.Cellsはまた、[**WorkbookRender.ToPrinter()**](https://reference.aspose.com/cells/net/aspose.cells.rendering.workbookrender/toprinter/methods/3)および[**SheetRender.ToPrinter()**](https://reference.aspose.com/cells/net/aspose.cells.rendering.sheetrender/toprinter/methods/2)メソッドのオーバーロードを提供しており、Excelスプレッドシートを印刷する際に印刷ジョブの名前を設定することができます。デフォルトでは、すべての印刷ジョブは"Document"という名前で作成されます。

{{% /alert %}}

## **印刷プレビュー**

数百万ページのExcelファイルをPDFまたは画像に変換する必要がある場合があります。このようなファイルを処理すると、多くの時間とリソースが消費されます。そのような場合に、ワークブックおよびワークシートの印刷プレビュー機能が役立つ可能性があります。ファイルを変換する前に、ユーザーは総ページ数を確認し、ファイルを変換するかどうかを決定できます。この記事では、[**WorkbookPrintingPreview**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookprintingpreview)と[**SheetPrintingPreview**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetprintingpreview) クラスを使用して、生成されたプレビューの総ページ数を調べる方法に焦点を当てています。

Aspose.Cellsは印刷プレビュー機能を提供しています。APIは[**WorkbookPrintingPreview**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookprintingpreview)および[**SheetPrintingPreview**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetprintingpreview)クラスを提供しています。ワークブック全体の印刷プレビューを作成するには、[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)と[**ImageOrPrintOptions**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions)オブジェクトをコンストラクタに渡して[**WorkbookPrintingPreview**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookprintingpreview)クラスのインスタンスを作成します。[**WorkbookPrintingPreview**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookprintingpreview)クラスは、生成されたプレビューのページ数を返す[**EvaluatedPageCount**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookprintingpreview/properties/evaluatedpagecount)メソッドを提供します。[**WorkbookPrintingPreview**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookprintingpreview)クラスに類似して、[**SheetPrintingPreview**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetprintingpreview)クラスは特定のワークシートの印刷プレビューを生成するために使用されます。ワークシートの印刷プレビューを作成するには、[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)と[**ImageOrPrintOptions**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions)オブジェクトをコンストラクタに渡して[**SheetPrintingPreview**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetprintingpreview)クラスのインスタンスを作成します。[**SheetPrintingPreview**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetprintingpreview)クラスもまた、生成されたプレビューのページ数を返す[**EvaluatedPageCount**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetprintingpreview/properties/evaluatedpagecount)メソッドを提供します。

次のコードスニペットは、[サンプルExcelファイル](94896177.xlsx)を使用して、[**WorkbookPrintingPreview**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookprintingpreview)と[**SheetPrintingPreview**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetprintingpreview)クラスの両方の使用方法を示しています。

### **サンプルコード**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-PrintPreview-1.cs" >}}

上記のコードを実行した結果生成された出力は次のとおりです。

### **コンソール出力**

{{< highlight java >}}

Workbook page count: 1
Worksheet page count: 1

{{< /highlight >}}

## **高度なトピック**
- [スプレッドシートのレンダリング用フォントの設定](/cells/ja/net/configuring-fonts-for-rendering-spreadsheets/)
- [ワークシートをイメージに変換 - データ周りの空白を削除](/cells/ja/net/convert-worksheet-to-image-remove-whitespace-around-data/)
- [ワークシートを画像に変換し、ページごとに画像をワークシートに変換する](/cells/ja/net/converting-worksheet-to-image-and-worksheet-to-image-by-page/)
- [ImageOrPrintオプションを使用してワークシートを画像に変換](/cells/ja/net/converting-worksheet-to-image-using-imageorprint-options/)
- [ワークシートのセルの範囲をイメージにエクスポート](/cells/ja/net/export-range-of-cells-in-a-worksheet-to-image/)
- [希望の幅と高さでワークシートまたはチャートを画像にエクスポート](/cells/ja/net/export-worksheet-or-chart-into-image-with-desired-width-and-height/)
- [ImageOrPrintOptionsを使用してワークシートから画像を抽出](/cells/ja/net/extract-images-from-worksheets-using-imageorprintoptions/)
- [ワークシートのサムネイルを生成](/cells/ja/net/generate-thumbnail-of-the-worksheet/)
- [印刷するものがない場合、空白ページを出力](/cells/ja/net/output-blank-page-when-there-is-nothing-to-print/)
- [ページ設定および印刷オプション](/cells/ja/net/page-setup-and-printing-options/)
- [SheetRenderとWorkbookRenderを使用してページの範囲を印刷](/cells/ja/net/printing-range-of-pages-using-sheetrender-and-workbookrender/)
- [ImageOrPrintOptionsのPageIndexおよびPageCountプロパティを使用したページのシーケンスをレンダリングする](/cells/ja/net/render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions/)
- [ワークシートをグラフィックコンテキストにレンダリング](/cells/ja/net/render-worksheet-to-graphic-context/)
- [ワークブックのレンダリング用に個々またはプライベートなフォントセットを指定する](/cells/ja/net/specify-individual-or-private-set-of-fonts-for-workbook-rendering/)
- [Aspose.Cellsを使用して印刷時にジョブまたは文書名を指定する](/cells/ja/net/specify-job-or-document-name-while-printing-with-aspose-cells/)
