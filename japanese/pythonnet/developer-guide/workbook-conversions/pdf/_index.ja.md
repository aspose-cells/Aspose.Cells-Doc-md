---
title: Pdf
type: docs
weight: 220
url: /ja/python-net/convert-excel-to-pdf/
description: Aspose.Cells for Python via .NET APIを使用してExcelをPDFに変換する方法を学ぶ。
keywords: PythonでExcelをPDFに変換する、PythonでExcelをPDFに変換する、PythonでExcelをPDFに保存する、PythonでExcelをPDFに変換する。
---

{{% alert color="primary" %}}

Aspose.Cells for Python via .NETは、ExcelワークブックをPDFに完全に変換することをサポートしています。この例では、Excelワークブックを完全にPDFに変換する方法を見ていきます。

{{% /alert %}}

## **ExcelワークブックをPDFに変換する**

PDFファイルは、組織、政府部門、個人間で文書を交換するために広く使用されています。これは標準のドキュメント形式であり、ソフトウェア開発者はしばしばMicrosoft ExcelファイルをPDFドキュメントに変換する方法を見つけるよう求められます。

Aspose.Cells for Python via .NETは、高いビジュアルの忠実度を保ちながらExcelファイルをPDFに変換することをサポートしています。

{{% alert color="primary" %}}

Aspose.Cells for Python via .NETは、出力ドキュメントにAPIとバージョン番号の情報を直接書き込みます。例えば、DocumentをPDFにレンダリングする際、Aspose.Cells for Python via .NETは**PDF Producer**フィールドに値を出力します。たとえば、'Aspose.Cells for Python via .NET v23.2'。

出力ドキュメントでこの情報を変更することができることに注意してください。

{{% /alert %}}

### **直接変換**

