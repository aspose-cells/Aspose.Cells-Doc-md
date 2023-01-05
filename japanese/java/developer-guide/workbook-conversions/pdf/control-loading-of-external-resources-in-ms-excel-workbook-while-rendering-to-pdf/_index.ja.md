---
title: PDF へのレンダリング中に、MS Excel ワークブックの外部リソースの読み込みを制御します
type: docs
weight: 40
url: /ja/java/control-loading-of-external-resources-in-ms-excel-workbook-while-rendering-to-pdf/
---
## **考えられる使用シナリオ**

Excel ファイルには、リンクされた画像やオブジェクトなどの外部リソースが含まれている場合があります。 Excel ファイルを PDF に変換すると、Aspose.Cells はこれらの外部リソースを取得し、それらを PDF にレンダリングします。これを使用して行うことができます[**PdfSaveOptions.StreamProvider**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#StreamProvider)を実装する[**IStreamProvider**](https://reference.aspose.com/cells/java/com.aspose.cells/IStreamProvider)インターフェース。

## **PDF へのレンダリング中に、MS Excel ワークブックの外部リソースの読み込みを制御します**

次のサンプル コードは、[**PdfSaveOptions.StreamProvider**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#StreamProvider)外部リソースのロードを制御し、それらを操作します。を確認してください[サンプル Excel ファイル](50528353.xlsx)コード内で使用され、[出力 PDF](50528354.pdf)コードによって生成されます。の[スクリーンショット](50528357.png)方法を示します[古い外観イメージ](50528356.png)サンプル Excel ファイルの[新しいイメージ](50528355.png)出力 PDF で。

![todo:画像_代替_文章](control-loading-of-external-resources-in-ms-excel-workbook-while-rendering-to-pdf_1.png)

## **サンプルコード**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Rendering-ControlLoadingOfExternalResourcesInExcelToPDF.java" >}}
