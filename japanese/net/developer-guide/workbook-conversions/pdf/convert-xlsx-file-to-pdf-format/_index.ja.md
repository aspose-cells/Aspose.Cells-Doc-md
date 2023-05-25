---
title: XLSXファイルをPDF形式に変換
type: docs
weight: 30
url: /ja/net/convert-xlsx-file-to-pdf-format/
---
{{% alert color="primary" %}}

PDF (Portable Document Format) は、文書の作成に使用されたソフトウェア、ハードウェア、オペレーティング システムとは独立した文書を表します。 PDF ファイルは、デバイスや解像度に依存しない方法で、テキスト、グラフィック、画像を任意に組み合わせたドキュメントにすることができます。 PDF ファイルは圧縮されることが多いため、元のファイルよりも占有するスペースが少なくなります。

場合によっては、Microsoft Excel ファイルを PDF に変換する必要があります。そのためには、PDF ドキュメントを世界中に配布できる、高速、安全、正確で信頼性の高いソリューションが必要です。このタスクを実行できる変換ツールは多数あります。ただし、元の Excel ドキュメントのレイアウトが出力 PDF ファイルに保持されていることを確認する必要があります。画像、グラフ、図形、データ書式設定、フォント、属性、色、ページ設定、テキストの向き、枠線、グラフなどは、正確かつ正確にレンダリングされる必要があります。[Aspose.Cells](https://products.aspose.com/cells/net/)高忠実度の変換を保証します。

このドキュメントは、Microsoft Excel ドキュメント (画像、グラフ、書式設定などを含む) を PDF に変換する方法を包括的に理解できるように設計されています。そのために、Visual Studio.Net で変換する簡単なコンソール アプリケーションを作成する方法を示します。 Aspose.Cells API を使用して、Excel ファイルを PDF に変換します。変換は高度な精度で実行されます。

{{% /alert %}}

##  **Excel を PDF に変換する**

この例では、Excel ファイル (SampleInput.xlsx) をテンプレートとして使用します。ワークブックには、グラフと画像を含むワークシートが含まれています。各ワークシートには、フォント、属性、色、シェーディング効果、境界線を使用したさまざまなタイプのフォーマットが含まれています。最初のワークシートに縦棒グラフがあり、最後のワークシートに画像があります。

###  **テンプレート Excel ファイル**

テンプレート ファイルには、メディアとしてのグラフと画像を含む 3 つのワークシートが含まれています。以下のスクリーンショットに示すように、最初のワークシートにはグラフが含まれ、最後のワークシートには画像が含まれています。

|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Sheet1.png)|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Sheet2.png)|
| :- | :- |
|最初のワークシート**（販売予測）**| 2 番目のワークシート**(売上報告書)**|
|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Sheet3.png)|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Sheet4.png)|
| 3 番目のワークシート**（データ入力）**|最後のワークシート**（画像）**|

###  **変換プロセス**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Docs-Pdf-ConvertXlsxFileToPdf.cs" >}}

{{% alert color="primary" %}}

スプレッドシートに数式が含まれている場合は、次のように呼び出すのが最善です。[Workbook.CalculateFormula](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula)これにより、式に依存する値が再計算され、正しい値が PDF にレンダリングされます。

{{% /alert %}}

###  **結果**

上記のコードが実行されると、アプリケーション ディレクトリの Files フォルダーに PDF ファイルが作成されます。
次のスクリーンショットは、PDF ページを示しています。ヘッダーとフッターは出力 PDF ファイルにも保持されることに注意してください。

|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted1.png)|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted2.png)|
| :- | :- |
|最初のワークシート**（販売予測）**| 2 番目のワークシート**(売上報告書)**|
|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted3.png)|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted4.png)|
| 3 番目のワークシート**（データ入力）**|最後のワークシート**（画像）**|