Aspose.Cells for Python via .NETは、他のソフトウェアに依存せずにスプレッドシートをPDFに変換することをサポートしています。ネイティブのExcelファイルをPDF形式に変換するための[**save**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/save/#str-aspose.cells.SaveFormat)メソッドを使用してExcelファイルをPDFに保存する。

以下の手順に従って、Excelスプレッドシートを直接PDF形式に変換します:

1. 空のコンストラクタを呼び出して[**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)クラスのオブジェクトをインスタンス化します。
1. 既存のテンプレートファイルを開いたり読み込んだりするか、ワークブックをゼロから作成している場合は、この手順をスキップします。
1. Aspose.Cells for Python via .NETのAPIを使用してスプレッドシートで作業を行います（入力データを設定、書式を適用、数式を設定、画像やその他の図形オブジェクトを挿入など）。
1. スプレッドシートのコードが完了したら、[**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)クラスの[**save**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/save/#str-aspose.cells.SaveFormat)メソッドを呼び出してスプレッドシートを保存します。

ファイル形式はPDFである必要があるため、最終的なPDFドキュメントを生成するために[**SaveFormat**](https://reference.aspose.com/cells/python-net/aspose.cells/saveformat/)（事前定義された値）から選択します。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-XlstoPDFDirectConversation-1.py" >}}

### **高度な変換**

[**PdfSaveOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions)クラスを使用して、変換のためにさまざまな属性を設定することもできます。[**PdfSaveOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions)クラスのさまざまなプロパティを設定すると、出力PDFの印刷、フォント、セキュリティ、圧縮設定を制御できます。最も重要なプロパティは[**PdfSaveOptions.compliance**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/compliance/)で、このプロパティを使用するとExcelファイルをPDF/A準拠のPDFファイルに保存できます。

#### **PDF/A準拠ファイルへのワークブックの保存**

以下のコードスニペットは、[**PdfSaveOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions) クラスを使用してExcelファイルをPDF/A準拠のPDF形式に保存する方法を示しています。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-AdvancedConversiontoPdf-1.py" >}}

{{% alert color="primary" %}}

[**PdfSaveOptions.compliance**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/compliance/)プロパティは、Aspose.Cells for Python via .NET for .NET 5.3.0で追加されましたので、ご留意ください。

{{% /alert %}}

#### **PDF作成時間の設定**

[**PdfSaveOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions) クラスを使用すると、PDF作成時刻を取得または設定することができます。次のコードは、[**PdfSaveOptions.created_time**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/created_time/) プロパティを使用してPDFファイルの作成時刻を設定する方法を示しています。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-SetPDFCreationTime-1.py" >}}

#### **ContentCopyForAccessibilityオプションの設定**

[**PdfSaveOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions) クラスを使用すると、変換されたPDFのコンテンツアクセスを制御するためのPDF [**PdfSecurityOptions.accessibility_extract_content**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering.pdfsecurity/pdfsecurityoptions/accessibility_extract_content/) オプションを取得または設定できます。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-SetContentCopyForAccessibility-1.py" >}}

#### **PDFへのカスタムプロパティのエクスポート**

[**PdfSaveOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions) クラスを使用すると、元のワークブック内のカスタムプロパティをPDFにエクスポートすることができます。プロパティのエクスポート方法を指定するために [**PdfCustomPropertiesExport**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/pdfcustompropertiesexport/) 列挙型が提供されています。これらのプロパティは、次の画像に示すように、Adobe Acrobat Readerで[ファイル]をクリックして[プロパティ]オプションをクリックすることで観察することができます。テンプレートファイル "sourceWithCustProps.xlsx" は[こちら](sourceWithCustProps.xlsx)からダウンロードでき、解析用の出力PDFファイル "outSourceWithCustProps" は[こちら](outSourceWithCustProps.pdf)で利用できます。

![todo:image_alt_text](convert-excel-workbook-to-pdf_1.png)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-ExportCustomPropertiesToPdf-1.py" >}}

### **変換属性**

新しいリリースごとに変換機能を強化しています。Aspose.CellのExcelからPDFへの変換にはまだいくつかの制限があります。MapChartはPDF形式への変換時にサポートされていません。また、一部の図形オブジェクトには十分なサポートがありません。

以下の表は、Aspose.Cells for Python via .NETを使用してPDFに変換する際に完全または一部サポートされている機能を示しています。この表は最終版ではなく、スプレッドシート属性のすべてを網羅していませんが、PDFへの変換において完全にサポートされていないまたは部分的にサポートされている機能を識別しています。

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

スプレッドシートに数式が含まれている場合、スプレッドシートをPDF形式にレンダリングする直前に[Workbook.calculate_formula](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/#)メソッドを呼び出すのが最適です。これにより、数式に依存する値が再計算され、PDFに正しい値がレンダリングされます。

{{% /alert %}}

## **高度なトピック**
- [PDFブックマークを追加](/cells/ja/python-net/add-pdf-bookmarks/)
- [名前付き目次でPDFブックマークを追加する](/cells/ja/python-net/add-pdf-bookmarks-with-named-destinations/)
- [出力PDFの空白ページを回避する](/cells/ja/python-net/avoid-blank-page-in-output-pdf-when-there-is-nothing-to-print/)
- [XLSXファイルをPDF形式に変換](/cells/ja/python-net/convert-xlsx-file-to-pdf-format/)
- [PDFA-1aに準拠したExcelファイルをPDF形式に変換する](/cells/ja/python-net/convert-excel-file-to-pdf-format-compatible-with-pdfa-1a/)
- [画像やチャートを含むXLSファイルをPDFに変換](/cells/ja/python-net/convert-xls-file-with-images-or-charts-to-pdf/)
- [チャートシートの PdfBookmarkEntry を作成](/cells/ja/python-net/create-pdfbookmarkentry-for-chart-sheet/)
- [1つのPDFページでワークシートのすべての列を表示する](/cells/ja/python-net/fit-all-worksheet-columns-on-single-pdf-page/)
- [Excel を PDF にレンダリングする際のエラーを無視](/cells/ja/python-net/ignore-errors-while-rendering-excel-to-pdf/)
- [生成されるページ数を制限する - ExcelからPDFへの変換](/cells/ja/python-net/limit-the-number-of-pages-generated-excel-to-pdf-conversion/)
- [PDFへ保存する際にコメントを印刷する](/cells/ja/python-net/print-comments-while-saving-to-pdf/)
- [ExcelをPDFに変換する際のOffice Add-Insのレンダリング](/cells/ja/python-net/render-office-add-ins-while-converting-excel-to-pdf/)
- [Excelのワークシートごとに1つのPDFページをレンダリング - ExcelからPDFへの変換](/cells/ja/python-net/render-one-pdf-page-per-excel-worksheet-excel-to-pdf-conversion/)
- [Aspose.Cellsによる出力PDFでUnicode補助文字をレンダリングする](/cells/ja/python-net/render-unicode-supplementary-characters-in-output-pdf-by-aspose-cells/)
- [追加された画像のリサンプリング - ExcelからPDFへの変換](/cells/ja/python-net/resampling-added-images-excel-to-pdf-conversion/)
- [異なるPDFファイルごとに各ワークシートを保存](/cells/ja/python-net/save-each-worksheet-to-a-different-pdf-file/)
- [標準または最小サイズでExcelをPDFに保存](/cells/ja/python-net/save-excel-into-pdf-with-standard-or-minimum-size/)
- [指定されたワークシートをPDFに保存](/cells/ja/python-net/save-specified-worksheets-to-pdf/)
- [PDFドキュメントをセキュアにする](/cells/ja/python-net/secure-pdf-documents/)
- [出力PDFおよび画像内の文字列の交差方法を指定](/cells/ja/python-net/specify-how-to-cross-string-in-output-pdf-and-image/)
{{< app/cells/assistant language="python-net" >}}
