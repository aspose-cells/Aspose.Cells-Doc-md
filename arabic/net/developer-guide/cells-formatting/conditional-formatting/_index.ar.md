---
title: تعيين تنسيقات مشروطة للملفات Excel وODS.
linktitle: تنسيقات مشروطة
type: docs
weight: 60
url: /ar/net/conditional-formatting/
description: كيفية تطبيق تنسيقات مشروطة على ملفات Excel وODS في CSharp.
keywords: تطبيق تنسيقات مشروطة 
---

## **مقدمة**

تعتبر التنسيق الشرطي ميزة متقدمة في Microsoft Excel تسمح لك بتطبيق تنسيقات على خلية أو مجموعة من الخلايا وجعل تنسيق ذلك يتغير اعتمادًا على قيمة الخلية أو قيمة صيغة. على سبيل المثال، يمكنك جعل الخلية تظهر بخط عريض فقط عندما تكون قيمة الخلية أكبر من 500. عندما تفي قيمة الخلية بالشرط، يتم تطبيق التنسيق المحدد على الخلية. إذا لم تفي قيمة الخلية بشرط التنسيق، يتم استخدام التنسيق الافتراضي للخلية. في Microsoft Excel، حدد **تنسيق** ثم **التنسيق الشرطي** لفتح مربع حوار التنسيق الشرطي.

Aspose.Cells تدعم تطبيق التنسيق الشرطي على الخلايا أثناء التشغيل. يوضح هذا المقال كيفية القيام بذلك. كما يوضح كيفية حساب اللون الذي يستخدمه Excel لتنسيق اللون الشرطي.

## **تطبيق التنسيق الشرطي**

Aspose.Cells تدعم التنسيق الشرطي بعدة طرق:

- باستخدام جدول البيانات للمصمم
- باستخدام طريقة النسخ.
- إنشاء التنسيق الشرطي أثناء التشغيل.

### **استخدام جدول البيانات للمصمم**

يمكن للمطورين إنشاء جدول بيانات للمصمم يحتوي على تنسيق شرطي في Microsoft Excel ثم فتح هذا الجدول بواسطة Aspose.Cells. تحمل Aspose.Cells وتحفظ جدول البيانات الخاص بالمصمم، مع الإبقاء على أي إعدادات تنسيق شرطي.

### **استخدام طريقة النسخ**

تسمح Aspose.Cells للمطورين بنسخ إعدادات التنسيق الشرطي من خلية إلى أخرى في ورقة العمل عن طريق استدعاء الطريقة [**Range.Copy()**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/copy/index).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-UsingCopyMethod-1.cs" >}}

## **تطبيق التنسيق الشرطي أثناء التشغيل**

Aspose.Cells تتيح لك إضافة وإزالة التنسيق الشرطي أثناء التشغيل. الأمثلة البرمجية أدناه تُظهر كيفية تحديد التنسيق الشرطي:

1. قم بإنشاء ورقة العمل.
1. أضف تنسيق شرطي فارغ.
1. حدد النطاق الذي ينبغي تطبيق التنسيق عليه.
1. حدد شروط التنسيق.
4. حفظ الملف.

بعد هذا المثال يأتي عدد من الأمثلة الصغيرة الأخرى التي توضح كيفية تطبيق إعدادات الخط، إعدادات الحدود، وأنماط.

أضاف Excel 2007 المزيد من التنسيق الشرطي المتقدم الذي تدعمه أيضًا Aspose.Cells. الأمثلة هنا، توضح كيفية استخدام التنسيق البسيط، والأمثلة ك Excel 2007 تظهر كيفية تطبيق التنسيق الشرطي المتقدم أكثر.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ConditionalFormattingatRuntime-1.cs" >}}

### **تعيين الخط**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingFontStyle-1.cs" >}}

{{% alert color="primary" %}}

يمكنك تغيير نمط الخط فقط، لون النص، نمط التسطير، ونمط الإشطار فقط.

{{% /alert %}}

### **تعيين الحدود**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-SetBorder-1.cs" >}}

{{% alert color="primary" %}}

يمكنك استخدام أنماط الخطوط الرفيعة فقط لحدود التخطيط. الخطوط المائلة غير مسموح بها.

{{% /alert %}}

### **تعيين النمط**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-SetPattern-1.cs" >}}

## **مواضيع متقدمة**
- [إضافة التدرج اللوني ثنائي اللون والثلاثي اللون](/cells/ar/net/adding-2-color-scale-and-3-color-scale-conditional-formattings/)
- [تطبيق تنسيقات متقدمة للتنسيق](/cells/ar/net/apply-advanced-conditional-formatting/)
- [تطبيق التنسيق الشرطي في الأوراق العمل](/cells/ar/net/apply-conditional-formatting-in-worksheets/)
- [تطبيق التظليل على الصفوف والأعمدة البديلة باستخدام التنسيق الشرطي](/cells/ar/net/apply-shading-to-alternate-rows-and-columns-with-conditional-formatting/)
- [توليد صور شريط بيانات التنسيق الشرطي](/cells/ar/net/generate-conditional-formatting-databars-images/)
- [الحصول على مجموعات الرموز، أشرطة البيانات أو كائنات مقياس الألوان المستخدمة في التنسيق الشرطي](/cells/ar/net/get-icon-sets-data-bars-or-color-scales-objects-used-in-conditional-formatting/)

