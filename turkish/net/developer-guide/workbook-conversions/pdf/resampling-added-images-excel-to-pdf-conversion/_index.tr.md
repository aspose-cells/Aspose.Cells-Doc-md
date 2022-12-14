---
title: Eklenen Görüntüleri Yeniden Örnekleme - Excel'den PDF'e Dönüştürme
type: docs
weight: 150
url: /tr/net/resampling-added-images-excel-to-pdf-conversion/
---
{{% alert color="primary" %}}

Çok sayıda görüntü içeren büyük Microsoft Excel dosyalarıyla çalışırken, çıktı PDF dosyasının boyutunu azaltmak ve genel dönüştürme performansını artırmak için eklenen görüntüleri sıkıştırmanız gerekebilir. Aspose.Cells, çıktı PDF dosyasının boyutunu azaltmak ve performansı biraz artırmak için eklenen görüntülerin yeniden örneklenmesini destekler.

{{% /alert %}}

Lütfen Aspose.Cells API kullanarak görevin nasıl gerçekleştirileceğini açıklayan aşağıdaki örnek koda bakın. Örnek, dosyadaki görüntüleri sıkıştırırken bir Microsoft Excel dosyasını bir PDF dosyasına dönüştürür.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ResamplingAddedImages-1.cs" >}}

{{% alert color="primary" %}}

 kullanarak[**SetImageResample**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/methods/setimageresample)seçeneği, çıktı PDF'sinin boyutunu en aza indirir ancak görüntü kalitesini biraz etkileyebilir.

{{% /alert %}} {{% alert color="primary" %}}

 E-tablonuz formüller içeriyorsa, aramak en iyisidir[**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula) elektronik tabloyu PDF formatına dönüştürmeden hemen önce. Bunu yapmak, formüle bağlı değerlerin yeniden hesaplanmasını ve doğru değerlerin PDF'de oluşturulmasını sağlar.

{{% /alert %}}
