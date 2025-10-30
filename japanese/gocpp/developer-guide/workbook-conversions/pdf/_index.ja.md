---
title: GolangとC++経由でExcelをPDFに変換
linktitle: ExcelをPDFに変換
type: docs
weight: 220
url: /ja/go-cpp/convert-excel-to-pdf/
description: Aspose.Cellsを使ってGolangとC++経由でExcelワークブックをPDF形式に変換する方法を学ぶ。
---

{{% alert color="primary" %}}

Aspose.CellsはExcelワークブックのPDFへの変換をサポートしています。こちらの例では、ExcelワークブックをPDFに完全に変換する手順を示します。

{{% /alert %}}

## **ExcelワークブックをPDFに変換する**

PDFファイルは、企業、政府機関、個人間で文書を交換するために広く使用されています。標準的な文書形式であり、ソフトウェア開発者からはMicrosoft ExcelファイルをPDFに変換する方法の提案をよく求められます。

Aspose.Cellsは、ExcelファイルをPDFに変換する機能をサポートし、変換時に高い視覚的忠実度を維持します。

{{% alert color="primary" %}}

Aspose.Cells for C++は、出力ドキュメントにAPIとバージョン番号についての情報を直接書き込みます。例えば、ドキュメントをPDFにレンダリングするとき、Aspose.Cells for C++は**PDFプロデューサ**フィールドに値（例：'Aspose.Cells v23.2'）を設定します。

