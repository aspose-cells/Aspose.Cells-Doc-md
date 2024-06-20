---
title: Stil.Custom Özelliğini Ayarlarken Özel Sayı Biçimini Kontrol Edin
description: Aspose.Cells, elektronik tablo dosyalarıyla çalışmak için bir .NET kütüphanesidir, ve stili belirlerken özel sayı biçimlerini kontrol etmeyi destekler. Bu makale, stili doğrulamak için Aspose.Cells kütüphanesini nasıl kullanacağınızı gösterecektir.
keywords: Aspose.Cells, NET kütüphaneleri, elektronik tablolar, stil, özel sayı biçimi, kontrol, doğrulama
type: docs
weight: 170
url: /tr/net/check-custom-number-format-when-setting-style-custom-property/
---

## **Olası Kullanım Senaryoları**

Eğer [**Style.Custom**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/custom) özelliğine geçersiz bir özel sayı biçimi atamışsanız, Aspose.Cells herhangi bir istisna fırlatmaz. Ancak Aspose.Cells'ın atanan özel sayı biçiminin geçerli olup olmadığını kontrol etmesini istiyorsanız, lütfen [**Workbook.Settings.CheckCustomNumberFormat**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/checkcustomnumberformat) özelliğini **true** olarak ayarlayın.

## **Stil.Custom özelliğini ayarladığınızda özel sayı biçimine geçersiz bir özel sayı biçimi atayan aşağıdaki örnek kod. {1} özelliğini zaten **true** olarak ayarladığımız için, bu nedenle Geçersiz özel sayı biçimi gibi bir istisna fırlatır. Daha fazla yardım için kodun içindeki yorumları okuyun.**

Aşağıdaki örnek kod, [**Style.Custom**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/custom) özelliğine geçersiz özel bir sayı biçimi atar. [**Workbook.Settings.CheckCustomNumberFormat**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/checkcustomnumberformat) özelliğini zaten **true** olarak ayarladığımız için, bunun sonucunda geçersiz sayı biçimi gibi bir istisna fırlatır. Daha fazla yardım için kod içindeki yorumları okuyun.

## **Örnek Kod**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-StylingAndDataFormatting-CheckCustomFormatPattern.cs" >}}
