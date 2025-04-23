---
title: تنفيذ تسميات المجموع الفرعي أو الإجمالي الكلي بلغات أخرى
type: docs
weight: 50
url: /ar/net/implement-subtotal-or-grand-total-labels-in-other-languages/
---

## **سيناريوهات الاستخدام المحتملة**

أحيانًا، ترغب في عرض تسميات إجمالي الفرعي والإجمالي الكلي بلغات غير إنجليزية مثل الصينية، واليابانية، والعربية، والهندية وما إلى ذلك. تُتيح Aspose.Cells لك القيام بذلك باستخدام فئة [**GlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings) والخاصية [**Workbook.GlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/globalizationsettings). يُرجى مراجعة هذه المقالة حول كيفية الاستفادة من فئة [**GlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings).

- [استخدام فئة GlobalizationSettings لتحديد تسميات الإجمالي الفرعي المخصصة وتسمية أخرى لمخطط القطاع](/cells/ar/net/using-globalizationsettings-class-for-custom-subtotal-labels-and-other-label-of-pie-chart/)

## **تنفيذ تسميات المجموع الفرعي أو الإجمالي الكلي بلغات أخرى**

الشيفرة النموذجية التالية تحمل [ملف الإكسل النموذجي](5115151.xlsx) وتنفذ أسماء الإجمالي الفرعي والإجمالي الكلي باللغة الصينية. يُرجى التحقق من [الملف الإكسل الناتج](5115152.xlsx) الذي تم إنشاؤه بواسطة هذا الشيفرة للرجوع إليه. نقوم أولاً بإنشاء فئة [**GlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings) ثم نستخدمها في شيفرتنا.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-TotalsInOtherLanguages-GlobalizationSettings.cs" >}}

استخدم الفئة التي تم إنشاؤها أعلاه في الشيفرة كالتالي:

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-TotalsInOtherLanguages-UsingGlobalizationSettings.cs" >}}
{{< app/cells/assistant language="csharp" >}}
