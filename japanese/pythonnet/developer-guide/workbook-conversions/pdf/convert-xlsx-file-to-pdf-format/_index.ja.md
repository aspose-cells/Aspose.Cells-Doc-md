---
title: XLSX ファイルを PDF フォーマットに変換する
type: docs
weight: 30
url: /ja/python-net/convert-xlsx-file-to-pdf-format/
description: Aspose.Cells for Python via .NET APIを使用して、XLSXファイルをPDF形式に変換する方法について学びます。
keywords: PythonでXLSXファイルをPDF形式に変換する方法、Pythonを使用したxlsxからpdfへの変換、Pythonでxlsxをpdfに保存、Pythonでxlsxをpdf形式に変換
---

{{% alert color="primary" %}}

PDF（Portable Document Format）は、ドキュメントの作成に使用されるソフトウェア、ハードウェア、およびオペレーティングシステムに依存せずにドキュメントを表現するフォーマットです。PDF ファイルには、テキスト、グラフィックス、画像の任意の組み合わせをデバイスに依存せず、解像度に依存しない方法で表現することができます。PDF ファイルはしばしば圧縮されるため、元のファイルよりも少ないスペースを占めます。

時折、Microsoft ExcelファイルをPDFに変換する必要があります。この場合、世界中にPDFドキュメントを配布できる高速で安全、正確で信頼性のあるソリューションが必要となります。このタスクを実行できる多くの変換ツールがあります。ただし、元のExcelドキュメントのレイアウトが、出力PDFファイルで正確に保持されることを確認する必要があります。画像、グラフ、図形、データの書式設定、フォント、属性、色、ページ設定、テキストの向き、枠線、グラフなどが正確かつ精密にレンダリングされなければなりません。[Aspose.Cells for Python via .NET](https://products.aspose.com/cells/python-net/) は、高度な適合変換を保証します。

このドキュメントは、画像、グラフ、書式などを含むMicrosoft Excel文書をPDFに変換する方法について包括的な理解を提供するように設計されています。そのために、Visual Studio.Netの簡単なコンソールアプリケーションを作成し、Aspose.Cells for Python via .NET APIを使用してExcelファイルをPDFに変換します。変換は高度な精度と正確さで行われます。

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

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-ConvertXlsxFileToPdf.py" >}}

{{% alert color="primary" %}}

スプレッドシートに数式が含まれている場合、スプレッドシートをPDFにレンダリングする直前に、[Workbook.calculate_formula](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/#) メソッドを呼び出すことが最適です。これにより、数式に依存する値が再計算され、正しい値がPDFにレンダリングされます。

{{% /alert %}}

### **結果**

上記のコードを実行すると、アプリケーションディレクトリのFilesフォルダにPDFファイルが作成されます。
以下のスクリーンショットは、PDFページを示しています。ヘッダーとフッターも出力されたPDFファイルに保持されていることに注意してください。

|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted1.png)|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted2.png)|
| :- | :- |
|最初のワークシート**(売上予測)**|2番目のワークシート**(売上報告)**|
|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted3.png)|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted4.png)|
|3番目のワークシート**(データ入力)**|最後のワークシート**(画像)**|
{{< app/cells/assistant language="python-net" >}}
