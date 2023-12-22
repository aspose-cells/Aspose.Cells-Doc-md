---
title: سمات وألوان Excel
type: docs
weight: 100
url: /ar/net/excel-themes-and-colors/
description: كود C# لاستخدام نظام ألوان Excel مع Aspose.Cells for .NET API
keywords: C# to Create and Apply Color Schemes, c# programmatically Create a Custom Color Scheme, programmatically how to Apply a Custom Color Scheme, c# how to Use Color Scheme in excel
---
##  **كيفية تطبيق وإنشاء نظام الألوان في Excel**
تعمل سمات المستندات على تسهيل تنسيق الألوان والخطوط وتأثيرات تنسيق الرسوم في مستندات Excel وتحديثها بسرعة.
توفر النُسق مظهرًا موحدًا مع الأنماط المسماة والتأثيرات الرسومية والكائنات الأخرى المستخدمة في المصنف. على سبيل المثال، يبدو نمط Accent1 مختلفًا في سمات Office وApex. في كثير من الأحيان، تقوم بتطبيق سمة مستند ثم تعديلها بالطريقة التي تريدها.

###  **كيفية تطبيق نظام الألوان في إكسل**
1. افتح Excel وانتقل إلى علامة التبويب "تخطيط الصفحة" في شريط Excel.
1. انقر على زر "الألوان" في قسم "الموضوعات".
<br>
<img src="color.png" width=70% />
1. اختر لوحة ألوان تتوافق مع متطلباتك أو قم بالتمرير فوق أحد المخططات لمشاهدة معاينة مباشرة.

###  **كيفية إنشاء نظام ألوان مخصص في إكسيل**
يمكنك إنشاء مجموعة الألوان الخاصة بك لإضفاء مظهر جديد وفريد على مستندك أو التوافق مع معايير العلامة التجارية الخاصة بمؤسستك.

1. افتح Excel وانتقل إلى علامة التبويب "تخطيط الصفحة" في شريط Excel.
1. انقر على زر "الألوان" في قسم "الموضوعات".
1. انقر على زر "تخصيص الألوان...".
<br>
<img src="color2.png" width=70% />

1. في مربع الحوار "إنشاء ألوان سمة جديدة"، يمكنك تحديد الألوان لكل عنصر من خلال النقر على قوائم الألوان المنسدلة المجاورة لها. يمكنك اختيار الألوان من اللوحة أو تحديد ألوان مخصصة باستخدام خيار "المزيد من الألوان".
<br>
<img src="color3.png" width=70% />
1. بعد تحديد جميع الألوان المطلوبة، قم بتوفير اسم لنظام الألوان المخصص الخاص بك في حقل "الاسم".

1. انقر فوق الزر "حفظ" لحفظ نظام الألوان المخصص الخاص بك. سيكون نظام الألوان المخصص الخاص بك متاحًا الآن في القائمة المنسدلة "الألوان" لاستخدامه في المستقبل.

##  **كيفية إنشاء وتطبيق نظام الألوان في Aspose.Cells**
يوفر Aspose.Cells ميزات لتخصيص السمات والألوان.

###  **كيفية إنشاء سمة لون مخصصة في Aspose.Cells**
إذا تم استخدام ألوان السمة في الملف، فلن نحتاج إلى تعديل كل خلية على حدة، نحتاج فقط إلى تعديل الألوان في السمة.

يوضح المثال التالي كيفية تطبيق السمات المخصصة بالألوان التي تريدها. نحن نستخدم ملف قالب نموذجي تم إنشاؤه يدويًا في Microsoft Excel 2007.

يقوم المثال التالي بتحميل ملف قالب XLSX، وتحديد الألوان لأنواع ألوان السمات المختلفة، وتطبيق الألوان المخصصة، وحفظ ملف Excel.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-Excel2007Themes-CustomizeThemes-1.cs" >}}

###  **كيفية تطبيق ألوان السمات في Aspose.Cells**

يطبق المثال التالي ألوان مقدمة الخلية وألوان الخطوط بناءً على أنواع ألوان السمة الافتراضية (للمصنف). كما أنه يحفظ ملف Excel على القرص.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-Excel2007Themes-UtilizeThemeColors-1.cs" >}}

###  **كيفية الحصول على ألوان السمات وتعيينها في Aspose.Cells**
 فيما يلي بعض الأساليب والخصائص التي تطبق ألوان السمات.

- [**Style.ForegroundThemeColor**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/foregroundthemecolor): يستخدم لضبط اللون الأمامي.
- [**Style.BackgroundThemeColor**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/backgroundthemecolor): يستخدم لضبط لون الخلفية.
- [**لون الخط**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/themecolor): يستخدم لتعيين لون الخط.
- [**Workbook.GetThemeColor**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/getthemecolor): يستخدم للحصول على لون السمة.
- [**Workbook.SetThemeColor**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/setthemecolor): يستخدم لتعيين لون السمة.

يوضح المثال التالي كيفية الحصول على ألوان السمة وتعيينها.

يستخدم المثال التالي ملف قالب XLSX، ويحصل على الألوان لأنواع ألوان السمات المختلفة، ويغير الألوان ويحفظ ملف Excel Microsoft.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-Excel2007Themes-GetSetThemeColors-1.cs" >}}

##  **مواضيع متقدمة**
- [استخراج بيانات الموضوع من ملف Excel](/cells/ar/net/extract-theme-data-from-excel-file/)
