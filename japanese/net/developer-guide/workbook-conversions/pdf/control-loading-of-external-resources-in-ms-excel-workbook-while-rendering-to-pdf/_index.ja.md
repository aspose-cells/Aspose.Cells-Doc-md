---
title: PDFにレンダリングする際のMS Excelワークブックの外部リソースの読み込みを制御する
type: docs
weight: 40
url: /ja/net/control-loading-of-external-resources-in-ms-excel-workbook-while-rendering-to-pdf/
---

## **可能な使用シナリオ**

Excel ファイルには、リンクされた画像やオブジェクトなどの外部リソースが含まれている場合があります。Excel ファイルを PDF に変換すると、Aspose.Cells はこれらの外部リソースを取得してそれらを PDF にレンダリングします。しかし、時々これらの外部リソースをロードしたくないだけでなく、操作したい場合があります。これは、[**WorkbookSettings.StreamProvider**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/streamprovider) で実装された [**IStreamProvider**](https://reference.aspose.com/cells/net/aspose.cells/istreamprovider) インターフェースを使用することで可能です。

## **PDFに変換する際のMS Excelブックの外部リソースの読み込みを制御する**

次のサンプルコードでは、[**WorkbookSettings.StreamProvider**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/streamprovider) を使用して外部リソースの読み込みを制御し、それらを操作する方法について説明しています。コード内で使用される [サンプル Excel ファイル](50528322.xlsx) とコードによって生成された [出力 PDF](50528325.pdf) 、[スクリーンショット](50528326.png)をご確認ください。[サンプル Excel ファイル](50528324.png) の [古い外部イメージ](50528324.png) が [新しいイメージ](50528323.png) に置換された様子が示されています。

![todo:image_alt_text](control-loading-of-external-resources-in-ms-excel-workbook-while-rendering-to-pdf_1.png)

## **サンプルコード**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Rendering-ControlLoadingOfExternalResourcesInExcelToPDF-1.cs" >}}
