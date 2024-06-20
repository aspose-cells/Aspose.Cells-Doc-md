---
title: Tüm Çalışsayfa Sütunlarını Tek PDF Sayfasına Sığdır
type: docs
weight: 160
url: /tr/python-net/fit-all-worksheet-columns-on-single-pdf-page/
description: Aspose.Cells for Python via .NET API ile Tüm Çalışma Sayfası Sütunlarını Tek PDF Sayfasına Sığdırmayı Öğrenin.
keywords: Python ile Tüm Çalışma Sayfası Sütunlarını Tek PDF Sayfasına Sığdır, Python kullanarak Çalışma Sayfası Sütunlarını Tek PDF Sayfasına Sığdır, Python ile Tüm Çalışma Sütunlarını Tek PDF Sayfasına Kaydet, Python da Tüm Sütunları Tek PDF Sayfasına Kaydet
---

{{% alert color="primary" %}}

Bazı durumlarda, bir çalışsayfanın tüm sütunlarını tek bir sayfaya sığdıran bir PDF dosyası oluşturmak isteyebilirsiniz. [**PdfSaveOptions.all_columns_in_one_page_per_sheet**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/all_columns_in_one_page_per_sheet/) özelliği bu özelliği çok kullanışlı bir şekilde sağlar. Çıktı PDF'in yükseklik ve genişliği gibi karmaşık hesaplamalar dahili olarak işlenir ve çalışsayfadaki verilere göre belirlenir.

{{% /alert %}}

## **Tüm Çalışsayfa Sütunlarını Tek PDF Sayfasına Sığdır**

[**PdfSaveOptions.all_columns_in_one_page_per_sheet**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/all_columns_in_one_page_per_sheet/), bir çalışsayfadaki tüm sütunların tek bir PDF sayfasına render edilmesini sağlar, ancak satırlar çalışsayfadaki verilere bağlı olarak birden fazla sayfaya genişleyebilir.

Aşağıdaki örnek kod, 100 sütunu olan büyük bir çalışsayfayı render etmek için [**PdfSaveOptions.all_columns_in_one_page_per_sheet**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/all_columns_in_one_page_per_sheet/) özelliğini nasıl kullanacağını göstermektedir.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-FitAllWorksheetColumns-1.py" >}}

{{% alert color="primary" %}}

Verilen bir çalışsayfada çok sayıda sütun bulunduğunda, render edilen PDF dosyası içeriği çok küçük bir boyutta görülebilir. Acrobat Reader gibi bir görüntüleme uygulamasında büyütüldüğünde hala okunabilir.

{{% /alert %}} {{% alert color="primary" %}}

Eğer elektronik tablonuz formüller içeriyorsa, elektronik tabloyu PDF formatına dönüştürmeden önce [Workbook.calculate_formula](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/#) yöntemini çağırmanız en iyisidir. Böyle yapmak, formül bağımlı değerlerin yeniden hesaplanmasını sağlayacak ve doğru değerler PDF olarak oluşturulacaktır.

{{% /alert %}}
