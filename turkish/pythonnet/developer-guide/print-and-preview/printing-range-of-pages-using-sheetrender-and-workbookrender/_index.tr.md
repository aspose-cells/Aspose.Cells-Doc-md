---
title: SayfaRender ve WorkbookRender kullanarak Sayfa Aralığını Yazdırma
type: docs
weight: 250
url: /tr/python-net/printing-range-of-pages-using-sheetrender-and-workbookrender/
---

{{% alert color="primary" %}} 

Microsoft Excel, çalışma kitabının veya çalışma sayfasının sayfa aralığını yazdırmanıza olanak tanır. Aşağıdaki ekran görüntüsü, sayfa aralığını belirtmek için Microsoft Excel arayüzünü gösterir.

Aspose.Cells for Python via .NET, bu amaçla WorkbookRender.ToPrinter(string PrinterName, int PrintPageIndex, int PrintPageCount) ve SheetRender.ToPrinter(string PrinterName, int PrintPageIndex, int PrintPageCount) metodlarını sağlar.

{{% /alert %}} 

## **Yazdırılacak Sayfaların Aralığını Belirtmek İçin Microsoft Excel Arayüzü**
Aşağıdaki örnek kod, WorkbookRender.ToPrinter(string PrinterName, int PrintPageIndex, int PrintPageCount) ve SheetRender.ToPrinter(string PrinterName, int PrintPageIndex, int PrintPageCount) yöntemlerinin kullanımını açıklar. Bu kod, çalışma kitabının ve çalışma sayfasının 2-5 sayfalarını yazdırır.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PrintAndPreview-PrintingSpecificRangeOfPages.py" >}}
