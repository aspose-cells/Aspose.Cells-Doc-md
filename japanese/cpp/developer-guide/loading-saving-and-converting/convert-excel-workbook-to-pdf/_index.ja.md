---
title: ExcelワークブックをPDFに変換する
type: docs
weight: 80
url: /ja/cpp/convert-excel-workbook-to-pdf/
---

## **ExcelワークブックをPDFに変換する**
PDFファイルは、組織、政府部門、個人間で文書を交換するために広く使用されています。これは標準のドキュメント形式であり、ソフトウェア開発者はしばしばMicrosoft ExcelファイルをPDFドキュメントに変換する方法を見つけるよう求められます。

Aspose.Cellsは、ExcelファイルをPDFに変換する機能をサポートし、変換時に高い視覚的忠実度を維持します。

{{% alert color="primary" %}} 

Aspose.Cellsは、出力ドキュメントにAPIとバージョン番号の情報を直接書き込みます。例えば、ドキュメントをPDFにレンダリングすると、Aspose.Cells for C++が**アプリケーション**フィールドに'Aspose.Cells'と入力し、**PDFプロデューサー**フィールドに'value'、例：'Aspose.Cells v18.5.0'を入力します。

{{% /alert %}} 
### **直接変換**
Aspose.Cellsは、他のソフトウェアに依存せずにスプレッドシートからPDFへの変換をサポートしています。[Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)クラスの[Save](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/)メソッドを使用して、Excelファイルを単独でPDFに保存できます。[SaveFormat_Pdf](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/)列挙メンバーを使用して、ネイティブExcelファイルをPDF形式に変換します。

以下の手順に従って、Excelスプレッドシートを直接PDF形式に変換します:

1. 空のコンストラクタを呼び出して[Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)クラスのオブジェクトをインスタンス化します。
1. 既存のテンプレートファイルを開いたり読み込んだりするか、ワークブックをゼロから作成している場合は、この手順をスキップします。
1. Aspose.CellsのAPIを使用して、スプレッドシート上で作業を行います（入力データ、書式設定の適用、数式の設定、画像の挿入など）。
1. スプレッドシートのコードが完成したら、[Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)クラスの[Save](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/)メソッドを呼び出してスプレッドシートを保存してください。

ファイル形式はPDFである必要があるため、最終的なPDFドキュメントを生成するために[SaveFormat](https://reference.aspose.com/cells/cpp/aspose.cells/savedirs/saveformat/)列挙型から関連するPDF（事前定義された値）を選択してください。

次のサンプルコードと、参照用の[サンプルExcelファイル](67338368.xlsx)および[出力PDFファイル](67338369.pdf)をご覧ください。

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "LoadingSavingAndConverting-ConvertExcelWorkbookToPDF_DirectConversion-new.cpp" >}}
### **高度な変換**
変換の異なる属性を設定するために[PdfSaveOptions](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/)クラスを使用することもできます。**PdfSaveOptions**クラスの異なるプロパティを設定すると、出力PDFの印刷、フォント、セキュリティ、および圧縮設定を制御できます。 最も重要なプロパティは[SetCompliance](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/setcompliance/)であり、ExcelファイルをPDF/A準拠のPDFファイルとして保存できます。
#### **PDF/A準拠ファイルへのワークブックの保存**
次のコードスニペットは、**PdfSaveOptions**クラスを使用してExcelファイルをPDF/A準拠のPDF形式で保存する方法を示しています。

次のサンプルコードと、参照用の[出力PDF](67338370.pdf)をご覧ください。

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "LoadingSavingAndConverting-ConvertExcelWorkbookToPDF_A_CompliedFiles-new.cpp" >}}
#### **PDF作成時間の設定**
**IPdfSaveOptions**クラスを使用すると、PDFの作成時間を取得または設定できます。

次のサンプルコードと、参照用の[出力PDF](67338371.pdf)をご覧ください。

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "LoadingSavingAndConverting-ConvertExcelWorkbookToPDF_SetPDFCreationTime-new.cpp" >}}
