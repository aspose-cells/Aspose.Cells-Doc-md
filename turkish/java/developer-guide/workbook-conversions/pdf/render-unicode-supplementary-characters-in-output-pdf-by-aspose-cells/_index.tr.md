---
title: Aspose.Cells ile çıktı PDF de Unicode Ek Sayısal karakterlerin oluşturulması
type: docs
weight: 690
url: /tr/java/render-unicode-supplementary-characters-in-output-pdf-by-aspose-cells/
---

{{% alert color="primary" %}} 

Normal Unicode karakterleri 2 bayt uzunluğunda iken Unicode Ek Sayısal karakterleri 4 bayt uzunluğundadır. Aspose.Cells şimdi bu 4 bayt Unicode karakterlerin oluşturulmasını destekliyor.

Unicode Karakter Standartında, Ek Sayısal Karakterler U+10000'den U+10FFFF'e kadar olan kod noktalarına atanmış karakterlerdir. Diğer bir deyişle, bunlar U+FFFF'den büyük Unicode karakterlerdir.

- UTF-8'de bu karakterlerin her biri 4 bayt uzunluğundadır.
- UTF-16'da bu karakterler 2 takyeyi (16 bit birimler) gerektirir.

{{% /alert %}} 
## **Aspose.Cells ile çıktı PDF'inde Unicode Ek Karakterlerini renderla**
Aşağıdaki ekran görüntüsü, Aspose.Cells'in [kaynak excel dosyasını](5473390.xlsx) [çıktı PDF'sine](5473391.pdf) nasıl dönüştürdüğünü gösterir. Görebileceğiniz gibi, üç Unicode Ek karakteri de Microsoft Excel tarafından yapıldığı gibi tam olarak gösterilmiştir.

![todo:image_alt_text](render-unicode-supplementary-characters-in-output-pdf-by-aspose-cells_1.png)

Bu örnek kodu kullanarak [kaynak excel dosyasını](5473390.xlsx) [çıktı PDF'sine](5473391.pdf) dönüştürebilirsiniz.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-files-utility-RenderUnicodeSupplimentaryCharacterToPDF-1.java" >}}
{{< app/cells/assistant language="java" >}}
