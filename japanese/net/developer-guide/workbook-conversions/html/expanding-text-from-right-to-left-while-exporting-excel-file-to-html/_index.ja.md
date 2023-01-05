---
title: ExcelファイルをHTMLにエクスポートする際にテキストを右から左に展開する
type: docs
weight: 60
url: /ja/net/expanding-text-from-right-to-left-while-exporting-excel-file-to/
---
{{% alert color="primary" %}} 

Aspose.Cells は、Excel ファイルを HTML にエクスポートする際に、右から左へのテキストの展開をサポートするようになりました。この機能は v8.9.0.0 以降に実装されています。ソース Excel ファイルに右から左に展開するテキストが含まれている場合、Aspose.Cells はそれを HTML に正しくエクスポートします。

{{% /alert %}} 
## **ExcelファイルをHTMLにエクスポートする際にテキストを右から左に展開する**
次のサンプル コードは、[サンプルエクセルファイル](5115502.xlsx)このスクリーンショットは、サンプルの Excel が Microsoft Excel 2013 でどのように表示されるかを示しています。

![todo:画像_代替_文章](expanding-text-from-right-to-left-while-exporting-excel-file-to-html_1.png)

このスクリーンショットは、[古いバージョンで生成された出力 HTML](5115509).

![todo:画像_代替_文章](expanding-text-from-right-to-left-while-exporting-excel-file-to-html_2.png)

このスクリーンショットは、[新しいバージョンで生成された出力 HTML](5115508).

![todo:画像_代替_文章](expanding-text-from-right-to-left-while-exporting-excel-file-to-html_3.png)

スクリーンショットでわかるように、新しいバージョンでは、右揃えのテキストが Microsoft Excel のように正しく左に展開されます。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithHTMLFormat-ExpandTextFromRightToLeft-1.cs" >}}
