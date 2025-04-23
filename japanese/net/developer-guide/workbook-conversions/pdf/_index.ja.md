---
title: Pdf
type: docs
weight: 220
url: /ja/net/convert-excel-to-pdf/
---

{{% alert color="primary" %}}

Aspose.CellsはExcelワークブックをPDFに変換することをサポートしています。この例では、Excelワークブックを完全にPDFに変換する方法を示します。

{{% /alert %}}

## **ExcelワークブックをPDFに変換する**

PDFファイルは、組織、政府部門、個人間で文書を交換するために広く使用されています。これは標準のドキュメント形式であり、ソフトウェア開発者はしばしばMicrosoft ExcelファイルをPDFドキュメントに変換する方法を見つけるよう求められます。

Aspose.Cellsは、ExcelファイルをPDFに変換する機能をサポートし、変換時に高い視覚的忠実度を維持します。

{{% alert color="primary" %}}

Aspose.Cells for .NETは出力ドキュメントにAPIおよびバージョン番号に関する情報を直接書き込みます。たとえば、[Aspose.Cells v23.2]などの値で**PDF Producer**フィールドを埋めます。

出力ドキュメントでこの情報を変更することができることに注意してください。

{{% /alert %}}

### **直接変換**

Aspose.Cells for .NETは他のソフトウェアに依存せずにスプレッドシートからPDFへの変換をサポートしています。[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)クラスの[**Save**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index)メソッドを使用してExcelファイルをPDFに保存します。[**Save**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index)メソッドは、ネイティブのExcelファイルをPDF形式に変換する[**SaveFormat.Pdf**](https://reference.aspose.com/cells/net/aspose.cells/saveformat)列挙型メンバーを提供します。

以下の手順に従って、Excelスプレッドシートを直接PDF形式に変換します:

1. 空のコンストラクタを呼び出して[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)クラスのオブジェクトをインスタンス化します。
1. 既存のテンプレートファイルを開いたり読み込んだりするか、ワークブックをゼロから作成している場合は、この手順をスキップします。
1. Aspose.CellsのAPIを使用して、スプレッドシート上で作業を行います（入力データ、書式設定の適用、数式の設定、画像の挿入など）。
1. スプレッドシートのコードが完了したら、[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)クラスの[**Save**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index)メソッドを呼び出してスプレッドシートを保存します。

ファイル形式はPDFである必要がありますので、[**SaveFormat**](https://reference.aspose.com/cells/net/aspose.cells/saveformat)列挙型から*Pdf*（事前に定義された値）を選択して最終的なPDFドキュメントを生成します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-XlstoPDFDirectConversation-1.cs" >}}

### **高度な変換**

異なる属性を設定するために[**PdfSaveOptions**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)クラスを使用したり、出力PDFの印刷、フォント、セキュリティ、圧縮設定を制御するために[**PdfSaveOptions**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)クラスの異なるプロパティを設定することもできます。 

[**Compliance**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/compliance)は最も重要なプロパティで、PDFの標準遵守レベルを設定できます。現在はPDF 1.4、PDF 1.5、PDF 1.6、PDF 1.7、PDF/A-1a、PDF/A-1b、PDF/A-2a、PDF/A-2b、PDF/A-2u、PDF/A-3a、PDF/A-2ab、PDF/A-3u形式に保存できます。PDF/A形式では、出力ファイルのサイズが通常のPDFファイルよりも大きくなります。

#### **PDF/A準拠ファイルへのワークブックの保存**

以下のコードスニペットは、[**PdfSaveOptions**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions) クラスを使用してExcelファイルをPDF/A準拠のPDF形式に保存する方法を示しています。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-AdvancedConversiontoPdf-1.cs" >}}

{{% alert color="primary" %}}

[**Compliance**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/compliance) プロパティはリリースAspose.Cells for .NET 5.3.0で追加されましたのでご注意ください。

{{% /alert %}}

#### **PDF作成時間の設定**

[**PdfSaveOptions**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions) クラスを使用すると、PDF作成時刻を取得または設定することができます。次のコードは、[**PdfSaveOptions.CreatedTime**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/createdtime) プロパティを使用してPDFファイルの作成時刻を設定する方法を示しています。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-SetPDFCreationTime-1.cs" >}}

#### **ContentCopyForAccessibilityオプションの設定**

[**PdfSaveOptions**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions) クラスを使用すると、変換されたPDFのコンテンツアクセスを制御するためのPDF [**AccessibilityExtractContent**](https://reference.aspose.com/cells/net/aspose.cells.rendering.pdfsecurity/pdfsecurityoptions/properties/accessibilityextractcontent) オプションを取得または設定できます。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-SetContentCopyForAccessibility-1.cs" >}}

#### **PDFへのカスタムプロパティのエクスポート**

[**PdfSaveOptions**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions) クラスを使用すると、元のワークブック内のカスタムプロパティをPDFにエクスポートすることができます。プロパティのエクスポート方法を指定するために [**PdfCustomPropertiesExport**](https://reference.aspose.com/cells/net/aspose.cells.rendering/pdfcustompropertiesexport) 列挙型が提供されています。これらのプロパティは、次の画像に示すように、Adobe Acrobat Readerで[ファイル]をクリックして[プロパティ]オプションをクリックすることで観察することができます。テンプレートファイル "sourceWithCustProps.xlsx" は[こちら](sourceWithCustProps.xlsx)からダウンロードでき、解析用の出力PDFファイル "outSourceWithCustProps" は[こちら](outSourceWithCustProps.pdf)で利用できます。

![todo:image_alt_text](convert-excel-workbook-to-pdf_1.png)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-ExportCustomPropertiesToPdf-1.cs" >}}

### **変換属性**

新しいリリースごとに変換機能を強化しています。Aspose.CellのExcelからPDFへの変換にはまだいくつかの制限があります。MapChartはPDF形式への変換時にサポートされていません。また、一部の図形オブジェクトには十分なサポートがありません。

以下の表は、Aspose.Cellsを使用してPDFにエクスポートする際に完全または部分的にサポートされているすべての機能をリストしています。この表は最終的なものではなく、すべてのスプレッドシート属性を網羅していませんが、PDFへの変換にはサポートされていないまたは部分的にサポートされている機能を特定しています。

|**ドキュメント要素**|**属性**|**サポート**|**注釈**|
| :- | :- | :- | :- |
|配置| |はい| |
|背景設定| |はい| |
|ボーダー|色|はい| |
|ボーダー|線のスタイル|はい| |
|ボーダー|線の幅|はい| |
|セルデータ| |はい| |
|コメント| |はい| |
|条件付き書式| |はい| |
|ドキュメントプロパティ| |はい| |
|図形オブジェクト| |部分的|図形オブジェクトの影や3D効果には十分なサポートがありません。WordArtとSmartArtは部分的にサポートされています。|
|フォント|サイズ|はい| |
|フォント|色|はい| |
|フォント|スタイル|はい| |
|フォント|下線|はい| |
|フォント|効果|はい||
|画像| |はい| |
|ハイパーリンク| |はい| |
|チャート|  |部分的に| MapChartはサポートされていません。|
|セルの結合|  |はい|  |
|改ページ|  |はい|  |
|ページ設定|ヘッダー/フッター|はい|  |
|ページ設定|余白|はい|  |
|ページ設定|ページの向き|はい|  |
|ページ設定|ページサイズ|はい|  |
|ページ設定|印刷範囲|はい|  |
|ページ設定|印刷タイトル|はい|  |
|ページ設定|拡大/縮小|はい|  |
|行の高さ/列の幅|  |はい|  |
|右から左への言語|  |はい|  |

{{% alert color="primary" %}}

スプレッドシートに数式が含まれている場合、スプレッドシートをPDF形式に変換する直前に[**Workbook.CalculateFormula()](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula)を呼び出すことをお勧めします。これにより、数式に依存する値が再計算され、PDFに正しい値が表示されます。

{{% /alert %}}

## **高度なトピック**
- [PDFブックマークを追加](/cells/ja/net/add-pdf-bookmarks/)
- [名前付き目次でPDFブックマークを追加する](/cells/ja/net/add-pdf-bookmarks-with-named-destinations/)
- [出力PDFの空白ページを回避する](/cells/ja/net/avoid-blank-page-in-output-pdf-when-there-is-nothing-to-print/)
- [PDFへの変換時に特定のUnicode文字のフォントを変更する](/cells/ja/net/change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf/)
- [PDFに変換する際のMS Excelブックの外部リソースの読み込みを制御する](/cells/ja/net/control-loading-of-external-resources-in-ms-excel-workbook-while-rendering-to-pdf/)
- [XLSXファイルをPDF形式に変換](/cells/ja/net/convert-xlsx-file-to-pdf-format/)
- [PDFA-1aに準拠したExcelファイルをPDF形式に変換する](/cells/ja/net/convert-excel-file-to-pdf-format-compatible-with-pdfa-1a/)
- [画像やチャートを含むXLSファイルをPDFに変換](/cells/ja/net/convert-xls-file-with-images-or-charts-to-pdf/)
- [チャートシートの PdfBookmarkEntry を作成](/cells/ja/net/create-pdfbookmarkentry-for-chart-sheet/)
- [1つのPDFページでワークシートのすべての列を表示する](/cells/ja/net/fit-all-worksheet-columns-on-single-pdf-page/)
- [DrawObjectEventHandlerクラスを使用してPDFへのレンダリング中にDrawObjectとバインドを取得](/cells/ja/net/get-drawobject-and-bound-while-rendering-to-pdf-using-drawobjecteventhandler-class/)
- [Excelファイルを変換する際のフォントの置換に関する警告を取得](/cells/ja/net/get-warnings-for-font-substitution-while-rendering-excel-file/)
- [Excel を PDF にレンダリングする際のエラーを無視](/cells/ja/net/ignore-errors-while-rendering-excel-to-pdf/)
- [生成されるページ数を制限する - ExcelからPDFへの変換](/cells/ja/net/limit-the-number-of-pages-generated-excel-to-pdf-conversion/)
- [PDFへ保存する際にコメントを印刷する](/cells/ja/net/print-comments-while-saving-to-pdf/)
- [ExcelをPDFに変換する際のOffice Add-Insのレンダリング](/cells/ja/net/render-office-add-ins-while-converting-excel-to-pdf/)
- [Excelのワークシートごとに1つのPDFページをレンダリング - ExcelからPDFへの変換](/cells/ja/net/render-one-pdf-page-per-excel-worksheet-excel-to-pdf-conversion/)
- [Aspose.Cellsによる出力PDFでUnicode補助文字をレンダリングする](/cells/ja/net/render-unicode-supplementary-characters-in-output-pdf-by-aspose-cells/)
- [追加された画像のリサンプリング - ExcelからPDFへの変換](/cells/ja/net/resampling-added-images-excel-to-pdf-conversion/)
- [異なるPDFファイルごとに各ワークシートを保存](/cells/ja/net/save-each-worksheet-to-a-different-pdf-file/)
- [標準または最小サイズでExcelをPDFに保存](/cells/ja/net/save-excel-into-pdf-with-standard-or-minimum-size/)
- [指定されたワークシートをPDFに保存](/cells/ja/net/save-specified-worksheets-to-pdf/)
- [PDFドキュメントをセキュアにする](/cells/ja/net/secure-pdf-documents/)
- [出力PDFおよび画像内の文字列の交差方法を指定](/cells/ja/net/specify-how-to-cross-string-in-output-pdf-and-image/)
{{< app/cells/assistant language="csharp" >}}
