---
title: ضبط مظهر الرسم البياني
description: تعلم كيفية تكوين مظهر الرسوم البيانية في Aspose.Cells for .NET. سيوضح دليلنا لك كيفية تعديل تخطيطات الرسم البياني والألوان والخطوط والتأثيرات لتحقيق النمط البصري المرغوب وتعزيز أوراق العمل الخاصة بك.
keywords: Aspose.Cells for .NET، إيضاح، مظهر الرسم البياني، تخطيطات، ألوان، خطوط، تأثيرات، أوراق عمل.
linktitle: تنسيق الرسم البياني
type: docs
weight: 20
url: /ar/net/setting-chart-appearance/
---

## **ضبط مظهر الرسم البياني**
في كيفية إنشاء رسم بياني أعطينا مقدمة موجزة عن أنواع الرسوم البيانية وكائنات الرسم البياني التي تقدمها Aspose.Cells، ووصفنا كيفية إنشاء واحد. يتناول هذا المقال كيفية تخصيص مظهر الرسوم البيانية عن طريق تعيين خصائصها:

- تعيين منطقة الرسم البياني.
- تعيين خطوط الرسم البياني.
- تطبيق السمات.
- تعيين عناوين للرسوم البيانية والمحاور.
- العمل مع خطوط الشبكة.
### **تعيين منطقة الرسم البياني**
هناك أنواع مختلفة من المناطق في رسم بياني وتوفر Aspose.Cells قدرة للمطورين على تعديل مظهر كل منطقة. يمكن للمطورين تطبيق إعدادات تنسيق مختلفة على منطقة عن طريق تغيير لون الأمامية والخلفية وتنسيق الملء وما إلى ذلك.

في المثال الوارد أدناه، قمنا بتطبيق إعدادات تنسيق مختلفة على أنواع مختلفة من المناطق في رسم بياني. هذه المناطق تشمل:

- منطقة الرسم
- منطقة الرسم البياني
- منطقة مجموعات السلاسل
- منطقة نقطة واحدة في مجموعة سلاسل

الكود البرمجي التالي يوضح كيفية ضبط منطقة الرسم البياني.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SettingChartsAppearance-SettingChartArea-1.cs" >}}
### **تعيين خطوط الرسم البياني**
يمكن للمطورين أيضًا تطبيق أنواع مختلفة من الأنماط على الخطوط أو علامات البيانات في [مجموعات السلاسل](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection). يوضح الكود البرمجي التالي كيفية تعيين خطوط الرسم البياني باستخدام واجهة برمجة تطبيقات Aspose.Cells.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SettingChartsAppearance-SettingChartLines-1.cs" >}}
### **تطبيق سمات مايكروسوفت اكسيل 2007/2010 على الرسوم البيانية**
يمكن للمطورين تطبيق مختلف سمات أو ألوان Microsoft Excel على [مجموعات السلاسل](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection) أو كائنات الرسم البياني الأخرى كما هو موضح أدناه في المثال.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SettingChartsAppearance-ApplyingThemes-1.cs" >}}
### **ضبط عناوين الرسوم البيانية أو المحاور**
يمكنك استخدام Microsoft Excel لضبط عناوين الرسم البياني ومحوريه في بيئة WYSIWYG. تسمح Aspose.Cells أيضًا للمطورين بضبط عناوين الرسم البياني ومحوريه في وقت التشغيل. جميع الرسوم البيانية ومحوراتها تحتوي على خاصية [Title](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/properties/title) يمكن استخدامها لضبط عناوينها كما هو موضح أدناه في المثال.

يوضح مقتطف الكود التالي كيفية ضبط عناوين الرسوم البيانية والمحاور.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SettingChartsAppearance-SettingTitlesAxes-1.cs" >}}
### **العمل مع خطوط الشبكة الرئيسية**
من الممكن تخصيص شكل خطوط الشبكة الرئيسية. يمكن إخفاء أو إظهار خطوط الشبكة أو تحديد لونها وإعدادات أخرى. فيما يلي، نُوضّح كيفية إخفاء خطوط الشبكة وكيفية تغيير لونها.
#### **إخفاء خطوط الشبكة الرئيسية**
يمكن للمطورين التحكم في إمكانية رؤية خطوط الشبكة الرئيسية عن طريق تعيين خاصية الـ [IsVisible](https://reference.aspose.com/cells/net/aspose.cells.drawing/line/properties/isvisible) لكائن الـ [Line](https://reference.aspose.com/cells/net/aspose.cells.drawing/line) إلى **true** أو **false**.

الكود البرمجي التالي يوضح كيفية إخفاء خطوط الشبكة الرئيسية. بعد إخفاء خطوط الشبكة الرئيسية، سيتم إضافة رسم بياني للأعمدة إلى ورقة العمل بدون خطوط شبكة.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SettingChartsAppearance-MajorGridlines-1.cs" >}}
#### **تغيير إعدادات خطوط الشبكة الرئيسية**
لا يستطيع المطورون فقط التحكم في رؤية خطوط الشبكة الرئيسية ولكن أيضًا خصائص أخرى بما في ذلك لونها وما إلى ذلك.

الكود البرمجي التالي يوضح كيفية تغيير لون خطوط الشبكة الرئيسية. بعد تعيين لون خطوط الشبكة الرئيسية، سيتم إضافة رسم بياني للأعمدة إلى ورقة العمل بخطوط شبكة معدلة.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SettingChartsAppearance-ChangingMajorGridlines-1.cs" >}}

## **مواضيع متقدمة**
- [تعيين رمز تنسيق القيم لسلاسل الرسم البياني](/cells/ar/net/set-the-values-format-code-of-chart-series/)
- [تعيين صورة كحشو خلفية في الرسم البياني](/cells/ar/net/set-picture-as-background-fill-in-the-chart/)
{{< app/cells/assistant language="csharp" >}}
