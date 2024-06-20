---
title: SheetRenderとWorkbookRenderを使用してページの印刷範囲を印刷する
type: docs
weight: 250
url: /ja/net/printing-range-of-pages-using-sheetrender-and-workbookrender/
---

{{% alert color="primary" %}} 

Microsoft Excelでは、ブックまたはワークシートのページの範囲を印刷できます。次のスクリーンショットは、ページの範囲を指定するMicrosoft Excelのインターフェースを示しています。

Aspose.Cellsでは、この目的のためにWorkbookRender.ToPrinter(string PrinterName, int PrintPageIndex, int PrintPageCount)およびSheetRender.ToPrinter(string PrinterName, int PrintPageIndex, int PrintPageCount)メソッドを提供しています。

{{% /alert %}} 
## **Microsoft Excelのページ範囲を指定するインターフェース**
次のサンプルコードは、WorkbookRender.ToPrinter(string PrinterName, int PrintPageIndex, int PrintPageCount)およびSheetRender.ToPrinter(string PrinterName, int PrintPageIndex, int PrintPageCount)メソッドの使用法を示しています。このコードは、ブックおよびワークシートのページ2から5を印刷します。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderingAndPrinting-PrintingRangeOfPages-PrintingSpecificRangeOfPages.cs" >}}
