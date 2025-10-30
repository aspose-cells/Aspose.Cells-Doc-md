---
title: Aspose.Cells kullanarak Golang ile C++ ile çıktı PDF sinde Unicode Destekli karakterleri nasıl göstereceğinizi öğrenin
linktitle: Unicode Yardımcı Karakterleri Göster
type: docs
weight: 350
url: /tr/go-cpp/render-unicode-supplementary-characters-in-output-pdf-by-aspose-cells/
description: Aspose.Cells for C++ kullanarak Unicode Yardımcı karakterlerini çıktı PDF sinde nasıl göstereceğinizi öğrenin.
---

{{% alert color="primary" %}}

Normal Unicode karakterleri 2 bayt uzunluğunda iken Unicode Ek Sayısal karakterleri 4 bayt uzunluğundadır. Aspose.Cells şimdi bu 4 bayt Unicode karakterlerin oluşturulmasını destekliyor.

Unicode Karakter Standartında, Ek Sayısal Karakterler U+10000'den U+10FFFF'e kadar olan kod noktalarına atanmış karakterlerdir. Diğer bir deyişle, bunlar U+FFFF'den büyük Unicode karakterlerdir.

- UTF-8'de bu karakterlerin her biri 4 bayt uzunluğundadır.
- UTF-16'da bu karakterler 2 takyeyi (16 bit birimler) gerektirir.

{{% /alert %}}

## Aspose.Cells ile çıktı PDF'de Unicode Ek Sayısal karakterlerin oluşturulması

Aşağıdaki ekran görüntüsü, Aspose.Cells'ın [kaynak excel dosyasını](5115563.xlsx) [çıktı PDF'ye](5115564.pdf) nasıl dönüştürdüğünü göstermektedir. Görebileceğiniz gibi, tüm üç Unicode Ek Sayısal karakter Microsoft Excel tarafından yapılan gibi tam olarak oluşturulmuştur.

![todo:image_alt_text](output.png)

## Örnek Kod

[Kaynak excel dosyasını](5115563.xlsx) [çıktı PDF'ye](5115564.pdf) dönüştürmek için bu örnek kodu kullanabilirsiniz.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-RenderUnicodeSupplementaryCharactersInOutputPdfByAsposeCells.go" >}}
