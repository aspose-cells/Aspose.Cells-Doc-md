﻿---
title: كيف يستخدم Aspose.Cells خطوط TrueType
type: docs
weight: 10
url: /ar/java/how-aspose-cells-uses-truetype-fonts/
---
{{% alert color="primary" %}}

يتطلب Aspose.Cells خطوط TrueType عند تحويل جداول البيانات إلى تنسيقات مثل PDF و XPS والصور.

عندما يقوم Aspose.Cells بتصيير جدول بيانات ، فإنه يتطلب الوصول إلى خطوط TrueType المستخدمة في جدول البيانات. هذه ممارسة عادية أثناء إنشاء الصور PDF و XPS وتضمن ظهور المستند أو الصورة المحولة متطابقة لأي عارض.

{{% /alert %}}

## **حول الخطوط**

### **توافر الخطوط واستبدالها**

يمكن تنسيق جدول البيانات باستخدام خطوط مختلفة مثل Arial و Times New Roman و Verdana وغيرها. عندما يقوم Aspose.Cells بتصيير جدول حسابي ، فإنه يحاول تحديد أطقم الطباعة المستخدمة في جدول البيانات. ومع ذلك ، هناك حالات قد لا يكون فيها الخط الدقيق متاحًا ، لذا يتعين على Aspose.Cells استبدال خط مشابه بدلاً من ذلك.

فيما يلي العملية التي يتبعها Aspose.Cells خلف الكواليس.

1. يحاول Aspose.Cells العثور على الخطوط في نظام الملفات المطابقة لاسم الخط الدقيق المستخدم في جدول البيانات.
1. إذا لم يتمكن Aspose.Cells من العثور على خطوط بنفس الاسم بالضبط ، فإنه يحاول استخدام الخط الافتراضي المحدد ضمن الخاصية DefaultStyle.Font الخاصة بالمصنف.
1. إذا لم يتمكن Aspose.Cells من تحديد موقع الخط المحدد ضمن الخاصية DefaultStyle.Font الخاص بالمصنف ، فإنه يحاول تحديد أنسب الخطوط من كافة الخطوط المتاحة.
1. أخيرًا ، إذا لم يتمكن Aspose.Cells من العثور على أي خطوط في نظام الملفات ، فسيتم عرض جدول البيانات باستخدام Arial.

### **حيث يبحث Aspose.Cells عن الخطوط**

يحاول Aspose.Cells ايجاد خطوط TrueType في نظام الملفات آليا. في معظم الأوقات ، يمكنك الاعتماد على السلوك الافتراضي لـ Aspose.Cell للعثور على خطوط TrueType ، ولكن في بعض الأحيان قد تحتاج إلى تحديد المجلدات التي تحتوي على خطوط TrueType باستخدام طريقة المصنع FontConfigs.setFontFolder.

### **المشكلات والحلول النموذجية المتعلقة بالخطوط**

يسرد هذا الجدول بعض المشكلات التي قد تواجهها عند تقديم جداول البيانات إلى PDF باستخدام Aspose.Cells وحلولها.

{{% alert color="primary" %}}

 ضع في اعتبارك عند نسخ أي خطوط تكون معظم الخطوط محمية بحقوق الطبع والنشر. حدد أولاً موقع ترخيص الخط مسبقًا وتحقق من إمكانية نقله بحرية إلى جهاز آخر.

{{% /alert %}}

|**مشكلة** |**سبب** |**المحلول** |
|:- |:- |:- |
| يختلف التخطيط والخطوط في المستند المقدم عن المستند الأصلي.| أنت تستخدم Aspose.Cells على Linux أو Mac OS حيث لا تكون خطوط TureType موجودة بشكل افتراضي ، لذلك لا يمكن لـ Aspose.Cells تحديد موقع الخطوط على جهاز الكمبيوتر الخاص بك.|انسخ ملفات خط TrueType من جهاز Windows أو قم بتثبيت حزمة خطوط TrueType. استخدم طريقة المصنع FontConfigs.setFontFolder لتحديد موقع ملفات الخط.|

{{% alert color="primary" %}}

تحقق من المقالات التفصيلية على

- [كيفية وضع خطوط TrueType على نظام Linux](/cells/ar/java/how-to-install-truetype-fonts-on-linux/).
- [كيفية تحديد موقع خطوط تروتايب](/cells/ar/java/how-to-specify-truetype-fonts-location/).
- [كيفية الحصول على تحذيرات عند حدوث استبدال للخط](/cells/ar/java/get-warnings-for-font-substitution-while-rendering-excel-file/)

{{% /alert %}}