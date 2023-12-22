---
title: Excel Çalışma Sayfası Başına Bir PDF Sayfa Oluşturma - Excel'den PDF'e Dönüştürme
type: docs
weight: 100
url: /tr/python-net/render-one-pdf-page-per-excel-worksheet-excel-to-pdf-conversion/
description: Excel'i Aspose.Cells for Python via .NET API ile PDF'e dönüştürürken Excel Çalışma Sayfası Başına Bir PDF Sayfa İşlemeyi öğrenin.
keywords: Python Render One PDF Page Per Excel Worksheet while saving file to PDF, One PDF Page Per Excel Worksheet while saving Excel to PDF using Python, Python show one page per worksheet when converting Excel to PDF
---
{{% alert color="primary" %}} 

Büyük Microsoft Excel dosyalarıyla çalışırken (örneğin, her biri 50 sütun ve 300 veya daha fazla veri satırı içeren çok sayıda sayfa içeren bir çalışma kitabı), çalışma sayfasının boyutundan bağımsız olarak PDF çıktısının çalışma sayfası başına bir sayfa göstermesini isteyebilirsiniz. . Bu, her sayfanın muhtemelen tamamen farklı bir sayfa boyutuna sahip olacağı anlamına gelir. Bu, Aspose.Cells for Python via .NET API kullanılarak gerçekleştirilebilir.

{{% /alert %}} 

Lütfen birden çok çalışma sayfası içeren bir Excel dosyasını PDF'e dönüştüren aşağıdaki örnek koda bakın.



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-RenderOnePdfPagePerExcelWorksheet-1.py" >}}

{{% alert color="primary" %}} 

 Eğer[PdfSaveOptions.one_page_per_sheet](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/one_page_per_sheet/)seçeneği *true** olarak ayarlandığında, tüm sayfa içeriği tek bir PDF sayfasına dönüştürülecektir.

{{% /alert %}} {{% alert color="primary" %}} 

 E-tablonuz formüller içeriyorsa, aramak en iyisidir.[Workbook.calculate_formula](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/#) Bu yöntem, elektronik tabloyu PDF'e dönüştürmeden hemen önce kullanılır. Bu, formüle bağlı değerlerin yeniden hesaplanmasını ve PDF'de doğru değerlerin oluşturulmasını sağlar.

{{% /alert %}}
