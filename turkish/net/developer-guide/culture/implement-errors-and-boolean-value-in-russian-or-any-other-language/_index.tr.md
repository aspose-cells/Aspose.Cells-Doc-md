---
title: Rusça veya başka bir dilde Hataları ve Boolean Değerleri Uygulayın
type: docs
weight: 40
url: /tr/net/implement-errors-and-boolean-value-in-russian-or-any-other-language/
---

## **Olası Kullanım Senaryoları**

Eğer Rusça Locale veya Dil veya başka bir Locale veya Dil kullanıyorsanız Microsoft Excel, o zaman Hataları ve Boolean değerleri o Locale veya Dile göre görüntüleyecektir. Aspose.Cells kullanarak benzer bir davranış elde edebilirsiniz [**Workbook.Settings.GlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/globalizationsettings) özelliğini kullanarak. Aşağıdaki yöntemleri geçersiz kılmanız gerekecektir: [**GlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings) sınıfının.

- [**GlobalizationSettings.GetErrorValueString()**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/geterrorvaluestring)
- [**GlobalizationSettings.GetBooleanValueString()**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/getbooleanvaluestring)

## **Rusça veya Başka Bir Dilde Hataları ve Boolean Değerleri Uygulayın**

Aşağıdaki örnek kod, Rusça veya başka bir dilde Hataları ve Boolean Değerleri nasıl uygulayacağınızı göstermektedir. Bu kodda kullanılan bu [Örnek Excel Dosyasını](73990159.xlsx) ve [Çıktı PDF](73990160.pdf) dosyasını kontrol edin. Ekran görüntüsü, Örnek Excel Dosyası ile Çıktı PDF arasındaki farkı göstermektedir.

![todo:image_alt_text](implement-errors-and-boolean-value-in-russian-or-any-other-language_1.png)

## **Örnek Kod**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-WorkbookSettings-ImplementErrorsAndBooleanValueInRussianOrAnyOtherLanguage.cs" >}}
{{< app/cells/assistant language="csharp" >}}
