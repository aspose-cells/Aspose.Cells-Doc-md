---
title: ExcelファイルをHTMLにエクスポートする際にテキストを右から左に展開する
type: docs
weight: 820
url: /ja/java/expanding-text-from-right-to-left-while-exporting-excel-file-to/
---
{{% alert color="primary" %}} 

Aspose.Cells は、Excel ファイルを HTML にエクスポートする際に、右から左へのテキストの展開をサポートするようになりました。この機能は v8.9.0.0 以降に実装されています。ソース Excel ファイルに右から左に展開するテキストが含まれている場合、Aspose.Cells はそれを HTML に正しくエクスポートします。

{{% /alert %}} 
## **ExcelファイルをHTMLにエクスポートする際にテキストを右から左に展開する**
次のサンプル コードは、[サンプルエクセルファイル](5472562.xlsx)このスクリーンショットは、サンプルの Excel が Microsoft Excel 2013 でどのように表示されるかを示しています。

![todo:画像_代替_文章](expanding-text-from-right-to-left-while-exporting-excel-file-to-html_1.png)

このスクリーンショットは、[古いバージョンで生成された出力 HTML](5472570).

![todo:画像_代替_文章](expanding-text-from-right-to-left-while-exporting-excel-file-to-html_2.png)

このスクリーンショットは、[新しいバージョンで生成された出力 HTML](5472563).

![todo:画像_代替_文章](expanding-text-from-right-to-left-while-exporting-excel-file-to-html_3.png)

スクリーンショットでわかるように、新しいバージョンでは、右揃えのテキストが Microsoft Excel のように正しく左に展開されます。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-files-utility-ExpandTextFromRightToLeftWhileExportingExcelFileToHTML-.java" >}}
