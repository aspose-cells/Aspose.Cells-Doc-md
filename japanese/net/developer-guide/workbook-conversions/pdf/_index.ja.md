---
title: PDF
type: docs
weight: 220
url: /ja/net/convert-excel-to-pdf/
---
{{% alert color="primary" %}}

Aspose.Cells は、Excel ワークブックの PDF への変換をサポートします。この例では、Excel ワークブックを PDF に完全に変換しています。

{{% /alert %}}

## **Excel ワークブックを PDF に変換する**

PDF ファイルは、組織、政府機関、および個人の間でドキュメントを交換するために広く使用されています。これは標準的なドキュメント形式であり、ソフトウェア開発者は Microsoft Excel ファイルを PDF ドキュメントに変換する方法を見つけるように求められることがよくあります。

Aspose.Cells は、Excel ファイルから PDF への変換をサポートし、変換で高い視覚的忠実度を維持します。

{{% alert color="primary" %}}

 Aspose.Cells for .NET は、出力ドキュメントに API とバージョン番号に関する情報を直接書き込みます。たとえば、ドキュメントを PDF にレンダリングすると、Aspose.Cells for .NET が読み込まれます。**応用**値が「Aspose.Cells」のフィールドと**PDF プロデューサー**値を持つフィールド、例えば「Aspose.Cells v17.9」。

出力ドキュメントからこの情報を変更または削除するように Aspose.Cells for .NET に指示することはできないことに注意してください。

{{% /alert %}}

