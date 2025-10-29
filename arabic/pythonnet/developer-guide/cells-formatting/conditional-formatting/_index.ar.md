---
title: تعيين تنسيقات مشروطة للملفات Excel وODS.
linktitle: تنسيقات مشروطة
type: docs
weight: 60
url: /ar/python-net/conditional-formatting/
description: كيفية تطبيق التنسيقات الشرطية على ملفات إكسل و ODS باستخدام بايثون.
keywords: تطبيق تنسيقات مشروطة 
---

## **مقدمة**

تعتبر التنسيق الشرطي ميزة متقدمة في Microsoft Excel تسمح لك بتطبيق تنسيقات على خلية أو مجموعة من الخلايا وجعل تنسيق ذلك يتغير اعتمادًا على قيمة الخلية أو قيمة صيغة. على سبيل المثال، يمكنك جعل الخلية تظهر بخط عريض فقط عندما تكون قيمة الخلية أكبر من 500. عندما تفي قيمة الخلية بالشرط، يتم تطبيق التنسيق المحدد على الخلية. إذا لم تفي قيمة الخلية بشرط التنسيق، يتم استخدام التنسيق الافتراضي للخلية. في Microsoft Excel، حدد **تنسيق** ثم **التنسيق الشرطي** لفتح مربع حوار التنسيق الشرطي.

يدعم Aspose.Cells لبايثون via .NET تطبيق التنسيق الشرطي على الخلايا أثناء التشغيل. يوضح هذا المقال كيف. كما يشرح كيفية حساب اللون المستخدم بواسطة إكسل للتنسيق الشرطي لدرجة اللون.

## **تطبيق التنسيق الشرطي**

يدعم Aspose.Cells لبايثون via .NET التنسيق الشرطي بعدة طرق:

- باستخدام جدول البيانات للمصمم
- باستخدام طريقة النسخ.
- إنشاء التنسيق الشرطي أثناء التشغيل.

### **استخدام جدول البيانات للمصمم**

يمكن للمطورين إنشاء جدول تصميمي يتضمن تنسيقًا شرطيًا في Microsoft Excel ثم فتح ذلك الملف باستخدام Aspose.Cells لبايثون via .NET. يقوم Aspose.Cells لبايثون via .NET بتحميل وحفظ الملف التصميمي، مع الاحتفاظ بأي إعدادات للتنسيق الشرطي.

### **استخدام طريقة النسخ**

يسمح Aspose.Cells لبايثون via .NET للمطورين بنسخ إعدادات التنسيق الشرطي من خلية إلى أخرى في ورقة العمل عن طريق استدعاء وظيفة [**Range.copy()**](https://reference.aspose.com/cells/python-net/aspose.cells/range/copy).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-UsingCopyMethod-1.py" >}}

## **تطبيق التنسيق الشرطي أثناء التشغيل**

يمكنك Aspose.Cells لبايثون via .NET من إضافة وإزالة التنسيق الشرطي أثناء التشغيل. تعرض العينات البرمجية أدناه كيفية تعيين التنسيق الشرطي:

1. قم بإنشاء ورقة العمل.
1. أضف تنسيق شرطي فارغ.
1. حدد النطاق الذي ينبغي تطبيق التنسيق عليه.
1. حدد شروط التنسيق.
4. حفظ الملف.

بعد هذا المثال يأتي عدد من الأمثلة الصغيرة الأخرى التي توضح كيفية تطبيق إعدادات الخط، إعدادات الحدود، وأنماط.

أضاف Microsoft Excel 2007 تنسيقًا شرطياً أكثر تقدمًا ويدعمه Aspose.Cells لبايثون via .NET أيضًا. توضح الأمثلة هنا كيفية استخدام التنسيق البسيط، وتوضح أمثلة Microsoft Excel 2007 كيفية تطبيق تنسيق شرطي أكثر تقدمًا.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-ConditionalFormattingatRuntime-1.py" >}}

### **تعيين الخط**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-SettingFontStyle-1.py" >}}

{{% alert color="primary" %}}

يمكنك تغيير نمط الخط فقط، لون النص، نمط التسطير، ونمط الإشطار فقط.

{{% /alert %}}

### **تعيين الحدود**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-SetBorder-1.py" >}}

{{% alert color="primary" %}}

يمكنك استخدام أنماط الخطوط الرفيعة فقط لحدود التخطيط. الخطوط المائلة غير مسموح بها.

{{% /alert %}}

### **تعيين النمط**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-SetPattern-1.py" >}}

## **مواضيع متقدمة**
- [إضافة التدرج اللوني ثنائي اللون والثلاثي اللون](/cells/ar/python-net/adding-2-color-scale-and-3-color-scale-conditional-formattings/)
- [تطبيق التنسيق الشرطي في الأوراق العمل](/cells/ar/python-net/apply-conditional-formatting-in-worksheets/)
- [تطبيق التظليل على الصفوف والأعمدة البديلة باستخدام التنسيق الشرطي](/cells/ar/python-net/apply-shading-to-alternate-rows-and-columns-with-conditional-formatting/)
- [توليد صور شريط بيانات التنسيق الشرطي](/cells/ar/python-net/generate-conditional-formatting-databars-images/)
- [الحصول على مجموعات الرموز، أشرطة البيانات أو كائنات مقياس الألوان المستخدمة في التنسيق الشرطي](/cells/ar/python-net/get-icon-sets-data-bars-or-color-scales-objects-used-in-conditional-formatting/)

{{< app/cells/assistant language="csharp" >}}
{{< app/cells/assistant language="python-net" >}}
