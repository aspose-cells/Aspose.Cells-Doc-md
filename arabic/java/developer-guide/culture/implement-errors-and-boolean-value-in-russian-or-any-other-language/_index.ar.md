---
title: تنفيذ الأخطاء وقيمة بوليانية باللغة الروسية أو أي لغة أخرى
type: docs
weight: 30
url: /ar/java/implement-errors-and-boolean-value-in-russian-or-any-other-language/
---

## **سيناريوهات الاستخدام المحتملة**
إذا كنت تستخدم Microsoft Excel في لوكالة أو لغة روسية أو أي لوكالة أو لغة أخرى ، فسوف تعرض أخطاء وقيم بوليانية وفقًا لذلك اللوكالة أو اللغة. يمكنك تحقيق سلوك مماثل باستخدام خاصية أو الطريقة [Workbook.getSettings().setGlobalizationSettings()](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#GlobalizationSettings)  من Aspose.Cells. سيتعين عليك تعديل الطرق التالية في فئة [GlobalizationSettings](https://reference.aspose.com/cells/java/com.aspose.cells/GlobalizationSettings).

- [GlobalizationSettings.getErrorValueString()](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getErrorValueString\(java.lang.String\))
- [GlobalizationSettings.getBooleanValueString()](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getBooleanValueString\(boolean\))
## **تنفيذ الأخطاء والقيمة البوليانية باللغة الروسية أو أي لغة أخرى**
الكود العيني التالي يوضح كيفية تنفيذ أخطاء وقيمة بوليانية باللغة الروسية أو أي لغة أخرى. يُرجى التحقق من ملف Excel العيني المستخدم في هذا الكود وملف ال PDF الناتج. تُظهر اللقطة الشاشية الفرق بين [ملف Excel العيني](48496697.xlsx) و [ملف PDF الناتج](48496696.pdf) للإشارة.

![todo:image_alt_text](implement-errors-and-boolean-value-in-russian-or-any-other-language_1.png)
## **الكود المثالي**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-WorkbookSettings-ImplementErrorsAndBooleanValueInRussianOrAnyOtherLanguage.java" >}}
