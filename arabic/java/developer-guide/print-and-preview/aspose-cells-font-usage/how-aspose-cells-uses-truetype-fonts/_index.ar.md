---
title: كيف تستخدم Aspose.Cells الخطوط TrueType
type: docs
weight: 10
url: /ar/java/how-aspose-cells-uses-truetype-fonts/
---

{{% alert color="primary" %}}

تتطلب Aspose.Cells الخطوط TrueType عند عرض جداول البيانات إلى تنسيقات مثل PDF و XPS والصور.

عندما يقوم Aspose.Cells بعرض جدول بيانات، يتطلب الوصول إلى الخطوط TrueType المستخدمة في الجدول. هذه ممارسة طبيعية خلال تكوين PDF و XPS والصور وتضمن أن يظهر المستند أو الصورة المحولة بشكل متطابق لأي مشاهد.

{{% /alert %}}

## **عن الخطوط**

### **توافر الخطوط واستبدالها**

يمكن تنسيق جدول بيانات باستخدام مجموعة متنوعة من الخطوط مثل Arial و Times New Roman و Verdana وغيرها. عندما يقوم Aspose.Cells بعرض جدول بيانات، يحاول اختيار الخطوط المستخدمة في الجدول. ومع ذلك، هناك حالات قد لا يتوفر فيها الخط بالضبط لذا يجب أن يقوم Aspose.Cells بالاستبدال باستخدام خط مماثل بدلاً منه.

أدناه هو العملية التي يتبعها Aspose.Cells خلف الكواليس.

1. يحاول Aspose.Cells العثور على الخطوط في نظام الملفات التي تطابق اسم الخط المحدد استخدامه في الجدول.
1. إذا لم يتمكن Aspose.Cells من العثور على الخطوط بنفس الاسم، فإنه يحاول استخدام الخط الافتراضي المحدد بموجب خاصية الخط الافتراضي للورقة العمل.
1. إذا لم يتمكن Aspose.Cells من تحديد الخط المحدد بموجب خاصية الخط الافتراضي للورقة العمل، فإنه يحاول اختيار الخطوط الأكثر ملاءمة من جميع الخطوط المتاحة.
1. وأخيرًا، إذا لم يتمكن Aspose.Cells من العثور على أي خطوط في نظام الملفات، فإنه يقوم بعرض الجدول بيانات باستخدام الخط Arial.

### **مكان البحث عن الخطوط في Aspose.Cells**

يحاول Aspose.Cells البحث عن خطوط TrueType تلقائيًا على نظام الملفات. في معظم الأحيان يمكنك الاعتماد على سلوك Aspose.Cells الافتراضي للعثور على خطوط TrueType، ولكن في بعض الأحيان قد تحتاج إلى تحديد المجلدات التي تحتوي على خطوط TrueType باستخدام طريقة الصناعة FontConfigs.setFontFolder.

### **مشاكل الخط النمطية وحلولها**

تحدد هذه الجدول بعض المشاكل التي قد تواجهك عند عرض جداول البيانات على صيغة PDF باستخدام Aspose.Cells وحلولها.

{{% alert color="primary" %}}

تذكر أن معظم الخطوط محمية بحقوق النشر. ابحث أولا عن ترخيص الخط قبل نقله بحيث يمكن التأكد من أنه يمكن نقله بحرية إلى جهاز آخر. 

{{% /alert %}}

|**المشكلة** |**السبب** |**الحل** |
| :- | :- | :- |
|تختلف الخطوط وتخطيط الوثيقة المقدمة عما هو أصلي. |تقوم باستخدام Aspose.Cells على نظام Linux أو Mac OS حيث لا تكون خطوط TureType متوفرة افتراضيًا لذا لا يمكن لـ Aspose.Cells تحديد موقع الخطوط على جهاز الكمبيوتر الخاص بك. |انسخ ملفات الخطوط TrueType من جهاز كمبيوتر Windows أو قم بتثبيت حزمة خطوط TrueType. استخدم طريقة الصناعة FontConfigs.setFontFolder لتحديد موقع ملفات الخطوط.|

{{% alert color="primary" %}}

تحقق من المقالات المفصلة حول

- [كيفية وضع خطوط TrueType على Linux](/cells/ar/java/how-to-install-truetype-fonts-on-linux/).
- [كيفية تحديد موقع خطوط TrueType](/cells/ar/java/how-to-specify-truetype-fonts-location/).
- [كيفية الحصول على تحذيرات عند حدوث استبدال الخطوط](/cells/ar/java/get-warnings-for-font-substitution-while-rendering-excel-file/)

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
