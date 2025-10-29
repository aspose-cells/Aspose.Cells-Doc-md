---
title: تنفيذ الأخطاء والقيمة المنطقية باللغة الروسية أو أي لغة أخرى مع Golang عبر C++
linktitle: تنفيذ الأخطاء والقيم المنطقية
type: docs
weight: 40
url: /ar/go-cpp/implement-errors-and-boolean-value-in-russian-or-any-other-language/
description: تعلم كيفية تنفيذ الأخطاء والقيم المنطقية باللغة الروسية أو أي لغة أخرى باستخدام Aspose.Cells مع Golang عبر C++.
---

## **سيناريوهات الاستخدام المحتملة**

إذا كنت تستخدم Microsoft Excel باللغة الروسية أو في إعدادات لغة أو منطقة أخرى، فسيعرض أخطاء وقيم بوليانية وفقًا لتلك الإعدادات أو اللغة. يمكنك تحقيق سلوك مشابه باستخدام Aspose.Cells عبر خاصية [**Workbook.GetGlobalizationSettings()**](https://reference.aspose.com/cells/go-cpp/workbooksettings/getglobalizationsettings/). سيتعين عليك تجاوز الطرق التالية لفئة [**GlobalizationSettings**](https://reference.aspose.com/cells/cpp/aspose.cells/globalizationsettings/).

- [**GlobalizationSettings.GetErrorValueString()**](https://reference.aspose.com/cells/go-cpp/globalizationsettings/geterrorvaluestring/)
- [**GlobalizationSettings.GetBooleanValueString()**](https://reference.aspose.com/cells/go-cpp/globalizationsettings/getbooleanvaluestring/)

## **تنفيذ الأخطاء والقيمة البوليانية باللغة الروسية أو أي لغة أخرى**

الشيفرة النموذجية التالية توضح كيفية تنفيذ الأخطاء والقيمة البوليانية باللغة الروسية أو أي لغة أخرى. يرجى التحقق من [ملف الإكسل النموذجي](73990159.xlsx) المستخدم في هذا الشيفرة و [PDF الناتج](73990160.pdf) الخاص به. تُظهر اللقطة الفوتوغرافية الفرق بين ملف الإكسل النموذجي والملف الناتج بصيغة PDF للرجوع إليها.

![todo:image_alt_text](implement-errors-and-boolean-value-in-russian-or-any-other-language_1.png)

## **الكود المثالي**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ImplementErrorsAndBooleanValueInRussianOrAnyOtherLanguage.go" >}}
