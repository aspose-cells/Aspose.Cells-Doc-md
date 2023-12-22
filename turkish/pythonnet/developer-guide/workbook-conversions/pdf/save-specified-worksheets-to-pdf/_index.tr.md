---
title: Belirtilen Çalışma Sayfalarını PDF'e Kaydet
type: docs
weight: 140
url: /tr/python-net/save-specified-worksheets-to-pdf/
description: Belirtilen Çalışma Sayfalarını Aspose.Cells for Python via .NET API ile PDF'e nasıl kaydedeceğinizi öğrenin.
keywords: Python Save Active Worksheet to PDF, Save All Worksheets to PDF, Save Specified Worksheets to PDF
---
 Varsayılan olarak Aspose.Cells for Python via .NET tümünü kaydet**görünür** Çalışma kitabındaki çalışma sayfalarını pdf dosyasına dönüştürme. İle**[`PdfSaveOptions.sheet_set`](https://reference.aspose.com/cells/python-net/aspose.cells/paginatedsaveoptions/sheet_set/)** seçeneğiyle belirtilen çalışma sayfalarını pdf dosyasına kaydedebilirsiniz. örneğin aktif çalışma sayfasını pdf'e kaydedebilir, tüm çalışma sayfalarını (hem görünür hem de gizli çalışma sayfaları) pdf'e kaydedebilir, özel çoklu çalışma sayfalarını pdf'e kaydedebilirsiniz.

##  **Aktif Çalışma Sayfasını PDF'e kaydet**

Yalnızca etkin sayfayı pdf'ye aktarmak istiyorsanız, bunu geçerek başarabilirsiniz.**[`SheetSet.active`](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetset/active/)** ile**[`PdfSaveOptions.sheet_set`](https://reference.aspose.com/cells/python-net/aspose.cells/paginatedsaveoptions/sheet_set/)** seçenek.

 `Sheet2` numaralı sayfa kaynak dosyanın aktif sayfasıdır[sayfa seti örneği.xlsx](sheetset-example.xlsx).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-ActiveSheetToPdf.py" >}}

##  **Tüm Çalışma Sayfalarını PDF'e Kaydet**

**[`SheetSet.visible`](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetset/visible/)** çalışma kitabındaki görünür sayfaları gösterir ve**[`SheetSet.all`](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetset/all/)** çalışma kitabındaki hem görünür sayfalar hem de gizli/görünmez sayfalar dahil tüm sayfaları belirtir. Tüm sayfaları pdf'e aktarmak istiyorsanız,**[`SheetSet.all`](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetset/all/)** ile**[`PdfSaveOptions.sheet_set`](https://reference.aspose.com/cells/python-net/aspose.cells/paginatedsaveoptions/sheet_set/)** seçenek.

 Kaynak dosyası[sayfa seti örneği.xlsx](sheetset-example.xlsx) gizli sayfa `Sheet3` ile dört sayfanın tümünü içerir.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-AllSheetsToPdf.py" >}}

##  **Belirtilen Çalışma Sayfalarını PDF'e Kaydet**
 İstenilen/özel birden çok sayfayı pdf'e aktarmak istiyorsanız, bunu birden çok sayfa dizinini ileterek başarabilirsiniz.**[`PdfSaveOptions.sheet_set`](https://reference.aspose.com/cells/python-net/aspose.cells/paginatedsaveoptions/sheet_set/)** seçenek.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-MultiSheetsToPdf.py" >}}

{{% alert color="primary" %}} 

 E-tablonuz formüller içeriyorsa, aramak en iyisidir.[**Workbook.calculate_formula()**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/#) e-tabloyu PDF biçimine dönüştürmeden hemen önce. Bunu yapmak, formüle bağlı değerlerin yeniden hesaplanmasını ve PDF'de doğru değerlerin oluşturulmasını sağlayacaktır.

{{% /alert %}}
