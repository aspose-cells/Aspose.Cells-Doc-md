---
title: Aspose.Cells for Python via .NET ile çıktı PDF de Unicode Supplementary karakterlerin render edilmesi
type: docs
weight: 350
url: /tr/python-net/render-unicode-supplementary-characters-in-output-pdf-by-aspose-cells/
description: Aspose.Cells for Python via .NET API si ile Excel i PDF ye dönüştürürken Unicode Supplementary karakterlerin render edilmesini öğrenin.
keywords: Python ile dosyayı PDF olarak kaydederken Unicode Supplementary karakterlerini render etme, Excel i PDF e dönüştürürken Python ile Unicode Supplementary karakterlerini gösterme, Excel den PDF e dönüştürürken Python kullanarak Unicode Supplementary karakterlerini çıktı olarak gösterme
---

{{% alert color="primary" %}}

Normal Unicode karakterleri 2 bayt uzunluğundadır, Unicode Supplementary karakterleri ise 4 bayt uzunluğundadır. Şimdi, Aspose.Cells for Python via .NET 4 bayt Unicode karakterlerin render edilmesini destekliyor.

Unicode Karakter Standartında, Ek Sayısal Karakterler U+10000'den U+10FFFF'e kadar olan kod noktalarına atanmış karakterlerdir. Diğer bir deyişle, bunlar U+FFFF'den büyük Unicode karakterlerdir.

- UTF-8'de bu karakterlerin her biri 4 bayt uzunluğundadır.
- UTF-16'da bu karakterler 2 takyeyi (16 bit birimler) gerektirir.

{{% /alert %}}

Aspose.Cells for Python via .NET ile çıktı PDF'de Unicode Supplementary karakterlerin render edilmesi

Aşağıdaki ekran görüntüsü, Aspose.Cells for Python via .NET'nin [kaynak excel dosyasını](5115563.xlsx) [çıktı PDF'ye](5115564.pdf) nasıl render ettiğini gösterir. Görebileceğiniz gibi, tüm üç Unicode Supplementary karakteri Microsoft Excel tarafından yapıldığı gibi aynı şekilde render edilmiştir.

![todo:image_alt_text](output.png)

## Örnek Kod

[Kaynak excel dosyasını](5115563.xlsx) [çıktı PDF'ye](5115564.pdf) dönüştürmek için bu örnek kodu kullanabilirsiniz.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-RenderUnicodeInOutput.py" >}}
{{< app/cells/assistant language="python-net" >}}
