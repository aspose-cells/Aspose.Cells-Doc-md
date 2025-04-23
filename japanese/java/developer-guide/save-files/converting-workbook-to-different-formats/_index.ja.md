---
title: 異なるフォーマットにワークブックを変換する
type: docs
weight: 20
url: /ja/java/converting-workbook-to-different-formats/
---

{{% alert color="primary" %}}

Aspose.Cellsは多くの形式間での変換をサポートしています。技術的には、変換とはワークブックを1つのファイル形式で読み込み、別の形式で保存することを指します。

{{% /alert %}}

## **ExcelをXPSに変換**

XPS文書形式は、文書のレイアウト、各ページの視覚的な外観、ページの配布、アーカイブ化、レンダリング、処理、および印刷に関するレンダリング規則を定義する構造化されたXMLマークアップから構成されています。

XPSのマークアップ言語は、XPSでベクターグラフィック要素を組み込むことを可能にするXAMLのサブセットであり、Windows Presentation Foundation（WPF）プリミティブをマークアップするためにXAMLを使用します。使用される要素はパスおよびその他の幾何学的プリミティブとして記述されます。

XPSファイルは、Open Packaging Conventionsを使用したUnicode ZIPアーカイブで実際には構成されており、これにはドキュメントを構成するファイルが含まれています。これには各ページのXMLマークアップファイル、テキスト、埋め込みフォント、ラスタイメージ、2Dベクターグラフィックなどが含まれます。また、デジタル著作権管理情報も含まれます。XPSファイルの内容は、ZIPファイルをサポートするアプリケーションで開くことで簡単に確認できます。

Aspose.Cells 6.0.0から、 Microsoft ExcelからXPSへの変換がサポートされています。

### **単一のワークシートをXPSに変換する**

次の例は、ExcelファイルのワークシートをXPSに変換する方法を示しています。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-ConvertingsingleWorksheetToXPS-ConvertingsingleWorksheetToXPS.java" >}}

### **XPSへのワークブック全体のエクスポート**

次の例は、ワークブック全体をXPS形式に変換する方法を示しています。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-ExportWholeWorkbookToXPS-ExportWholeWorkbookToXPS.java" >}}

### **クイックExcelからXPSへの変換**

次の例は、Excelファイルを直接XPS形式に変換する簡単な方法を示しています。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-QuickExcelToXPSConversion-QuickExcelToXPSConversion.java" >}}

## **ExcelをMHTMLファイルに変換する**

