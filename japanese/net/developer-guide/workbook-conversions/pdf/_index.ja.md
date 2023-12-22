---
title: Pdf
type: docs
weight: 220
url: /ja/net/convert-excel-to-pdf/
---
{{% alert color="primary" %}}

Aspose.Cells は、Excel ワークブックから PDF への変換をサポートしています。この例では、Excel ワークブックから PDF への完全な変換を確認します。

{{% /alert %}}

##  **Excel ワークブックを PDF に変換する**

PDF ファイルは、組織、政府部門、個人の間で文書を交換するために広く使用されています。これは標準のドキュメント形式であり、ソフトウェア開発者はよく Microsoft Excel ファイルを PDF ドキュメントに変換する方法を見つけるように求められます。

Aspose.Cells は、Excel ファイルから PDF への変換をサポートし、変換時に高い視覚的忠実度を維持します。

{{% alert color="primary" %}}

 Aspose.Cells for .NET は、API とバージョン番号に関する情報を出力ドキュメントに直接書き込みます。たとえば、Document を PDF にレンダリングすると、Aspose.Cells for .NET が設定されます。**PDF プロデューサー**値を含むフィールド (例: 「Aspose.Cells v23.2」)。

出力ドキュメント内のこの情報は、次の方法で変更できることに注意してください。**[PdfSaveOptions.Producer](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/Producer/)**財産。

{{% /alert %}}

