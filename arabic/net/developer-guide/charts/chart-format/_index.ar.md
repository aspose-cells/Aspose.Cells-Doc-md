---
title: ضبط مظهر المخطط
linktitle: تنسيق المخطط
type: docs
weight: 20
url: /ar/net/setting-chart-appearance/
---
## **ضبط مظهر المخطط**
في كيفية إنشاء مخطط ، قدمنا مقدمة موجزة لأنواع المخططات وكائنات الرسوم البيانية التي يقدمها Aspose.Cells ، ووصفنا كيفية إنشاء مخطط. تتناول هذه المقالة كيفية تخصيص مظهر المخططات عن طريق تعيين خصائصها:

- تحديد منطقة المخطط.
- تحديد خطوط الرسم البياني.
- تطبيق السمات.
- تحديد العناوين للمخططات والمحاور.
- العمل مع خطوط الشبكة.
### **إعداد منطقة المخطط**
هناك أنواع مختلفة من المساحات في المخطط ويوفر Aspose.Cells المرونة لتعديل مظهر كل منطقة. يمكن للمطورين تطبيق إعدادات تنسيق مختلفة على منطقة ما عن طريق تغيير لون المقدمة ولون الخلفية وتنسيق التعبئة وما إلى ذلك.

في المثال الموضح أدناه ، قمنا بتطبيق إعدادات تنسيق مختلفة على أنواع مختلفة من مناطق الرسم البياني. تشمل هذه المناطق:

- منطقة المؤامرة
- منطقة الرسم البياني
- منطقة المجموعة
- مساحة نقطة واحدة في مجموعة SeriesCollection

يوضح مقتطف الشفرة التالي كيفية تعيين منطقة المخطط.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SettingChartsAppearance-SettingChartArea-1.cs" >}}
### **تحديد خطوط الرسم البياني**
 يمكن للمطورين أيضًا تطبيق أنواع مختلفة من الأنماط على الخطوط أو علامات البيانات في ملف[السلسلة](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection). يوضح مقتطف الكود التالي كيفية تعيين خطوط المخطط باستخدام Aspose.Cells API.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SettingChartsAppearance-SettingChartLines-1.cs" >}}
### **تطبيق سمات Microsoft Excel 2007/2010 على المخططات**
 يمكن للمطورين تطبيق Microsoft سمات / ألوان Excel مختلفة على[السلسلة](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection)أو كائنات أخرى في المخطط كما هو موضح أدناه في المثال.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SettingChartsAppearance-ApplyingThemes-1.cs" >}}
### **تحديد عناوين المخططات أو المحاور**
يمكنك استخدام Microsoft Excel لتعيين عناوين المخطط ومحاوره في بيئة WYSIWYG. يسمح Aspose.Cells أيضًا للمطورين بتعيين عناوين المخطط ومحاوره في وقت التشغيل. تحتوي جميع المخططات ومحاورها على ملف[عنوان](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/properties/title)الخاصية التي يمكن استخدامها لتعيين عناوينها كما هو موضح أدناه في مثال.

يوضح مقتطف التعليمات البرمجية التالي كيفية تعيين العناوين للمخططات والمحاور.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SettingChartsAppearance-SettingTitlesAxes-1.cs" >}}
### **العمل مع خطوط الشبكة الرئيسية**
من الممكن تخصيص مظهر خطوط الشبكة الرئيسية. إخفاء خطوط الشبكة أو إظهارها ، أو تحديد لونها والإعدادات الأخرى. أدناه ، نعرض كيفية إخفاء خطوط الشبكة وكيفية تغيير لونها.
#### **إخفاء خطوط الشبكة الرئيسية**
يمكن للمطورين التحكم في رؤية خطوط الشبكة الرئيسية عن طريق تعيين[مرئي](https://reference.aspose.com/cells/net/aspose.cells.drawing/line/properties/isvisible) ممتلكات[خط](https://reference.aspose.com/cells/net/aspose.cells.drawing/line) يعترض على**حقيقي** أو**خاطئة**.

يوضح مقتطف الشفرة التالي كيفية إخفاء خطوط الشبكة الرئيسية. بعد إخفاء خطوط الشبكة الرئيسية ، ستتم إضافة مخطط عمودي إلى ورقة العمل ولن يحتوي على خطوط شبكة.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SettingChartsAppearance-MajorGridlines-1.cs" >}}
#### **تغيير إعدادات خطوط الشبكة الرئيسية**
لا يستطيع المطورون فقط التحكم في رؤية خطوط الشبكة الرئيسية ولكن أيضًا في الخصائص الأخرى بما في ذلك لونها وما إلى ذلك.

يوضح مقتطف الشفرة التالي كيفية تغيير لون خطوط الشبكة الرئيسية. بعد تعيين لون خطوط الشبكة الرئيسية ، ستتم إضافة مخطط عمودي إلى ورقة العمل بخطوط الشبكة المعدلة.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SettingChartsAppearance-ChangingMajorGridlines-1.cs" >}}

## **موضوعات مسبقة**
- [قم بتعيين رمز تنسيق القيم لسلسلة التخطيطات](/cells/ar/net/set-the-values-format-code-of-chart-series/)
- [قم بتعيين الصورة كخلفية تعبئة في المخطط](/cells/ar/net/set-picture-as-background-fill-in-the-chart/)
