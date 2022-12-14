---
title: قم بتعيين التنسيقات الشرطية لملفات Excel و ODS.
linktitle: الصيغ الشرطية
type: docs
weight: 60
url: /ar/net/conditional-formatting/
description: كيفية تطبيق التنسيقات الشرطية على ملفات Excel و ODS في CSharp.
keywords: apply conditional formats 
---
## **مقدمة**

 التنسيق الشرطي عبارة عن ميزة Microsoft Excel متقدمة تتيح لك تطبيق التنسيقات على خلية أو نطاق من الخلايا وتغيير التنسيق بناءً على قيمة الخلية أو قيمة الصيغة. على سبيل المثال ، يمكنك جعل خلية تظهر بخط غامق فقط عندما تكون قيمة الخلية أكبر من 500. عندما تتوافق قيمة الخلية مع الشرط ، يتم تطبيق التنسيق المحدد على الخلية. إذا كانت قيمة الخلية لا تفي بشرط التنسيق ، فسيتم استخدام التنسيق الافتراضي للخلية. في Microsoft Excel ، حدد**شكل** ، ومن بعد**تنسيق مشروط** لفتح مربع الحوار "تنسيق شرطي".

يدعم Aspose.Cells تطبيق التنسيق الشرطي على الخلايا في وقت التشغيل. يشرح هذا المقال كيف. يشرح أيضًا كيفية حساب اللون الذي يستخدمه Excel للتنسيق الشرطي لمقياس الألوان.

## **تطبيق التنسيق الشرطي**

Aspose.Cells يدعم التنسيق الشرطي بعدة طرق:

- باستخدام جدول بيانات المصمم
- باستخدام طريقة النسخ.
- إنشاء تنسيق شرطي في وقت التشغيل.

### **استخدام جدول بيانات المصمم**

يمكن للمطورين إنشاء جدول بيانات مصمم يحتوي على تنسيق شرطي في Microsoft Excel ثم فتح جدول البيانات هذا باستخدام Aspose.Cells. يقوم Aspose.Cells بتحميل وحفظ جدول بيانات المصمم ، مع الاحتفاظ بأي إعداد تنسيق شرطي.

### **باستخدام طريقة النسخ**

 Aspose.Cells يسمح للمطورين بنسخ إعدادات التنسيق الشرطي من خلية إلى أخرى في ورقة العمل عن طريق استدعاء[**المدى. نسخ ()**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/copy/index) طريقة.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-UsingCopyMethod-1.cs" >}}

## **تطبيق التنسيق الشرطي في وقت التشغيل**

يتيح لك Aspose.Cells إضافة التنسيق الشرطي وإزالته في وقت التشغيل. توضح نماذج التعليمات البرمجية أدناه كيفية تعيين التنسيق الشرطي:

1. إنشاء مصنف.
1. أضف صيغة شرطية فارغة.
1. عيّن النطاق الذي يجب أن ينطبق عليه التنسيق.
1. حدد شروط التنسيق.
1. حفظ الملف.

بعد هذا المثال ، يأتي عدد من الأمثلة الأصغر الأخرى التي توضح كيفية تطبيق إعدادات الخط وإعدادات الحدود والأنماط.

أضاف Microsoft Excel 2007 تنسيقًا شرطيًا أكثر تقدمًا يدعمه أيضًا Aspose.Cells. توضح الأمثلة الواردة هنا كيفية استخدام تنسيق بسيط ، توضح أمثلة Microsoft Excel 2007 كيفية تطبيق تنسيق شرطي أكثر تقدمًا.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ConditionalFormattingatRuntime-1.cs" >}}

### **تعيين الخط**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingFontStyle-1.cs" >}}

{{% alert color="primary" %}}

يمكنك فقط تغيير نمط الخط ولون النص ونمط التسطير ونمط الخط.

{{% /alert %}}

### **تعيين الحدود**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-SetBorder-1.cs" >}}

{{% alert color="primary" %}}

يمكنك فقط استخدام أنماط الخطوط الرفيعة للحدود الخارجية. الخطوط القطرية غير مسموح بها.

{{% /alert %}}

### **تعيين النقش**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-SetPattern-1.cs" >}}

## **موضوعات مسبقة**
- [إضافة مقياس لونين وتنسيقات شرطية ذات 3 ألوان](/cells/ar/net/adding-2-color-scale-and-3-color-scale-conditional-formattings/)
- [تطبيق التنسيق الشرطي المتقدم](/cells/ar/net/apply-advanced-conditional-formatting/)
- [تطبيق التنسيق الشرطي في أوراق العمل](/cells/ar/net/apply-conditional-formatting-in-worksheets/)
- [تطبيق التظليل على الصفوف والأعمدة البديلة بالتنسيق الشرطي](/cells/ar/net/apply-shading-to-alternate-rows-and-columns-with-conditional-formatting/)
- [إنشاء صور أشرطة بيانات التنسيق الشرطي](/cells/ar/net/generate-conditional-formatting-databars-images/)
- [احصل على مجموعات الرموز أو أشرطة البيانات أو كائنات مقاييس الألوان المستخدمة في التنسيق الشرطي](/cells/ar/net/get-icon-sets-data-bars-or-color-scales-objects-used-in-conditional-formatting/)

