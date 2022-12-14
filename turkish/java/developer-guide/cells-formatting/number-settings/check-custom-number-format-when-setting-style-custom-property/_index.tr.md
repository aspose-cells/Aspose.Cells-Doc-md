---
title: Style.Custom Özelliğini Ayarlarken Özel Sayı Formatını Kontrol Edin
type: docs
weight: 160
url: /tr/java/check-custom-number-format-when-setting-style-custom-property/
---
## **Olası Kullanım Senaryoları**

 için geçersiz özel sayı biçimi atarsanız[**Stil. Özel**](https://reference.aspose.com/cells/java/com.aspose.cells/style#Custom)özelliğinden sonra Aspose.Cells herhangi bir istisna atmaz. Ancak, Aspose.Cells'in atanan özel numara biçiminin geçerli olup olmadığını kontrol etmesini istiyorsanız, lütfen[**Workbook.Settings.CheckCustomNumberFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#CheckCustomNumberFormat) mülkiyet**doğru**.

## **Style.Custom özelliğini ayarlarken Özel Sayı Formatını kontrol edin**

 Aşağıdaki örnek kod, geçersiz bir özel sayı biçimi atar.[**Stil. Özel**](https://reference.aspose.com/cells/java/com.aspose.cells/style#Custom) Emlak. zaten ayarladığımız için[**Workbook.Settings.CheckCustomNumberFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#CheckCustomNumberFormat) mülkiyet**doğru** , bu nedenle API örneğin CellsException'ı atar*Geçersiz sayı biçimi*.

## **Basit kod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-CheckCustomNumberFormat-CheckCustomNumberFormat.java" >}}