この情報は、[**PdfSaveOptions.GetProducer()**](https://reference.aspose.com/cells/go-cpp/pdfsaveoptions/getproducer/)プロパティを使用して出力ドキュメント内で変更可能です。

{{% /alert %}}

### **直接変換**

Aspose.Cells for C++は、他のソフトウェアに依存せずにスプレッドシートからPDFへの変換をサポートします。[**Workbook**](https://reference.aspose.com/cells/go-cpp/workbook/)クラスの[**Save**](https://reference.aspose.com/cells/go-cpp/workbook/save/)メソッドを使ってExcelファイルをPDFに保存します。[**Save**](https://reference.aspose.com/cells/go-cpp/workbook/save/)メソッドは、ネイティブなExcelファイルをPDF形式に変換するための[**SaveFormat.Pdf**](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/)列挙型のメンバーを提供します。

以下の手順に従って、Excelスプレッドシートを直接PDF形式に変換します:

1. [**Workbook**](https://reference.aspose.com/cells/go-cpp/workbook/)クラスの空コンストラクターを呼び出してオブジェクトを作成します。
1. 既存のテンプレートファイルを開いたり読み込んだりするか、ワークブックをゼロから作成している場合は、この手順をスキップします。
1. Aspose.CellsのAPIを使用してスプレッドシート上で任意の作業（データの入力、書式設定の適用、数式の設定、画像やその他の描画オブジェクトの挿入など）を行います。
1. スプレッドシートのコードが完了したら、[**Workbook**](https://reference.aspose.com/cells/go-cpp/workbook/)クラスの[**Save**](https://reference.aspose.com/cells/go-cpp/workbook/save/)メソッドを呼び出してスプレッドシートを保存します。

ファイル形式はPDFを選択し、[**SaveFormat**](https://reference.aspose.com/cells/go-cpp/saveformat/)列挙型から*Pdf*（事前定義された値）を選ぶことで最終的なPDFドキュメントを生成します。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-Pdf.go" >}}
### **高度な変換**

また、[**PdfSaveOptions**](https://reference.aspose.com/cells/go-cpp/pdfsaveoptions/)クラスを使用して変換の異なる属性を設定することも可能です。[**PdfSaveOptions**](https://reference.aspose.com/cells/go-cpp/pdfsaveoptions/)クラスのさまざまなプロパティを設定することで、出力PDFの印刷、フォント、セキュリティ、圧縮設定を制御できます。

最も重要なプロパティは[**GetCompliance()**](https://reference.aspose.com/cells/go-cpp/pdfsaveoptions/getcompliance/)で、これによりPDFの標準準拠レベルを設定できます。現在、PDF 1.4、PDF 1.5、PDF 1.6、PDF 1.7、PDF/A-1a、PDF/A-1b、PDF/A-2a、PDF/A-2b、PDF/A-2u、PDF/A-3a、PDF/A-2ab、PDF/A-3u形式で保存可能です。PDF/A形式を使用すると、出力ファイルのサイズは通常のPDFより大きくなることに注意してください。

#### **PDF/A準拠ファイルへのワークブックの保存**

以下のコードスニペットは、[**PdfSaveOptions**](https://reference.aspose.com/cells/go-cpp/pdfsaveoptions/)クラスを使用してExcelファイルをPDF/A準拠のPDF形式に保存する方法を示しています。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-Pdf-1.go" >}}
{{% alert color="primary" %}}

この[**GetCompliance()**](https://reference.aspose.com/cells/go-cpp/pdfsaveoptions/getcompliance/)プロパティは、Aspose.Cells for C++バージョンのリリース以降に追加されました。

{{% /alert %}}

#### **PDF作成時間の設定**

[**PdfSaveOptions**](https://reference.aspose.com/cells/go-cpp/pdfsaveoptions/)クラスを使用すると、PDFの作成時間を取得または設定できます。次のコードは、[**PdfSaveOptions.GetCreatedTime()**](https://reference.aspose.com/cells/go-cpp/pdfsaveoptions/getcreatedtime/)プロパティを使ってPDFの作成時間を設定する例です。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-Pdf-2.go" >}}
#### **ContentCopyForAccessibilityオプションの設定**

[**PdfSaveOptions**](https://reference.aspose.com/cells/go-cpp/pdfsaveoptions/)クラスを使って、PDFの[**GetAccessibilityExtractContent()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering.pdfsecurity/pdfsecurityoptions/getaccessibilityextractcontent/)オプションを取得または設定し、変換されたPDFの内容アクセスを制御できます。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-Pdf-3.go" >}}
#### **PDFへのカスタムプロパティのエクスポート**

[**PdfSaveOptions**](https://reference.aspose.com/cells/go-cpp/pdfsaveoptions/)クラスを使用して、ソースワークブックのカスタムプロパティをPDFにエクスポートできます。[**PdfCustomPropertiesExport**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/pdfcustompropertiesexport/)列挙体は、プロパティのエクスポート方法を指定するために提供されます。これらのプロパティは、Adobe Acrobat Readerの[ファイル]→[プロパティ]をクリックして確認できます。テスト用のテンプレートファイル"sourceWithCustProps.xlsx"は[こちら](sourceWithCustProps.xlsx)からダウンロードでき、出力PDFファイル"outSourceWithCustProps"は[こちら](outSourceWithCustProps.pdf)で確認できます。

![todo:image_alt_text](convert-excel-workbook-to-pdf_1.png)

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-Pdf-4.go" >}}
### **変換属性**

私たちは新しいリリースごとに変換機能の強化に努めています。Aspose.CellsのExcelからPDFへの変換にはいくつかの制限があります。MapChartはPDF形式への変換時にサポートされていません。また、一部の描画オブジェクトもうまくサポートされていません。

以下の表は、Aspose.Cellsを使用してPDFにエクスポートする際に完全または部分的にサポートされているすべての機能を一覧にしています。こちらの表は最終版ではなく、すべてのスプレッドシート属性を網羅しているわけではありませんが、サポートされていないまたは部分的にサポートされている機能を特定しています。

| **ドキュメント要素** | **属性** | **サポート状況** | **備考** |
| :- | :- | :- | :- |
| 配置 |  | はい |  |
| 背景設定 |  | はい |  |
| 境界線 | 色 | はい |  |
| 境界線 | 線種 | はい |  |
| 境界線 | 線の太さ | はい |  |
| セルのデータ |  | はい |  |
| コメント |  | はい |  |
| 条件付き書式 |  | はい |  |
| ドキュメントのプロパティ |  | はい |  |
| 描画オブジェクト |  | 一部のみサポート | 描画オブジェクトのシャドウと3D効果は十分にサポートされていません。WordArtとSmartArtは部分的にサポートされています。 |
| フォント | サイズ | はい |  |
| フォント | 色 | はい |  |
| フォント | スタイル | はい |  |
| フォント | 下線 | はい |  |
| フォント | 効果 | はい |  |
| 画像 |  | はい |  |
| ハイパーリンク |  | はい |  |
| チャート |  | 一部のみサポート | MapChartはサポートされていません。 |
| 結合セル |  | はい |  |
| ページ区切り |  | はい |  |
| ページ設定 | ヘッダー/フッター | はい |  |
| ページ設定 | マージン | はい |  |
| ページ設定 | ページ方向 | はい |  |
| ページ設定 | ページサイズ | はい |  |
| ページ設定 | 印刷範囲 | はい |  |
| ページ設定 | 印刷タイトル | はい |  |
| ページ設定 | 拡大縮小 | はい |  |
| 行高さ/列幅 |  | はい |  |
| RTL（右から左）言語 |  | はい |  |

{{% alert color="primary" %}}

スプレッドシートに数式が含まれている場合は、絶対に[Workbook::CalculateFormula()](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/calculateformula/)を呼び出してからPDFにレンダリングするのが最良です。これにより、数式に依存した値が再計算され、正しい値がPDFに表示されます。

{{% /alert %}}

## **高度なトピック**
- [名前付き目次でPDFブックマークを追加する](/cells/ja/cpp/add-pdf-bookmarks-with-named-destinations/)
- [PDFへの変換時に特定のUnicode文字のフォントを変更する](/cells/ja/cpp/change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf/)
- [XLSXファイルをPDF形式に変換](/cells/ja/cpp/convert-xlsx-file-to-pdf-format/)
- [PDFA-1aに準拠したExcelファイルをPDF形式に変換する](/cells/ja/cpp/convert-excel-file-to-pdf-format-compatible-with-pdfa-1a/)
- [画像やチャートを含むXLSファイルをPDFに変換](/cells/ja/cpp/convert-xls-file-with-images-or-charts-to-pdf/)
- [チャートシートの PdfBookmarkEntry を作成](/cells/ja/cpp/create-pdfbookmarkentry-for-chart-sheet/)
- [1つのPDFページでワークシートのすべての列を表示する](/cells/ja/cpp/fit-all-worksheet-columns-on-single-pdf-page/)
- [DrawObjectEventHandlerクラスを使用してPDFへのレンダリング中にDrawObjectとバインドを取得](/cells/ja/cpp/get-drawobject-and-bound-while-rendering-to-pdf-using-drawobjecteventhandler-class/)
- [Excelファイルを変換する際のフォントの置換に関する警告を取得](/cells/ja/cpp/get-warnings-for-font-substitution-while-rendering-excel-file/)
- [Excel を PDF にレンダリングする際のエラーを無視](/cells/ja/cpp/ignore-errors-while-rendering-excel-to-pdf/)
- [生成されるページ数を制限する - ExcelからPDFへの変換](/cells/ja/cpp/limit-the-number-of-pages-generated-excel-to-pdf-conversion/)
- [PDFへ保存する際にコメントを印刷する](/cells/ja/cpp/print-comments-while-saving-to-pdf/)
- [ExcelをPDFに変換する際のOffice Add-Insのレンダリング](/cells/ja/cpp/render-office-add-ins-while-converting-excel-to-pdf/)
- [Excelのワークシートごとに1つのPDFページをレンダリング - ExcelからPDFへの変換](/cells/ja/cpp/render-one-pdf-page-per-excel-worksheet-excel-to-pdf-conversion/)
- [Aspose.Cellsによる出力PDFでUnicode補助文字をレンダリングする](/cells/ja/cpp/render-unicode-supplementary-characters-in-output-pdf-by-aspose-cells/)
- [追加された画像のリサンプリング - ExcelからPDFへの変換](/cells/ja/cpp/resampling-added-images-excel-to-pdf-conversion/)
- [異なるPDFファイルごとに各ワークシートを保存](/cells/ja/cpp/save-each-worksheet-to-a-different-pdf-file/)
- [標準または最小サイズでExcelをPDFに保存](/cells/ja/cpp/save-excel-into-pdf-with-standard-or-minimum-size/)
- [指定されたワークシートをPDFに保存](/cells/ja/cpp/save-specified-worksheets-to-pdf/)
- [PDFドキュメントをセキュアにする](/cells/ja/cpp/secure-pdf-documents/)
- [出力PDFおよび画像内の文字列の交差方法を指定](/cells/ja/cpp/specify-how-to-cross-string-in-output-pdf-and-image/)
