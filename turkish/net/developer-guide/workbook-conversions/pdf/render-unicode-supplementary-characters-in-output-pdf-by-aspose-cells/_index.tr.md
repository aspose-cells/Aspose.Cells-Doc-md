---
title: Aspose.Cells ile çıktı PDF de Unicode Ek Sayısal karakterlerin oluşturulması
type: docs
weight: 350
url: /tr/net/render-unicode-supplementary-characters-in-output-pdf-by-aspose-cells/
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

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderUnicodeInOutput-RenderUnicodeInOutput.cs" >}}
