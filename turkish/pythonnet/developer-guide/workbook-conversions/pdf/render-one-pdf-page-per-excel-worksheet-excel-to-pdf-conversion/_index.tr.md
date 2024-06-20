---
title: Excel Çalışsayfası Başına Bir PDF Sayfası Oluşturma  Excel den PDF ye Dönüştürme
type: docs
weight: 100
url: /tr/python-net/render-one-pdf-page-per-excel-worksheet-excel-to-pdf-conversion/
description: Aspose.Cells for Python via .NET API ile Excel den PDF ye dönüştürürken her Excel çalışsayfası için bir PDF sayfası render etmeyi öğrenin.
keywords: Python dosyasını PDF olarak kaydederken her Excel çalışsayfası için bir PDF sayfası render etme, Python kullanarak Excel i PDF e dönüştürürken her çalışsayfa için bir PDF sayfası, Excel i PDF e dönüştürürken Python ile birlikte bir sayfa gösterme
---

{{% alert color="primary" %}} 

Büyük Microsoft Excel dosyalarıyla çalışırken (örneğin her biri 50 sütun ve 300 veya daha fazla veri satırı bulunan çok sayıda çalışsayfaya sahip bir çalışma kitabı), PDF çıktısının çalışsayfa başına bir sayfa gösterilmesini isteyebilirsiniz, çalışsayfa boyutundan bağımsız olarak. Bu, her sayfanın büyük olasılıkla radikal farklı bir sayfa boyutuna sahip olması demektir. Bu, Aspose.Cells for Python via .NET API'sini kullanarak elde edilebilir.

{{% /alert %}} 

Lütfen birden çok çalışsayfasına sahip bir Excel dosyasını PDF'ye dönüştüren aşağıdaki örnek kodu inceleyin.



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-RenderOnePdfPagePerExcelWorksheet-1.py" >}}

{{% alert color="primary" %}} 

[PdfSaveOptions.one_page_per_sheet](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/one_page_per_sheet/) seçeneği **true** olarak ayarlanırsa, tüm çalışsayfa içeriği bir PDF sayfasına render edilir.

{{% /alert %}} {{% alert color="primary" %}} 

Eğer elektronik tablonuzda formüller varsa, elektronik tabloyu PDF'ye dönüştürmeden önce [Workbook.calculate_formula](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/#) yöntemini çağırmak en iyisidir. Bu, formül bağımlı değerlerin yeniden hesaplanmasını sağlar ve doğru değerler PDF'ye render edilir.

{{% /alert %}}
