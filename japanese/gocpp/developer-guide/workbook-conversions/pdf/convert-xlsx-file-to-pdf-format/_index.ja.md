---
title: XLSXファイルをGolangを使ってC++でPDF形式に変換する
linktitle: XLSX ファイルを PDF フォーマットに変換する
type: docs
weight: 30
url: /ja/go-cpp/convert-xlsx-file-to-pdf-format/
description: Aspose.Cells for C++を使用してExcelファイルを高精度・高忠実度でPDFに変換する方法を学ぶ。
---

{{% alert color="primary" %}}

PDF（ポータブルドキュメントフォーマット）は、作成に使用されたソフトウェア、ハードウェア、オペレーティングシステムとは関係なくドキュメントを表します。PDFファイルは、テキスト、グラフィックス、画像の任意の組み合わせをデバイス非依存かつ解像度非依存の方式で含むことができます。PDFファイルは圧縮されていることが多く、元のファイルより容量が小さくなります。

Microsoft ExcelファイルをPDFに変換する必要がある場合、迅速、安全、正確で信頼性の高いソリューションが必要です。これにより、世界中にPDFドキュメントを配布できます。多くの変換ツールがこれを行うことができますが、元のExcelドキュメントのレイアウトが出力されたPDFに保持されることを確認してください。画像、チャート、シェイプ、データの書式設定、フォント、属性、色、ページ設定、テキストの向き、ボーダー、チャートなどが正確にレンダリングされる必要があります。[Aspose.Cells](https://products.aspose.com/cells/go-cpp/)は高精度の変換を保証します。

このドキュメントは、画像、チャート、書式設定などを含むMicrosoft ExcelドキュメントのPDFへの変換方法について包括的に理解できるように設計されています。そのために、C++でExcelファイルをPDFに変換するシンプルなコンソールアプリケーションの作成方法を示しています。高精度、高忠実度の変換を行います。

{{% /alert %}}

## **ExcelをPDFに変換する**

この例では、テンプレートとしてExcelファイル（SampleInput.xlsx）を使用しています。ワークブックにはチャートと画像が含まれたシートがあります。各シートにはフォント、属性、色、シェーディング効果、境界線を使用したさまざまな書式があります。最初のシートには縦列チャート、最後には画像があります。

### **テンプレートの Excel ファイル**

テンプレートファイルには、チャートと画像を含む3つのシートがあります。最初のシートはチャートを持ち、最後のシートには画像があります。スクリーンショットは以下の通りです。

|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Sheet1.png)|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Sheet2.png)|
| :- | :- |
|最初のワークシート**(売上予測)**|2番目のワークシート**(売上報告)**|
|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Sheet3.png)|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Sheet4.png)|
|3番目のワークシート**(データ入力)**|最後のワークシート**(画像)**|

### **変換プロセス**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ConvertXlsxFileToPdfFormat.go" >}}
{{% alert color="primary" %}}

スプレッドシートに数式が含まれている場合は、[Workbook.CalculateFormula](https://reference.aspose.com/cells/go-cpp/workbook/calculateformula/)メソッドを呼び出してからスプレッドシートをPDFにレンダリングするのが最適です。これにより、数式に依存する値が再計算され、正しい値がPDFに表示されます。

{{% /alert %}}

### **結果**

上記のコードを実行すると、アプリケーションディレクトリのFilesフォルダにPDFファイルが作成されます。
以下のスクリーンショットは、PDFページを示しています。ヘッダーとフッターも出力されたPDFファイルに保持されていることに注意してください。

|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted1.png)|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted2.png)|
| :- | :- |
|最初のワークシート**(売上予測)**|2番目のワークシート**(売上報告)**|
|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted3.png)|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted4.png)|
|3番目のワークシート**(データ入力)**|最後のワークシート**(画像)**|
