---
title: ضبط مظهر الرسم البياني
description: تعرف على كيفية تكوين مظهر المخططات في Aspose.Cells for .NET. سيوضح لك دليلنا كيفية تعديل تخطيطات المخططات والألوان والخطوط والتأثيرات لتحقيق النمط المرئي المطلوب وتحسين أوراق العمل الخاصة بك.
keywords: Aspose.Cells for .NET, charting, chart appearance, layouts, colors, fonts, effects, worksheets.
linktitle: تنسيق الرسم البياني
type: docs
weight: 20
url: /ar/net/setting-chart-appearance/
---
##  **ضبط مظهر الرسم البياني**
في كيفية إنشاء مخطط، قدمنا مقدمة مختصرة لأنواع المخططات وكائنات المخططات التي يقدمها Aspose.Cells، ووصفنا كيفية إنشاء واحد. تتناول هذه المقالة كيفية تخصيص مظهر المخططات عن طريق تعيين خصائصها:

- تحديد منطقة الرسم البياني.
- تحديد خطوط الرسم البياني.
- تطبيق المواضيع.
- تحديد عناوين المخططات والمحاور.
- العمل مع خطوط الشبكة.
###  **تحديد منطقة الرسم البياني**
هناك أنواع مختلفة من المناطق في المخطط ويوفر Aspose.Cells المرونة لتعديل مظهر كل منطقة. يمكن للمطورين تطبيق إعدادات تنسيق مختلفة على منطقة ما عن طريق تغيير لون المقدمة ولون الخلفية وتنسيق التعبئة وما إلى ذلك.

في المثال الموضح أدناه، قمنا بتطبيق إعدادات تنسيق مختلفة على أنواع مختلفة من مناطق المخطط. وتشمل هذه المجالات:

- منطقة المؤامرة
- منطقة الرسم البياني
- منطقة تجميع السلسلة
- مساحة نقطة واحدة في مجموعة متسلسلة

يوضح مقتطف التعليمات البرمجية التالي كيفية تعيين منطقة المخطط.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SettingChartsAppearance-SettingChartArea-1.cs" >}}
###  **ضبط خطوط الرسم البياني**
 يمكن للمطورين أيضًا تطبيق أنواع مختلفة من الأنماط على الأسطر أو علامات البيانات الخاصة بالملف[مجموعة السلسلة](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection). يوضح مقتطف الكود التالي كيفية تعيين خطوط المخطط باستخدام Aspose.Cells API.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SettingChartsAppearance-SettingChartLines-1.cs" >}}
###  **تطبيق سمات Microsoft Excel 2007/2010 على المخططات**
 يمكن للمطورين تطبيق سمات/ألوان Excel مختلفة على Microsoft[مجموعة السلسلة](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection)أو كائنات مخطط أخرى كما هو موضح أدناه في المثال.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SettingChartsAppearance-ApplyingThemes-1.cs" >}}
###  **تحديد عناوين المخططات أو المحاور**
 يمكنك استخدام Microsoft Excel لتعيين عناوين المخطط ومحاوره في بيئة WYSIWYG. Aspose.Cells يسمح أيضًا للمطورين بتعيين عناوين المخطط ومحاوره في وقت التشغيل. تحتوي كافة المخططات ومحاورها على أ[عنوان](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/properties/title)الخاصية التي يمكن استخدامها لتعيين عناوينها كما هو موضح أدناه في المثال.

يوضح مقتطف التعليمات البرمجية التالي كيفية تعيين عناوين المخططات والمحاور.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SettingChartsAppearance-SettingTitlesAxes-1.cs" >}}
###  **العمل مع خطوط الشبكة الرئيسية**
من الممكن تخصيص مظهر خطوط الشبكة الرئيسية. إخفاء خطوط الشبكة أو إظهارها، أو تحديد ألوانها وإعداداتها الأخرى. وفيما يلي نعرض كيفية إخفاء خطوط الشبكة وكيفية تغيير لونها.
####  **إخفاء خطوط الشبكة الرئيسية**
 يمكن للمطورين التحكم في رؤية خطوط الشبكة الرئيسية عن طريق تعيين[مرئي](https://reference.aspose.com/cells/net/aspose.cells.drawing/line/properties/isvisible) ملكية[خط](https://reference.aspose.com/cells/net/aspose.cells.drawing/line) يعترض على**حقيقي** أو كاذبة**.

يوضح مقتطف التعليمات البرمجية التالي كيفية إخفاء خطوط الشبكة الرئيسية. بعد إخفاء خطوط الشبكة الرئيسية، ستتم إضافة مخطط عمودي إلى ورقة العمل ولن يحتوي على خطوط شبكة.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SettingChartsAppearance-MajorGridlines-1.cs" >}}
####  **تغيير إعدادات خطوط الشبكة الرئيسية**
لا يمكن للمطورين التحكم في رؤية خطوط الشبكة الرئيسية فحسب، بل أيضًا في الخصائص الأخرى بما في ذلك لونها وما إلى ذلك.

يوضح مقتطف التعليمات البرمجية التالي كيفية تغيير لون خطوط الشبكة الرئيسية. بعد تعيين لون خطوط الشبكة الرئيسية، ستتم إضافة مخطط عمودي إلى ورقة العمل مع خطوط الشبكة المعدلة.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SettingChartsAppearance-ChangingMajorGridlines-1.cs" >}}

##  **مواضيع متقدمة**
- [قم بتعيين رمز تنسيق القيم لسلسلة المخططات](/cells/ar/net/set-the-values-format-code-of-chart-series/)
- [تعيين الصورة كخلفية، املأ المخطط](/cells/ar/net/set-picture-as-background-fill-in-the-chart/)
