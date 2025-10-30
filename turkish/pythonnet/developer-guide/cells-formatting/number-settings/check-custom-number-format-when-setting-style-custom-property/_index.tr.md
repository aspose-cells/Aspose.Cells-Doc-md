---
title: Stil.Custom Özelliğini Ayarlarken Özel Sayı Biçimini Kontrol Edin
description: Aspose.Cells, elektronik tablo dosyalarıyla çalışmak için kullanılan bir Python kütüphanesidir ve stil verirken özel sayı formatlarının kontrol edilmesini destekler. Bu makale, stil vermenin doğru olup olmadığını kontrol etmek için Aspose.Cells kütüphanesini kullanarak özel sayı formatlarını nasıl kontrol edeceğinizi gösterecek.
keywords: Aspose.Cells, Python kütüphaneleri, elektronik tablolar, stil verme, özel sayı biçimlendirme, kontrol, doğrulama
type: docs
weight: 170
url: /tr/python-net/check-custom-number-format-when-setting-style-custom-property/
---

## **Olası Kullanım Senaryoları**

Eğer [**Style.custom**](https://reference.aspose.com/cells/python-net/aspose.cells/style/custom) özelliğine geçersiz bir özel sayı biçimi atamışsanız, Aspose.Cells herhangi bir istisna fırlatmaz. Ancak Aspose.Cells'ın atanan özel sayı biçiminin geçerli olup olmadığını kontrol etmesini istiyorsanız, lütfen [**Workbook.settings.check_custom_number_format**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/check_custom_number_format/) özelliğini **true** olarak ayarlayın.

## **Stil.Custom özelliğini ayarladığınızda özel sayı biçimine geçersiz bir özel sayı biçimi atayan aşağıdaki örnek kod. {1} özelliğini zaten **true** olarak ayarladığımız için, bu nedenle Geçersiz özel sayı biçimi gibi bir istisna fırlatır. Daha fazla yardım için kodun içindeki yorumları okuyun.**

Aşağıdaki örnek kod, [**Style.custom**](https://reference.aspose.com/cells/python-net/aspose.cells/style/custom) özelliğine geçersiz özel bir sayı biçimi atar. [**Workbook.settings.check_custom_number_format**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/check_custom_number_format/) özelliğini zaten **true** olarak ayarladığımız için, bunun sonucunda geçersiz sayı biçimi gibi bir istisna fırlatır. Daha fazla yardım için kod içindeki yorumları okuyun.

## **Örnek Kod**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-CheckCustomFormatPattern.py" >}}

{{< app/cells/assistant language="python-net" >}}