### **直接変換**

 Aspose.Cells for .NET は、他のソフトウェアとは独立してスプレッドシートから PDF への変換をサポートします。を使用して Excel ファイルを PDF に保存するだけです。**[ワークブック](https://reference.aspose.com/cells/net/aspose.cells/workbook)**クラス'**[保存](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index)**方法。の**[保存](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index)**メソッドは、**[SaveFormat.Pdf](https://reference.aspose.com/cells/net/aspose.cells/saveformat)**ネイティブ Excel ファイルを PDF 形式に変換する列挙型メンバー。

以下の手順に従って、Excel スプレッドシートを PDF 形式に直接変換します。

1. のオブジェクトをインスタンス化する**[ワークブック](https://reference.aspose.com/cells/net/aspose.cells/workbook)**空のコンストラクターを呼び出してクラスを作成します。
1. ワークブックを最初から作成する場合は、既存のテンプレート ファイルを開いて読み込むか、この手順をスキップできます。
1. Aspose.Cells' API を使用して、スプレッドシートで任意の作業 (データの入力、書式の適用、数式の設定、画像やその他の描画オブジェクトの挿入など) を実行します。
1. スプレッドシート コードが完成したら、**[ワークブック](https://reference.aspose.com/cells/net/aspose.cells/workbook)**クラス'**[保存](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index)**スプレッドシートを保存するメソッド。

ファイル形式は PDF である必要があるため、選択します。*PDF* (定義済みの値) から**[保存形式](https://reference.aspose.com/cells/net/aspose.cells/saveformat)**最終的な PDF ドキュメントを生成するための列挙。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-XlstoPDFDirectConversation-1.cs" >}}

### **高度な変換**

また、**[PdfSaveOptions](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)**クラスを使用して、変換用にさまざまな属性を設定します。のさまざまなプロパティの設定**[PdfSaveOptions](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)**クラスを使用すると、出力 PDF の印刷、フォント、セキュリティ、および圧縮の設定を制御できます。最も重要なプロパティは、**[コンプライアンス](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/compliance)**これにより、Excel ファイルを PDF/A 準拠の PDF ファイルに保存できます。

#### **ワークブックを PDF/A コンパイル済みファイルに保存する**

以下のコード スニペットは、**[PdfSaveOptions](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)**Excel ファイルを PDF/A 準拠の PDF 形式で保存するためのクラス。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-AdvancedConversiontoPdf-1.cs" >}}

{{% alert color="primary" %}}

注意してください、**[コンプライアンス](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/compliance)**プロパティは、Aspose.Cells for .NET 5.3.0 のリリースで追加されました。

{{% /alert %}}

#### **PDF 作成時間を設定する**

とともに**[PdfSaveOptions](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)**クラスで、PDF の作成時刻を取得または設定できます。次のコードは、**[PdfSaveOptions.CreatedTime](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/createdtime)** PDF ファイルの作成時刻を設定するプロパティ。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-SetPDFCreationTime-1.cs" >}}

#### **ContentCopyForAccessibility オプションを設定する**

とともに**[PdfSaveOptions](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)**クラス、PDFを取得または設定できます**[AccessibilityExtractContent](https://reference.aspose.com/cells/net/aspose.cells.rendering.pdfsecurity/pdfsecurityoptions/properties/accessibilityextractcontent)**変換された PDF のコンテンツ アクセスを制御するオプション。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-SetContentCopyForAccessibility-1.cs" >}}

#### **カスタム プロパティを PDF にエクスポート**

とともに**[PdfSaveOptions](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)**クラスを使用すると、ソース ワークブックのカスタム プロパティを PDF にエクスポートできます。**[PdfCustomPropertiesExport](https://reference.aspose.com/cells/net/aspose.cells.rendering/pdfcustompropertiesexport)**列挙子は、プロパティをエクスポートする方法を指定するために提供されています。これらのプロパティは、次の図に示すように、[ファイル] をクリックしてから [プロパティ] オプションをクリックすると、Adobe Acrobat Reader で確認できます。テンプレートファイル「sourceWithCustProps.xlsx」がダウンロード可能[ここ](sourceWithCustProps.xlsx)テストおよび出力用の PDF ファイル「outSourceWithCustProps」が利用可能[ここ](outSourceWithCustProps.pdf)分析のために。

![todo:画像_代替_文章](convert-excel-workbook-to-pdf_1.png)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-ExportCustomPropertiesToPdf-1.cs" >}}

### **コンバージョン属性**

新しいリリースごとに変換機能の強化に取り組んでいます。 Aspose.Cell の Excel から PDF への変換には、まだいくつかの制限があります。 PDF 形式に変換すると、一部のスプレッドシートの書式が失われる場合があります。また、一部の描画オブジェクトはまだサポートされていません。

次の表は、Aspose.Cells を使用して PDF にエクスポートするときに完全または部分的にサポートされるすべての機能を示しています。 .

|**ドキュメント要素**|**属性**|**対応**|**ノート**|
|:- |:- |:- |:- |
|アライメント||はい||
|背景設定||はい||
|国境|色|はい||
|国境|線のスタイル|はい||
|国境|線幅|はい||
|Cell データ||はい||
|コメント||はい||
|条件付き書式||はい||
|ドキュメント プロパティ||はい||
|描画オブジェクト||部分的に|サポートされているオブジェクト: TextBox、Line、Rectangle、Oval、GroupBox、Button、CheckBox、RadioButton、ListBox、ComboBox、Label|
|フォント|サイズ|はい||
|フォント|色|はい||
|フォント|スタイル|はい||
|フォント|下線|はい||
|フォント|効果|部分的に|取り消し線効果のみがサポートされています|
|画像||はい||
|ハイパーリンク||はい||
|チャート||部分的に||
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
|RTL (右から左) 言語||はい||

{{% alert color="primary" %}}

スプレッドシートに数式が含まれている場合は、**[Workbook.CalculateFormula()](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula)**スプレッドシートを PDF 形式にレンダリングする直前。そうすることで、数式に依存する値が再計算され、正しい値が PDF に表示されます。

{{% /alert %}}

## **先行トピック**
- [PDFブックマークを追加](/cells/ja/net/add-pdf-bookmarks/)
- [名前付き宛先を含む PDF ブックマークを追加する](/cells/ja/net/add-pdf-bookmarks-with-named-destinations/)
- [印刷するものが何もない場合、出力 PDF で空白ページを回避する](/cells/ja/net/avoid-blank-page-in-output-pdf-when-there-is-nothing-to-print/)
- [PDF への保存中に特定の Unicode 文字だけのフォントを変更する](/cells/ja/net/change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf/)
- [PDF へのレンダリング中に、MS Excel ワークブックの外部リソースの読み込みを制御する](/cells/ja/net/control-loading-of-external-resources-in-ms-excel-workbook-while-rendering-to-pdf/)
- [XLS ファイルを PDF 形式に変換する](/cells/ja/net/convert-an-xls-file-to-pdf-format/)
- [Excel ファイルを PDFA-1a と互換性のある PDF 形式に変換する](/cells/ja/net/convert-excel-file-to-pdf-format-compatible-with-pdfa-1a/)
- [画像またはチャートを含む XLS ファイルを PDF に変換する](/cells/ja/net/convert-xls-file-with-images-or-charts-to-pdf/)
- [グラフ シートの PdfBookmarkEntry を作成する](/cells/ja/net/create-pdfbookmarkentry-for-chart-sheet/)
- [ワークシートのすべての列を 1 つの PDF ページに収める](/cells/ja/net/fit-all-worksheet-columns-on-single-pdf-page/)
- [DrawObjectEventHandler クラスを使用して PDF へのレンダリング中に DrawObject と Bound を取得する](/cells/ja/net/get-drawobject-and-bound-while-rendering-to-pdf-using-drawobjecteventhandler-class/)
- [Excel ファイルのレンダリング中にフォントの置換に関する警告を受け取る](/cells/ja/net/get-warnings-for-font-substitution-while-rendering-excel-file/)
- [Excel を PDF にレンダリングする際のエラーを無視する](/cells/ja/net/ignore-errors-while-rendering-excel-to-pdf/)
- [生成されるページ数を制限する - Excel から PDF への変換](/cells/ja/net/limit-the-number-of-pages-generated-excel-to-pdf-conversion/)
- [PDF に保存しながらコメントを印刷する](/cells/ja/net/print-comments-while-saving-to-pdf/)
- [Excel を PDF に変換しながら Office アドインをレンダリングする](/cells/ja/net/render-office-add-ins-while-converting-excel-to-pdf/)
- [Excel ワークシートごとに 1 つの PDF ページをレンダリング - Excel から PDF への変換](/cells/ja/net/render-one-pdf-page-per-excel-worksheet-excel-to-pdf-conversion/)
- [Aspose.Cells による出力 PDF の Unicode 補助文字のレンダリング](/cells/ja/net/render-unicode-supplementary-characters-in-output-pdf-by-aspose-cells/)
- [追加された画像のリサンプリング - Excel から PDF への変換](/cells/ja/net/resampling-added-images-excel-to-pdf-conversion/)
- [各ワークシートを異なる PDF ファイルに保存する](/cells/ja/net/save-each-worksheet-to-a-different-pdf-file/)
- [Excel を標準サイズまたは最小サイズで PDF に保存](/cells/ja/net/save-excel-into-pdf-with-standard-or-minimum-size/)
- [安全な PDF ドキュメント](/cells/ja/net/secure-pdf-documents/)
- [出力 PDF と画像での文字列の交差方法を指定する](/cells/ja/net/specify-how-to-cross-string-in-output-pdf-and-image/)
