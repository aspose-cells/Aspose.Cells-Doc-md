---
title: تنفيذ الأخطاء وقيمة بوليانية باللغة الروسية أو أي لغة أخرى
type: docs
weight: 40
url: /ar/net/implement-errors-and-boolean-value-in-russian-or-any-other-language/
---

## **سيناريوهات الاستخدام المحتملة**

إذا كنت تستخدم Microsoft Excel بتوجيه محلي بالروسية أو بلغة أخرى، فسيعرض الأخطاء وقيم البوليان وفقًا لهذا الإعداد المحلي أو اللغة. يمكنك تحقيق سلوك مماثل باستخدام خاصية [**Workbook.Settings.GlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/globalizationsettings) لـ Aspose.Cells. يجب عليك تجاوز الطرق التالية لفئة [**GlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings) في Aspose.Cells.

- [**GlobalizationSettings.GetErrorValueString()**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/geterrorvaluestring)
- [**GlobalizationSettings.GetBooleanValueString()**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/getbooleanvaluestring)

## **تنفيذ الأخطاء والقيمة البوليانية باللغة الروسية أو أي لغة أخرى**

الشيفرة النموذجية التالية توضح كيفية تنفيذ الأخطاء والقيمة البوليانية باللغة الروسية أو أي لغة أخرى. يرجى التحقق من [ملف الإكسل النموذجي](73990159.xlsx) المستخدم في هذا الشيفرة و [PDF الناتج](73990160.pdf) الخاص به. تُظهر اللقطة الفوتوغرافية الفرق بين ملف الإكسل النموذجي والملف الناتج بصيغة PDF للرجوع إليها.

![todo:image_alt_text](implement-errors-and-boolean-value-in-russian-or-any-other-language_1.png)

## **الكود المثالي**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-WorkbookSettings-ImplementErrorsAndBooleanValueInRussianOrAnyOtherLanguage.cs" >}}
{{< app/cells/assistant language="csharp" >}}
