---
title: ワークブックを別の形式に変換する
type: docs
weight: 20
url: /ja/java/converting-workbook-to-different-formats/
---
{{% alert color="primary" %}}

Aspose.Cells は、多くのフォーマット間の変換をサポートしています。技術的には、変換とは、ワークブックをあるファイル形式で読み込み、別のファイル形式に保存することを意味します。

{{% /alert %}}

## **Excel から XPS への変換**

XPS ドキュメント形式は、ドキュメントのレイアウトと各ページの外観を定義する構造化された XML マークアップと、ドキュメントの配布、アーカイブ、レンダリング、処理、および印刷のためのレンダリング ルールで構成されます。

XPS のマークアップ言語は XAML のサブセットであり、XAML を使用して Windows Presentation Foundation (WPF) プリミティブをマークアップし、ドキュメントにベクター グラフィック要素を組み込むことができます。使用される要素は、パスおよびその他のジオメトリ プリミティブの観点から記述されます。

XPS ファイルは、実際には、ドキュメントを構成するファイルを含む、Open Packaging Conventions を使用した Unicode ZIP アーカイブです。これらには、各ページの XML マークアップ ファイル、テキスト、埋め込みフォント、ラスター イメージ、2D ベクター グラフィックス、およびデジタル著作権管理情報が含まれます。 XPS ファイルの内容は、ZIP ファイルをサポートするアプリケーションで開くだけで調べることができます。

Aspose.Cells 6.0.0 から、Microsoft Excel tp XPS 変換に対応しました。

### **単一のワークシートを XPS に変換する**

次の例は、Excel ファイル内の 1 つのワークシートを XPS に変換する方法を示しています。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-ConvertingsingleWorksheetToXPS-ConvertingsingleWorksheetToXPS.java" >}}

### **ワークブック全体を XPS にエクスポート**

次の例は、ブック全体を XPS 形式に変換する方法を示しています。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-ExportWholeWorkbookToXPS-ExportWholeWorkbookToXPS.java" >}}

### **Excel から XPS へのクイック変換**

次の例は、Excel ファイルを XPS 形式に直接変換する簡単な方法を示しています。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-QuickExcelToXPSConversion-QuickExcelToXPSConversion.java" >}}

## **Excel から MHTML ファイルへの変換**

