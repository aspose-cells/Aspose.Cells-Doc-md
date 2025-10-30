---
title: GolangをC++経由でExcelファイルをHTMLにエクスポートする際に右から左へのテキスト展開
linktitle: Excel ファイルを HTML にエクスポートする際にテキストを右から左に展開
type: docs
weight: 60
url: /ja/go-cpp/expanding-text-from-right-to-left-while-exporting-excel-file-to/
description: Aspose.Cells for C++を使用して、ExcelファイルのHTMLエクスポート時に右から左へのテキスト展開を行う方法を学びます。
---

{{% alert color="primary" %}} 

Aspose.Cells for C++は、ExcelファイルのHTMLエクスポート時に右から左へのテキスト展開をサポートしています。この機能はv8.9.0.0以降に実装されました。ソースExcelファイルに右から左に展開するテキストが含まれている場合、Aspose.Cellsは正しくHTMLにエクスポートします。

{{% /alert %}} 

## **Excel ファイルを HTML にエクスポートする際にテキストを右から左に展開**

次のサンプルコードは [サンプルExcelファイル](5115502.xlsx) をHTMLに変換する例です。このスクリーンショットは、Microsoft Excel 2013でのファイルの見た目を示しています。

![todo:image_alt_text](expanding-text-from-right-to-left-while-exporting-excel-file-to-html_1.png)

このスクリーンショットは [古いバージョンで生成された出力HTML](5115509) を示しています。

![todo:image_alt_text](expanding-text-from-right-to-left-while-exporting-excel-file-to-html_2.png)

このスクリーンショットは [新しいバージョンで生成された出力HTML](5115508) を示しています。

![todo:image_alt_text](expanding-text-from-right-to-left-while-exporting-excel-file-to-html_3.png)

スクリーンショットからわかるように、新しいバージョンはMicrosoft Excelと同様に、右揃えのテキストを左に正しく展開します。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ExpandingTextFromRightToLeftWhileExportingExcelFileToHtml.go" >}}
