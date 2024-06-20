---
title: XLSX ファイルを PDF フォーマットに変換する
type: docs
weight: 30
url: /ja/net/convert-xlsx-file-to-pdf-format/
---

{{% alert color="primary" %}}

PDF（Portable Document Format）は、ドキュメントの作成に使用されるソフトウェア、ハードウェア、およびオペレーティングシステムに依存せずにドキュメントを表現するフォーマットです。PDF ファイルには、テキスト、グラフィックス、画像の任意の組み合わせをデバイスに依存せず、解像度に依存しない方法で表現することができます。PDF ファイルはしばしば圧縮されるため、元のファイルよりも少ないスペースを占めます。

時折、マイクロソフトの Excel ファイルを PDF に変換する必要があります。このためには、世界中に PDF ドキュメントを配布できるように、高速かつ正確で信頼性のあるソリューションが必要です。このタスクを実行できる多くの変換ツールがあります。ただし、元の Excel ドキュメントのレイアウトが出力 PDF ファイルで維持されることを確認する必要があります。画像、グラフ、図形、データの書式設定、フォント、属性、色、ページ設定の設定、テキストの向き、境界、グラフなどは正確かつ精密にレンダリングされる必要があります。[Aspose.Cells](https://products.aspose.com/cells/net/) は高品質な変換を保証します。

このドキュメントは、マイクロソフトの Excel ドキュメント（画像、グラフ、書式設定などを含む）をどのように PDF に変換するかについて詳細な理解を提供するよう設計されています。そのために、Aspose.Cells API を使用して Excel ファイルを PDF に変換する Visual Studio.Net での簡単なコンソールアプリケーションの作成方法を示しています。変換は高度な精度と正確さで行われます。

{{% /alert %}}

## **ExcelをPDFに変換する**

この例では、Excel ファイル（SampleInput.xlsx）をテンプレートとして使用しています。ワークブックには、フォント、属性、色、網掛け効果、境界などを使用したさまざまな形式のワークシートが含まれています。最初のワークシートには列グラフがあり、最後のワークシートには画像が含まれています。

### **テンプレートの Excel ファイル**

テンプレートファイルには、グラフが含まれたワークシートが3つあり、最後のワークシートには画像が含まれています。以下のスクリーンショットに例示されています。

|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Sheet1.png)|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Sheet2.png)|
| :- | :- |
|最初のワークシート**(売上予測)**|2番目のワークシート**(売上報告)**|
|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Sheet3.png)|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Sheet4.png)|
|3番目のワークシート**(データ入力)**|最後のワークシート**(画像)**|

### **変換プロセス**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Docs-Pdf-ConvertXlsxFileToPdf.cs" >}}

{{% alert color="primary" %}}

スプレッドシートに数式が含まれている場合は、スプレッドシートをPDFにレンダリングする直前に[Workbook.CalculateFormula](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula)メソッドを呼び出すのが最適です。これにより、数式に依存する値が再計算され、正しい値がPDFにレンダリングされます。

{{% /alert %}}

### **結果**

上記のコードを実行すると、アプリケーションディレクトリのFilesフォルダにPDFファイルが作成されます。
以下のスクリーンショットは、PDFページを示しています。ヘッダーとフッターも出力されたPDFファイルに保持されていることに注意してください。

|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted1.png)|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted2.png)|
| :- | :- |
|最初のワークシート**(売上予測)**|2番目のワークシート**(売上報告)**|
|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted3.png)|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted4.png)|
|3番目のワークシート**(データ入力)**|最後のワークシート**(画像)**|