[**MHTML**](https://en.wikipedia.org/wiki/MHTML)は通常HTMLと外部リソース（画像、アニメーション、オーディオなど）を1つのファイルに結合します。.mhtファイル拡張子を持つメールで使用されます。

{{% alert color="primary" %}}

Aspose.CellsはMHTMLファイルの読み書きをサポートしています。

{{% /alert %}}

スプレッドシートをMHTMLに変換することは、以下に示すように迅速な操作です。

以下のコード例は、ワークブックをMHTMLファイルとして保存する方法を示しています。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-ConvertingToMHTMLFiles-ConvertingToMHTMLFiles.java" >}}

## **ExcelファイルをHTMLに変換する**

Aspose.Cells APIは、スプレッドシートをHTML形式にエクスポートするためのサポートを提供します。この目的において、Aspose.Cellsは[**HtmlSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/HtmlSaveOptions)クラスを使用し、出力HTMLの複数の側面を制御することができます。

以下のコードは、追加パラメータを指定せずにMicrosoft ExcelファイルをHTML形式にエクスポートするために[**HtmlSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/HtmlSaveOptions)クラスを使用する方法を示しています。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-ConvertingToHTMLFiles-ConvertingToHTMLFiles.java" >}}

{{% alert color="primary" %}}

[**SaveFormat.HTML**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#HTML)を[**Workbook.save**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save-java.io.OutputStream-com.aspose.cells.SaveOptions-)メソッドに渡すことで同じ結果を得ることができます。

{{% /alert %}}

### **HTMLの画像設定**

Aspose.Cells 8.0.2から、スプレッドシートをHTML形式で保存する際に画像の設定を指定するための[**HtmlSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/HtmlSaveOptions)クラス用に[**ImageOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ImageOptions)が公開されています。

適用可能な画像設定は次の通りです:

- [**ImageType**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#ImageType): 画像タイプを取得または設定します。すべての形状（チャートを含む）は、出力HTMLで画像としてレンダリングされます。
- [**Quality**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#Quality): JpegとしてImageFormatが指定されている場合、画像の品質を0～100で取得または設定します。
- [**VerticalResolution**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#VerticalResolution): ImageFormatが指定されている場合の画像の垂直方向解像度を取得または設定します。
- [**HorizontalResolution**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#HorizontalResolution): ImageFormatが指定されている場合の画像の水平方向解像度を取得または設定します。
- [**TiffCompression**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#TiffCompression): TiffとしてImageFormatが指定されている場合の画像の圧縮タイプを取得または設定します。
- [**Transparent**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#Transparent): PngとしてImageFormatが指定されている場合、画像の背景を透明にするかどうかを示します。

以下のコードは、異なる設定を指定するために[**HtmlSaveOptions.ImageOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ImageOptions)を使用する方法を示しています。

|**エクスポート前のスプレッドシート表示**|**エクスポート後のHTML表示**|
| :- | :- |
|![エクスポート前のスプレッドシート表示](converting-workbook-to-different-formats_1.png)|![エクスポート後のHTML表示](converting-workbook-to-different-formats_2.png)|

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-SettingImagePrefrencesforHTML-SettingImagePrefrencesforHTML.java" >}}

## **ExcelをPDFファイルに変換する**

PDF文書は、組織、政府部門、個人間で文書を交換する標準的な形式として広く使用されています。ソフトウェア開発者は、Microsoft Excelファイルを簡単にPDF文書に変換する方法を考案するように求められることがあります。Aspose.Cellsはこれらの機能をサポートしています。この記事では、その方法を示しています。

### **ExcelをPDFに変換する**

Microsoft ExcelからPDFへの変換はAspose.Cells for Java 2.3.0で導入されました。そのリリースから、Aspose.Cellsは[直接スプレッドシートをPDFに変換](#直接変換)（[PDF/A](#excelスプレッドシートをpdfa準拠ファイルに保存)を含む）することができます。以前のバージョンのAspose.Cellsでスプレッドシートを変換するには、[Aspose.PDFを使用します](#asposepdf-asposecells 230より前のバージョンでの変換)。

Aspose.Cellsは高い精度と忠実度でスプレッドシートをPDFに変換します。ただし、この記事の最後に[制限事項](/cells/ja/java/converting-workbook-to-different-formats/#conversion-attributes)がいくつかリストされています。

{{% alert color="primary" %}}

Aspose.Cells for Javaは、APIとバージョン番号に関する情報を直接出力ドキュメントに記述します。たとえば、DocumentをPDFにレンダリングする際、Aspose.Cells for Javaは**Application**フィールドに値「Aspose.Cells」、**PDF Producer**フィールドに値「Aspose.Cells for Java v17.9」などを埋めます。

この情報を出力ドキュメントから変更または削除するようにAspose.Cells for Javaに指示することはできません。

{{% /alert %}}

#### **直接変換**

最も効率的な変換方法である、[**Workbook.save**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save-java.io.OutputStream-com.aspose.cells.SaveOptions-)メソッドを使用してExcelファイルを直接PDFに保存し、[**SaveFormat.PDF**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#PDF)インターフェースメンバーを提供します。これにより、データや書式を失うことなく、出力されるPDFが入力のExcelファイルに似た外観になります。

PDFに保存する際にセキュリティオプションを指定するには、[**PdfSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/PdfSaveOptions) を使用してください。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-Excel2PDFConversion-Excel2PDFConversion.java" >}}

#### **高度な変換**

変換の別の属性を設定するために[**PdfSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/PdfSaveOptions)クラスを使用することも選択できます。[**PdfSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/PdfSaveOptions)クラスの異なるプロパティを設定すると、出力されるPDFファイルの印刷、フォント、セキュリティ、圧縮設定をコントロールできます。最も注目すべきプロパティは[**Compliance**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#Compliance)で、ExcelファイルをPDF/Aに準拠したPDFファイルに保存できるようにします。

##### **ExcelスプレッドシートをPDF/A適合ファイルに保存**

次に示すコードスニペットは、[**PdfSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/PdfSaveOptions)クラスを使用してExcelファイルをPDF/Aに準拠したPDF形式で保存する方法を示しています。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-AdvancedConversiontoPdf-AdvancedConversiontoPdf.java" >}}

#### **Aspose.Pdfを使用した変換：Aspose.Cells 2.3.0以前**

Aspose.Cellsバージョン2.3.0より前のバージョンでは、[Aspose.PDF for Java](/pdf/java/)のようなコンポーネントを使用してスプレッドシートをPDFファイルに変換する必要があります。 Aspose.CellsとAspose.PDFは中間ステップを経てスプレッドシートをPDFに変換します。

Aspose.CellsとAspose.PDFを使用してスプレッドシートをPDFに変換するには、次のようにします。

1. 空のコンストラクタを呼び出して[**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)クラスのオブジェクトをインスタンス化します。
1. Aspose.Cells APIを使用して、スプレッドシートで必要な作業を行います。
1. [**Workbook.save**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save-java.io.OutputStream-com.aspose.cells.SaveOptions-)メソッドを呼び出して、スプレッドシートを保存します。
   1. ファイル形式をXMLに設定します。
   1. FileFormatTypeインタフェースからAspose_Pdf（事前定義値）を選択します。これにより、保存メソッドがAspose.PDF for Javaと互換性のあるXML形式のスプレッドシートを生成します。
1. XMLファイルが作成されたら、aspose.pdfパッケージのPdfクラスのオブジェクトを作成します。
1. PdfクラスのbindXMLメソッドを呼び出し、出力XMLファイルの名前を渡します。
1. Pdfクラスのsaveメソッドを呼び出し、PDFドキュメントを生成します。

上記の手順を以下の例で実装します。

{{% alert color="primary" %}}

スプレッドシートに数式が含まれている場合、PDF 形式に変換する直前に [**Workbook.calculateFormula**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula--) メソッドを呼び出すことが最適です。これにより、数式に依存する値が再計算され、正しい値が PDF にレンダリングされます。

{{% /alert %}}

#### **変換属性**

Aspose.Cellsの変換およびその他の側面を改善するために、我々は毎リリース努力しています。 ExcelからPDFへの変換にはいくつかの制約があります。スプレッドシートで指定された一部のフォーマット設定が失われる場合があり、すべての描画オブジェクトがサポートされているわけではありません。

以下の表は、Aspose.Cellsを使用してPDFにエクスポートする際に完全または部分的にサポートされるすべての機能をリスト表示しています。この表は最終的なものではなく、すべてのスプレッドシート属性をカバーしているわけではありません。また、変換に対応していない機能や部分的にサポートされる機能を特定できます。

{{% alert color="primary" %}}

|**ドキュメント要素**|**属性**|**サポートされている**|**備考**|
| :- | :- | :- | :- |
|配置| |はい| |
|回転| |部分的に|90度と-90度のみサポートされています。
|背景設定| |はい| |
|ボーダー|色|はい| |
|ボーダー|線のスタイル|はい| |
|ボーダー|線の幅|はい| |
|セルデータ| |はい| |
|コメント| |なし| |
|条件付き書式| |はい| |
|ドキュメントプロパティ| |はい| |
|描画オブジェクト| |はい| |
|フォント|サイズ|はい| |
|フォント|色|はい| |
|フォント|スタイル|はい| |
|フォント|下線|はい| |
|フォント|エフェクト|部分的に|打ち消し線のエフェクトのみサポートされています。
|画像| |はい| |
|ハイパーリンク| |はい| |
|チャート| |はい| |
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
{{% /alert %}}
{{< app/cells/assistant language="java" >}}