###  **直接変換**

 Aspose.Cells for .NET は、他のソフトウェアから独立してスプレッドシートから PDF への変換をサポートします。次のコマンドを使用して Excel ファイルを PDF に保存するだけです。**[ワークブック](https://reference.aspose.com/cells/net/aspose.cells/workbook)**クラス'**[保存](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index)**方法。の**[保存](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index)**メソッドが提供するのは、**[SaveFormat.Pdf](https://reference.aspose.com/cells/net/aspose.cells/saveformat)**ネイティブ Excel ファイルを PDF 形式に変換する列挙メンバー。

Excel スプレッドシートを PDF 形式に直接変換するには、以下の手順に従ってください。

1. のオブジェクトをインスタンス化します。**[ワークブック](https://reference.aspose.com/cells/net/aspose.cells/workbook)**空のコンストラクターを呼び出してクラスを作成します。
1. 既存のテンプレート ファイルを開いて読み込むことも、ワークブックを最初から作成する場合はこの手順をスキップすることもできます。
1. Aspose.Cells' API を使用して、スプレッドシート上で作業 (データの入力、書式設定の適用、数式の設定、画像やその他の描画オブジェクトの挿入など) を実行します。
1. スプレッドシートのコードが完成したら、**[ワークブック](https://reference.aspose.com/cells/net/aspose.cells/workbook)**クラス'**[保存](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index)**スプレッドシートを保存するメソッド。

ファイル形式は PDF である必要があるので、選択します。*Pdf* (事前定義された値)**[保存形式](https://reference.aspose.com/cells/net/aspose.cells/saveformat)**列挙して最終的な PDF ドキュメントを生成します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-XlstoPDFDirectConversation-1.cs" >}}

###  **高度な変換**

を使用することもできます。**[PdfSaveOptions](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)**変換用のさまざまな属性を設定するクラス。のさまざまなプロパティを設定する**[PdfSaveOptions](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)**クラスを使用すると、出力 PDF の印刷、フォント、セキュリティ、圧縮設定を制御できます。最も重要なプロパティは次のとおりです。**[コンプライアンス](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/compliance)**これにより、Excel ファイルを PDF/A 準拠の PDF ファイルに保存できるようになります。

####  **ワークブックを PDF/A コンパイル済みファイルに保存**

以下に提供されるコード スニペットは、**[PdfSaveOptions](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)**Excel ファイルを PDF/A 準拠の PDF 形式で保存するクラス。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-AdvancedConversiontoPdf-1.cs" >}}

{{% alert color="primary" %}}

ご注意ください。**[コンプライアンス](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/compliance)**プロパティは Aspose.Cells for .NET 5.3.0 のリリースで追加されました。

{{% /alert %}}

####  **PDF 作成時刻を設定します**

とともに**[PdfSaveOptions](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)**クラスでは、PDF の作成時間を取得または設定できます。次のコードは、の使用法を示しています。**[PdfSaveOptions.CreatedTime](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/createdtime)**プロパティを使用して、PDF ファイルの作成時間を設定します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-SetPDFCreationTime-1.cs" >}}

####  **ContentCopyForAccessibility オプションを設定する**

とともに**[PdfSaveOptions](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)**クラスでは、PDF を取得または設定できます**[AccessibilityExtractContent](https://reference.aspose.com/cells/net/aspose.cells.rendering.pdfsecurity/pdfsecurityoptions/properties/accessibilityextractcontent)**変換された PDF のコンテンツ アクセスを制御するオプション。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-SetContentCopyForAccessibility-1.cs" >}}

####  **カスタム プロパティを PDF にエクスポート**

とともに**[PdfSaveOptions](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)**クラスを使用すると、ソース ワークブックのカスタム プロパティを PDF にエクスポートできます。**[PdfCustomPropertiesExport](https://reference.aspose.com/cells/net/aspose.cells.rendering/pdfcustompropertiesexport)**列挙子は、プロパティをエクスポートする方法を指定するために提供されます。これらのプロパティは、次の図に示すように、「ファイル」をクリックしてから「プロパティ」オプションをクリックすることで、Adobe Acrobat Reader で確認できます。テンプレートファイル「sourceWithCustProps.xlsx」がダウンロード可能[ここ](sourceWithCustProps.xlsx)テストと出力用に PDF ファイル「outSourceWithCustProps」が利用可能です[ここ](outSourceWithCustProps.pdf)分析用に。

![todo:image_alt_text](convert-excel-workbook-to-pdf_1.png)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-ExportCustomPropertiesToPdf-1.cs" >}}

###  **変換属性**

新しいリリースごとに変換機能の強化に取り組んでいます。 Aspose.Cell の Excel から PDF への変換には、まだいくつかの制限があります。 PDF 形式に変換する場合、MapChart はサポートされません。また、一部の描画オブジェクトは適切にサポートされていません。

次の表には、Aspose.Cells を使用して PDF にエクスポートするときに完全または部分的にサポートされるすべての機能がリストされています。この表は最終的なものではなく、すべてのスプレッドシート属性を網羅しているわけではありませんが、PDF への変換でサポートされない、または部分的にサポートされている機能を示しています。 。

|**文書要素**|**属性**|**サポートされています**|**ノート**|
| :- | :- | :- | :- |
|位置合わせ| |はい| |
|背景設定| |はい| |
|国境|色|はい| |
|国境|線のスタイル|はい| |
|国境|線幅|はい| |
|Cell データ| |はい| |
|コメント| |はい| |
|条件付き書式| |はい| |
|ドキュメントのプロパティ| |はい| |
|描画オブジェクト| |部分的に|描画オブジェクトの影と 3D 効果は十分にサポートされていません。ワードアートとスマートアートは部分的にサポートされています。|
|フォント|サイズ|はい| |
|フォント|色|はい| |
|フォント|スタイル|はい| |
|フォント|下線|はい| |
|フォント|効果|はい||
|画像| |はい| |
|ハイパーリンク| |はい| |
|チャート| |部分的に|マップチャートはサポートされていません。|
|合併済み Cells| |はい| |
|改ページ| |はい| |
|ページ設定|ヘッダー/フッター|はい| |
|ページ設定|余白|はい| |
|ページ設定|ページの向き|はい| |
|ページ設定|ページサイズ|はい| |
|ページ設定|印刷領域|はい| |
|ページ設定|タイトルを印刷する|はい| |
|ページ設定|スケーリング|はい| |
|行の高さ/列の幅| |はい| |
|RTL (右から左へ) 言語| |はい| |

{{% alert color="primary" %}}

スプレッドシートに数式が含まれている場合は、次のように呼び出すのが最善です。**[Workbook.CalculateFormula()](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula)**スプレッドシートを PDF 形式にレンダリングする直前。そうすることで、式に依存する値が再計算され、PDF に正しい値が表示されるようになります。

{{% /alert %}}

##  **アドバンストトピック**
- [PDF ブックマークを追加](/cells/ja/net/add-pdf-bookmarks/)
- [名前付き宛先を含む PDF ブックマークを追加する](/cells/ja/net/add-pdf-bookmarks-with-named-destinations/)
- [印刷するものが何もない場合の出力 PDF の空白ページを回避する](/cells/ja/net/avoid-blank-page-in-output-pdf-when-there-is-nothing-to-print/)
- [PDF に保存するときに、特定の Unicode 文字のみのフォントを変更します。](/cells/ja/net/change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf/)
- [PDF へのレンダリング中の MS Excel ワークブックでの外部リソースの読み込みを制御する](/cells/ja/net/control-loading-of-external-resources-in-ms-excel-workbook-while-rendering-to-pdf/)
- [XLSXファイルをPDF形式に変換](/cells/ja/net/convert-xlsx-file-to-pdf-format/)
- [Excel ファイルを PDFA-1a と互換性のある PDF 形式に変換します](/cells/ja/net/convert-excel-file-to-pdf-format-compatible-with-pdfa-1a/)
- [画像またはグラフを含む XLS ファイルを PDF に変換します](/cells/ja/net/convert-xls-file-with-images-or-charts-to-pdf/)
- [グラフ シートの PdfBookmarkEntry を作成する](/cells/ja/net/create-pdfbookmarkentry-for-chart-sheet/)
- [ワークシートのすべての列を 1 つの PDF ページに収める](/cells/ja/net/fit-all-worksheet-columns-on-single-pdf-page/)
- [DrawObjectEventHandler クラスを使用して PDF にレンダリング中に DrawObject と Bound を取得します](/cells/ja/net/get-drawobject-and-bound-while-rendering-to-pdf-using-drawobjecteventhandler-class/)
- [Excel ファイルのレンダリング中にフォント置換に関する警告が表示される](/cells/ja/net/get-warnings-for-font-substitution-while-rendering-excel-file/)
- [Excel を PDF にレンダリングする際のエラーを無視する](/cells/ja/net/ignore-errors-while-rendering-excel-to-pdf/)
- [生成されるページ数を制限する - Excel から PDF への変換](/cells/ja/net/limit-the-number-of-pages-generated-excel-to-pdf-conversion/)
- [PDF に保存中にコメントを印刷](/cells/ja/net/print-comments-while-saving-to-pdf/)
- [Excel を PDF に変換するときに Office アドインをレンダリングする](/cells/ja/net/render-office-add-ins-while-converting-excel-to-pdf/)
- [Excel ワークシートごとに 1 つの PDF ページをレンダリング - Excel から PDF への変換](/cells/ja/net/render-one-pdf-page-per-excel-worksheet-excel-to-pdf-conversion/)
- [出力 PDF の Unicode 補助文字を Aspose.Cells でレンダリングします](/cells/ja/net/render-unicode-supplementary-characters-in-output-pdf-by-aspose-cells/)
- [追加された画像のリサンプリング - Excel から PDF への変換](/cells/ja/net/resampling-added-images-excel-to-pdf-conversion/)
- [各ワークシートを別の PDF ファイルに保存](/cells/ja/net/save-each-worksheet-to-a-different-pdf-file/)
- [標準または最小サイズで Excel を PDF に保存します](/cells/ja/net/save-excel-into-pdf-with-standard-or-minimum-size/)
- [指定したワークシートを PDF に保存](/cells/ja/net/save-specified-worksheets-to-pdf/)
- [安全な PDF ドキュメント](/cells/ja/net/secure-pdf-documents/)
- [出力PDFと画像の文字列を交差させる方法を指定します](/cells/ja/net/specify-how-to-cross-string-in-output-pdf-and-image/)
