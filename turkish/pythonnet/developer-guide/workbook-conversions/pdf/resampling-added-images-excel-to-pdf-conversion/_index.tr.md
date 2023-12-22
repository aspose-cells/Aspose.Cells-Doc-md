---
title: Eklenen Görselleri Yeniden Örnekleme - Excel'den PDF'e Dönüştürme
type: docs
weight: 150
url: /tr/python-net/resample-added-images-excel-to-pdf-conversion/
description: Aspose.Cells for Python via .NET API ile excel'i pdf'ye dönüştürürken eklenen görselleri nasıl yeniden örnekleyeceğinizi öğrenin.
keywords: Python Resample Added Images when Convert Excel to PDF
---
{{% alert color="primary" %}}

Çok sayıda görüntü içeren büyük Microsoft Excel dosyalarıyla çalışırken, çıktı PDF dosya boyutunu azaltmak ve genel dönüştürme performansını artırmak için eklenen görüntüleri sıkıştırmanız gerekebilir. Aspose.Cells for Python via .NET, çıktı PDF dosya boyutunu azaltmak ve performansı bir miktar artırmak için eklenen görüntülerin yeniden örneklenmesini destekler.

{{% /alert %}}

Lütfen Aspose.Cells for Python via .NET API kullanılarak görevin nasıl gerçekleştirileceğini açıklayan aşağıdaki örnek koda bakın. Örnek, dosyadaki görüntüleri sıkıştırırken Microsoft Excel dosyasını PDF dosyasına dönüştürür.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-ResamplingAddedImages-1.py" >}}

{{% alert color="primary" %}}

 kullanarak[**PdfSaveOptions.set_image_resample**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/set_image_resample/#int-int)seçeneği, PDF çıktısının boyutunu en aza indirir ancak görüntü kalitesini biraz etkileyebilir.

{{% /alert %}} {{% alert color="primary" %}}

 E-tablonuz formüller içeriyorsa, aramak en iyisidir.[**Workbook.calculate_formula()**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/#) e-tabloyu PDF biçimine dönüştürmeden hemen önce. Bunu yapmak, formüle bağlı değerlerin yeniden hesaplanmasını ve PDF'de doğru değerlerin oluşturulmasını sağlayacaktır.

{{% /alert %}}
