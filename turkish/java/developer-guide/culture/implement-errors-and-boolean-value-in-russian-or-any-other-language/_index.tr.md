---
title: Rusça veya başka bir dilde Hataları ve Boolean Değerleri Uygulayın
type: docs
weight: 30
url: /tr/java/implement-errors-and-boolean-value-in-russian-or-any-other-language/
---

## **Olası Kullanım Senaryoları**
Microsoft Excel'i Rusça Locale veya Dil veya başka bir Locale veya Dil olarak kullanıyorsanız, Hataları ve Boolean değerlerini o Locale'a veya Dile göre görüntüler. Benzer davranışı Aspose.Cells [Workbook.getSettings().setGlobalizationSettings()](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#GlobalizationSettings) yöntemi veya özelliği kullanarak elde edebilirsiniz. [GlobalizationSettings](https://reference.aspose.com/cells/java/com.aspose.cells/GlobalizationSettings) sınıfının aşağıdaki yöntemlerini geçersiz kılmanız gerekecektir.

- [GlobalizationSettings.getErrorValueString()](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getErrorValueString\(java.lang.String\))
- [GlobalizationSettings.getBooleanValueString()](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getBooleanValueString\(boolean\))
## **Rusça veya Başka Bir Dilde Hataları ve Boolean Değerleri Uygulayın**
Aşağıdaki örnek kod, Hataları ve Boolean Değerlerini Rusça veya başka bir Dilde Uygulamanın nasıl olduğunu göstermektedir. Bu kodda kullanılan Örnek Excel Dosyasını ve Çıktı PDF'sini kontrol edebilirsiniz. Ekran görüntüsü, [Örnek Excel Dosyasını](48496697.xlsx) ve [Çıktı PDF'sini](48496696.pdf) referans için farkını göstermektedir.

![todo:image_alt_text](implement-errors-and-boolean-value-in-russian-or-any-other-language_1.png)
## **Örnek Kod**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-WorkbookSettings-ImplementErrorsAndBooleanValueInRussianOrAnyOtherLanguage.java" >}}
