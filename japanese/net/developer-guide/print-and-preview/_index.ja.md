---
title: ワークブックの印刷とプレビュー
linktitle: 印刷とプレビュー
type: docs
weight: 70
url: /ja/net/workbook-and-worksheet-print-preview/
description: Aspose.Cells は、Microsoft Excel のインストールなしで、Excel ファイルの印刷とプレビューをサポートします。
---
{{% alert color="primary" %}}

ワークシートを作成した後、そのハード コピーを印刷したいことがよくあります。この記事では、Aspose.Cells でスプレッドシートを印刷する方法について説明します。

{{% /alert %}}

## **はじめにを印刷**

Microsoft Excel は、選択範囲を指定しない限り、ワークシート領域全体を印刷すると想定します。 Aspose.Cells を使用して印刷するには、最初に Aspose.Cells.Rendering 名前空間をプログラムにインポートします。いくつかの便利なクラスがあります。たとえば、[**シートレンダリング**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender)と[**WorkbookRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookrender).

### **SheetRender を使用して印刷する**

の[**Aspose.Cells.Rendering.SheetRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender)クラスはワークシートを表し、[**プリンタへ**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender/methods/toprinter/index)ワークシートを印刷できるメソッド。次のサンプル コードは、ワークシートを印刷する方法を示しています。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderingAndPrinting-PrintingUsingSheetRender-PrintingExcelWorkbookUsingSheetRender.cs" >}}

### **WorkbookRender を使用して印刷する**

ワークブック全体を印刷するには、シートを繰り返し印刷するか、[**WorkbookRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookrender)クラス。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderingAndPrinting-PrintingUsingWorkbookRender-1.cs" >}}

{{% alert color="primary" %}}

 Aspose.Cells は、[**WorkbookRender.ToPrinter()**](https://reference.aspose.com/cells/net/aspose.cells.rendering.workbookrender/toprinter/methods/3)と[**SheetRender.ToPrinter()**](https://reference.aspose.com/cells/net/aspose.cells.rendering.sheetrender/toprinter/methods/2)そのため、Excel スプレッドシートの印刷中に印刷ジョブ名を設定できます。デフォルトでは、すべての印刷ジョブは「Document」という名前で作成されます。

{{% /alert %}}

## **印刷プレビュー**

数百万ページの Excel ファイルを PDF や画像に変換する必要がある場合があります。このようなファイルの処理には、多くの時間とリソースが消費されます。このような場合、ワークブックとワークシートの印刷プレビュー機能が役立つことがあります。このようなファイルを変換する前に、ユーザーは総ページ数を確認してから、ファイルを変換するかどうかを決定できます。この記事では、[**ワークブック印刷プレビュー**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookprintingpreview)と[**シート印刷プレビュー**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetprintingpreview)総ページ数を調べるためのクラス。

 Aspose.Cells は、印刷プレビュー機能を提供します。このために、API が提供します。[**ワークブック印刷プレビュー**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookprintingpreview)と[**シート印刷プレビュー**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetprintingpreview)クラス。ワークブック全体の印刷プレビューを作成するには、[**ワークブック印刷プレビュー**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookprintingpreview)合格によるクラス[**ワークブック**](https://reference.aspose.com/cells/net/aspose.cells/workbook)と[**ImageOrPrintOptions**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions)オブジェクトをコンストラクターに渡します。の[**ワークブック印刷プレビュー**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookprintingpreview)クラスは[**EvaluatedPageCount**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookprintingpreview/properties/evaluatedpagecount)生成されたプレビューのページ数を返すメソッド。に似ている[**ワークブック印刷プレビュー**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookprintingpreview)クラス、[**シート印刷プレビュー**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetprintingpreview)クラスは、特定のワークシートの印刷プレビューを生成するために使用されます。ワークシートの印刷プレビューを作成するには、[**シート印刷プレビュー**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetprintingpreview)合格によるクラス[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)と[**ImageOrPrintOptions**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions)オブジェクトをコンストラクターに渡します。の[**シート印刷プレビュー**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetprintingpreview)クラスも提供します[**EvaluatedPageCount**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetprintingpreview/properties/evaluatedpagecount)生成されたプレビューのページ数を返すメソッド。

次のコード スニペットは、両方の使用方法を示しています。[**ワークブック印刷プレビュー**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookprintingpreview)と[**シート印刷プレビュー**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetprintingpreview)を使用したクラス[サンプルエクセルファイル](94896177.xlsx).

### **サンプルコード**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-PrintPreview-1.cs" >}}

以下は、上記のコードを実行して生成された出力です。

### **コンソール出力**

ワークブックのページ数: 1
ワークシートのページ数: 1


## **先行トピック**
- [スプレッドシートをレンダリングするためのフォントの構成](/cells/ja/net/configuring-fonts-for-rendering-spreadsheets/)
- [ワークシートを画像に変換 - データの周りの空白を削除](/cells/ja/net/convert-worksheet-to-image-remove-whitespace-around-data/)
- [ワークシートから画像へ、ワークシートから画像へのページ単位での変換](/cells/ja/net/converting-worksheet-to-image-and-worksheet-to-image-by-page/)
- [ImageOrPrint オプションを使用してワークシートを画像に変換する](/cells/ja/net/converting-worksheet-to-image-using-imageorprint-options/)
- [ワークシートの Cells の範囲を画像にエクスポート](/cells/ja/net/export-range-of-cells-in-a-worksheet-to-image/)
- [ワークシートまたはチャートを目的の幅と高さの画像にエクスポート](/cells/ja/net/export-worksheet-or-chart-into-image-with-desired-width-and-height/)
- [ImageOrPrintOptions を使用してワークシートから画像を抽出する](/cells/ja/net/extract-images-from-worksheets-using-imageorprintoptions/)
- [ワークシートのサムネイルを生成](/cells/ja/net/generate-thumbnail-of-the-worksheet/)
- [印刷するものがない場合に白紙ページを出力する](/cells/ja/net/output-blank-page-when-there-is-nothing-to-print/)
- [ページ設定と印刷オプション](/cells/ja/net/page-setup-and-printing-options/)
- [SheetRender と WorkbookRender を使用したページ範囲の印刷](/cells/ja/net/printing-range-of-pages-using-sheetrender-and-workbookrender/)
- [ImageOrPrintOptions の PageIndex および PageCount プロパティを使用したページのシーケンスのレンダリング](/cells/ja/net/render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions/)
- [ワークシートをグラフィック コンテキストにレンダリング](/cells/ja/net/render-worksheet-to-graphic-context/)
- [ワークブックのレンダリング用に個別またはプライベートのフォント セットを指定する](/cells/ja/net/specify-individual-or-private-set-of-fonts-for-workbook-rendering/)
- [Aspose.Cells で印刷中にジョブまたはドキュメント名を指定する](/cells/ja/net/specify-job-or-document-name-while-printing-with-aspose-cells/)
