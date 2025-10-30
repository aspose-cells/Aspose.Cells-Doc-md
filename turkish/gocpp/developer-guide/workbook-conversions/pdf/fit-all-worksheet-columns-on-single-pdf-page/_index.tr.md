---
title: Golang ile C++ kullanarak Tüm Sayfa Yaprağı Sütunlarını Tek PDF Sayfasında Sığdır
linktitle: Tüm Çalışsayfa Sütunlarını Tek PDF Sayfasına Sığdır
type: docs
weight: 160
url: /tr/go-cpp/fit-all-worksheet-columns-on-single-pdf-page/
description: Aspose.Cells ile Golang kullanarak tüm çalışma sayfası sütunlarını tek sayfaya sığdıran bir PDF oluşturun.
---

{{% alert color="primary" %}}

 Bazen, tüm çalışma sayfası sütunlarını tek bir sayfaya sığdıran bir PDF dosyası üretmek istersiniz. [**PdfSaveOptions.PaginatedSaveOptions(PaginatedSaveOptions_Impl* impl)**](https://reference.aspose.com/cells/go-cpp/paginatedsaveoptions/~paginatedsaveoptions/) özelliği bu özelliği son derece kullanışlı hale getirir. Çıktı PDF'sinin yüksekliği ve genişliği gibi karmaşık hesaplamalar iç tarafından yönetilir ve çalışma sayfasındaki verilere göre belirlenir.

{{% /alert %}}

## **Tüm Çalışsayfa Sütunlarını Tek PDF Sayfasına Sığdır**

 [**PdfSaveOptions.PaginatedSaveOptions(PaginatedSaveOptions_Impl* impl)**](https://reference.aspose.com/cells/go-cpp/paginatedsaveoptions/~paginatedsaveoptions/) tüm çalışma sayfasındaki tüm sütunların tek PDF sayfasına render edilmesini sağlar, satırlar ise çalışma sayfasındaki verilere bağlı olarak birkaç sayfaya genişleyebilir.

 Aşağıdaki örnek kod, [**PdfSaveOptions.PaginatedSaveOptions(PaginatedSaveOptions_Impl* impl)**](https://reference.aspose.com/cells/go-cpp/paginatedsaveoptions/~paginatedsaveoptions/) özelliğini kullanarak büyük bir 100 sütunlu çalışma sayfasını nasıl render edeceğinizi gösterir.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FitAllWorksheetColumnsOnSinglePdfPage.go" >}}
{{% alert color="primary" %}}

Verilen bir çalışsayfada çok sayıda sütun bulunduğunda, render edilen PDF dosyası içeriği çok küçük bir boyutta görülebilir. Acrobat Reader gibi bir görüntüleme uygulamasında büyütüldüğünde hala okunabilir.

{{% /alert %}} {{% alert color="primary" %}}

Eğer elektronik tablonuz formüller içeriyorsa, PDF formatına dönüştürmeden hemen önce [**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/go-cpp/workbook/calculateformula/) çağrısını yapmanız en iyisidir. Böyle yaparak formüle bağımlı değerler yeniden hesaplanacak ve doğru değerler PDF'de gösterilecektir.

{{% /alert %}}
