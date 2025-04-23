---
title: Stil.Custom Özelliğini Ayarlarken Özel Sayı Biçimini Kontrol Edin
linktitle: Stil.Custom Özelliğini Ayarlarken Özel Sayı Biçimini Kontrol Edin
description: Aspose.Cells, elektronik tablo dosyalarıyla çalışma yapmaya uygun Node.js kütüphanesidir ve stil verirken özel sayı biçimlerini kontrol etmeyi destekler. Bu makale, stilin doğru olup olmadığını kontrol etmek için Aspose.Cells kütüphanesinin nasıl kullanılacağını gösterecek.
keywords: Aspose.Cells, Node.js kütüphaneleri, elektronik tablolar, stil verme, özel sayı biçimi, kontrol, doğrulama
type: docs
weight: 170
url: /tr/nodejs-cpp/check-custom-number-format-when-setting-style-custom-property/
---

## **Olası Kullanım Senaryoları**

Geçersiz özel sayı biçimi [**Style.setCustom(string)**](https://reference.aspose.com/cells/nodejs-cpp/style/#setCustom-string-) yöntemine atanırsa, Aspose.Cells for Node.js via C++ herhangi bir istisna atmaz. Ancak, Aspose.Cells'in atanan özel sayı biçiminin geçerli olup olmadığını kontrol etmesini istiyorsanız, lütfen [**Workbook.getSettings().setCheckCustomNumberFormat(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#setCheckCustomNumberFormat-boolean-) yöntemini **doğru** olarak ayarlayın.

## **Style.setCustom(string) yöntemini ayarlarken Özel Sayı Biçimini Kontrol Edin**

Aşağıdaki örnek kod, [**Style.setCustom(string)**](https://reference.aspose.com/cells/nodejs-cpp/style/#setCustom-string-) yöntemine geçersiz bir özel sayı biçimi atar. Zaten [**Workbook.getSettings().setCheckCustomNumberFormat(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#setCheckCustomNumberFormat-boolean-) yöntemini **doğru** olarak ayarladığımızdan, bir istisna fırlatır, örn., Geçersiz sayı biçimi. Daha fazla yardım için kod içindeki yorumları okuyun.

## **Örnek Kod**

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-NumberSetting-CheckCustomNumberFormat.js" >}}

