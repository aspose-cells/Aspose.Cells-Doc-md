---
title: Eklenen Resimleri Yeniden Örnekle  Excel den PDF ye Dönüştürme
type: docs
weight: 150
url: /tr/python-net/resample-added-images-excel-to-pdf-conversion/
description: Aspose.Cells for Python via .NET API siyle Excel den PDF ye dönüştürürken eklenen resimleri yeniden örnekleme yöntemini öğrenin.
keywords: Çok sayıda resmi içeren büyük Microsoft Excel dosyalarıyla çalışırken, eklenen resimleri sıkıştırmak ve çıktı PDF dosya boyutunu azaltmak, genel dönüştürme performansını iyileştirmek için resimleri yeniden örneklemek gerekebilir. Aspose.Cells for Python via .NET eklenen resimleri yeniden örnekleme işlemini destekler.
---

{{% alert color="primary" %}}

Büyük Microsoft Excel dosyalarıyla çalışırken, eklenen ve çıkarılmış resimleri sıkıştırmak, çıktı PDF dosya boyutunu azaltmak ve genel dönüşüm performansını geliştirmek isteyebilirsiniz. Aspose.Cells for Python via .NET, eklenen resimleri sıkıştırmayı destekler, çıktı PDF dosyası boyutunu azaltmak ve performansı biraz artırmak için resimleri örnekleme yapabilir.

{{% /alert %}}

Aşağıdaki örnek kod, Aspose.Cells for Python via .NET API'si kullanılarak görevi nasıl gerçekleştireceğinizi açıklar. Örnek, Microsoft Excel dosyasını PDF dosyasına dönüştürürken dosyadaki resimleri sıkıştırır.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-ResamplingAddedImages-1.py" >}}

{{% alert color="primary" %}}

[**PdfSaveOptions.set_image_resample**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/set_image_resample/#int-int) seçeneğini kullanarak çıktı PDF dosyasının boyutunu küçültür, ancak biraz görüntü kalitesini etkileyebilir.

{{% /alert %}} {{% alert color="primary" %}}

Eğer elektronik tablonuz formüller içeriyorsa, PDF formatına dönüştürmeden hemen önce [**Workbook.calculate_formula()**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/#) çağrısını yapmanız en iyisidir. Böyle yaparak formüle bağımlı değerler yeniden hesaplanacak ve doğru değerler PDF'de gösterilecektir.

{{% /alert %}}
