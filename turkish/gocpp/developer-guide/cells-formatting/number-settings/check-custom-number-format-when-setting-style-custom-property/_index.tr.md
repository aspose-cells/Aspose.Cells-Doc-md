---
title: Golang ile C++ kullanarak Style.Custom Özelliği Ayarlanırken Özel Sayı Formatını Kontrol Edin
description: Aspose.Cells, C++ kütüphanesi olan ve stil verilirken özel sayı formatlarını kontrol etmeyi destekleyen bir elektronik tablo kütüphanesidir. Bu makale, Aspose.Cells kütüphanesini kullanarak stilin doğru olup olmadığını kontrol etmek için özel sayı formatlarını nasıl kullanacağınızı gösterecek.
keywords: Aspose.Cells, C++ kütüphaneleri, elektronik tablolar, stil verme, özel sayı biçimlendirme, kontrol, doğrulama
type: docs
weight: 170
url: /tr/go-cpp/check-custom-number-format-when-setting-style-custom-property/
---

## **Olası Kullanım Senaryoları**

Eğer [**Style.GetCustom()**](https://reference.aspose.com/cells/go-cpp/style/getcustom/) özelliğine geçersiz bir özel sayı biçimi atarsanız, Aspose.Cells herhangi bir istisna atmaz. Ancak, Aspose.Cells'in atanan özel sayı biçiminin geçerli olup olmadığını kontrol etmesini istiyorsanız, lütfen [**Workbook.GetCheckCustomNumberFormat()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getcheckcustomnumberformat/) özelliğini **true** olarak ayarlayın.

## **Stil.Custom özelliğini ayarladığınızda özel sayı biçimine geçersiz bir özel sayı biçimi atayan aşağıdaki örnek kod. {1} özelliğini zaten **true** olarak ayarladığımız için, bu nedenle Geçersiz özel sayı biçimi gibi bir istisna fırlatır. Daha fazla yardım için kodun içindeki yorumları okuyun.**

Aşağıdaki örnek kod, [**Style.GetCustom()**](https://reference.aspose.com/cells/go-cpp/style/getcustom/) özelliğine geçersiz bir özel sayı biçimi atar. Zaten [**Workbook.GetCheckCustomNumberFormat()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getcheckcustomnumberformat/) özelliği **true** olarak ayarlandığından, bir istisna fırlatır, örneğin Geçersiz sayı formatı. Daha fazla yardım için kod içindeki yorumları okuyun.

## **Örnek Kod**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CheckCustomNumberFormatWhenSettingStyleCustomProperty.go" >}}
