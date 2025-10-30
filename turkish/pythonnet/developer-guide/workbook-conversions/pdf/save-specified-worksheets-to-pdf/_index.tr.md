---
title: Belirtilen Çalışma Sayfalarını PDF Olarak Kaydet
type: docs
weight: 140
url: /tr/python-net/save-specified-worksheets-to-pdf/
description: Aspose.Cells for Python via .NET API sı ile Belirtilen Çalışma Sayfalarını PDF Olarak Kaydetmeyi Öğrenin.
keywords: Python ile Aktif Çalışma Sayfasını PDF Olarak Kaydetme, Tüm Çalışma Sayfalarını PDF Olarak Kaydetme, Belirtilen Çalışma Sayfalarını PDF Olarak Kaydetme
---

Aspose.Cells for Python via .NET varsayılan olarak bir elektronik tablodaki tüm **görünen** çalışma sayfalarını pdf dosyasına kaydeder. [**PdfSaveOptions.sheet_set**](https://reference.aspose.com/cells/python-net/aspose.cells/paginatedsaveoptions/sheet_set/) seçeneği ile belirtilen çalışma sayfalarını pdf dosyasına kaydedebilirsiniz. Örn. aktif çalışma sayfasını pdf olarak kaydedebilir, tüm çalışma sayfalarını (hem görünen hem gizli çalışma sayfalarını) pdf olarak kaydedebilir, özel çoklu çalışma sayfalarını pdf olarak kaydedebilirsiniz.

## **Etkin Çalışma Sayfasını PDF Olarak Kaydet**

Sadece etkin çalışma sayfasını PDF'ye dışa aktarmak istiyorsanız, bunu [**SheetSet.active**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetset/active/) seçeneğine [**PdfSaveOptions.sheet_set**](https://reference.aspose.com/cells/python-net/aspose.cells/paginatedsaveoptions/sheet_set/) seçeneği ile geçerek başarabilirsiniz.

Sheet2 sayfası kaynak dosyanın [sheetset-example.xlsx](sheetset-example.xlsx) dosyasında etkin sayfadır.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-ActiveSheetToPdf.py" >}}

## **Tüm Çalışma Sayfalarını PDF Olarak Kaydet**

[**SheetSet.visible**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetset/visible/), çalışma kitabındaki görünür sayfaları gösterir ve [**SheetSet.all**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetset/all/) görünür sayfaları ve gizli/görünmez sayfaları içeren tüm sayfaları gösterir. Tüm sayfaları PDF olarak dışa aktarmak istiyorsanız, sadece [**SheetSet.all**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetset/all/) seçeneğini [**PdfSaveOptions.sheet_set**](https://reference.aspose.com/cells/python-net/aspose.cells/paginatedsaveoptions/sheet_set/) seçeneğine geçebilirsiniz.

Kaynak dosya [sheetset-example.xlsx](sheetset-example.xlsx) gizli Sheet3 sayfası dahil olmak üzere dört sayfayı içerir.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-AllSheetsToPdf.py" >}}

## **Belirtilen Çalışsayfalarını PDF olarak kaydet**
İstenen/özel birden fazla çalışma sayfasını PDF olarak dışa aktarmak istiyorsanız, [**PdfSaveOptions.sheet_set**](https://reference.aspose.com/cells/python-net/aspose.cells/paginatedsaveoptions/sheet_set/) seçeneğine birden fazla sayfa indeksini geçerek bunu başarabilirsiniz.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-MultiSheetsToPdf.py" >}}

{{% alert color="primary" %}} 

Eğer elektronik tablonuz formüller içeriyorsa, PDF formatına dönüştürmeden hemen önce [**Workbook.calculate_formula()**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/#) çağrısını yapmanız en iyisidir. Böyle yaparak formüle bağımlı değerler yeniden hesaplanacak ve doğru değerler PDF'de gösterilecektir.

{{% /alert %}}
{{< app/cells/assistant language="python-net" >}}
