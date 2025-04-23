---
title: Eklenen Resimleri Yeniden Örnekleme  Excel den PDF ye Dönütürme
type: docs
weight: 150
url: /tr/net/resampling-added-images-excel-to-pdf-conversion/
---

{{% alert color="primary" %}}

Birçok resmi içeren büyük Microsoft Excel dosyaları ile çalışırken, çıktı PDF dosyasının boyutunu küçültmek ve genel dönüşüm performansını iyileştirmek için eklenen resimleri yeniden örneklemek gerekebilir. Aspose.Cells, eklenen resimleri yeniden örnekleme ve çıktı PDF dosya boyutunu küçültme konusunda destek sağlar.

{{% /alert %}}

Aşağıdaki örnek kod, Aspose.Cells API'sını kullanarak görevi nasıl gerçekleştirebileceğinizi açıklamaktadır. Örnek, dosyadaki resimleri sıkıştırarak Microsoft Excel dosyasını PDF dosyasına dönüştürmektedir.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ResamplingAddedImages-1.cs" >}}

{{% alert color="primary" %}}

[**SetImageResample**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/methods/setimageresample) seçeneğini kullanarak çıktı PDF dosyasının boyutunu küçültür, ancak biraz görüntü kalitesini etkileyebilir.

{{% /alert %}} {{% alert color="primary" %}}

Eğer elektronik tablonuz formüller içeriyorsa, PDF formatına dönüştürmeden hemen önce [**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula) çağrısını yapmanız en iyisidir. Böyle yaparak formüle bağımlı değerler yeniden hesaplanacak ve doğru değerler PDF'de gösterilecektir.

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}
