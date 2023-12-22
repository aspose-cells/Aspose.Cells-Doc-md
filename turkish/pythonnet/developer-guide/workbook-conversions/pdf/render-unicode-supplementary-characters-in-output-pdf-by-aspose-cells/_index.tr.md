---
title: PDF çıktısındaki Unicode Tamamlayıcı karakterleri işleme Aspose.Cells for Python via .NET
type: docs
weight: 350
url: /tr/python-net/render-unicode-supplementary-characters-in-output-pdf-by-aspose-cells/
description: Excel'i Aspose.Cells for Python via .NET API ile PDF'e dönüştürürken Unicode Tamamlayıcı karakterleri nasıl oluşturacağınızı öğrenin.
keywords: Python Render Unicode Supplementary characters while saving file to PDF, Print Unicode Supplementary characters while saving Excel to PDF using Python, Python Show Unicode Supplementary characters when converting Excel to PDF, Output Unicode Supplementary characters for excel to pdf
---
{{% alert color="primary" %}}

Normal Unicode karakterler 2 bayt uzunluğunda, Unicode Tamamlayıcı karakterler ise 4 bayt uzunluğundadır. Aspose.Cells for Python via .NET artık bu 4 baytlık Unicode karakterlerin oluşturulmasını destekliyor.

Unicode Karakter Standardında Ek Karakterler, U+10000'den U+10FFFF'ye kadar kod noktaları atanan karakterlerdir. Başka bir deyişle bunlar U+FFFF'den büyük Unicode karakterlerdir.

- UTF-8'de bu karakterlerin her biri 4 bayt uzunluğundadır.
- UTF-16'da bu karakterler 2 vekil (16 bit birim) gerektirir.

{{% /alert %}}

##  PDF çıktısındaki Unicode Tamamlayıcı karakterleri işleme Aspose.Cells for Python via .NET

 Aşağıdaki ekran görüntüsü Aspose.Cells for Python via .NET'in[kaynak excel dosyası](5115563.xlsx) içine[çıkış PDF](5115564.pdf). Gördüğünüz gibi üç Unicode Tamamlayıcı karakterin tümü, Microsoft Excel tarafından yapılanla tamamen aynı şekilde oluşturulmuştur.

![yapılacak şey:image_alt_text](output.png)

##  Basit kod

Dönüştürmek için bu örnek kodu kullanabilirsiniz.[kaynak excel dosyası](5115563.xlsx) içine[çıkış PDF](5115564.pdf).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-RenderUnicodeInOutput.py" >}}
