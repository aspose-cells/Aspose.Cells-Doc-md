---
title: PDF へのレンダリング中に、MS Excel ワークブックの外部リソースの読み込みを制御する
type: docs
weight: 40
url: /ja/net/control-loading-of-external-resources-in-ms-excel-workbook-while-rendering-to-pdf/
---
## **考えられる使用シナリオ**

Excel ファイルには、リンクされた画像やオブジェクトなどの外部リソースが含まれている場合があります。 Excel ファイルを PDF に変換すると、Aspose.Cells はこれらの外部リソースを取得し、PDF にレンダリングします。しかし、これらの外部リソースをロードしたくない場合や、それ以上にそれらを操作したい場合があります。これを使用して行うことができます[**WorkbookSettings.StreamProvider**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/streamprovider)を実装する[**IStreamProvider**](https://reference.aspose.com/cells/net/aspose.cells/istreamprovider)インターフェース。

## **PDF へのレンダリング中に、MS Excel ワークブックの外部リソースの読み込みを制御する**

次のサンプル コードは、[**WorkbookSettings.StreamProvider**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/streamprovider)外部リソースのロードを制御し、それらを操作します。を確認してください[サンプル Excel ファイル](50528322.xlsx)コード内で使用され、[PDF出力](50528325.pdf)コードによって生成されます。の[スクリーンショット](50528326.png)方法を示します[古い外観イメージ](50528324.png)サンプル Excel ファイルの[新しいイメージ](50528323.png)出力PDFで。

![todo:画像_代替_文章](control-loading-of-external-resources-in-ms-excel-workbook-while-rendering-to-pdf_1.png)

## **サンプルコード**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Rendering-ControlLoadingOfExternalResourcesInExcelToPDF-1.cs" >}}
