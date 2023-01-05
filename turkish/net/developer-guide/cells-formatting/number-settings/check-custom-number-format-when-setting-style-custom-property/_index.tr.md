---
title: Style.Custom Özelliğini Ayarlarken Özel Sayı Formatını Kontrol Edin
type: docs
weight: 170
url: /tr/net/check-custom-number-format-when-setting-style-custom-property/
---
## **Olası Kullanım Senaryoları**

 için geçersiz özel sayı biçimi atarsanız[**Stil. Özel**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/custom)özellik, o zaman Aspose.Cells herhangi bir istisna atmaz. Ancak, Aspose.Cells'in atanan özel numara biçiminin geçerli olup olmadığını kontrol etmesini istiyorsanız, lütfen[**Workbook.Settings.CheckCustomNumberFormat**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/checkcustomnumberformat) mülkiyet**doğru**.

## **Style.Custom özelliğini ayarlarken Özel Sayı Formatını kontrol edin**

 Aşağıdaki örnek kod, geçersiz bir özel sayı biçimi atar.[**Stil. Özel**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/custom) Emlak. beri, zaten ayarladık[**Workbook.Settings.CheckCustomNumberFormat**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/checkcustomnumberformat) mülkiyet**doğru**, bu nedenle istisna atar, örneğin Geçersiz sayı biçimi. Daha fazla yardım için lütfen kodun içindeki yorumları okuyun.

## **Basit kod**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-StylingAndDataFormatting-CheckCustomFormatPattern.cs" >}}
