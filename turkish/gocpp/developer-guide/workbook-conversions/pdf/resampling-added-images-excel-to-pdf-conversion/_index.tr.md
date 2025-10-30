---
title: Resampling ile Eklenmiş Resimleri  Golang ile C++ kullanarak Excel den PDF ye Dönüştürme
linktitle: Eklenen Resimleri Yeniden Örnekleme  Excel den PDF ye Dönütürme
type: docs
weight: 150
url: /tr/go-cpp/resampling-added-images-excel-to-pdf-conversion/
description: Aspose.Cells kullanarak Golang ile C++ üzerinden PDF boyutunu azaltmak için eklenmiş resimleri yeniden örneklemeyi öğrenin.
---

{{% alert color="primary" %}}

Birçok resmi içeren büyük Microsoft Excel dosyaları ile çalışırken, çıktı PDF dosyasının boyutunu küçültmek ve genel dönüşüm performansını iyileştirmek için eklenen resimleri yeniden örneklemek gerekebilir. Aspose.Cells, eklenen resimleri yeniden örnekleme ve çıktı PDF dosya boyutunu küçültme konusunda destek sağlar.

{{% /alert %}}

Aşağıdaki örnek kod, Aspose.Cells API'sını kullanarak görevi nasıl gerçekleştirebileceğinizi açıklamaktadır. Örnek, dosyadaki resimleri sıkıştırarak Microsoft Excel dosyasını PDF dosyasına dönüştürmektedir.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ResamplingAddedImagesExcelToPdfConversion.go" >}}
{{% alert color="primary" %}}

[**SetImageResample**](https://reference.aspose.com/cells/go-cpp/pdfsaveoptions/setimageresample/) seçeneğini kullanarak çıktı PDF dosyasının boyutunu en aza indirir, ancak görüntü kalitesini biraz etkileyebilir.

{{% /alert %}} 

{{% alert color="primary" %}}

Eğer elektronik tablonuz formüller içeriyorsa, PDF formatına dönüştürmeden hemen önce [**CalculateFormula**](https://reference.aspose.com/cells/go-cpp/workbook/calculateformula/) çağrısını yapmanız en iyisidir. Böyle yaparak formüle bağımlı değerler yeniden hesaplanacak ve doğru değerler PDF'de gösterilecektir.

{{% /alert %}}

