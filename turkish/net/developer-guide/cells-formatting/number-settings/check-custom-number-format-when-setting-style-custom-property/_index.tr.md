---
title: Style.Custom Özelliğini Ayarlarken Özel Sayı Formatını Kontrol Edin
description: Aspose.Cells, elektronik tablo dosyalarıyla çalışmaya yönelik, stil oluşturma sırasında özel sayı biçimlerinin kontrol edilmesini destekleyen bir .NET kitaplığıdır. Bu makale, stilin doğru olduğundan emin olmak amacıyla özel sayı biçimlerini kontrol etmek için Aspose.Cells kitaplığını nasıl kullanacağınızı gösterecektir.
keywords: Aspose.Cells, NET libraries, spreadsheets, styling, custom number formatting, checking, validation
type: docs
weight: 170
url: /tr/net/check-custom-number-format-when-setting-style-custom-property/
---
##  **Olası Kullanım Senaryoları**

 Geçersiz özel sayı biçimini atarsanız[**Stil.Özel**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/custom) özelliği, o zaman Aspose.Cells herhangi bir istisna atmayacak. Ancak Aspose.Cells'in atanan özel numara biçiminin geçerli olup olmadığını kontrol etmesini istiyorsanız lütfen[**Workbook.Settings.CheckCustomNumberFormat**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/checkcustomnumberformat) özelliği *true** olarak değiştirin.

##  **Style.Custom özelliğini ayarlarken Özel Sayı Formatını kontrol edin**

 Aşağıdaki örnek kod, geçersiz bir özel sayı biçimini şuna atar:[**Stil.Özel**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/custom) mülk. Çünkü zaten ayarladık[**Workbook.Settings.CheckCustomNumberFormat**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/checkcustomnumberformat) özelliği *true** olarak değiştirir, bu nedenle örneğin Geçersiz sayı biçimi gibi bir istisna atar. Daha fazla yardım için lütfen kodun içindeki yorumları okuyun.

##  **Basit kod**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-StylingAndDataFormatting-CheckCustomFormatPattern.cs" >}}
