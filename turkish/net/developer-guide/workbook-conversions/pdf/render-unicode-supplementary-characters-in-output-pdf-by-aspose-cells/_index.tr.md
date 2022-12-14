---
title: Çıkış PDF'sinde Aspose.Cells ile Unicode Tamamlayıcı karakterleri işleyin
type: docs
weight: 350
url: /tr/net/render-unicode-supplementary-characters-in-output-pdf-by-aspose-cells/
---
{{% alert color="primary" %}}

Normal Unicode karakterleri 2 bayt uzunluğundayken Unicode Ek karakterleri 4 bayt uzunluğundadır. Aspose.Cells artık bu 4 baytlık Unicode karakterlerin oluşturulmasını desteklemektedir.

Unicode Karakter Standardında, Tamamlayıcı Karakterler, U+10000'den U+10FFFF'ye kadar kod noktaları atanan karakterlerdir. Başka bir deyişle, bunlar U+FFFF'den büyük Unicode karakterlerdir.

- UTF-8'de bu karakterlerin her biri 4 bayt uzunluğundadır.
- UTF-16'da bu karakterler 2 vekil (16 bitlik birimler) gerektirir.

{{% /alert %}}

## Çıkış PDF'sinde Aspose.Cells ile Unicode Tamamlayıcı karakterleri işleyin

 Aşağıdaki ekran görüntüsü, Aspose.Cells'in[kaynak excel dosyası](5115563.xlsx) içine[çıktı PDF](5115564.pdf). Gördüğünüz gibi, üç Unicode Ek karakteri de Microsoft Excel tarafından yapılanla tamamen aynı hale getirildi.

![yapılacaklar:resim_alternatif_Metin](output.png)

## Basit kod

 Dönüştürmek için bu örnek kodu kullanabilirsiniz.[kaynak excel dosyası](5115563.xlsx) içine[çıktı PDF](5115564.pdf).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderUnicodeInOutput-RenderUnicodeInOutput.cs" >}}
