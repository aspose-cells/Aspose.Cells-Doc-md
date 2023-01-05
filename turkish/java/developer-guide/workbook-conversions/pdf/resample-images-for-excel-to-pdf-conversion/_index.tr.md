---
title: Excel için Görüntüleri PDF Dönüşümüne Yeniden Örnekleyin
type: docs
weight: 250
url: /tr/java/resample-images-for-excel-to-pdf-conversion/
description: Bu makale, Excel dosyalarını PDF'e dönüştürürken görüntü boyutlarının küçültülmesini göstermektedir.
keywords: excel to pdf, resample images during excel to pdf conversion, compress images during excel to pdf conversion, reduce image sizes during excel to pdf conversion, convert excel to pdf with smaller size, excel to pdf conversion with image resampling, excel to pdf conversion with image compression, resample images during excel to pdf conversion java
---
{{% alert color="primary" %}}

Çok fazla resim içeren büyük Microsoft Excel dosyalarıyla çalışırken, PDF çıktı dosya boyutunu azaltmak ve genel dönüştürme performansını artırmak için eklenen resimleri sıkıştırmanız gerekebilir. Aspose.Cells, çıktı PDF dosya boyutunu azaltmak ve performansı artırmak için eklenen görüntülerin yeniden örneklenmesini destekler.

{{% /alert %}}

## **Excel için Görüntüleri PDF Dönüşümüne Yeniden Örnekleyin**

Lütfen Aspose.Cells API kullanarak görevin nasıl gerçekleştirileceğini açıklayan aşağıdaki örnek koda bakın. Örnek, dosyadaki görüntüleri sıkıştırırken Microsoft Excel dosyasını PDF dosyasına dönüştürür.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ResampleImagesforExceltoPDFConversion-ResampleImagesforExceltoPDFConversion.java" >}}

{{% alert color="primary" %}}

 Kullanmak[**PdfSaveOptions.setImageResample**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#setImageResample(int,%20int)) seçeneği, PDF çıktısının boyutunu en aza indirir ancak görüntü kalitesini biraz etkileyebilir.

{{% /alert %}} {{% alert color="primary" %}}

E-tablonuz formüller içeriyorsa, aramak en iyisidir[**Workbook.calculateFormula()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula()elektronik tabloyu PDF biçimine dönüştürmeden hemen önce. Bunu yapmak, formüle bağlı değerlerin yeniden hesaplanmasını ve PDF'de doğru değerlerin oluşturulmasını sağlar.

{{% /alert %}}
