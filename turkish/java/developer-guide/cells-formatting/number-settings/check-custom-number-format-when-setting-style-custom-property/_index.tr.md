---
title: Stil.Custom Özelliğini Ayarlarken Özel Sayı Biçimini Kontrol Edin
type: docs
weight: 160
url: /tr/java/check-custom-number-format-when-setting-style-custom-property/
---

## **Olası Kullanım Senaryoları**

Eğer geçersiz özel sayı biçimini [**Style.Custom**](https://reference.aspose.com/cells/java/com.aspose.cells/style#Custom) özelliğine atarsanız, Aspose.Cells herhangi bir istisna fırlatmaz. Ancak Aspose.Cells'in atanan özel sayı biçiminin geçerli olup olmadığını kontrol etmesini istiyorsanız, lütfen [**Workbook.Settings.CheckCustomNumberFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#CheckCustomNumberFormat) özelliğini **true** olarak ayarlayın.

## **Stil.Custom özelliğine özel sayı biçimini atayan aşağıdaki örnek kod geçersiz özel sayı biçimini {0} özelliğine atar. Zaten {1} özelliğini **true** olarak ayarladığımızdan dolayı, API, *Geçersiz sayı biçimi* gibi bir hata fırlatacaktır.**

Aşağıdaki örnek kod, [**Style.Custom**](https://reference.aspose.com/cells/java/com.aspose.cells/style#Custom) özelliğine geçersiz özel sayı formatı atar. Zaten [**Workbook.Settings.CheckCustomNumberFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#CheckCustomNumberFormat) özelliğini **true** olarak ayarladığımızdan, API **Invalid number format** yani *Geçersiz sayı formatı* hata fırlatacaktır..

## **Örnek Kod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-CheckCustomNumberFormat-CheckCustomNumberFormat.java" >}}
