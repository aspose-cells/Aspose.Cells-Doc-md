---
title: SheetRender と WorkbookRender を使用したページ範囲の印刷
type: docs
weight: 250
url: /ja/net/printing-range-of-pages-using-sheetrender-and-workbookrender/
---
{{% alert color="primary" %}} 

Microsoft Excel では、ワークブックまたはワークシートのページ範囲を印刷できます。次のスクリーンショットは、ページの範囲を指定するための Microsoft Excel インターフェイスを示しています。

Aspose.Cells は、この目的のために WorkbookRender.ToPrinter(string PrinterName, int PrintPageIndex, int PrintPageCount) および SheetRender.ToPrinter(string PrinterName, int PrintPageIndex, int PrintPageCount) メソッドを提供します。

{{% /alert %}} 
## **Microsoft 印刷するページ範囲を指定するための Excel インターフェイス**
次のサンプル コードは、WorkbookRender.ToPrinter(string PrinterName, int PrintPageIndex, int PrintPageCount) および SheetRender.ToPrinter(string PrinterName, int PrintPageIndex, int PrintPageCount) メソッドの使用方法を示しています。ワークブックとワークシートの 2 ～ 5 ページを印刷します。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderingAndPrinting-PrintingRangeOfPages-PrintingSpecificRangeOfPages.cs" >}}
