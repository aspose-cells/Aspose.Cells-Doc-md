---
title: Excel ファイルを HTML にエクスポートする際にテキストを右から左に展開
type: docs
weight: 60
url: /ja/python-net/expanding-text-from-right-to-left-while-exporting-excel-file-to/
---

{{% alert color="primary" %}} 

Aspose.Cells for Python via .NETは、ExcelファイルをHTMLにエクスポートする際に、右から左へのテキスト展開をサポートします。この機能はバージョン8.9.0.0から実装されています。ソースのExcelファイルに右から左に展開されるテキストが含まれている場合、Aspose.Cellsはそれを正しくHTMLにエクスポートします。

{{% /alert %}} 

## **Excel ファイルを HTML にエクスポートする際にテキストを右から左に展開**
[サンプルexcelファイル](5115502.xlsx)をHTMLに変換するサンプルコードは次のとおりです。このスクリーンショットは、サンプルExcelがMicrosoft Excel 2013でどのように表示されるかを示しています。

![todo:image_alt_text](expanding-text-from-right-to-left-while-exporting-excel-file-to-html_1.png)

このスクリーンショットは、古いバージョンで生成された[output HTML](5115509)を示しています。

![todo:image_alt_text](expanding-text-from-right-to-left-while-exporting-excel-file-to-html_2.png)

このスクリーンショットは、新しいバージョンで生成された[output HTML](5115508)を示しています。

![todo:image_alt_text](expanding-text-from-right-to-left-while-exporting-excel-file-to-html_3.png)

スクリーンショットに示されるように、新しいバージョンでは右寄せされたテキストを Microsoft Excel と同様に適切に左に展開します。



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "HTML-ExpandTextFromRightToLeft-1.py" >}}
