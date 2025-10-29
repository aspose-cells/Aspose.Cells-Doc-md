---  
title: ضبط التنسيقات الشرطية لملفات Excel و ODS
linktitle: تنسيقات مشروطة  
type: docs  
weight: 60  
url: /ar/nodejs-cpp/conditional-formatting/  
description: كيفية تطبيق التنسيقات الشرطية على ملفات Excel و ODS في Node.js عبر C++.  
keywords: تطبيق التنسيقات الشرطية في Node.js عبر C++  
---  

## **مقدمة**

التنسيق الشرطي هو ميزة متقدمة تسمح لك بتطبيق تنسيقات على خلية أو نطاق خلايا وتغير ذلك التنسيق اعتمادًا على قيمة الخلية أو قيمة صيغة. على سبيل المثال، يمكنك جعل خلية غامقة فقط عندما تكون قيمة الخلية أكبر من 500. عندما تستوفي قيمة الخلية الشرط، يتم تطبيق التنسيق المحدد على الخلية. إذا لم تستوفِ قيمة الخلية الشرط، يتم استخدام التنسيق الافتراضي للخلية. في Microsoft Excel، اختر **تنسيق**، ثم **التنسيق الشرطي** لفتح مربع حوار التنسيق الشرطي.

Aspose.Cells تدعم تطبيق التنسيق الشرطي على الخلايا أثناء التشغيل. يوضح هذا المقال كيفية القيام بذلك. كما يوضح كيفية حساب اللون الذي يستخدمه Excel لتنسيق اللون الشرطي.

## **تطبيق التنسيق الشرطي**

Aspose.Cells تدعم التنسيق الشرطي بعدة طرق:

- باستخدام جدول البيانات للمصمم
- باستخدام طريقة النسخ.
- إنشاء التنسيق الشرطي أثناء التشغيل.

### **استخدام جدول البيانات للمصمم**

يمكن للمطورين إنشاء جدول بيانات للمصمم يحتوي على تنسيق شرطي في Microsoft Excel ثم فتح هذا الجدول بواسطة Aspose.Cells. تحمل Aspose.Cells وتحفظ جدول البيانات الخاص بالمصمم، مع الإبقاء على أي إعدادات تنسيق شرطي.

### **استخدام طريقة النسخ**

تسمح Aspose.Cells للمطورين بنسخ إعدادات التنسيق الشرطي من خلية إلى أخرى في ورقة العمل عن طريق استدعاء الطريقة [**Range.copy()**](https://reference.aspose.com/cells/nodejs-cpp/range/#copy-range-).

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-ConditionalFormatting-CopyConditionalFormattsByCopyRange.js" >}}


## **تطبيق التنسيق الشرطي أثناء التشغيل**

Aspose.Cells تتيح لك إضافة وإزالة التنسيق الشرطي أثناء التشغيل. الأمثلة البرمجية أدناه تُظهر كيفية تحديد التنسيق الشرطي:

1. قم بإنشاء ورقة العمل.
1. أضف تنسيق شرطي فارغ.
1. حدد النطاق الذي ينبغي تطبيق التنسيق عليه.
1. حدد شروط التنسيق.
4. حفظ الملف.

بعد هذا المثال يأتي عدد من الأمثلة الصغيرة الأخرى التي توضح كيفية تطبيق إعدادات الخط، إعدادات الحدود، وأنماط.

أضاف Microsoft Excel 2007 تنسيقًا شرطيًا أكثر تقدمًا تدعمه Aspose.Cells أيضًا. توضح الأمثلة هنا كيفية استخدام التنسيق البسيط، في حين توضح أمثلة Microsoft Excel 2007 كيفية تطبيق تنسيق شرطي أكثر تقدمًا.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-ConditionalFormatting-ApplyingConditionalFormattingAtRuntime.js" >}}


### **تعيين الخط**

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-ConditionalFormatting-SetFont.js" >}}



{{% alert color="primary" %}}

يمكنك تغيير نمط الخط فقط، لون النص، نمط التسطير، ونمط الإشطار فقط.

{{% /alert %}}

### **تعيين الحدود**

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-ConditionalFormatting-SetBorder.js" >}}


{{% alert color="primary" %}}

يمكنك استخدام أنماط خط رفيع فقط للحد الخارجي. لا يُسمح بالخطوط القطرية.

{{% /alert %}}

### **تعيين النمط**

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-ConditionalFormatting-SetPattern.js" >}}



## **مواضيع متقدمة**  
- [إضافة التدرج اللوني ثنائي اللون والثلاثي اللون](/cells/ar/nodejs-cpp/adding-2-color-scale-and-3-color-scale-conditional-formattings/)  
- [تطبيق التنسيق الشرطي في الأوراق العمل](/cells/ar/nodejs-cpp/apply-conditional-formatting-in-worksheets/)  
- [تطبيق التظليل على الصفوف والأعمدة البديلة باستخدام التنسيق الشرطي](/cells/ar/nodejs-cpp/apply-shading-to-alternate-rows-and-columns-with-conditional-formatting/)  
- [توليد صور شريط بيانات التنسيق الشرطي](/cells/ar/nodejs-cpp/generate-conditional-formatting-databars-images/)  
- [الحصول على مجموعات الرموز، أشرطة البيانات أو كائنات مقياس الألوان المستخدمة في التنسيق الشرطي](/cells/ar/nodejs-cpp/get-icon-sets-data-bars-or-color-scales-objects-used-in-conditional-formatting/)  


{{< app/cells/assistant language="nodejs-cpp" >}}
