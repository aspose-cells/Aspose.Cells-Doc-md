---
title: Hataları ve Boole Değerini Rusça veya Başka Bir Dilde Uygulama
type: docs
weight: 30
url: /tr/java/implement-errors-and-boolean-value-in-russian-or-any-other-language/
---
## **Olası Kullanım Senaryoları**
Microsoft Excel'i Rusça Yerel Ayar veya Dilde veya başka bir Yerel Ayar veya Dilde kullanıyorsanız, o Yerel Ayar veya Dile göre Hatalar ve Boole değerleri görüntüler. Aspose.Cells'i kullanarak benzer bir davranış elde edebilirsiniz.[Workbook.getSettings().setGlobalizationSettings()](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#GlobalizationSettings) yöntem veya özellik. Aşağıdaki yöntemleri geçersiz kılmanız gerekecek[KüreselleşmeAyarları](https://reference.aspose.com/cells/java/com.aspose.cells/GlobalizationSettings)sınıf.

- [GlobalizationSettings.getErrorValueString()](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getErrorValueString\(java.lang.String\))
- [GlobalizationSettings.getBooleanValueString()](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getBooleanValueString\(boolean\))
## **Hataları ve Boole Değerini Rusça veya Başka Bir Dilde Uygulama**
 Aşağıdaki örnek kod, Hataların ve Boolean Değerinin Rusça veya Herhangi Bir Başka Dilde nasıl uygulanacağını gösterir. Lütfen bu kodda kullanılan Örnek Excel Dosyasını ve Çıktısı PDF'i kontrol edin. Ekran görüntüsü, arasındaki farkı gösterir.[Örnek Excel Dosyası](48496697.xlsx) ve[Çıkış PDF](48496696.pdf) referans için

![yapılacaklar:resim_alternatif_metin](implement-errors-and-boolean-value-in-russian-or-any-other-language_1.png)
## **Basit kod**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-WorkbookSettings-ImplementErrorsAndBooleanValueInRussianOrAnyOtherLanguage.java" >}}