[MHTML](https://en.wikipedia.org/wiki/MHTML)通常の HTML と外部リソースを組み合わせます。つまり、通常は画像、アニメーション、音声などを 1 つのファイルにリンクするコンテンツです。これらは、ファイル拡張子が .mht の電子メールに使用されます。

{{% alert color="primary" %}}

Aspose.Cells は、MHTML ファイルの読み取りと書き込みをサポートします。

{{% /alert %}}

以下に示すように、スプレッドシートを MHTML に変換する操作は簡単です。

次のコード例は、ワークブックを MHTML ファイルとして保存する方法を示しています。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-ConvertingToMHTMLFiles-ConvertingToMHTMLFiles.java" >}}

## **Excel ファイルを HTML に変換する**

Aspose.Cells API は、スプレッドシートを HTML 形式にエクスポートするためのサポートを提供します。この目的のために、Aspose.Cells は**[HtmlSaveOptions](https://reference.aspose.com/cells/java/com.aspose.cells/HtmlSaveOptions)**開発者が出力 HTML のいくつかの側面を制御できるようにするクラス。

以下のコードは、**[HtmlSaveOptions](https://reference.aspose.com/cells/java/com.aspose.cells/HtmlSaveOptions)**クラスを使用して、追加のパラメーターを指定せずに Microsoft Excel ファイルを HTML 形式にエクスポートします。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-ConvertingToHTMLFiles-ConvertingToHTMLFiles.java" >}}

{{% alert color="primary" %}}

を渡すことで同じ結果が得られる場合があります。**[SaveFormat.HTML](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#HTML)**に**[Workbook.save](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save(java.io.OutputStream,%20com.aspose.cells.SaveOptions))**方法。

{{% /alert %}}

### **HTML の画像プリファレンスの設定**

8.0.2から、Aspose.Cellsが公開されました**[ImageOptions](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ImageOptions)**のために**[HtmlSaveOptions](https://reference.aspose.com/cells/java/com.aspose.cells/HtmlSaveOptions)**クラスを使用すると、開発者はスプレッドシートを HTML 形式で保存するときに画像の設定を指定できます。

適用できる画像設定は次のとおりです。

- **[画像タイプ](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#ImageType)**: 画像の種類を取得または設定します。チャートを含むすべての形状は、出力 HTML で画像としてレンダリングされることに注意してください。
- **[品質](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#Quality)**: ImageFormat が Jpeg として指定されている場合、画像の品質を 0 ～ 100 で取得または設定します。
- **[VerticalResolution](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#VerticalResolution)**: イメージの垂直方向の解像度をドット/インチで取得または設定します。
- **[水平解像度](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#HorizontalResolution)**: イメージの水平方向の解像度をドット/インチで取得または設定します。
- **[TiffCompression](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#TiffCompression)**: ImageFormat が Tiff として指定されている場合、イメージの圧縮タイプを取得または設定します。
- **[透明](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#Transparent)**ImageFormat が Png として指定されている場合、画像の背景を透明にするかどうかを示します。

以下のコードは、使用方法を示しています**[HtmlSaveOptions.ImageOptions](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ImageOptions)**さまざまな設定を指定します。

|**エクスポート前のスプレッドシート ビュー**|**エクスポート後の HTML ビュー**|
|:- |:- |
|![エクスポート前のスプレッドシート ビュー](converting-workbook-to-different-formats_1.png)|![エクスポート後の HTML ビュー](converting-workbook-to-different-formats_2.png)|

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-SettingImagePrefrencesforHTML-SettingImagePrefrencesforHTML.java" >}}

## **Excel を PDF ファイルに変換する**

PDF ドキュメントは、組織、政府部門、および個人の間でドキュメントを交換するための標準形式として広く使用されています。ソフトウェア開発者は、Microsoft Excel ファイルを PDF ドキュメントに簡単に変換する方法を考案するように求められることがよくあります。 Aspose.Cells はこれらの機能をサポートしています。この記事では、その方法を示します。

### **Excel から PDF への変換**

Microsoft Excel から PDF への変換は、Aspose.Cells for Java 2.3.0 で導入されました。そのリリースから、Aspose.Cells で[スプレッドシートを直接 PDF に変換](#direct-conversion)（含む[PDF/A](#saving-excel-spreadsheets-to-pdfa-complied-files))、別の製品なし。古いバージョンの Aspose.Cells のスプレッドシートを変換するには、[変換には Aspose.PDF を使用します](#conversion-with-asposepdf-asposecells-prior-to-230).

Aspose.Cell は、スプレッドシートを高い精度と忠実度で PDF に変換します。ただし、いくつかあります[制限事項](/cells/ja/java/converting-workbook-to-different-formats/#conversion-attributes)、この記事の最後に記載されています。

{{% alert color="primary" %}}

 Aspose.Cells for Java は、出力ドキュメントに API とバージョン番号に関する情報を直接書き込みます。たとえば、ドキュメントを PDF にレンダリングすると、Aspose.Cells for Java が読み込まれます。**応用**値が「Aspose.Cells」のフィールドと**PDF プロデューサー** 'Aspose.Cells for Java v17.9' などの値を持つフィールド。

出力ドキュメントからこの情報を変更または削除するように Aspose.Cells for Java に指示することはできないことに注意してください。

{{% /alert %}}

#### **直接変換**

を使用して、Excel ファイルを直接 PDF に保存します。**[Workbook.save](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save(java.io.OutputStream,%20com.aspose.cells.SaveOptions))**メソッドを提供し、**[SaveFormat.PDF](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#PDF)**インターフェイスメンバー。このような直接変換は、最も効率的な変換方法です。データやフォーマットは失われませんが、出力 PDF は入力 Excel ファイルのように見えます。

 PDF に保存するときにセキュリティ オプションを指定するには、次を使用します。**[PdfSaveOptions](https://reference.aspose.com/cells/java/com.aspose.cells/PdfSaveOptions)**.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-Excel2PDFConversion-Excel2PDFConversion.java" >}}

#### **高度な変換**

また、**[PdfSaveOptions](https://reference.aspose.com/cells/java/com.aspose.cells/PdfSaveOptions)**クラスを使用して、変換用にさまざまな属性を設定します。のさまざまなプロパティの設定**[PdfSaveOptions](https://reference.aspose.com/cells/java/com.aspose.cells/PdfSaveOptions)**クラスを使用すると、結果の PDF ファイルの印刷、フォント、セキュリティ、および圧縮設定を制御できます。最も注目すべきプロパティは、**[コンプライアンス](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#Compliance)**これにより、Excel ファイルを PDF/A 準拠の PDF ファイルに保存できます。

##### **Excel スプレッドシートを PDF/A コンパイル済みファイルに保存する**

以下のコード スニペットは、**[PdfSaveOptions](https://reference.aspose.com/cells/java/com.aspose.cells/PdfSaveOptions)**クラスを使用して、Excel ファイルを PDF/A 準拠の PDF 形式で保存します。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-AdvancedConversiontoPdf-AdvancedConversiontoPdf.java" >}}

#### **Aspose.Pdf での変換: Aspose.Cells 2.3.0 より前**

バージョン 2.3.0 より前の Aspose.Cells バージョンでは、次のようなコンポーネントを使用する必要があります[Aspose.PDF for Java](/pdf/java/)スプレッドシートを PDF ファイルに変換します。 Aspose.Cells と Aspose.PDF は連携して、中間ステップを介してスプレッドシートを PDF に変換します。

スプレッドシートを Aspose.Cells および Aspose.PDF で PDF に変換するには:

1. のオブジェクトをインスタンス化する**[ワークブック](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)**空のコンストラクターを呼び出してクラスを作成します。
1. Aspose.Cells API を使用して、スプレッドシートで必要な作業を行います。
1. 電話する**[Workbook.save](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save(java.io.OutputStream,%20com.aspose.cells.SaveOptions))**スプレッドシートを保存する方法:
1. ファイル形式を XML に設定します。
 1. FileFormatType インターフェイスから Aspose_Pdf (定義済みの値) を選択します。これにより、Aspose.PDF for Java が PDF ドキュメントを生成できるように、Aspose.PDF スキーマと互換性のある XML 形式でスプレッドシートを生成するように save メソッドに指示されます。
1. XML ファイルが作成されたら、aspose.pdf パッケージに Pdf クラスのオブジェクトを作成します。
1. Pdf クラスの bindXML メソッドを呼び出し、出力 XML ファイルの名前を渡します。
1. PDF ドキュメントを生成するには、Pdf クラスの save メソッドを呼び出します。

上記の手順は、以下の例で実装されています。

{{% alert color="primary" %}}

スプレッドシートに数式が含まれている場合は、**[Workbook.calculateFormula](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula())**スプレッドシートを PDF 形式にレンダリングする直前のメソッド。そうすることで、数式に依存する値が再計算され、正しい値が PDF に表示されます。

{{% /alert %}}

#### **コンバージョン属性**

私たちは、すべてのリリースで Aspose.Cells の変換およびその他の側面を改善するために懸命に取り組んでいます。 Excel から PDF への変換にはいくつかの制限があります。スプレッドシートで指定された一部の形式設定が失われる可能性があり、すべての描画オブジェクトがサポートされているわけではありません。

以下の表は、Aspose.Cells を使用して PDF にエクスポートするときに完全または部分的にサポートされるすべての機能を示しています。この表は最終的なものではなく、すべてのスプレッドシート属性を網羅しているわけではありません。また、変換でサポートされていない機能や部分的にサポートされている機能を特定することもできます。

{{% alert color="primary" %}}

|**ドキュメント要素**|**属性**|**ネット対応**|**ノート**|
|:- |:- |:- |:- |
|アライメント||はい||
|回転||部分的に|90 と -90 のみをサポートします。|
|背景設定||はい||
|国境|色|はい||
|国境|線のスタイル|はい||
|国境|線幅|はい||
|Cell データ||はい||
|コメント||いいえ||
|条件付き書式||はい||
|ドキュメント プロパティ||はい||
|描画オブジェクト||はい||
|フォント|サイズ|はい||
|フォント|色|はい||
|フォント|スタイル|はい||
|フォント|下線|はい||
|フォント|効果|部分的に|取り消し線効果のみがサポートされています|
|画像||はい||
|ハイパーリンク||はい||
|チャート||はい||
|合併Cells||はい||
|改ページ||はい||
|ページ設定|ヘッダー/フッター|はい||
|ページ設定|余白|はい||
|ページ設定|ページの向き|はい||
|ページ設定|ページサイズ|はい||
|ページ設定|印刷範囲|はい||
|ページ設定|タイトルを印刷する|はい||
|ページ設定|スケーリング|はい||
|行の高さ/列の幅||はい||
{{% /alert %}}
