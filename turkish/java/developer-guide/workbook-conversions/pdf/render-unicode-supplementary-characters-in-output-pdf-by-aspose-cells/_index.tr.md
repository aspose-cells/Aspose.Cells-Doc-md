---
title: Unicode Tamamlayıcı karakterleri PDF çıktısında Aspose.Cells ile işleyin
type: docs
weight: 690
url: /tr/java/render-unicode-supplementary-characters-in-output-pdf-by-aspose-cells/
---
{{% alert color="primary" %}} 

Normal Unicode karakterleri 2 bayt uzunluğundayken Unicode Ek karakterleri 4 bayt uzunluğundadır. Aspose.Cells artık bu 4 baytlık Unicode karakterlerin oluşturulmasını desteklemektedir.

Unicode Karakter Standardında, Tamamlayıcı Karakterler, U+10000'den U+10FFFF'ye kadar kod noktaları atanan karakterlerdir. Başka bir deyişle, bunlar U+FFFF'den büyük Unicode karakterlerdir.

- UTF-8'de bu karakterlerin her biri 4 bayt uzunluğundadır.
- UTF-16'da bu karakterler 2 vekil (16 bitlik birimler) gerektirir.

{{% /alert %}} 
## **Unicode Tamamlayıcı karakterleri PDF çıktısında Aspose.Cells ile işleyin**
 Aşağıdaki ekran görüntüsü, Aspose.Cells'in[kaynak excel dosyası](5473390.xlsx) içine[çıkış PDF](5473391.pdf). Gördüğünüz gibi, üç Unicode Ek karakteri de Microsoft Excel tarafından yapılanla tamamen aynı şekilde oluşturulmuştur.

![yapılacaklar:resim_alternatif_metin](render-unicode-supplementary-characters-in-output-pdf-by-aspose-cells_1.png)

dönüştürmek için bu örnek kodu kullanabilirsiniz.[kaynak excel dosyası](5473390.xlsx) içine[çıkış PDF](5473391.pdf).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-files-utility-RenderUnicodeSupplimentaryCharacterToPDF-1.java" >}}
