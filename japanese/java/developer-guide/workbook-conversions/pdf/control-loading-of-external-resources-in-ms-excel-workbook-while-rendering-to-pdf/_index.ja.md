---
title: PDFにレンダリングする際のMS Excelワークブックの外部リソースの読み込みを制御する
type: docs
weight: 40
url: /ja/java/control-loading-of-external-resources-in-ms-excel-workbook-while-rendering-to-pdf/
---

## **可能な使用シナリオ**

Excelファイルには、リンクされた画像やオブジェクトなどの外部リソースが含まれている場合があります。ExcelファイルをPDFに変換すると、Aspose.Cellsはこれらの外部リソースを取得し、PDFにレンダリングします。ただし、これらの外部リソースを読み込みたくないことがあるかもしれません。さらに、それらを操作したいとも思うかもしれません。これは [**PdfSaveOptions.StreamProvider**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#StreamProvider) を使用して実現できます。これは [**IStreamProvider**](https://reference.aspose.com/cells/java/com.aspose.cells/IStreamProvider) インターフェースを実装しています。

## **PDFに変換する際のMS Excelブックの外部リソースの読み込みを制御する**

以下のサンプルコードは、外部リソースの読み込みを制御し、それらを操作するために[**PdfSaveOptions.StreamProvider**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#StreamProvider)をどのように使用するかを説明しています。コード内で使用される[sample Excel file](50528353.xlsx)およびコードによって生成された[output PDF](50528354.pdf)を確認してください。[screenshot](50528357.png)では、サンプルのExcelファイル内の[old external image](50528356.png)が出力されたPDF内の[new image](50528355.png)に置き換えられた様子が示されています。

![todo:image_alt_text](control-loading-of-external-resources-in-ms-excel-workbook-while-rendering-to-pdf_1.png)

## **サンプルコード**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Rendering-ControlLoadingOfExternalResourcesInExcelToPDF.java" >}}
{{< app/cells/assistant language="java" >}}
