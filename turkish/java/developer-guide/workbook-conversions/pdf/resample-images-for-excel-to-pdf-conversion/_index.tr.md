---
title: Excel den PDF ye Dönüşüm için Görüntüleri Yeniden Örnekle
type: docs
weight: 250
url: /tr/java/resample-images-for-excel-to-pdf-conversion/
description: Bu makale, Excel dosyalarını PDF e dönüştürürken görüntü boyutlarını azaltmayı gösterir
keywords: excel to pdf, excel to pdf dönüşümü sırasında görüntüleri yeniden örneklerken, excel to pdf dönüşümü sırasında görüntüleri sıkıştırırken, excel to pdf dönüşümü sırasında görüntü boyutlarını azaltırken, excel to pdf dönüştürme işlemi daha küçük boyutlu, excel to pdf dönüşümü sırasında görüntü örnekleme, excel to pdf dönüşümü sırasında görüntü sıkıştırma, excel to pdf dönüşümü sırasında görüntüleri yeniden ornekleme java
---

{{% alert color="primary" %}}

Büyük Microsoft Excel dosyalarıyla çalışırken, çıktı PDF dosyasının boyutunu küçültmek ve genel dönüşüm performansını artırmak için eklenen görüntüleri sıkıştırmanız gerekebilir. Aspose.Cells, eklenen görüntüleri yeniden örnekleyerek çıktı PDF dosyasının boyutunu küçültme ve performansı artırmayı destekler.

{{% /alert %}}

## **Excel'den PDF'ye Dönüşüm için Görüntüleri Yeniden Örnekle**

Aşağıdaki örnek kod, Aspose.Cells API'sını kullanarak görevi nasıl gerçekleştirebileceğinizi açıklamaktadır. Örnek, dosyadaki resimleri sıkıştırarak Microsoft Excel dosyasını PDF dosyasına dönüştürmektedir.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ResampleImagesforExceltoPDFConversion-ResampleImagesforExceltoPDFConversion.java" >}}

{{% alert color="primary" %}}

[**PdfSaveOptions.setImageResample**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#setImageResample(int,%20int)) seçeneğini kullanarak çıktı PDF dosyasının boyutunu en aza indirir, ancak görüntü kalitesini biraz etkileyebilir.

{{% /alert %}} {{% alert color="primary" %}}

Eğer elektronik tablonuz formüller içeriyorsa, PDF formatına dönüştürmeden hemen önce [**Workbook.calculateFormula()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula--) çağrısını yapmanız en iyisidir. Böyle yaparak formüle bağımlı değerler yeniden hesaplanacak ve doğru değerler PDF'de gösterilecektir.

{{% /alert %}}
